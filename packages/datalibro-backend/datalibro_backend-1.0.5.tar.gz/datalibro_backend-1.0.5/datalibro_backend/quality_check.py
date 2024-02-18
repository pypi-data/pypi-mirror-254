from .read_file import send_message_user,send_card_message_user
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime
import datarecipe as dc
class QualityCheck():
    def __init__(self,database,table_name,sql='',date_col='',start_date='',end_date=''):
        self.database = database
        self.table_name = table_name
        self.standard_name_ods= 'ods_业务/渠道_业务过程_国家_更新频率'.split('_')
        self.standard_name_tb_bi= 'tb/bi/map_业务/渠道_业务过程_stat/detail/log_国家_更新频率'.split('_')
        if sql != '':
            self.sql = sql
        else:
            self.sql = f"select * from {self.table_name}"
        self.df = dc.sql_query('cfg.yaml',self.database,self.sql)
        if date_col !='':
            self.date_col = date_col
        if start_date !='':
            self.start_date = start_date
        if end_date != '':
            self.end_date = end_date

    def check_name_database(self):
        tb = self.table_name
        seperate_table = tb.split('_')
        wrong_col = []
        right_sugg = []
        for i in range(1,len(seperate_table)):
            if seperate_table[0] == 'ods':
                
                if i == 1:
                    if seperate_table[i] in ('amz','wb','app','sc','vc'):
                        continue
                    else:
                        suggestion = f"{i} position of the table's name is {seperate_table[i]}. The {i} position for this table should be {self.standard_name_ods[i]}. Please double check it!"
                        wrong_col.append(seperate_table[i])
                        right_sugg.append(suggestion)
                elif i >1:
                    suggestion = f"{i} position of the table's name is {seperate_table[i]}. The {i} position for this table should be{self.standard_name_ods[i]}. Please carefully check it!"
                    wrong_col.append(seperate_table[i])
                    right_sugg.append(suggestion)
            elif seperate_table[0] in ('tb','bi','map'):
                if i == 1:
                    if seperate_table[i] in ('amz','wb','app','sc','vc'):
                        continue
                    else:
                        suggestion = f"{i} position of the table's name is {seperate_table[i]}. The {i} position for this table should be {self.standard_name_ods[i]}. Please double check it!"
                        wrong_col.append(seperate_table[i])
                        right_sugg.append(suggestion)
                elif i >1:
                    try:
                        suggestion = f"{i} position of the table's name is {seperate_table[i]}. The {i} position for this table should be {self.standard_name_ods[i]}. Please carefully check it!"
                        wrong_col.append(seperate_table[i])
                        right_sugg.append(suggestion)
                    except:
                        suggestion = f"{i} position of the table's name is {seperate_table[i]}. Please carefully check it!"
                        wrong_col.append(seperate_table[i])
                        right_sugg.append(suggestion)
            else:
                    suggestion = f"{i} position of the table's name is incorrect! Please find the suitable name for this position! The enums for {i} position are ('tb','bi','map')."
                    wrong_col.append(seperate_table[i])
                    right_sugg.append(suggestion)
        data_frame = {'Wrong Column':wrong_col,"Optimized Suggestion":right_sugg}
        data = pd.DataFrame(data_frame)
        return data
                    


    def basic_info_tb(self):
        tb = self.table_name
        sql = f"describe {tb}"
        execution_query= dc.sql_query('cfg.yaml',self.database,sql)
        col_len = execution_query['Field'].apply('nunique')
        sql_2 = f"select count(*) as cnt from {tb}"
        execution_query_2= dc.sql_query('cfg.yaml',self.database,sql_2)
        count_len = execution_query_2['cnt'][0]
        tot_len = 'The table '+str(tb)+' has '+str(col_len)+' columns'+' and '+str(count_len)+' records'
        return tot_len
    
    def check_missing_value(self):
        tb = self.df
        
        miss = []
        index = []
        for col in tb.columns:
            for i in range(len(tb[col])):
                if tb[col][i] is None or tb[col][i] == '':
                    miss.append(col)
                    index.append(i)
        if len(index)< 1:
            dat = f'The table {self.table_name} has no missing value!'
        else:
            data = {'miss_column':miss,'index':index}
        
            dat = pd.DataFrame(data)
        return dat
                    
    def check_primary_key(self,primary_key_1,primary_key_2,primary_key_3):
        tb = self.table_name
        database = self.database
        primary_sql = f"""select count(*) as total_cnt,count(distinct {primary_key_1},{primary_key_2},{primary_key_3}) as primary_key_cnt from {tb}"""
        df_primary = dc.sql_query('cfg.yaml',database,primary_sql)
        if df_primary['total_cnt'][0] == df_primary['primary_key_cnt'][0]:
            result = '主键唯一，无重复记录。'
        else:
            result = f'主键不唯一，有重复记录。主键记录数：{df_primary["primary_key_cnt"][0]}, 全表记录数：{df_primary["total_cnt"][0]}'
        return result
    
    def check_qc(self,notification='disabled',user_id = ''):
        result_1 = self.check_name_database()
        result_2 = self.basic_info_tb()
        result_3 = self.check_missing_value()
        if notification !='disabled':
            content_1 = result_1
            send_card_message_user(user_id,content =content_1,title='Name QC')  
            content_2 = result_2
            send_card_message_user(user_id,content = content_2,title=f'Basic Info of {self.table_name}')  
            content_3 = result_3
            send_card_message_user(user_id,content = content_3,title=f'Missing Value of {self.table_name}')  
        
    def check_strange_data(self,checked_col,date_col,x1='',cur_start_date='',cur_end_date='',prev_start_date='',prev_end_date='',notification='disabled',user_id = ''):
        df = self.df
        df[date_col] = df[date_col].apply(lambda x:(pd.to_datetime(x)).strftime('%Y-%m-%d'))
        today = (datetime.now()).strftime('%Y-%m-%d')
        if cur_start_date=='' and cur_end_date=='':
            
            cur_start_date = today
            cur_end_date = today
        else:
            cur_start_date = (pd.to_datetime(cur_start_date)).strftime('%Y-%m-%d')
            cur_end_date = (pd.to_datetime(cur_end_date)).strftime('%Y-%m-%d')
        if prev_start_date == '' and prev_end_date == '':
            prev_start_date = (pd.to_datetime(cur_start_date)- relativedelta(days=31)).strftime('%Y-%m-%d')
            prev_end_date = (pd.to_datetime(prev_start_date)+relativedelta(days = 30)).strftime('%Y-%m-%d')
                    
        
        if x1 == '':
            x1 = 1.4
        
        df_cur = df.copy()
        df_cur = df_cur.loc[(df_cur[date_col]>= cur_start_date)&(df_cur[date_col]<= cur_end_date)]
        df_cur[checked_col] = df_cur[checked_col].astype('float')
        df_prev = df.copy()
        df_prev = df_prev.loc[(df_prev[date_col]>= prev_start_date)&(df_prev[date_col]<= prev_end_date)]
        df_prev[checked_col] = df_prev[checked_col].astype('float')
        
        if df_prev[checked_col].max() < df_cur[checked_col].min():
            result = f"compare with the {prev_start_date}-{prev_end_date}, the current date range of data is much higher than the previous date range, {df_prev[checked_col].max()}<{df_cur[checked_col].min()}, {checked_col} is out of range!"
        elif df_cur[checked_col].max()/df_prev[checked_col].max() >= x1:
            result = f"compare with the {prev_start_date}-{prev_end_date}, the current date range of data is {x1} higher than the previous date range, {df_cur[checked_col].max()}/{df_prev[checked_col].max()}>={x1}, {checked_col} is out of range!"
        elif df_prev[checked_col].min()/df_cur[checked_col].min() >= x1:
            result = f"compare with the {prev_start_date}-{prev_end_date}, the current date range of data is {x1} lower than the previous date range, {df_prev[checked_col].min()}/{df_cur[checked_col].min()}>={x1}, {checked_col} is out of range!"
        elif  df_prev[checked_col].min() >df_cur[checked_col].max():
            result = f"compare with the {prev_start_date}-{prev_end_date}, the current date range of data is much lower than the previous date range, {df_prev[checked_col].min()}>{df_cur[checked_col].max()}, {checked_col} is out of range!"
        elif  abs(df_cur[checked_col].median()) / abs(df_prev[checked_col].median()) >= x1:
            result = f"compare with the {prev_start_date}-{prev_end_date}, the current date range of median of data is {x1} higher than the previous date range, {df_cur[checked_col].median()}/{df_prev[checked_col].median()}>={x1}, {checked_col} is out of range!"
        else:
            result = f"compare with the {prev_start_date}-{prev_end_date}, {checked_col} is in the range."
        if notification != 'disabled':
            content = result
            send_message_user(user_id,content)  
        return result
    def check_enum(self,enum_col):
        tb = self.df
        col_enum = tb.groupby(enum_col)[enum_col].count()
        result = f"The {enum_col} has following enums:{col_enum.index}. \n Please check carefully if the enums are complete!"
        return result
    
    

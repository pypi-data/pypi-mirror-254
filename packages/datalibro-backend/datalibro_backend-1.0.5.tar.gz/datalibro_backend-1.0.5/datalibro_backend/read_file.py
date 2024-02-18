import requests
import yaml

def read_config_file(file_id):


    app_id = 'cli_a5eeb3ad3837100b'
    app_secret = 'ftLZbDJOzDxSx0xiigALNev1tgHTvR4V'

    # Obtain an access token
    auth_url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "app_id": app_id,
        "app_secret": app_secret
    }
    # Authenticate and get your access token from Feishu
    response = requests.post(auth_url, headers=headers, json=payload)
    auth_token = response.json().get("app_access_token")

    # The endpoint for downloading files from Feishu might look like this

    download_endpoint = f'https://open.feishu.cn/open-apis/drive/v1/files/{file_id}/download'

    # Make the request to download the file
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.get(download_endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Assuming the response content is the binary content of the YAML file
        file_content = response.content

        # Load the YAML content
        content = yaml.safe_load(file_content)
        try:
            yaml_file_path = './cfg.yaml'
            with open(yaml_file_path, 'r') as file:
                yaml_content = yaml.safe_load(file)
            yaml_content = content
        except:
            yaml_file_path = 'cfg.yaml'
            yaml_content = content
        with open(yaml_file_path, 'w') as file:
            yaml.safe_dump(yaml_content, file)

    else:
        return 'Failed to download the file:'+response.text
    
def send_message(chat_id,content,user_id=None):
    
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    app_id = 'cli_a5eeb3ad3837100b'
    app_secret = 'ftLZbDJOzDxSx0xiigALNev1tgHTvR4V'

    payload = {
        'app_id': app_id,
        'app_secret': app_secret
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    """Send a message to a Feishu chat."""
    url = 'https://open.feishu.cn/open-apis/message/v4/send/'
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    if user_id:
        payload = {
            'chat_id': chat_id,
            'msg_type': 'text',
            'content': {
                'text': f"<at user_id = \"{user_id}\">Tom</at> {content}",
            }
        }
    else:
        payload = {
            'chat_id': chat_id,
            'msg_type': 'text',
            'content': {
                'text': f"{content}",
            }
        }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def send_message_user(user_id, content):
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    app_id = 'cli_a5eeb3ad3837100b'
    app_secret = 'ftLZbDJOzDxSx0xiigALNev1tgHTvR4V'

    payload = {
        'app_id': app_id,
        'app_secret': app_secret
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    """Send a message to a Feishu chat."""
    url = 'https://open.feishu.cn/open-apis/message/v4/send/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'user_id': user_id,
        'msg_type': 'text',
        'content': {
            'text': f"{content}",
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
def send_card_message(chat_id,title,content):
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    app_id = 'cli_a5eeb3ad3837100b'
    app_secret = 'ftLZbDJOzDxSx0xiigALNev1tgHTvR4V'

    payload = {
        'app_id': app_id,
        'app_secret': app_secret
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    card_content = {
    'chat_id': chat_id,
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "title": {
                "tag": "plain_text",
                "content": f"{title}"
            }
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "plain_text",
                    "content": f"{content}"
                }
            },
            
            # 其他卡片组件，例如按钮等
        ]
    }
}
    # 发送消息的API端点
    message_url = 'https://open.feishu.cn/open-apis/message/v4/send/'

    # 发送POST请求的headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # 发送卡片消息
    response = requests.post(message_url, headers=headers, json=card_content)
    return response.json()
def send_card_message_user(user_id,title,content):
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    app_id = 'cli_a5eeb3ad3837100b'
    app_secret = 'ftLZbDJOzDxSx0xiigALNev1tgHTvR4V'

    payload = {
        'app_id': app_id,
        'app_secret': app_secret
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    card_content = {
    'user_id': user_id,
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "title": {
                "tag": "plain_text",
                "content": f"{title}"
            }
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "plain_text",
                    "content": f"{content}"
                }
            },
            
            # 其他卡片组件，例如按钮等
        ]
    }
}
    # 发送消息的API端点
    message_url = 'https://open.feishu.cn/open-apis/message/v4/send/'

    # 发送POST请求的headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # 发送卡片消息
    response = requests.post(message_url, headers=headers, json=card_content)
    return response.json()

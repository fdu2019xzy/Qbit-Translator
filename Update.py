import requests
import json
import time
import webbrowser

api_url = 'https://api.github.com/repos/fdu2019xzy/Qbit-Translator/releases'
github_url = 'https://github.com/fdu2019xzy/Qbit-Translator/releases'

def update_check(self):
    if(update_process()):
        choice = self.update_message(self)
        if(choice == self.update_message.Ok):
            webbrowser.open(github_url)

def update_process():
    # 1.发布时间分析
    old_time = time
    # 2.发送请求，获取数据
    try:
        header = {'User-agent':'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3'}
        all_info = requests.get(api_url,headers=header).json()
    except:
        return False
    try:
        with open('./updatetime.txt','r') as f:
            old_time = f.read()
    except:
        with open('./updatetime.txt','w') as f:
            f.write(all_info[0]["published_at"])
        return False
    new_time = all_info[0]["published_at"]
    if new_time > old_time:
        old_time = new_time
        with open('./updatetime.txt','w') as f:
            f.write(str(new_time))
        return True
    else:
        return False
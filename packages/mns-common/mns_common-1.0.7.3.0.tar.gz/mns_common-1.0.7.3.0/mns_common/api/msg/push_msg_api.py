import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 14
project_path = file_path[0:end]
sys.path.append(project_path)
import json

import requests
from pypushdeer import PushDeer


# token= AT_vL1h0mFSHtyRvbAED2mRozcEj8eFm4xh
def push_msg_to_wechat(title, msg):
    # push = PushDeer(pushkey="PDU14860TJitHPGdTo3a7Gx0xMvV79aizrGXUs5No")
    # push.send_text(title, desp=msg)

    url = 'http://wxpusher.zjiecode.com/api/send/message'

    s = json.dumps({'appToken': 'AT_vL1h0mFSHtyRvbAED2mRozcEj8eFm4xh',
                    'content': msg,
                    'summary': title,
                    'contentType': 1,
                    'uids': ['UID_vqzsUn5qXDROV2dbIZuZrioewJ9D']
                    })
    headers = {
        "Content-Type": "application/json"
    }

    requests.post(url, data=s, headers=headers)


if __name__ == '__main__':
    push_msg_to_wechat('test', 'big win')

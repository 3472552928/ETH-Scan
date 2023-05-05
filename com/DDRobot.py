import json
import requests
# url = "https://oapi.dingtalk.com/robot/send?access_token=98bce2d980abdd565efe2b55e3cad2aec65cfd6e16154d40d320c1442eca171b"
# 钉钉机器人Webhook URL

access_token="98bce2d980abdd565efe2b55e3cad2aec65cfd6e16154d40d320c1442eca171b"
dingtalk_robot_url = 'https://oapi.dingtalk.com/robot/send?access_token='+access_token

# 要发送的消息内容和链接
# message = {
#     'msgtype': 'text',
#     'text': {
#         'content': '请查看最新消息：[点击链接](http://example.com)'
#     }
# }

message = {
    'msgtype': 'text',
    'text': {
        'content': '请查看最新消息：[点击链接](http://baidu.com)'
    }
}

# 将消息内容和链接转换为JSON格式
message_json = json.dumps(message)

# 使用requests库向钉钉机器人发送POST请求
response = requests.post(dingtalk_robot_url, data=message_json, headers={'Content-Type': 'application/json'})

# 检查请求是否成功
if response.status_code == 200:
    print('消息已发送')
else:
    print('发送消息失败，错误代码：', response.status_code)
import requests
import json

# 让用户输入内容
user_input = input("请输入你想要发送的内容：")
# 请求的 URL 和参数
url = "https://agentapi.baidu.com/assistant/conversation"
params = {
    "appId": "WHNtFgW5SyWUFmXRevTMhm0ugTIkKAbr",
    "secretKey": "qADNcRPAyM4OcvbUe5XwcBPaQbClKea8"
}
headers = {
    "Content-Type": "application/json"
}
data = {
    "message": {
        "content": {
            "type": "text",
            "value": {
                "showText": user_input
            }
        }
    },
    "source": "xxx",
    "from": "openapi",
    "openId": "xxx"
}

try:
    # 发送 POST 请求
    response = requests.post(url, params=params, headers=headers, data=json.dumps(data))
    
    # 获取响应内容
    response_content = response.text
    print("Response Content:", response_content)
    
    # 检查响应的编码
    print("Response Encoding:", response.encoding)
    
    # 将响应内容保存到文件
    with open("backend\\response_data.txt", "w", encoding="utf-8") as file:
        file.write(response_content)
    print("响应已成功保存到 response_data.txt 文件中。")
except Exception as e:
    print("Error:", str(e))
    with open("backend\\response_data.txt", "w", encoding="utf-8") as file:
        file.write("Error: " + str(e))
    print("错误信息已保存到 response_data.txt 文件中。")
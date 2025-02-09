import requests
import json

# 让用户输入内容
user_input = "你好"

# 请求的 URL 和参数
url = "https://agentapi.baidu.com/assistant/conversation"  # 确保 URL 是正确的
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

# 读取保存的响应文件并解析JSON数据
input_file = "backend\\response_data.txt"
output_file = "backend\\output.json"

# 读取文件内容
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 解析每行的 JSON 数据
json_data_list = []
for line in lines:
    # 检查是否是有效的 JSON 数据行
    if line.strip().startswith("data:"):
        # 提取 JSON 数据部分
        json_str = line.strip().replace("data:", "").strip()
        try:
            # 将 JSON 字符串解析为字典
            json_data = json.loads(json_str)
            json_data_list.append(json_data)
        except json.JSONDecodeError as e:
            print(f"JSON 解析失败: {e}，内容: {json_str}")

# 将解析后的 JSON 数据保存到文件
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(json_data_list, file, ensure_ascii=False, indent=4)

print(f"数据已成功保存到 {output_file}")

# 从JSON文件中提取特定字段的内容并保存到文本文件中
input_file = "backend\\output.json"
output_file = "backend\\output.txt"

try:
    # 打开并读取JSON文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data_list = json.load(f)  # 这是一个JSON数组

    # 用于存储所有提取的text内容
    all_text_content = []

    # 遍历数组中的每个JSON对象
    for data in data_list:
        # 检查data字段是否存在且不为null
        if 'data' in data and data['data'] is not None:
            # 检查message字段是否存在
            if 'message' in data['data']:
                # 检查content字段是否存在
                if 'content' in data['data']['message']:
                    content_list = data['data']['message']['content']
                    # 确保content列表不为空
                    if content_list:
                        # 获取第一个content元素中的data字段
                        first_content = content_list[0]
                        if 'data' in first_content and first_content['data'] is not None:
                            # 获取text字段
                            if 'text' in first_content['data']:
                                text_content = first_content['data']['text']
                                all_text_content.append(text_content)  # 将text内容添加到列表中

    # 将所有提取的text内容保存到output.txt文件中
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_text_content))  # 将所有文本内容用换行符分隔后写入文件

    print("提取完成，内容已保存到output.txt文件中。")
except Exception as e:
    print(f"发生错误：{e}")
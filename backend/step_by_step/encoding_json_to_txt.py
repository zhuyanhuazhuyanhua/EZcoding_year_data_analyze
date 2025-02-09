import json

# 输入文件路径
input_file = r"C:\Users\1\Desktop\mashang\output.json"
# 输出文件路径
output_file = r"C:\Users\1\Desktop\mashang\output.txt"

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
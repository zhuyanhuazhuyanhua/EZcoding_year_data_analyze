import json

# 假设你的数据存储在 "data.txt" 文件中
input_file = "C:\\Users\\1\\Desktop\\mashang\\backend\\response_data.txt"
output_file = "C:\\Users\\1\Desktop\\mashang\\backend\\output.json"

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
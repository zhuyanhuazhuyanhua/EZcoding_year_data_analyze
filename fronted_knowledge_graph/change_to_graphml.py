import pandas as pd
import networkx as nx

# 读取 Excel 文件
df = pd.read_excel("mashang.xlsx")

# 创建图对象
G = nx.DiGraph()  # 使用有向图

# 获取第四列的列名（假设第四列是固定的）
parent_column = df.columns[3]

# 获取第一行的列名（作为中间层节点的前缀）
child_columns = df.columns[:4].tolist() + df.columns[5:15].tolist()  # 排除第四列

# 遍历第四列的每一行数据（从第二行开始）
for i in range(1, len(df)):
    parent = df.loc[i, parent_column]  # 获取顶层节点（第四列的第i行数据）
    G.add_node(parent)  # 添加顶层节点

    # 遍历第一行的列名（中间层节点）
    for j, column in enumerate(child_columns):
        if column != parent_column:  # 排除第四列
            # 构造中间层节点名称：顶层节点的值 + 列名
            middle_node = f"{parent}的{column}"
            G.add_node(middle_node)  # 添加中间层节点
            G.add_edge(parent, middle_node)  # 添加边：顶层节点 -> 中间层节点

            # 获取底层节点（第i行第j列的数据）
            child = df.loc[i, column]
            if pd.notnull(child):  # 确保底层节点不是空值
                G.add_node(child)  # 添加底层节点
                G.add_edge(middle_node, child)  # 添加边：中间层节点 -> 底层节点

# 保存为 GraphML 文件
nx.write_graphml(G, "output.graphml")
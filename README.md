# 项目名称 EZcoding_year_data_analyze

## 项目结构说明

- **`backend`**  
  后端代码，负责与百度 Agent 进行通信。
  
 
- **`frontend_knowledge_graph`**  
  知识图谱相关的前端代码。

- **`frontend`**  
  前端代码，用于构建用户界面。

- **`static`**  
  静态资源，包括图片、CSS 文件、JavaScript 文件等。

- **`templates`**  
  模板文件，用于前端页面的模板渲染。

- **`lib`**  
  项目依赖的本地库文件。

- **`node_modules`**  
  通过 npm 安装的第三方依赖项。

## 使用方法

- **1. 克隆项目**：
   ```bash
   git clone https://github.com/yourusername/yourprojectname.git
- **2. 阅读backend中的readme**：
   将backend中的test_bug文件夹中的三个txt文件依次复制到终端，检测请求是否正常；之后将backend中step_by_step中的三个python文件依次运行，检测响应及返回数据是否正常
- **3. 运行backend中的total.py**：
   确认以上操作无误后，运行total.py;output.txt为最终解析好的数据
- **4. 运行total.py无误后，运行app.py**：
   使用flask框架实现前后端交互，运行后浏览器打开http://localhost:5000网址，可在前端与百度agent对话
- **5. fronted_knowledge_graph中knowledge_graphhtml**：
   在浏览器中打开该文件即可，为现代化的知识图谱，可视化数据
   

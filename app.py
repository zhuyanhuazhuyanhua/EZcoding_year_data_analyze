from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.json
    script_path = data['scriptPath']
    user_input = data['userInput']

    # 验证脚本路径是否安全
    if not os.path.isfile(script_path):
        return jsonify({'error': 'Invalid script path'}), 400

    try:
        # 修改脚本中的 user_input 并运行脚本
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
        script_content = script_content.replace('user_input = input("请输入你想要发送的内容：")', f'user_input = "{user_input}"')
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content)

        # 安全地运行脚本并捕获输出
        print(f"Running script: {script_path}")
        command = ['python', script_path]
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        output = result.stdout.strip()
        error = result.stderr.strip()

        if result.returncode != 0:
            print(f"Script execution failed: {error}")
            return jsonify({'error': f'Script execution failed: {error}'}), 500

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Script execution timed out'}), 500
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

    # 将输出保存到文件
    try:
        with open('C:\\Users\\1\\Desktop\\mashang\\backend\\output.txt', 'w', encoding='utf-8') as f:
            f.write(output)
    except Exception as e:
        return jsonify({'error': f'Failed to write output to file: {str(e)}'}), 500

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
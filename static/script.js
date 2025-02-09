document.getElementById('send-button').addEventListener('click', function () {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') {
        alert('请输入内容！');
        return;
    }

    // 将用户输入显示在聊天框中
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="user-message">${userInput}</div>`;

    // 调用后端接口
    fetch('/run-script', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            scriptPath: 'C:\\Users\\1\\Desktop\\mashang\\backend\\one_step\\total.py',
            userInput: userInput
        })
    })
    .then(response => response.json())
    .then(data => {
        // 将响应内容显示在聊天框中
        chatBox.innerHTML += `<div class="assistant-message">${data.output}</div>`;
    })
    .catch(error => {
        console.error('Error:', error);
        chatBox.innerHTML += `<div class="assistant-message">发生错误，请稍后重试。</div>`;
    });

    // 清空输入框
    document.getElementById('user-input').value = '';
});
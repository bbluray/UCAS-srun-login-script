document.getElementById('dataForm').addEventListener('submit', function(e) {
    try {
        e.preventDefault();
    } catch (error) {
        console.error('An error occurred:', error);
    }

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const ip_addr  = document.getElementById('ip_addr').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            password: password,
            ip_addr: ip_addr
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // 打印解析后的 JSON 数据
        document.getElementById('log').textContent = data.message;
    })
    .catch(error => {
        document.getElementById('log').textContent = 'Error: ' + error;
    });
});
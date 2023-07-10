document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    fetch('http://localhost:8000/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.access && data.refresh) {
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);
            document.getElementById('message').innerText = 'Login successful!';
            window.location.href = "/accounts/" + data.user_id;
        } else {
            document.getElementById('message').innerText = 'Login failed.';
            console.error(data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
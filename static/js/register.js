document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    fetch('http://localhost:8000/auth/register/', {
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
            document.getElementById('message').innerText = 'Registration successful!';
        } else {
            document.getElementById('message').innerText = 'Registration failed.';
            console.error(data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
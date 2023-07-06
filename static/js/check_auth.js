fetch('/api/check_auth/', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
    },
    credentials: 'include'
})
.then(response => response.json())
.then(data => {
    if (!data.authenticated) {
        window.location.href = "/auth/login/";
    }
})
.catch((error) => {
    console.error('Error:', error);
    window.location.href = "/auth/login/";
});

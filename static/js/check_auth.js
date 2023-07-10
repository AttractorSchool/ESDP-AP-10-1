function getCookie(name) {
    var cookieArr = document.cookie.split(";");
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");
        if(name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}
fetch('/api/check_auth/', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
    },
    credentials: 'include'
})
.then(response => {
    return response.json();
})
.then(data => {
    if (!data.authenticated) {
        window.location.href = "/auth/login/";
    }
})
.catch((error) => {
    console.error('Error:', error);
    window.location.href = "/auth/login/";
});
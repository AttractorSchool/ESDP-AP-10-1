window.onload = function() {
    const accessToken = localStorage.getItem('accessToken');
    if (!accessToken) {
        window.location.href = "/auth/login/";
    }
};
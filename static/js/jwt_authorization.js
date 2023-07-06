$.ajax({
    url: 'http://127.0.0.1:8000/api/newsline/',
    type: "GET",
    headers: {
        "Accept": "application/json",
        "Authorization": "JWT " + localStorage.getItem('accessToken'),
    },
    success: function(data, status) {
        console.log(data);
    }
});

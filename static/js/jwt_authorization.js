$.ajax({
    url: 'http://127.0.0.1:8000/api/newsline/',
    type: "GET",
    headers: {
        "Accept": "application/json",
        "Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MjAzNTU3LCJpYXQiOjE2ODcyMDMyNTcsImp0aSI6ImE3MTliMjM1NjU1NTQyNDY4NDE5MjkwYzlmNDA2YmExIiwidXNlcl9pZCI6Mn0.HEyJHiA7Bx94PuyCEWk4RUcjsl9HyLTJ8mu-VwOQCPk"
    },
    success: function(data, status) {
        console.log(data);
    }
});
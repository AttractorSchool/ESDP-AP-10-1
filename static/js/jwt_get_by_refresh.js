var fd = new FormData();
fd.append("refresh", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzI3NzA5MywiaWF0IjoxNjg3MTkwNjkzLCJqdGkiOiI3MGZhY2NjNjg4Njc0NTRmODU5OTc3ZGJhMDUxOTAyMiIsInVzZXJfaWQiOjJ9.llEE3TK7ECwdByQ57QUb58eQsk9BEyFQqRhSd83GgP4");
$.ajax({
    url: 'http://127.0.0.1:8000/api/token/refresh/',
    type: "POST",
    data: fd,
    processData: false,
    contentType: false,
    success: function(data, status) {
        console.log(data);
    }
});
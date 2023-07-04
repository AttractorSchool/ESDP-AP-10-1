$(document).ready(function () {
    $('.like_btn').click(function () {
        let user_id = $(this).data('pk');
        let url = '/auth/profile/api/user_like/' + user_id;
        url = url.replace('/auth/profile', '');
        $.ajax({
            url: url,
            type: 'POST',
            dataType: 'json',
            success: function (response) {
                // Handle successful response
                console.log(response.likes_qty);
            },
            error: function (xhr, status, error) {
                // Handle error
                console.log(error);
            }
        });
    });
});


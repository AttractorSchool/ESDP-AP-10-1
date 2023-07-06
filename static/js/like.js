$(document).ready(function () {
    $('.thank_profile_link').click(function (event) {
        event.preventDefault();

        let user_id = $(this).data('pk');
        let url = '/auth/profile/api/user_like/' + user_id;
        url = url.replace('/auth/profile', '');
        $.ajax({
            url: url,
            type: 'POST',
            dataType: 'json',
            success: function (response) {
                console.log(response.likes_qty);
                location.reload();
            },
            error: function (xhr, status, error) {
                console.log(error);
            }
        });
    });
});

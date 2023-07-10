$(document).ready(function () {
    $(".burger-button").click(function () {
        $(".burger-button").toggleClass("active");
        $(".burger-menu").toggleClass("active");
        if ($(".burger-menu").hasClass("active")) {
            $(".about_current_page").hide();
        } else {
            $(".about_current_page").show();
        }
    });
});

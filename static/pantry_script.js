$(document).ready(function(){

    var Navy = $('.nav').offset().top;

    var stickiNav = function(){
        var Scrolly = $(window).scrollTop();
    if (Scrolly > Navy) {
        $('.nav').addClass('sticky');
    } else {
        $('.nav').removeClass('sticky');
    }
    };
    
    stickiNav();
    $(window).scroll(function(){
        stickiNav()
    });
    });
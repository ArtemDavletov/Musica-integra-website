var all = $(window).width();

var left = $(this).offset().left;

var width = $(this).outerWidth(true);

var offset = all - (left + width);

if (offset < 0) {
    $('.dropdown-item').css('display','block').css('opacity','1').css('transition','opacity .3s 1s')
    $('.dropdown-menu').css('display','block').css('opacity','1').css('transition','opacity .3s 1s')
}
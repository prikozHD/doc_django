$(".main_category").click(function () {

    if($(this).children().css('display') == 'none'){
        $(this).children().slideDown();

    }
    else{
        $(this).children().slideUp();
    }
});
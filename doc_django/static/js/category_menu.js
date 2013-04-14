$(".main_category").click(function (event) {
    if($(this).children().css('display') == 'none'){
        $(this).children().css('margin',"15px");
        $(this).children().slideDown();

    }
    else{
        $(this).children().slideUp();
    }
});


$(".sub_category").click(function (event) {
    event.stopPropagation();
    console.log('ok');
});


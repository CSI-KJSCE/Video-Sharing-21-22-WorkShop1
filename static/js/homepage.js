$("#sidebar-row").click(function(){
    console.log("In javascript");
    $(this).addClass("selected").siblings().removeClass("selected");
});​
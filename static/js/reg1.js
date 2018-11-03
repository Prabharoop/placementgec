
$(document).ready(function(){
	$(".sh1").hide();
	$(".sh2").hide();
    $("#show").click(function(){
        $(".sh1").show();
        $(".sh2").hide();

    });
    $("#hide").click(function(){
        $(".sh1").hide();
        $(".sh2").show();
    });
});
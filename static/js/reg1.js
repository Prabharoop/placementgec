
$(document).ready(function(){
	$("#id_texte").hide();
	$("#id_textf").hide();
    $("#id_textg").hide();
    $("#id_choicee_0").click(function(){
        $("#id_texte").show();
        $("#id_textf").hide();
        $("#id_textg").hide();

    });
    $("#id_choicee_1").click(function(){
        $("#id_texte").hide();
        $("#id_textf").show();
        $("#id_textg").show();
    });
});
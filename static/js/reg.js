
$(function () {
        $("#id_choiced").click(function () {
            if ($(this).is(":checked")) {
                $("#id_textd").show();
                $("#AddPassport").hide();
            } else {
                $("#id_textd").hide();
                $("#AddPassport").show();
            }
        });
    });

$( function () {
        $("#id_choicee_0").click(function () {
            if($(this).is(":checked")) {
                $("#id_textf").show();
                $("#id_textg").show();
                $("#AddPassport").hide();
            }


        });
        $("#id_choicee_1").click(function () {
            if($(this).is(":checked")) {
                $("#id_textf").hide();
                $("#id_textg").hide();
                $("#AddPassport").show();
            }

        });

});
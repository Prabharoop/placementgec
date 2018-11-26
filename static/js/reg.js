
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
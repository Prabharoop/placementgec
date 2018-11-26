function checkVisibility(){
    var formgroups=document.querySelectorAll(".form-group");
    Array.prototype.forEach.call(formgroups,function(el,i){
        var checkbox = el.querySelectorAll(".checkbox");
        if(checkbox.length >0){
            var checkboxElem = el.querySelectorAll("input")[0];
            if(checkboxElem.id === "id_choiced"){

            }
            else if(checkboxElem.checked){
                formgroups[i+1].style.display ="block";
            }
            else{
                formgroups[i+1].style.display = "none";
            }
        }
    });
}
for(var i=0; i<radios.length;i++){
    radios[i].addEventListner("change",checkVisibility);
}
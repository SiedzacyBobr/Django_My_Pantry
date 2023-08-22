
var nrfoto = 0

function hidefoto(){
    $("#passions").fadeOut(500);
    }


function next_passion(){

    nrfoto++; if(nrfoto>7) nrfoto=1;

    var foto = "<img src=\"/static/image/fotopassion1/passion" + nrfoto +".jpg\" />"

    document.getElementById("passions").innerHTML= foto;

    $("#passions").fadeIn(500);

    setTimeout("next_passion()", 5000);
    setTimeout("hidefoto()", 4500);
}

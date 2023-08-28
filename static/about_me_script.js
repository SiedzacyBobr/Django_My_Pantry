
let slideIndex = 0;
nextPassion();


function nextPassion()  {
  let i;
  let slides = document.getElementsByClassName("passion");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";  
  
  setTimeout(nextPassion, 5000);
}


function myMenu(){
  var deve = document.getElementById("myNavbar");

  if (deve.className === "navbar"){
    deve.className += " responsive";
  } else {
    deve.className = "navbar";
  }

}


// testy i nauka Djqery 



function pythonp(){
  $("#pythoni").animate({fontSize: '2rem'});
  $("#pythoni").animate({ fontSize: '3rem'});
};

function htmlp(){
  $("#htmli").animate({fontSize: '2rem'});
  $("#htmli").animate({ fontSize: '3rem'});
};

function cssp(){
  $("#cssi").animate({fontSize: '2rem'});
  $("#cssi").animate({ fontSize: '3rem'});
};

function jsp(){
  $("#jsi").animate({fontSize: '2rem'});
  $("#jsi").animate({ fontSize: '3rem'});
};

function databasep(){
  $("#databasei").animate({fontSize: '2rem'});
  $("#databasei").animate({ fontSize: '3rem'});
};

function bootstrapp(){
  $("#bootstrapi").animate({fontSize: '2rem'});
  $("#bootstrapi").animate({ fontSize: '3rem'});
};

function reactp(){
  $("#reacti").animate({fontSize: '2rem'});
  $("#reacti").animate({ fontSize: '3rem'});
};

function gitp(){
  $("#giti").animate({fontSize: '2rem'});
  $("#giti").animate({ fontSize: '3rem'});
};

function wordpressp(){
  $("#wordpressi").animate({fontSize: '2rem'});
  $("#wordpressi").animate({ fontSize: '3rem'});
};

function linuxp(){
  $("#linuxi").animate({fontSize: '2rem'});
  $("#linuxi").animate({ fontSize: '3rem'});
};

function darkscreen(){
  $(".description, section, .bulkPackage").toggleClass("darkarticle");
  $("body").toggleClass("darkbody");
  $(".skills,.passion figcaption, nav").toggleClass("darkstripes");
  $("h2, h3, .description, figcaption").toggleClass("silvertext");



}


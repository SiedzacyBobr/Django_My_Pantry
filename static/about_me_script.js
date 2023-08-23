
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

function clickTest() {
  document.getElementById("demo").innerHTML="coś tam coś tam - trójząb";
}


function myMenu(){
  var deve = document.getElementById("myNavbar");

  if (deve.className === "navbar"){
    deve.className += " responsive";
  } else {
    deve.className = "navbar";
  }

}
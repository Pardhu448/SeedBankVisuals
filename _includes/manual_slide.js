//var slideIndex = 1;
//showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides_man(slideIndex_1 += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides_man(slideIndex_1 = n);
}

function showSlides_man(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex_1 = 1} 
  if (n < 1) {slideIndex_1 = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex_1-1].style.display = "block"; 
  dots[slideIndex_1-1].className += " active";
}
/*
var slideIndex = 0;
//slides_len = document.getElementsByClassName("mySlides")
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    slideIndex++;
    if (slideIndex> slides.length) {slideIndex = 1} 
    slides[slideIndex-1].style.display = "block"; 
    setTimeout(showSlides, 3000); // Change image every 5 seconds
}
*/
$(document).ready(function() {
  // changing background Navbar when scrolled
 $(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar-fixed-top");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});
  
});



$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){  
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});


 
const openFile1=e=>{
  $("#PRODUCTS").click()
}
const openFile2=e=>{
  $("#ORDERS").click()
}
const openFile3=e=>{
  $("#ORDER_PRODUCTS_TRAIN").click()
}
const openFile4=e=>{
  $("#ORDER_PRODUCTS_PRIOR").click()
}
const openFile5=e=>{
  $("#AILES").click()
}

const openFile6=e=>{
  $("#DEPARTMENTS").click()
}




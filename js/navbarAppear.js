(function ($) {
  $(document).ready(function(){
    // hide .navbar first
    $(".headerDisplay").hide();
    // fade in .navbar
    $(function () {
      $(window).scroll(function () {
      // set distance user needs to scroll before we start fadeIn
        if ($(this).scrollTop() > 800) {
          $('.headerDisplay').fadeIn();
        } else {
          $('.headerDisplay').fadeOut();
        }
      });
    });
  });
}(jQuery));
  var footerResize = function() {
    $('#footer').css('position', $("body").height() + $("#footer").innerHeight() > $(window).height() ? "inherit" : "fixed");
  };
  $(window).resize(footerResize).ready(footerResize);
//The purpose of this code is to get the table generated by the GWT code inside
//of a div to be styled.  The issue is that for some currently unknown reason the
//table is generated at a point after the page has loaded, so it cannot be selected easily.
//The code below is a poor solution to get access to the table generated by the GWT code.
//However, I have tried both using jQuery's $(document).ready and
// document.addEventListener("DOMContentLoaded", function(e) {wrap table}) to no avail.
//Adding a timeout is the only thing that has worked.


setTimeout(() => {
  $(".javatable").wrapAll("<div class='javatablecontainer' />");
}, 1000);
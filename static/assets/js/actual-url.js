$(document).ready(function () {
  var formatStr = $("#url-actual-web").html();
  formatStr = formatStr.replaceAll("www.example.com", window.location.href);
  $("#url-actual-web").html(formatStr);
});

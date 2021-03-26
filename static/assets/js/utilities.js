$(document).ready(function () {
  var birthday = new Date("04/30/1994");
  var diff = Date.now() - birthday.getTime();

  var formatStr = $("#actual-age").html();
  formatStr = formatStr.replaceAll(
    "99",
    Math.floor(diff / (1000 * 60 * 60 * 24 * 365.25))
  );
  $("#actual-age").html(formatStr);
});

window.setTimeout(function () {
  $(".alert")
    .fadeTo(500, 0)
    .slideUp(500, function () {
      $(this).remove();
    });
}, 1000);

$(document).ready(function () {
  $(".btn").click(function (e) {
    e.preventDefault();
    $.ajax({
      url: "",
      type: "GET",
      data: {
        request_text: $(this).text(),
      },
      dataType: "json",
      success: function (response) {
        $(".btn").text(response.response_text);
        $("#seconds").append(
          '<li class="list-group-item">' + response.response_text + "</li>"
        );
      },
      error: function (e) {
        console.error("Error receiving response ", e.statusText);
      },
    });
  });
});

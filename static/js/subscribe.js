$('#subscribe').submit(function(e){
      e.preventDefault();
      var email_address = $("#email_address").val();
      if(email_address){
        var csrfmiddlewaretoken = csrftoken;
        var email_data = {"email_address": email_address,
                          "csrfmiddlewaretoken" : csrfmiddlewaretoken};
        $.ajax({
          type : 'POST',
          url :  '/subscribe/',
          data : email_data,
          success : function(response){
            $('#email_address').val('');
            if(response.status == "200"){
              alert("Thank you for subscribing to the newsletter. Opt out via email or contact us at hello@jinevra.ai to unsubscribe.");
            }
            if(response.status == "404"){
              alert("This email address cannot be subscribed to our mailing list. Email hello@jinevra.ai for assistance.");
            }
          },
          error: function(response) {
            alert("This email address cannot be subscribed to our mailing list. Email hello@jinevra.ai for assistance.");
            $('#email_address').val('');
          }
        });
        return false;
      }
      else{
        alert("Please provide a valid email address to subscribe.");
      }
  });


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
})

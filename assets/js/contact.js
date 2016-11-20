$(document).ready(function() {

  $('#feedbackForm input')
    .not('.optional,.no-asterisk')
    .after('<span class="glyphicon glyphicon-asterisk form-control-feedback"></span>');

  $("#feedbackSubmit").click(function() {
    var $btn = $(this);
    $btn.button('loading');
    contactForm.clearErrors();

    //do a little client-side validation -- check that each field has a value and e-mail field is in proper format
    var hasErrors = false;
    $('#feedbackForm input,textarea').not('.optional').each(function() {
      var $this = $(this);
      if (($this.is(':checkbox') && !$this.is(':checked')) || !$this.val()) {
        hasErrors = true;
        contactForm.addError($(this));
      }
    });
    var $email = $('#email');
    if (!contactForm.isValidEmail($email.val())) {
      hasErrors = true;
      contactForm.addError($email);
    }


    //if there are any errors return without sending e-mail
    if (hasErrors) {
      $btn.button('reset');
      return false;
    }

    //send the feedback e-mail
    $.ajax({
      type: "POST",
      url: "sendmail.php",
      data: $("#feedbackForm").serialize(),
      success: function(data) {
        contactForm.addAjaxMessage(data.message, false);
        contactForm.clearForm();
        //get new Captcha on success
        $('#captcha').attr('src', '../assets/securimage/securimage_show.php?' + Math.random());
      },
      error: function(response) {
        contactForm.addAjaxMessage(response.responseJSON.message, true);
      },
      complete: function() {
        $btn.button('reset');
      }
   });
    return false;
  });
  $('#feedbackForm input').change(function () {
    var asteriskSpan = $(this).siblings('.glyphicon-asterisk');
    if ($(this).val()) {
      asteriskSpan.css('color', '#00FF00');
    } else {
      asteriskSpan.css('color', 'black');
    }
  });
});

//namespace as not to pollute global namespace
var contactForm = {
  isValidEmail: function (email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
  },
  clearErrors: function () {
    $('#emailAlert').remove();
    $('#feedbackForm .help-block').hide();
    $('#feedbackForm .form-group').removeClass('has-error');
  },
  clearForm: function () {
    $('.glyphicon-asterisk').css('color', 'black');
    $('#feedbackForm input,textarea').val("");
  },
  addError: function ($input) {
    var parentFormGroup = $input.parents('.form-group');
    parentFormGroup.children('.help-block').show();
    parentFormGroup.addClass('has-error');
  },
  addAjaxMessage: function(msg, isError) {
    $("#feedbackSubmit").after('<div id="emailAlert" class="alert alert-' + (isError ? 'danger' : 'success') + '" style="margin-top: 5px;">' + $('<div/>').text(msg).html() + '</div>');
  }
};

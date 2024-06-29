function message(text, state) {
  const msg = $('#successMsg').clone(true);
  $($($(msg).children()).children()[1]).text(text);
  $('#message').append($(msg));
  $(msg).toggleClass(`${state} animate__animated animate__fadeInRight`);
  $('#send-request-form').trigger('reset');// reset form
  setTimeout(function () {
    $(msg).toggleClass(`${state} animate__animated animate__fadeInRight`);
    $(msg).toggleClass(`${state} animate__animated animate__fadeOutRight`);
    setTimeout(function () {
      $(msg).toggleClass(`${state} animate__animated animate__fadeOutRight`);
      $(msg).remove();
    }, 1000);
  }, 2100);
}

function loader(state) { // on sending data to server
  if (state == 'wait') {
    $('#btn').hide();
    $('#entry-form .loader').show();
  } else if (state == 'done') {
    $('#btn').show();
    $('#entry-form .loader').hide();
  }
}

$(document).ready(function () {
  $('#btn').click(() => {
    loader('wait');
    if (
      $($('#entry-form').children()[2]).val() == '' ||
      $($('#entry-form').children()[3]).val() == ''
    ) {
      message('یک یا چند فیلد خالی می باشد', 'error');
      loader('done');
    } else {
      // submit form

    }
  });
});

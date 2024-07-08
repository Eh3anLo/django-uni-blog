// function message(text, state) {
//   const msg = $('#successMsg').clone(true);
//   $($($(msg).children()).children()[1]).text(text);
//   $('#message').append($(msg));
//   $(msg).toggleClass(`${state} animate__animated animate__fadeInRight`);
//   $('#send-request-form').trigger('reset');
//   setTimeout(function () {
//     $(msg).toggleClass(`${state} animate__animated animate__fadeInRight`);
//     $(msg).toggleClass(`${state} animate__animated animate__fadeOutRight`);
//     setTimeout(function () {
//       $(msg).toggleClass(`${state} animate__animated animate__fadeOutRight`);
//       $(msg).remove();
//     }, 1000);
//   }, 2100);
// }
// function loader(state) {
//   if (state == 'wait') {
//     $('#submitBtn').hide();
//     $('#send-request-form .loader').show();
//   } else if (state == 'done') {
//     $('#submitBtn').show();
//     $('#send-request-form .loader').hide();
//   }
// }
// $(document).ready(function () {
//   $('#submitBtn').click(() => {
//     loader('wait');
//     if (
//       $($('#send-request-form input')[1]).val() == '' ||
//       $($('#send-request-form input')[2]).val() == '' ||
//       $($('#send-request-form input')[3]).val() == '' ||
//       $($('#send-request-form input')[4]).val() == '' ||
//       $($('#send-request-form input')[5]).val() == '' ||
//       $($('#send-request-form input')[6]).val() == ''

//     ) {
//       message('یک یا چند فیلد خالی می باشد', 'error');
//       loader('done');
//     } else {
      
//     }
//   });
// });

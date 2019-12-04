$(document).ready(function() {
    $('#yes').click(() => handleBtnClick('yes'));
    $('#no').click(() => handleBtnClick('no'));
    $('#save-interest-btn').click(() => saveInterest({
      userId: userId, interest: $('input[name="interest"]:checked').val()
    }));
});

function saveInterest(data) {
  $('#save-interest-btn').prop('disabled', true);
  toggleLoaderInBtn('#save-interest-btn', true);
  $.ajax({
    type: "POST",
    url: '/user/interest',
    data: data,
    success: function(resp) {
      // reloading page on success to show modal page
      window.location.reload(true);
    },
    error: function(err) {
      console.log('Some error occurred', err);
    }
  });
}

function handleBtnClick(actionPath) {
  toggleLoaderInBtn('#' + actionPath, true);
  setBtnsDisable(true);

  callModalActionApi(actionPath)
    .then(function(resp) {
      return getNextUser();
    })
    .then(function(userDetails) {
      setUserDataInView(userDetails);
    })
    .catch(function(err) {
      console.log('Some error occurred', err);
    })
    .always(function() {
      toggleLoaderInBtn('#' + actionPath, false);
      setBtnsDisable(false);
    });
}

function setUserDataInView(userDetails) {
  const userName = `${userDetails.firstName} ${userDetails.lastName}`
  $("#profile-title").text(userName);
  $("#profile-image").css('background-image', `url(${userDetails.imageURL})`);
}

function setBtnsDisable(isDisabled) {
  $("#action-btns").find(".btn").prop('disabled', isDisabled);
}

function toggleLoaderInBtn(btnSelector, showLoader) {
  let $element = $(btnSelector);
  const classNames = 'animated loading loading-white u-center hide-text';
  if (showLoader) {
    $element.addClass(classNames);
  } else {
    $element.removeClass(classNames);
  }
}

function callModalActionApi(path) {
    return $.get('/minder/' + path);
}

// TODO: pass user details
function getNextUser() {
    return $.get('/minder/randomUser');
}

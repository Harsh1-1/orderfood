$(document).ready(function() {
    $('#yes').click(() => handleBtnClick('yes'));
    $('#no').click(() => handleBtnClick('no'));
});

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
  $("#action-btns").find(".btn").attr('disabled', isDisabled);
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

function getNextUser() {
    return $.get('/minder/randomUser');
}

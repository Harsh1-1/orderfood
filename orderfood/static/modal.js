$(document).ready(function() {
    $('#yes').click(() => handleBtnClick('yes'));
    $('#no').click(() => handleBtnClick('no'));
});

function handleBtnClick(actionPath) {
  toggleLoaderInBtn('#' + actionPath, true);
  setBtnsDisable(true);

  callModalActionApi(actionPath)
    .then(function(resp) {
      console.log(resp);
      return getNextImage();
    })
    .then(function(imageData) {
      // TODO: set new image in card
    })
    .catch(function(err) {
      console.log('Some error occurred', err);
    })
    .always(function() {
      toggleLoaderInBtn('#' + actionPath, false);
      setBtnsDisable(false);
    });
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

function getNextImage() {
    // TODO: add api url for get image
    return $.get('/');
}

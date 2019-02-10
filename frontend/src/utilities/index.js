import jQuery from "jquery";
import _ from "lodash";


/**
 * Tired of typing console.log? Become more like a Pythoneer and use print!
 *
 * @param {object} args - The things to print
 */
export function print(args) {
  console.log(...args);
}


/**
 *  DJANGO_VARS are stored in the `sessionStorage` when index.html is first
 *  severed. This function parses this item into a `JSON` object. Currently
 *  stores:
 *
 *    - is_authenticated {bool} - Whether the requesting user is logged in.
 *    - username {string} -  The requesting users username
 *    - version {string} - Version string of the currently running build.
 *
 *  @returns {Object}
 *
 */
export function getDjangoData() {
  let data = sessionStorage.getItem('DJANGO_VARS');
  if (_.isNil(data)) {
    return {};
  } else {
    return JSON.parse(data);
  }
}


/**
 * Adapted from django's documentation. Gets the csrf token from cookie data.
 *
 * @param {string} name - Cookie name.
 *
 *  @returns {string} token value
 */
export function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


export default {
  getCookie,
  getDjangoData,
  print,
}
import Vue from 'vue'

import router from "./router/index"
import store from "./store/index"

import App from "./App.vue"

import './styles/index.css'


const app = new Vue({
  el: '#app',
  router: router,
  store: store,
  components: {
    App,
  }
});

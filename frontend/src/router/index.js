import Vue from 'vue'
import Router from 'vue-router'

import Index from "../views/Index"
import PageNotFound from "../views/PageNotFound"
import Forbidden from "../views/Forbidden"
import ProfileView from "../views/ProfileView"

import {getDjangoData} from "../utilities";


Vue.use(Router);


let router = new Router({
  routes: [
    {
      path: "/",
      name: "index",
      component: Index
    },
    {
      path: '/profile',
      component: ProfileView,
      meta: {
        requiresAuth: true
      },
    },
    {
      path: "/forbidden",
      name: "forbidden",
      component: Forbidden
    },
    {
      path: "*",
      name: "page-not-found",
      component: PageNotFound,
    }
  ]
});


function userIsAuthenticated() {
  let djangoVars = getDjangoData();
  if (_.isNil(djangoVars)) {
    return false;
  } else {
    return djangoVars.isAuthenticated;
  }
}


router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (!userIsAuthenticated()) {
      next({
        path: '/forbidden',
        params: { nextUrl: to.fullPath }
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
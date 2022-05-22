import Vue from 'vue'
import VueRouter from 'vue-router'
import IntroView from '../views/IntroView.vue'

import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileView from '../views/ProfileView.vue'
import MileageShopView from '../views/MileageShopView.vue'

import MovieListView from '../views/MovieListView.vue'
import ArticleListView from '../views/ArticleListView'

import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'intro',
    component: IntroView
  },
  {
    path: 'article/',
    name: 'article',
    component: ArticleListView
  },

  {
    path: 'movie/',
    name: 'movie',
    component: MovieListView
  },
  {
    path: 'mileageShop/',
    name: 'mileageShop',
    component: MileageShopView
  },
  {
    path: 'profile/',
    name: 'profile',
    component: ProfileView
  },
  {
    path: 'login/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

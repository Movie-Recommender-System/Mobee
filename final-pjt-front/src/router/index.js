import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import CommunitySearchView from '../views/CommunitySearchView.vue'
import CommunityView from '../views/CommunityView.vue'
import IntroView from '../views/IntroView.vue'
import MilelageShopView from '../views/MilelageShopView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import MovieHomeView from '../views/HomeView.vue'
import MovieSearchView from '../views/MovieSearchView.vue'
import ProfileView from '../views/ProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: 'communitySearch/',
    name: 'communitySearch',
    component: CommunitySearchView
  },
  {
    path: 'community/',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/',
    name: 'intro',
    component: IntroView
  },
  {
    path: 'movieDetail/',
    name: 'movieDetail',
    component: MovieDetailView
  },
  {
    path: 'movieSearch/',
    name: 'movieSearch',
    component: MovieSearchView
  },
  {
    path: 'movieHome/',
    name: 'movieHome',
    component: MovieHomeView
  },
  {
    path: 'milelageShop/',
    name: 'milelageShop',
    component: MilelageShopView
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

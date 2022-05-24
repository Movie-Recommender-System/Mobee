import Vue from 'vue'
import Vuex from 'vuex'

import articles from './modules/articles.js'
import accounts from './modules/accounts.js'
import movies from './modules/movies.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, articles, movies },
})

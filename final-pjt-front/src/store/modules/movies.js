import router from '@/router'
import drf from "@/api/drf"
import axios from "axios"


export default {
  state: {
    movies: [],
    movie: {},
    new_movies: {},
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
  },
  mutations: {

  },
  actions: {
    fetchMovies({ commit, getters }, kind) {
      axios({
        url: drf.movies.movies(kind),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchRecommendMovies({ commit, getters }) {
      axios({
        url: drf.movies.recommendMovies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchMovie({ commit, getters }, moviePK) {
      axios({
        url: drf.movies.movie(moviePK),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    createMovies({ commit, getters }) {
      axios({
        url: drf.articles.createMovie(),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('NEW_MOVIES', res.data)
          alert('성공적으로 최신 영화를 받아왔습니다!')
        })
    },

    wishMovie( {commit, getters }) {
      axios({
        url: drf.articles.movie(),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    createReview({ commit, getters }, { moviePk, content }) {
      const review = { content }

      axios({
        url: drf.articles.comments(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEW', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateReview({ commit, getters }, { moviePk, reviewPk, content }) {
      const review = { content }

      axios({
        url: drf.articles.comment(moviePk, reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { moviePk, reviewPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.comment(moviePk, reviewPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_ARTICLE_COMMENTS', res.data)
          })
          .catch(err => console.error(err.response))
      }
    },
  },
}

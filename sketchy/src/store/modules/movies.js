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
    new_movies: state => state.new_movies,
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    NEW_MOVIES: (state, new_movies) => state.new_movies = new_movies,
  },
  actions: {
    fetchMovies({ commit }, kind) {
      axios({
        url: drf.movies.movies(kind),
        method: 'get',
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

    fetchMovie({ commit, getters }, moviePk) {
      // 로그인 한 경우 찜했는지 여부가 다르다!
      if (getters.isLoggedIn) {
        axios({
          url: drf.movies.movie(moviePk),
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
      // 로그인하지 않은 경우
      } else {
        axios({
          url: drf.movies.movie(moviePk),
          method: 'get',
        })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
      }
    },

    createMovies({ commit, getters }) {
      axios({
        url: drf.movies.createMovie(),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('NEW_MOVIES', res.data)
          alert('성공적으로 최신 영화를 받아왔습니다!')
        })
        .catch(err => console.error(err.response))
    },

    wishMovie( { commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    createReview({ dispatch, getters }, { moviePk, content, score }) {
      const review = { content, score }

      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(() => dispatch('fetchMovie', moviePk))
        .catch(err => {
          if (err.response.status === 403) {
            alert(err.response.data)
          } else {
            console.error(err.response)
          }
        })
    },

    updateReview({ dispatch, getters }, { moviePk, reviewPk, content, score }) {
      const review = { content, score }

      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader,
      })
        .then(() => dispatch('fetchMovie', moviePk))
        .catch(err => {
          if (err.response.status === 403) {
            alert(err.response.data)
          }
          else if (err.response.status === 401) {
            alert('로그인 하세요.')
          } 
          else {
            console.error(err.response)
          }
        })
    },

    deleteReview({ dispatch, getters }, { moviePk, reviewPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.review(moviePk, reviewPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(() => dispatch('fetchMovie', moviePk))
          .catch(err => {
            if (err.response.status === 403) {
              alert(err.response.data)
            } 
            else if (err.response.status === 401) {
              alert('로그인 하세요.')
            } 
            else {
              console.error(err.response)
            }
          })
      }
    },

    likeReview( { getters, dispatch }, { reviewPk, moviePk }) {
      axios({
        url: drf.movies.likeReview(reviewPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(() => dispatch('fetchMovie', moviePk))
        .catch(err => console.error(err.response))
    },
  },
}
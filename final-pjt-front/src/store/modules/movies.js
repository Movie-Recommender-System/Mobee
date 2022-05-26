import router from '@/router'
import drf from "@/api/drf"
import axios from "axios"
import _ from 'lodash'

export default {
  state: {
    movies: [],
    movie: {},
    genres: [],
    newMovies: {},      // 새로 영화 받아올 때 보여주기 위함
    moviesKind: '',    // 좋아요 버튼 클릭 시 영화 리스트의 하트도 변경
    isDownload: false,  // 영화 받아오는 중
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    newMovies: state => state.newMovies,
    moviesKind: state => state.moviesKind,
    isMovies: state => !_.isEmpty(state.movies),
    genres: state => state.genres,
    isDownload: state => state.isDownload,
  },
  mutations: {
    SET_MOVIES: (state, { movies, kind }) => {
      state.movies = movies
      state.moviesKind = kind
    },
    SET_MOVIE: (state, movie) => state.movie = movie,
    NEW_MOVIES: (state, newMovies) => {
      state.newMovies = newMovies
      state.isDownload = false
    },
    SET_GENRES: (state, genres) => state.genres = genres,
    SET_DOWNLOAD: state => state.isDownload = true
  },
  actions: {
    fetchGenres( {commit} ) {
      axios({
        url: drf.movies.genres(),
        method: 'get',
      })
        .then(res => commit('SET_GENRES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchMovies({ commit }, kind) {
      axios({
        url: drf.movies.movies(kind),
        method: 'get',
        // headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', {'movies' : res.data, 'kind' : kind}))
        .catch(err => console.error(err.response))
    },

    fetchRecommendMovies({ commit, getters }) {
      axios({
        url: drf.movies.recommendMovies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', {'movies' : res.data, 'kind' : 'recommend'}))
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
      if (confirm('정말 다운로드하시겠습니까?')) {
        commit('SET_DOWNLOAD')
        axios({
          url: drf.movies.createMovies(),
          method: 'post',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('NEW_MOVIES', res.data)
            setTimeout(() => {      
              alert('성공적으로 최신 영화를 받아왔습니다!')
              alert(getters.newMovies.movies)
            }, 500)
          })
          .catch(err => console.error(err.response))
      }
    },

    wishMovie( { commit, getters, dispatch }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
          dispatch('fetchMovies', getters.moviesKind)
        })
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

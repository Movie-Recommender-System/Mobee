import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    articles: [],
    article: {},
    onUpdateArticleModal: false,
    articlePage: 1,
    articleCount: 0,
  },

  getters: {
    articles: state => state.articles,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle: state => !_.isEmpty(state.article),
    articlePage: state => state.articlePage,
    articleCount: state => state.articleCount,
  },

  mutations: {
    SET_ARTICLES: (state, data) => {
      state.articles = data.articles
      state.articleCount = data.count
    },
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments),
    SET_ARTICLE_PAGE: (state, page) => state.articlePage = page,
  },

  actions: {    
    pageChange({ commit, dispatch }, page) {
      commit('SET_ARTICLE_PAGE', page)
      dispatch('fetchArticles')
    },

    fetchArticles({ commit, getters }) {
      axios({
        url: drf.articles.articles(getters.articlePage),
        method: 'get',
      })
        .then(res => commit('SET_ARTICLES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchArticle({ commit, getters }, articlePk) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.articles.article(articlePk),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_ARTICLE', res.data))
          .catch(err => {
            console.error(err.response)
            if (err.response.status === 404) {
              router.push({ name: 'NotFound404' })
            }
          })
      } else {
        axios({
          url: drf.articles.article(articlePk),
          method: 'get',
        })
          .then(res => commit('SET_ARTICLE', res.data))
          .catch(err => {
            console.error(err.response)
            if (err.response.status === 404) {
              router.push({ name: 'NotFound404' })
            }
          })
      }
    },

    createArticle({ commit, getters, dispatch }, article) {   
      axios({
        url: drf.articles.articles(),
        method: 'post',
        data: article,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          dispatch('fetchArticles')
        })
        .catch(err => console.error(err.response))
    },

    updateArticle({ commit, getters, dispatch }, { pk, title, content}) {
      axios({
        url: drf.articles.article(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          dispatch('fetchArticles')
        })
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

    deleteArticle({ commit, getters, dispatch }, articlePk) { 
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            dispatch('fetchArticles')
          })
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

    likeArticle({ commit, getters, dispatch }, articlePk) {
      axios({
        url: drf.articles.likeArticle(articlePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          dispatch('fetchArticles')
        })
        .catch(err => console.error(err.response))
    },

		createComment({ commit, getters, dispatch }, { articlePk, content }) {
      const comment = { content }

      axios({
        url: drf.articles.comments(articlePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
          dispatch('fetchArticles')
        })
        .catch(err => console.error(err.response))
    },

    updateComment({ commit, getters }, { articlePk, commentPk, content }) {
      const comment = { content }

      axios({
        url: drf.articles.comment(articlePk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch(err => {
          if (err.response.status === 403) {
            alert(err.response.data)
          }
          console.error(err.response)
        })
    },

    deleteComment({ commit, getters, dispatch }, { articlePk, commentPk }) {
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.articles.comment(articlePk, commentPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_ARTICLE_COMMENTS', res.data)
              dispatch('fetchArticles')
            })
            .catch(err => {
              if (err.response.status === 403) {
                alert(err.response.data)
              }
              console.error(err.response)
            })
        }
      },
  },
}
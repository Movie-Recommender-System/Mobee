import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'

export default {
  state: {
    articles: [],
    article: {},
  },

  getters: {
    articles: state => state.articles,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle: state => !_.isEmpty(state.article),
    // !_.isEmpty : 값이 비어있는지 확인하여 boolean값으로 반환해주는 lodash 기능 (예외: 숫자타입이면 어려움)

  },

  mutations: {
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state,comments) => (state.article.comments = comments),
  },

  artions: {

    // 게시글 목록 받아오기 (GET: articles URL (token))

    // 성공 => 응답받은 게시글을 state.articles에 저장
    // 실패 => 에러 메시지
    fetchArticles({ commit, getters }) {
      axios({
        url: drf.articles.articles(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLES', res.data))
        .catch(err => console.error(err.response))
    },


    // 하나의 게시글 받아오기 (GET: article URL (token))

    // 성공 => 응답받은 게시글들을 state.articles에 저장 (article에 저장)
    // 실패 => 단순에러면 에러메시지, 404에러면 NotFount404로 이동
    fetchArticle({ commit, getters }, articlePk) {
      axios({
        url: drf.articles.article(articlePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then( res => commit('SET_ARTICLE', res.data))
        .catch( err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },



    // 게시글 생성 (POST: articles URL (게시글입력정보, token))

    // 성공 => 응답받은 게시글을 state.article에 저장, ArticleDetailView로 이동
        // (생각: ArticleList까지만 View로 하고, ArticleDetail은 모달로 띄우고, 댓글도 그 안에 삽입하고 싶은데, 방법있을까?)
    // 실패 => 에러메시지
    createArticle({ commit, getters }, article) {
      
      // (!? 추가) 게시글 내용이 차있는지 확인 후 요청보냄
      if (article.isArticle) {

        axios({
          url: drf.articles.articles(),
          method: 'post',
          data: article,
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_ARTICLE', res.data)
            router.push({
              name: 'community',
              params: { articlePk: getters.article.pk }
            })
          })
      }
    },



    // 게시글 수정 (POST: article URL (게시글 입력정보, token)
    
    // 성공 => 응답받은 게시글을 state.article에 저장, ArticleDetialView로 이동
    // 실패 => 에러메시지

    updateArticle({ commit, getters }, { pk, title, content}) {
      if (article.isArticle()) {
        axios({
          url: drf.articles.article(pk),
          method: 'put',
          data: { title, content },
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_ARTICLE', res.data)
            router.push({
              name: 'communityDetail',
              params: { articlePk: getters.article.pk }
            })
          })
      }
    },



    // 게시글 삭제 (DELETE: article URL (token))
    
    // 사용자가 확인을 받고 토큰 axios 요청했을 때,
    // 성공 => state.article 비우기, ArticleListView로 이동
    // 실패 => 에러메시지

    deleteArticle({ commit, getters }, articlePk) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {}) // state의 게시글 내용을 지움
            router.push({ name: 'community' })
          })
          .catch(err => console.error(err.response))
      }
    },



    // 게시글 좋아요 (POST: likeArticle URL(token))

    // 성공 => state.article 갱신
    // 실패 => 에러메시지

    likeArticle({ commit, getters }, articlePk) {
      axios({
        url: drf.articles.likeArticle(articlePk),
        method: 'POST',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ARTICLE', res.data))
        // .catch(err => console.error(err.response))
        .catch(err => console.error(err.response))
    },



    // 댓글 생성 (POST: comments URL(댓글입력정보, token))

    // 성공 => 응답으로 state.article의 comments 갱신
    // 실패 => 에러메시지

    createComment({ commit, getters}, { articlePk, content }) {
      const comment = { content }

      axios({
        url: drf.articles.comments(articlePk),
        method: 'POST',
        headers: getters.authHeader,
      })
        .then( res => {
          commit('SET_ARTICLE_COMMENTS', res.data)
        })
        .catch( err => console.err(err.response))
    },




    // 댓글 수정 (POST: comment URL (token))

    // 성공 => 응답으로 state.article의 comments 갱신
    // 실패 => 에러메시지

    updateComment({ commit, getters}, { articlePk, commentPk, content }) {
      const comment = { content }
      if (!comment.isEmpty) {
        axios({
          url: drf.articles.comment(articlePk, commentPk),
          method: 'POST',
          data: comment,
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_ARTICLE_COMMENTS', res.data)
          })
          .catch(err => console.error(err.response))
      }
    },



    // 댓글 삭제 (DELETE: comment URL (token))

    // (!? 추가) 

    // 사용자가 확인을 받고 요청을 보냈을 때
    // 성공 => 응답으로 state.article의 comments 갱신
    // 실패 => 에러메시지

    deleteComment({ commit, getters }, { articlePk, commentPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.comment(articlePk, commentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_ARTICLE_COMMENTS', res.data)
          })
          .catch(err => console.error(err.response))
      }
    }

    
    








  }
}
<template>
  <div>
    <div v-if="onUpdateArticleModal == true">
      <article-form :article='article' action="update"/>
    </div>
    <div v-else>
      <div class='d-flex justify-content-between'>
        <div>
          <h3>{{ article.title }}</h3>
          <p>content: {{ article.content }}</p>
        </div>
        <div v-if='article.user'>
          <div>작성자 : {{ article.user.username }}</div>
          <h4>
            <button v-if="isLoggedIn" @click='likeArticle(article.pk)'>
              <i v-if="article.is_liked" class="fa-solid fa-heart"></i>
              <i v-else class="fa-regular fa-heart"></i>
            </button>
            <i v-else class="fa-solid fa-heart"></i>
            {{ article.like_users.length }}
          </h4>
        </div>
      </div>
      <button @click="switchUpdateArticleModal" class='btn btn-warning'>수정</button>
      <button @click="deleteArticle(article.pk)" class="btn btn-danger">삭제</button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import ArticleForm from './ArticleForm.vue'

export default {
  name: 'ArticleDetail',
  components: { ArticleForm },
  computed: {
    ...mapGetters(['article', 'isLoggedIn', 'onUpdateArticleModal'])
  },
  methods: {
    ...mapActions(['likeArticle', 'updateArticle', 'deleteArticle', 'switchUpdateArticleModal']),
  },
}
</script>

<style>

</style>
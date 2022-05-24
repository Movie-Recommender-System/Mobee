<template>
  <div>
    <div class='d-flex justify-content-between'>
      <div>
        <h3>{{ article.title }}</h3>
        <p>content: {{ article.content }}</p>
      </div>
      <div>
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
    <button class='btn btn-warning'>수정</button>
    <button class="btn btn-danger">삭제</button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ArticleDetail',
  computed: {
    ...mapGetters(['article', 'isLoggedIn'])
  },
  methods: {
    ...mapActions(['likeArticle']),
  }
}
</script>

<style>

</style>
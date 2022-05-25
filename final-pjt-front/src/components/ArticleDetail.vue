<template>
  <div class="modal-body">
    <div>
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
            {{ article.like_users.length }}<br>
            <button @click="open" class='btn btn-warning'>수정</button>
            <button @click="deleteArticle(article.pk)" class="btn btn-danger">삭제</button>
          </h4>
        </div>
      </div>
      <div>
        <CommentList :comments='article.comments'/>
        <hr>
        <CommentForm :articlePk='article.pk'/>
      </div>
    </div>
    <modal name='updateModal' height="auto" width="50%">
      <ArticleForm :article='article' action="update"/>
    </modal>
  </div>
</template>



<script>
import { mapActions, mapGetters } from 'vuex'
import ArticleForm from './ArticleForm.vue'
import CommentList from './CommentList.vue'
import CommentForm from './CommentForm.vue'
import Vue from 'vue'
import VModal from 'vue-js-modal'
import 'vue-js-modal/dist/styles.css'

Vue.use(VModal)

export default {
  name: 'ArticleDetail',
  components: { ArticleForm, CommentList, CommentForm },
  computed: {
    ...mapGetters(['article', 'isLoggedIn', 'onUpdateArticleModal'])
  },
  methods: {
    ...mapActions(['likeArticle', 'updateArticle', 'deleteArticle']),
    open () {
      this.$modal.show('updateModal')
    },
  },
}
</script>

<style scoped>
  .modal-body{
      height: 100%;
      overflow-y: auto;
  }
</style>
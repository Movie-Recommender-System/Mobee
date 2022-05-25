<template>
  <div class="modal-body">
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
            {{ article.like_users.length }}<br>
            <button @click="switchUpdateArticleModal" class='btn btn-warning'>수정</button>
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
  </div>
</template>



<script>
import { mapActions, mapGetters } from 'vuex'
import ArticleForm from './ArticleForm.vue'
import CommentList from './CommentList.vue'
import CommentForm from './CommentForm.vue'

export default {
  name: 'ArticleDetail',
  components: { ArticleForm, CommentList, CommentForm },
  computed: {
    ...mapGetters(['article', 'isLoggedIn', 'onUpdateArticleModal'])
  },
  methods: {
    ...mapActions(['likeArticle', 'updateArticle', 'deleteArticle', 
    'switchUpdateArticleModal']),
  },
}
</script>

<style scoped>
  .modal-body{
      height: 100%;
      overflow-y: auto;
  }
  [id="heart"] {
  position: absolute;
  left: -100vw;
}

[for="heart"] {
  color: #aab8c2;
  cursor: pointer;
  font-size: 6em;
  align-self: center;  
  transition: color 0.2s ease-in-out;
}

[for="heart"]:hover {
  color: grey;
}

[for="heart"]::selection {
  color: none;
  background: transparent;
}

[for="heart"]::moz-selection {
  color: none;
  background: transparent;
}

[id="heart"]:checked + label {
  color: #e2264d;
  will-change: font-size;
  animation: heart 1s cubic-bezier(.17, .89, .32, 1.49);
}



@keyframes heart {0%, 17.5% {font-size: 0;}}

.button {
  border: none;
  outline:none;
  }

</style>
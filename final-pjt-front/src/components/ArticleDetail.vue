<template>
  <div class="modal-body px-5 py-3">
    <div class="container">
      <div class="row text-center py-5">
        <h3>{{ article.title }}</h3>
      </div>

      <div class="row justify-content-between py-2">
        <div class="col-2">
          
        </div>
        <div class="col-2">
          작성자 : {{ article.user.username }}
        </div>
      </div>
      <div class="row text-center py-2">
        <p>{{ article.content }}</p> 
      </div>
      <div v-if='article.user' class="row py-5 ">
           <h4>
               <a v-if="isLoggedIn" @click='likeArticle(article.pk)'>
              <i v-if="article.is_liked" class="fa-solid fa-heart text-danger"></i>
              <i v-else class="fa-regular fa-heart"></i>
            </a>
            <i v-else class="fa-solid fa-heart"></i>
            {{ article.like_users.length }}<br>
           </h4>
      </div>
      <div class='text-end opacity-50'>
        <p>작성시간 : {{ article.created_at }}</p>
        <p>수정시간 : {{ article.updated_at }}</p>
      </div>
      <div class='row pb-5 d-flex justify-content-end'>
        <div class="col-1"> </div>
        <button class="btn btn-warning col-2" @click="open" >수정</button>
        <div class="col-1"> </div>
        <button class="btn btn-danger col-2" @click="deleteArticle(article.pk)" >삭제</button>
        
      </div>
      <hr>
      <br><br><br>
      
      <h4>댓글 목록</h4>
      <div>
        <CommentList :comments='article.comments'/>

        <CommentForm :articlePk='article.pk'/>
      </div>
 
    <modal name='updateModal' height="auto" width="50%">
      <ArticleForm :article='article' action="update"/>
    </modal>
    </div>
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
    ...mapGetters(['article', 'isLoggedIn'])
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
<template>
  <div>
    <button class="btn btn-secondary" @click="open">새 게시물 만들기</button>
    <modal name='newArticle' height="auto" width="50%">
      <ArticleForm :article="article" action="create"/>
    </modal>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">제목</th>
          <th scope="col">User</th>
          <th scope="col">댓글 | 좋아요</th>
        </tr>
      </thead>
      <tbody>
        <ArticleListItem v-for="(article, index) in articles" 
        :key="article.pk" :index='index' :article='article'/>
      </tbody>
    </table>
    <div>
      <ul class="pagination">
        <li class="page-item" :class="{'disabled': currentPage === 1}">
          <a class="page-link" href="#">&laquo;</a>
        </li>
        <li class="page-item active" v-for="page in pages" :key="page">
          <a class="page-link" href="#">{{ page }}</a>
        </li>
        <li class="page-item" :class="{'disabled': currentPage === pages}">
          <a class="page-link">&raquo;</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import router from '@/router'
  import { mapActions, mapGetters } from 'vuex'
  import ArticleListItem from '@/components/ArticleListItem.vue'
  import ArticleForm from '@/components/ArticleForm.vue'
  import Vue from 'vue'
  import VModal from 'vue-js-modal'
  import 'vue-js-modal/dist/styles.css'

  Vue.use(VModal)

  export default {
    name: 'ArticleListView',  
    components: { ArticleListItem, ArticleForm },
    data () {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        },
        currentPage: 1
      }
    },
    computed: {
      ...mapGetters(['articles', 'isLoggedIn']),
      pages () {
        return Math.ceil(this.articles.length / 10)
      }
    },
    methods: {
      ...mapActions(['fetchArticles']),
      open () {
        if ( this.isLoggedIn ) {
          this.$modal.show('newArticle')
        } else {
          alert('로그인 하세요.')
          router.push({ name: 'login'})
        }
      }
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>
  
</style>
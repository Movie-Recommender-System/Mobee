<template>
  <div>
    <h1 class="text-center my-5">꿀영화 이야기 나누기</h1>
    <div class="container">
      <button class="btn btn-secondary mb-3" @click="open">새 게시물 만들기</button>
      <modal name='newArticle' height="auto" width="30%">
        <ArticleForm :article="article" action="create"/>
      </modal>
      
      <table class="table table-hover">
        <thead>
          <tr class="table-warning">
            <th scope="col">#</th>
            <th scope="col">제목</th>
            <th scope="col">User</th>
            <th scope="col">댓글</th>
            <th scope="col">좋아요</th>
            <th scope="col">작성시간</th>
            <th scope="col">수정시간</th>
          </tr>
        </thead>
        <tbody>
          <ArticleListItem v-for="(article, index) in articles" 
          :key="article.pk" :index='index' :article='article' />
        </tbody>
      </table>
      <div class="d-flex justify-content-center">
        <ul class="pagination pagination-lg">
          <li v-if="articlePage === 1" class="page-item disabled">
            <a class="page-link" >&laquo;</a>
          </li>
          <li v-else class="page-item" @click="pageChange(articlePage - 1)">
            <a class="page-link" >&laquo;</a>
          </li>
          <li class="page-item" @click="pageChange(page)"
          v-for="page in pages" :key="page" :class="{'active': articlePage === page}">
            <a v-if="articlePage - 2 <= page && articlePage + 2 >= page" 
              class="page-link" >{{ page }}</a>
          </li>
          <li v-if="articlePage === pages" class="page-item disabled">
            <a class="page-link" >&raquo;</a>
          </li>
          <li v-else class="page-item" @click="pageChange(articlePage + 1)">
            <a class="page-link" >&raquo;</a>
          </li>
        </ul>
      </div>
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
      }
    },
    computed: {
      ...mapGetters(['articles', 'isLoggedIn', 'articlePage', 'articleCount']),
      pages () {
        return Math.ceil(this.articleCount / 10)
      }
    },
    methods: {
      ...mapActions(['fetchArticles', 'pageChange' ]),
      open () {
        if ( this.isLoggedIn ) {
          this.$modal.show('newArticle')
        } else {
          alert('로그인 하세요.')
          router.push({ name: 'login'})
        }
      },
    },
    created() {
      this.fetchArticles(this.currentPage)
    },
  }
</script>

<style>
  
</style>
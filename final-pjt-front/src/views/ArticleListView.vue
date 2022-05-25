<template>
  <div>
    <h1 class="text-center my-5">꿀영화 이야기 나누기</h1>
    <div class="container">
      <button v-if="isLoggedIn" type="button" class="btn btn-secondary" data-bs-toggle="modal" 
      data-bs-target="#newModal">새 게시물 만들기</button>

      <div class="modal fade" id="newModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="staticBackdropLabel">Modal title</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <ArticleForm :article="article" action="create"/>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary">Understood</button>
            </div>
          </div>
        </div>
      </div>

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
            <a class="page-link" >{{ page }}</a>
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
<template>
  <div>
    <ArticleForm/>
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
        :key="article.pk" :index='index' :article_info='article'/>
      </tbody>
    </table>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ArticleListItem from '@/components/ArticleListItem.vue'
  import ArticleForm from '@/components/ArticleForm.vue'

  export default {
    name: 'ArticleListView',  
    components: { ArticleListItem, ArticleForm },
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      ...mapActions(['fetchArticles']),
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>
  
</style>
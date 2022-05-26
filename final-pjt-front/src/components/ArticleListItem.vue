<template>
  <tr :class="`table-${index % 2 ? dark: dark}`">
    <th scope="row">{{ articleNum }}</th>
    <td>
        <div class="row">
          <div type="button" @click.prevent="open" class="text text-truncate col-6">{{ article.title }}</div>
        </div>
      </td>
    <td>{{ article.user.username }}</td>
    <td>{{ article.comment_count }}</td>
    <td>{{ article.like_count }}</td>
    <td>{{ article.created_at }}</td>
    <td>{{ article.updated_at }}</td>
    <modal :name='modalName' width="50%" :adaptive="true" height="50%">
      <ArticleDetail/>
    </modal>
  </tr>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ArticleDetail from './ArticleDetail.vue'
  import Vue from 'vue'
  import VModal from 'vue-js-modal'
  import 'vue-js-modal/dist/styles.css'
  Vue.use(VModal)
  export default {
    name: 'ArticleListItem',
    components: { ArticleDetail },
    props: {
      index: Number,
      article: Object,
    },
    data () {
      return {
        modalName: this.article.pk + '',    // 게시글 별로 다른 모달 이름을 주기 위함.
        warning : "warning",
        dark : "light"
      }
    },
    computed: {
      ...mapGetters(['articlePage']),
      articleNum () {
        return (this.articlePage - 1) * 10 + this.index + 1
      }
    },
    methods: {
      ...mapActions(['fetchArticle']),
      open () {
        this.fetchArticle(this.article.pk)
        
        setTimeout(() => {      
          this.$modal.show(this.modalName)
        }, 100) 
      },
    }
  }
</script>

<style>
</style>
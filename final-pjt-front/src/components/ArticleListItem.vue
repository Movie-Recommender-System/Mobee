<template>
  <tr>
    <th scope="row">{{ index + 1 }}</th>
    <td><a href="" @click.prevent="open">{{ article.title }}</a></td>
    <td>{{ article.user.username }}</td>
    <td>{{ article.comment_count }} | {{ article.like_count }}</td>
    <modal :name='modalName' height="auto" width="50%">
      <ArticleDetail/>
    </modal>
  </tr>
</template>

<script>
  import { mapActions } from 'vuex'
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
        modalName: this.article.pk + ''    // 게시글 별로 다른 모달 이름을 주기 위함.
      }
    },
    methods: {
      ...mapActions(['fetchArticle']),
      open () {
        this.fetchArticle(this.article.pk)
        console.log(this.modalName)
        this.$modal.show(this.modalName)
      },
    }
  }
</script>

<style>
  
</style>
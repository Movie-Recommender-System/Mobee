<template>
  <tr>
    <th scope="row" @click="open">{{ index }}</th>
    <td @click="open">{{ article_info.title }}</td>
    <td @click="open">{{ article_info.user.username }}</td>
    <td @click="open">{{ article_info.comment_count }} | {{ article_info.like_count }}</td>
    <modal name='showArticle' height="auto" width="50%">
      <h3>{{ article.title }}</h3>
      <p>{{ article.content }}</p>
    </modal>
  </tr>
</template>

<script>
  import Vue from 'vue'
  import { mapGetters, mapActions } from 'vuex'
  import VModal from 'vue-js-modal'
  import 'vue-js-modal/dist/styles.css'

  Vue.use(VModal)

  export default {
    name: 'ArticleListItem',
    props: {
      index: Number,
      article_info: Object,
    },
    computed: {
      ...mapGetters(['article'])
    },
    methods: {
      ...mapActions(['fetchArticle']),
      open () {
        this.fetchArticle(this.article_info.pk)
        this.$modal.show('showArticle')
      }
    }
  }
</script>

<style>
  
</style>
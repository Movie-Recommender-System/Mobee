<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">title: </label>
      <input v-model="newArticle.title" type="text" id="title" />
    </div>
    <div>
      <label for="content">content: </label>
      <textarea v-model.trim="newArticle.content" type="text" id="content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },
    methods: {
      ...mapActions(['createArticle', 'updateArticle', 'switchUpdateArticleModal']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
          this.$modal.hide('newArticle')
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
          this.switchUpdateArticleModal()
        }
      },
    }
  }
</script>

<style>
  
</style>
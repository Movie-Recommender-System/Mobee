<template>
  <form @submit.prevent="onSubmit">
    <div class="container">
      <div class="row">
        <label class="fs-4" for="title">TITLE </label>
      </div>
      <div class="row">
        <input v-model="newArticle.title" type="text" id="title" placeholder="제목을 입력해 주세요."  required/>
      </div>

      <div class="row">
        <label class="fs-4" for="content">CONTENT </label>
      </div>
      <div class="row">
        <textarea v-model.trim="newArticle.content" type="text" id="content"  placeholder="내용을 입력해 주세요." required></textarea>
      </div>
    </div>
    <div class="mt-1">
      <button class="btn btn-secondary py-2"  style="width:100%;">{{ action }}</button>
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
      ...mapActions(['createArticle', 'updateArticle']),
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
          this.$modal.hide('updateModal')
        }
      },
    }
  }
</script>

<style scoped>
  
</style>
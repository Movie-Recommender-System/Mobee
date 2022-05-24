<template>
  <div>
    <h5>댓글 Create</h5>
    <form @submit.prevent="onSubmit">
      <div>
        <label for="content">content: </label>
        <textarea v-model.trim="content" type="text" id="content">
        </textarea>
      </div>
      <div>
        <button>생성</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'CommentForm',
  data () {
    return {
      content: '',
    }
  },
  props: {
    articlePk: Number,
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      const payload = {
        articlePk: this.articlePk,
        content: this.content,
      }
      this.createComment(payload)
      this.content = ''
    }
  }
}
</script>

<style>

</style>
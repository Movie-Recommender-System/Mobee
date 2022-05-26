<template>
  <div>
    <h5>Comment Create</h5>
    <form @submit.prevent="onSubmit">
      <div>
        <label for="content "></label>
        <textarea placeholder="댓글을 입력해 주세요." v-model.trim="content" type="text" id="content" style="width:100%;" required>
        </textarea>
      </div>
      <div>
        <button class="btn btn-outline-primary">생성</button>
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
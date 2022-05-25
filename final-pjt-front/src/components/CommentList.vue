<template>
  <div>
    <h4>댓글 목록</h4>
    <ul class="list-group mb-5">
      <CommentListItem v-for="comment in comments" :key="comment.pk" :comment="comment"/>
    </ul>
  </div>
</template>

<script>
  import CommentListItem from './CommentListItem.vue'
  export default {
    name: 'CommentList',
    components: { CommentListItem },
    props: { comments: Array },
  }
</script>

<style>
  
</style>
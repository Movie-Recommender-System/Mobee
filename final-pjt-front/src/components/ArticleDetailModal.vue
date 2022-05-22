<template>
  <div>
    <h3>ArticleDetailModal</h3>
    <CommentList/>
  </div>
</template>

<script>
  import CommentList from './CommentList.vue'
  export default {
    name: 'ArticleDetailModal',
    components: { CommentList },
  }
</script>

<style>
  
</style>
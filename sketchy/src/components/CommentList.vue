<template>
  <div>
    <h3>CommentList</h3>
    <CommentCreateForm/>
    <CommentListItem/>
  </div>
</template>

<script>
  import CommentListItem from './CommentListItem.vue'
  import CommentCreateForm from './CommentCreateForm.vue'

  export default {
    name: 'CommentList',  
    components: { CommentListItem, CommentCreateForm },
  }
</script>

<style>
  
</style>
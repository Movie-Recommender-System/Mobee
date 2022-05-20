<template>
  <div>
    <h3>CommentList</h3>
    <CommentForm/>
    <CommentListItem/>
  </div>
</template>

<script>
import CommentListItem from 'CommentListItem'
import CommentForm from 'CommentForm'
export default {
  name: 'CommentList',  
  components: { CommentListItem, CommentForm },
}
</script>

<style>
  
</style>
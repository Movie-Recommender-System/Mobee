<template>
  <li class="list-group-item">
    <div class="d-flex justify-content-between">
      <h5>{{ comment.content }}</h5>
      <p>{{ comment.user.username }}</p>
    </div>
  </li>
</template>

<script>

  export default {
    name: 'CommentListItem',
    props: { comment: Object},
  }
</script>

<style>
  
</style>
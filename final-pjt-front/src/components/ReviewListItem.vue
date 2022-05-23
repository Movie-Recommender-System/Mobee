<template>
  <li class="list-group-item d-flex justify-content-between align-items-center">
    <div class="align-top">
      <p>내용 : {{ review.content }}</p>
      <p>평점 : {{ review.score }}</p>
    </div>
    <i class="fa-regular fa-heart"></i>
    <i class="fa-solid fa-heart"></i>
    <div class="dropdown">
      <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
        <i class="fa-solid fa-gear"></i>
      </button>
      <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
        <li><button class="dropdown-item" type="button">삭제</button></li>
        <li><button class="dropdown-item" type="button">수정</button></li>
      </ul>
    </div>
  </li>
</template>

<script>
  export default {
    name: 'ReviewListItem',
    props: {review: Object },
  }
</script>

<style>
  .rotate {
    transform: rotate(90deg);
  }
</style>
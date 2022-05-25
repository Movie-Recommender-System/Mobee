<template>
  <li class="list-group-item">
    <div class="d-flex justify-content-between">

      <div v-if="isUpdate">
        <form @submit.prevent="onSubmit">
          <div>
            <label for="content">content: </label>
            <textarea v-model.trim="payload.content" type="text" id="content">
            </textarea>
          </div>
          <div>
            <button>수정</button>
          </div>
        </form>
      </div>
      <div class="py-4" v-else>
        <h5>{{ comment.content }}</h5>
        <p>{{ comment.user.username }}</p>
      </div>
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" 
        id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
          <i class="fa-solid fa-gear"></i>
          
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
          <li><button class="dropdown-item" type="button"
          @click='deleteComment({articlePk : comment.article, commentPk : comment.pk})'>
          삭제</button></li>
          <li><button class="dropdown-item" type="button" @click="isUpdate=true">
          수정</button></li>
        </ul>
      </div>
    </div>
  </li>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'CommentListItem',

    props: { comment: Object },
    data () {
      return {
        isUpdate : false,
        payload : {
          articlePk : this.comment.article,
          commentPk : this.comment.pk,
          content : this.comment.content
        }
      }
    },
    methods: {
      ...mapActions(['deleteComment', 'updateComment']),
      onSubmit () {
        this.updateComment(this.payload)
        this.payload.content = this.comment.content 
        this.isUpdate = false
      }
    }
  }
</script>

<style>
  
</style>
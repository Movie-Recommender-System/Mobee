<template>
  <li class="list-group-item">
    <div class="d-flex justify-content-between">

      <div v-if="isUpdate" class="container">
        <form @submit.prevent="onSubmit">
          <div class="row" >
            <label for="content" width="80%"></label><br>
          </div>
          <div class="row p-2">
            <textarea v-model.trim="payload.content" type="text" id="content"></textarea>
          </div>
          <div class="row p-2 justify-content-end">
            <button class="btn btn-outline-primary">수정</button>
          </div>
        </form>
      </div>

      <div class="py-4" v-else>
        <p class="text-secondary">{{ comment.user.username }}</p>
        <h5>{{ comment.content }}</h5>
      </div>
      <div>

        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" 
          id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
            <i class="fa-solid fa-gear"></i>
            
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
            <li>
              <button
                class="dropdown-item"
                type="button"
                @click="isUpdate=true">
                수정
              </button>
            </li>
            <li>
              <button
                class="dropdown-item"
                type="button"
                @click='deleteComment({articlePk : comment.article, commentPk : comment.pk})'>삭제
              </button>
            </li>
          </ul>
        </div>
        <br>
        <p class="opacity-75">생성 시간 : {{ comment.created_at }}</p>
        <p class="opacity-75">수정 시간 : {{ comment.updated_at }}</p>
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
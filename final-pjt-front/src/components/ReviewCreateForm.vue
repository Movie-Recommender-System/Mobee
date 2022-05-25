<template>
  <form @submit.prevent="onSubmit">
    <div>
      <div class="d-flex">
        <span @click='onStar(0)'>
          <span v-if="stars[0]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
        <span @click='onStar(1)'>
          <span v-if="stars[1]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
        <span @click='onStar(2)'>
          <span v-if="stars[2]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
        <span @click='onStar(3)'>
          <span v-if="stars[3]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
        <span @click='onStar(4)'>
          <span v-if="stars[4]" class="material-symbols-outlined 
          text-warning">hexagon</span>
          <span v-else class="material-symbols-outlined">hexagon</span>
        </span>
      </div>
      <div>
        <label for="content">content: </label>
        <textarea v-model.trim="newReview.content" type="text" id="content" />
      </div>
    </div>
    <div>
      <button class="btn btn-outline-primary">생성</button>
    </div>
  </form>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'ReviewCreateItem',
    props: { moviePk : Number },
    data () {
      return {
        newReview: {
          content: "",
          score: 0,
        },
        stars: [false, false, false, false, false],
      }
    },
    methods: {
      ...mapActions([ 'createReview' ]),
      onStar ( num ) {
        if ( num == 0 ) {
          this.stars = [true, false, false, false, false]
          this.newReview.score = 1
        }
        else if ( num == 1 ) {
          this.stars = [true, true, false, false, false]
          this.newReview.score = 2
        }
        else if ( num == 2 ) {
          this.stars = [true, true, true, false, false]
          this.newReview.score = 3
        }
        else if ( num == 3 ) {
          this.stars = [true, true, true, true, false]
          this.newReview.score = 4
        }
        else if ( num == 4 ) {
          this.stars = [true, true, true, true, true]
          this.newReview.score = 5
        }
      },
      onSubmit() {
        if ( this.newReview.score > 0 ) {
          this.createReview({ moviePk: this.moviePk,
            content: this.newReview.content, score: this.newReview.score })
        } else {
          alert('평점을 넣어주세요.')
        }
        this.newReview.content = ''
        this.stars = [false, false, false, false, false]
      } 
    }
  }
</script>

<style>
  
</style>
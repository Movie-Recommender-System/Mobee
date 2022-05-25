<template>
<div class="container h-100 row align-items-center">
  <div v-if="movie.credits" class="col">
      <div class="ratio ratio-16x9">
        <iframe :src="movie.video_path" frameborder="0"></iframe>
      </div>
      <div class="text-con container px-3">
        <h3 class='text-wrap text-center py-4'>{{ movie.title }}</h3>
        <h4 class="py-2">
          <button v-if="isLoggedIn" @click='wishMovie(movie.pk)'>
            <i v-if="movie.is_wished" class="fa-solid fa-heart"></i>
            <i v-else class="fa-regular fa-heart"></i>
          </button>
          <i v-else class="fa-solid fa-heart"></i>
          {{ movie.wished_count }}
        </h4>
        <p class="py-2">
          <i v-if="movie.score_avg > 0.5" class="fa-solid fa-star"></i>
          <i v-if="movie.score_avg > 1.5" class="fa-solid fa-star"></i>
          <i v-if="movie.score_avg > 2.5" class="fa-solid fa-star"></i>
          <i v-if="movie.score_avg > 3.5" class="fa-solid fa-star"></i>
          <i v-if="movie.score_avg > 4.5" class="fa-solid fa-star"></i>
          <span v-if="movie.score_avg">{{ movie.score_avg }}</span>
          <span v-else class="text-muted">데이터가 없습니다.</span>
        </p>
        <p class="py-2">{{ movie.overview }}</p>
        <p class="py-2" >출시일 : {{ movie.release_date }}</p>
      </div>
      <section class="py-3 hero-section">
        <div class="card-grid">
          <a class="card" v-for="director in directors" :key="-director.pk">
            <div class="card__background" :style="`background-image: url(${director.profile_path})`"></div>
            <div class="card__content">
              <p class="card__category">Director</p>
              <h3 class="card__heading">{{ director.name }}</h3>
            </div>
          </a>
          <a class="card" v-for="actor in actors" :key="actor.pk">
            <div class="card__background" :style="`background-image: url(${actor.profile_path})`"></div>
            <div class="card__content">
              <p class="card__category">{{ actor.character }}</p>
              <h3 class="card__heading">{{ actor.name }}</h3>
            </div>
          </a>
        </div>
      </section>
      <div class="text-con container py-2 px-4">
        <h3 class="py-2" >장르</h3>
        <p class="py-2"> 
          <ul v-for="genre in movie.genres" :key="genre.pk">
            <li class="text-decoration-none">{{ genre.name }}</li>
          </ul>
        </p>
        <h3 class="py-2">리뷰 수</h3> {{ movie.reviews_count }}
          <ReviewList class="py-2" :reviews="movie.reviews"/>
          <ReviewCreateForm class="py-2" :moviePk="movie.pk"/>
      </div>
  </div>
</div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import ReviewList from './ReviewList.vue'
  import ReviewCreateForm from './ReviewCreateForm.vue'

  export default {
    name: 'MovieDetail',
    components: { ReviewList, ReviewCreateForm },
    computed: {
      ...mapGetters(['movie', 'isLoggedIn']),
      actors() {
        return this.movie.credits.actors
      },
      directors() {
        return this.movie.credits.directors
      }
    },
    methods: {
      ...mapActions(['wishMovie'])
    }
    
  }
</script>

<style scoped>



  :root{
  --background-dark: #2d3548;
  --text-light: rgba(255,255,255,0.6);
  --text-lighter: rgba(255,255,255,0.9);
  /* --spacing-s: 8px;
  --spacing-m: 16px;
  --spacing-l: 24px;
  --spacing-xl: 32px;
  --spacing-xxl: 64px;
  --width-container: 1200px; */
}

*{
  border: 0;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html{
  height: 100%;
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
}

body{
  height: 100%;
}

.hero-section{
  align-items: flex-start;
  /* background-image: linear-gradient(15deg, #d8ba4f 0%, #393201 150%); */
  display: flex;
  min-height: 100%;
  justify-content: center;
  padding: var(--spacing-xxl) var(--spacing-l);
}

.card-grid{
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  grid-column-gap: var(--spacing-l);
  grid-row-gap: var(--spacing-l);
  max-width: var(--width-container);
  width: 100%;
}

@media(min-width: 540px){
  .card-grid{
    grid-template-columns: repeat(3, 1fr); 
  }
}

@media(min-width: 960px){
  .card-grid{
    grid-template-columns: repeat(6, 1fr); 
  }
}

.card{
  list-style: none;
  position: relative;
}

.card:before{
  content: '';
  display: block;
  padding-bottom: 150%;
  width: 100%;
}

.card__background{
  background-size: cover;
  background-position: center;
  border-radius: var(--spacing-l);
  bottom: 0;
  filter: brightness(0.75) saturate(1.2) contrast(0.85);
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
  transform-origin: center;
  transform: scale(1) translateZ(0);
  transition: 
    filter 200ms linear,
    transform 200ms linear;
}

.card:hover .card__background{
  transform: scale(1.05) translateZ(0);
}

.card-grid:hover > .card:not(:hover) .card__background{
  filter: brightness(0.5) saturate(0) contrast(1.2) blur(20px);
}

.card__content{
  left: 0;
  padding: var(--spacing-l);
  position: absolute;
  top: 0;
}

.card__category{
  color: var(--text-light);
  font-size: 0.9rem;
  margin-bottom: var(--spacing-s);
  text-transform: uppercase;
}

.card__heading{
  color: var(--text-lighter);
  font-size: 1.9rem;
  text-shadow: 2px 2px 20px rgba(0,0,0,0.2);
  line-height: 1.4;
  word-spacing: 100vw;
}
</style>
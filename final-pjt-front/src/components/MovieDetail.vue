<template>
<div v-if="movie.credits" class="detailview align-items-center">
    
      <div class="movie-card">
        <!-- <div class="container"> -->
          <img :src="posterURL" alt="cover" class="cover" />
          <div class="hero" > 
            <div class="details">
            
            <div class="title1 fs-1">{{ movie.title }} <span>{{ movie.runtime }} min</span></div>
            <div class="title2" ><span>{{ movie.release_date }}, </span>  </div> 
            
            <p>
              <span v-if="movie.score_avg > 0.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="movie.score_avg > 1.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="movie.score_avg > 2.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="movie.score_avg > 3.5" class="material-symbols-outlined text-warning">hexagon</span>
              <span v-if="movie.score_avg > 4.5" class="material-symbols-outlined text-warning">hexagon</span>
              <!-- <h3 v-if="movie.score_avg">{{ movie.score_avg }}</h3> -->
            </p>

              
            </div> <!-- end details -->
            
          </div> <!-- end hero -->
          
          <div class="description">
            
            <div  class="column1">
              <span v-for="genre in movie.genres" :key="genre.pk" class="badge rounded-pill bg-warning tag">{{ genre.name }}<br></span>
              <div>

              <div  v-if="isLoggedIn" @click='wishMovie(movie.pk)'>
                <img v-if="movie.is_wished" src="../assets/honey (2).png" alt="">
                <img v-else src="../assets/honey.png" alt="">
              </div>
              <img v-else src="../assets/honey.png" alt="">
                  {{ movie.wished_users.length }}<br>
            </div>

          </div> <!-- end column1 -->
          
            <div class="column2">
              
              <p >{{ movie.overview }}</p>
              
          </div> <!-- end column2 -->
        </div> <!-- end description -->
  

      </div> <!-- end movie-card -->
      <br><br><br><br>
      <div class="ratio ratio-16x9">
        <iframe :src="videoURL" frameborder="0"></iframe>
      </div>


    
      <section class="py-3 hero-section">
        <div class="card-grid">
          <a class="card">
            <div class="card__background" :style="`background-image: url(https://image.tmdb.org/t/p/w500/${director.profile_key})`"></div>
            <div class="card__content">
              <p class="card__category">Director</p>
              <h3 class="card__heading">{{ director.name }}</h3>
            </div>
          </a>
          <a class="card" v-for="actor in actors" :key="actor.pk">
            <div class="card__background" :style="`background-image: url(https://image.tmdb.org/t/p/w500/${actor.profile_key})`"></div>
            <div class="card__content">
              <p class="card__category">{{ actor.character }}</p>
              <h3 class="actorname card__heading">{{ actor.name }}</h3>
            </div>
          </a>
        </div>
      </section>
      <div class="text-con  py-2 px-4">
       <hr>
       <div class="row">
          <ReviewList class="py-2 col-9" :reviews="movie.reviews"/>
          <div class="col-1"></div>
          <ReviewCreateForm class="py-2 col-2" :moviePk="movie.pk"/>
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
      director() {
        return this.movie.credits.directors[0]
      },
      backdropURL() {
        return `https://image.tmdb.org/t/p/w500/${this.movie.backdrop_key}`
      },
      posterURL() {
        return `https://image.tmdb.org/t/p/w200/${this.movie.poster_key}`
      },
      videoURL() {
        return `https://youtube.com/embed/${this.movie.video_key}?autoplay=1&mute=1`
      },
    },
    methods: {
      ...mapActions(['wishMovie'])
    },
     mounted() {
      // let styleElem = document.querySelector('.hero').style;
      // styleElem.setProperty('`--background', `url(${this.movie.poster_path})`);

      let styleElem = document.head.appendChild(document.createElement("style"));
      styleElem.innerHTML = `.hero:before {background: url(${this.backdropURL});}`;

      // let styleElem = window.getComputedStyle($('.hero')[0], ':before').getPropertyValue(`${this.movie.poster_path}`);

      // $('head').append("<style>.hero:before{background: `url(${this.movie.poster_path})`}</style>");
     }
    
  }
</script>

<style scoped>
@charset "UTF-8";
@import url(https://fonts.googleapis.com/css?family=Lato:400,300,700);
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);
*, *:before, *:after {
  box-sizing: border-box;
}

.detailview {
  color: #393939;
}

a {
  text-decoration: none;
  color: #767676;
  transition: 1s;
}

a:hover {
  text-decoration: underline;
  color: #cfcfcf;
  -webkit-transform: scale(1.05);
  /* font-size: 80%; */
}

/* .actorname:hover {
  -webkit-transform: scale(1.2);
} */

.movie-card {
  font: 14px/22px "Lato", Arial, sans-serif;
  color: #A9A8A3;
  padding: 40px 0;
  font-size: 15px;
  /* z-index: 100000000; */
}

.container {
  margin: 0 auto;
  width: 780px;
  height: 640px;
  background: #F0F0ED;
  border-radius: 5px;
  position: relative;
}

.hero {
  height: 342px;
  margin: 0;
  position: relative;
  overflow: hidden;
  z-index: 1;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}

.hero:before {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;

  /* background: var(--background);
  content: '';
  display: block; */

  /* background: red; */
  /* background: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/195612/hobbit_bg.jpg"); */
  filter: brightness(50%);
  z-index: -1;
  transform: skewY(-2.2deg);
  transform-origin: 0 0;
  -webkit-backface-visibility: hidden;
}

.cover {
  position: absolute;
  top: 160px;
  left: 40px;
  z-index: 2;
}

.details {
  padding: 190px 0 0 280px;
}
.details .title1 {
  color: white;
  font-size: 44px;
  margin-bottom: 13px;
  position: relative;
}
.details .title1 span {
  position: absolute;
  top: 3px;
  margin-left: 12px;
  background: #C4AF3D;
  border-radius: 5px;
  color: #544C21;
  font-size: 15px;
  padding: 0px 4px;
}
.details .title2 {
  color: #C7C1BA;
  font-size: 23px;
  font-weight: 300;
  margin-bottom: 15px;
}
.details .likes {
  margin-left: 24px;
}
.details .likes:before {
  content: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/195612/icon_like.png");
  position: relative;
  top: 2px;
  padding-right: 7px;
}

.description {
  bottom: 0px;
  height: 200px;
  font-size: 16px;
  line-height: 26px;
  color: #3e3e3e; /* 글씨색 */
}

.column1 {
  padding-left: 50px;
  padding-top: 120px;
  width: 220px;
  float: left;
  text-align: center;
}

.tag {
  background: white;
  border-radius: 10px;
  padding: 3px 8px;
  font-size: 14px;
  margin-right: 4px;
  line-height: 35px;
  cursor: pointer;
}

.tag:hover {
  background: #ddd;
}

.column2 {
  padding-left: 41px;
  padding-top: 30px;
  margin-left: 20px;
  width: 480px;
  float: left;
}

.avatars {
  margin-top: 23px;
}
.avatars img {
  cursor: pointer;
}
.avatars img:hover {
  opacity: 0.6;
}
.avatars a:hover {
  text-decoration: none;
}

fieldset, label {
  margin: 0;
  padding: 0;
}

/****** Style Star Rating Widget *****/
.rating {
  border: none;
  float: left;
}

.rating > input {
  display: none;
}

.rating > label:before {
  margin: 5px;
  margin-top: 0;
  font-size: 1em;
  font-family: FontAwesome;
  display: inline-block;
  content: "";
}

.rating > .half:before {
  content: "";
  position: absolute;
}

.rating > label {
  color: #ddd;
  float: right;
}

/***** CSS Magic to Highlight Stars on Hover *****/
.rating > input:checked ~ label,
.rating:not(:checked) > label:hover,
.rating:not(:checked) > label:hover ~ label {
  color: #FFD700;
}

/* hover previous stars in list */
.rating > input:checked + label:hover,
.rating > input:checked ~ label:hover,
.rating > label:hover ~ input:checked ~ label,
.rating > input:checked ~ label:hover ~ label {
  color: #FFED85;
}

a[data-tooltip] {
  position: relative;
}

a[data-tooltip]::before,
a[data-tooltip]::after {
  position: absolute;
  display: none;
  opacity: 0.85;
}

a[data-tooltip]::before {
  /*
   * using data-tooltip instead of title so we 
   * don't have the real tooltip overlapping
   */
  content: attr(data-tooltip);
  background: #000;
  color: #fff;
  font-size: 15px;
  padding: 5px;
  border-radius: 5px;
  /* we don't want the text to wrap */
  white-space: nowrap;
  text-decoration: none;
}

a[data-tooltip]::after {
  width: 0;
  height: 0;
  border: 6px solid transparent;
  content: "";
}

a[data-tooltip]:hover::before,
a[data-tooltip]:hover::after {
  display: block;
}

/** positioning **/
/* top tooltip */
a[data-tooltip][data-placement=top]::before {
  bottom: 100%;
  left: 0;
  margin-bottom: 40px;
}

a[data-tooltip][data-placement=top]::after {
  border-top-color: #000;
  border-bottom: none;
  bottom: 50px;
  left: 20px;
  margin-bottom: 4px;
}



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
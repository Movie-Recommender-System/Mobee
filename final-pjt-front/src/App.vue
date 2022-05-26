<template>
  <div id="app">
    <header class="header fixed-top align-items-center" id="header">
      <NavBar/>
    </header>
    <br>
    <br>

    <main>
      <div class="min-vh-100">
        <div class="Main pt-5 h-100">
          <router-view></router-view>
        </div>
        <div class="fixed-bottom text-muted text-center">
          <FooterPage ></FooterPage>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
  import FooterPage from '@/components/FooterPage.vue'
  import NavBar from '@/components/NavBar.vue'
  import { mapActions } from 'vuex'
  export default {
    name: "App",
    components: {
      NavBar, FooterPage, 
    },
    methods: {
      ...mapActions(['fetchCurrentUser', 'fetchGenres'])
    },
    created() {
      this.fetchCurrentUser(),
      this.fetchGenres()
    },
  }
</script>

<style>
@font-face {
    font-family: 'SuncheonB';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2202-2@1.0/SuncheonB.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'HallymGothic-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2204@1.0/HallymGothic-Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}
@font-face {
    font-family: 'GimpoGothicBold00';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2202-2@1.0/GimpoGothicBold00.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

@font-face {
    font-family: 'CookieRun-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/CookieRun-Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}


/* h1, h2, h3, h4, h5, h6 {
  font-family: 'CookieRun-Regular';
}

p { 
  font-family: Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
} */



body {

  background-color: var(--bg-color);
 
} 
@import url("../public/bootstrap.css");
@import url("../public/bootstrap.min.css");
  :root {
  --bg-color: #ffffff;
  --line-color: rgb(0, 0, 0);
  --main-color: rgb(255, 234, 0);
  --main-color-dark: rgb(140, 70, 20);
  --wing-color: rgb(193, 246, 255);
  --unit: 1vh;
  scroll-behavior: smooth;
}

input::placeholder {
  font-family: 'Stylish', sans-serif;
}


textarea::placeholder {
  font-family: 'Stylish', sans-serif;
}


.header {
  font-size: 20px;
}

.header a, .header .nav-link:hover {
  color:rgb(58, 58, 58);
}

/* 커서이미지 */
html, body{
  cursor: url(./assets/bee_cursor.png), auto;
}

a, a:link {
  cursor: url(./assets/bee_hover.png),auto;
}

a:hover, a:focus { 
  cursor: url(./assets/bee_hover.png),auto;
  color:#665f5f;
} 

a:active {cursor: url(./assets/bee_hover.png),auto;} 

input {cursor: url(./assets/bee_hover.png),auto;} 

#app {
  height: 100vh;
  /* cursor: url("./assets/bee.png"), auto; */
}

/* 글씨체 부분  자유롭게*/



/* 
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 1,
  'wght' 400,
  'GRAD' 0,
  'opsz' 24
} */
</style>


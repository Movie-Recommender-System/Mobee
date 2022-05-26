<template scoped>
  <div class="body">
    <div class="crawl">
      <div class="wrapper">
        <h1 class="pre-text">Mobee</h1>
        <h2 class="pre-text">꿀잼 영화 추천 사이트</h2>
          <p>Pursued by the Empire's sinister agents,Pursued by the Empire's sinister agents,Pursued by the Empire's sinister agents,Pursued by the Empire's sinister agents,Pursued by the Empire's sinister agents,Pursued by the Empire's sinister agents,"</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'EpilogueView',
}
</script>
<style scoped>
  #app {
  background: black;
  color: #212121;
  font-family: "Lato";
  text-shadow: 0px 0px 0px #e5b800;
  font-weight: 700;
  overflow: hidden;
}

.crawl {
  position: absolute;
  transform: perspective(320px) rotateX(30deg);
  transform-origin: 50% 100%;
  width: 100%;
  height: 30em;
  bottom: 0;
  font-size: 7.3vw;
  text-align: justify;
}

.wrapper {
  position: absolute;
  top: 100%;
  -webkit-animation: scroll 20s linear 0s infinite;
          animation: scroll 20s linear 0s infinite;
}

.pre-text {
  text-align: center;
}

h1 {
  font-size: 6vw;
}

h2 {
  font-size: 9vw;
}

@-webkit-keyframes scroll {
  0% {
    top: 100%;
  }
  50% {
    top: 0%;
  }
  100% {
    top: -140%;
  }
}

@keyframes scroll {
  0% {
    top: 100%;
  }
  50% {
    top: 0%;
  }
  100% {
    top: -140%;
  }
}
</style>
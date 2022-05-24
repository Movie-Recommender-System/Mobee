<template lang="">
  <div id="intro" class="intro boardc">
    
    <div class="container">
      <div class="honeydipper">
        <div class="honeydipper__bulb">
          <div class="honey">
            <div class="drip"></div>
            <div class="drip"></div>
          </div>
        </div>
      </div>
      <div class="honeypot">
        <div class="honeypot__top"></div>
      </div>
      <div class="honeypot__shadow"></div>
    </div>

    <div id='bug' class='bee'>
      <div class='wings'></div>
      <div class='limbs'></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "IntroView",
  mounted() {
    const bee = document.getElementById('bug')
    var last_x = 0
    console.clear()

    function moveBeeMobile(e){  
      var touch = e.touches[0];
      // get the DOM element
      // var leaf = document.elementFromPoint(touch.clientX, touch.clientY);

      var bx = touch.clientX 
      var by = touch.clientY 

      bee.style.left = bx + 'px'
      bee.style.top = by + 'px'  

      if(last_x < bx) {
        bee.classList.add('flip')
      } else {
        bee.classList.remove('flip')
      }
      last_x = bx

      // add honeycomb trail
      var h = document.createElement('div')
      h.className = 'honey_trail'
      h.style.left = bx + 10 +'px'
      h.style.top = by + 30 + 'px' 

      //limit the spew of honeycomb
      if(Math.random() < .5) {
        document.body.appendChild(h)  

        //remove trail once faded
        setTimeout(function(){      
          document.getElementsByClassName('honey_trail')[0].remove()       
        },2500)
      }
    }
    window.addEventListener('touchmove', moveBeeMobile)

    // function to move bee in conjunction with mouse
    window.addEventListener('mousemove', function(e) {
      var x = e.clientX - 15
      var y = e.clientY - 15  
      bee.style.left = x +'px'
      bee.style.top = y + 'px'
      console.log(e.clientX - (window.innerWidth/2))
      if(last_x < x) {
        bee.classList.add('flip')    
      } else {
        bee.classList.remove('flip')    
      }  
      last_x = x
      
      // add honeycomb trail
      var h = document.createElement('div')
      h.className = 'honey_trail'
      h.style.left = x + 10 +'px'
      h.style.top = y + 30 + 'px' 

      //limit the spew of honeycomb
      if(Math.random() < .5) {
        document.body.appendChild(h)  

        //remove trail once faded
        setTimeout(function(){      
          document.getElementsByClassName('honey_trail')[0].remove()       
        },2500)
      }
    })

    
  }
}
</script>


<style scoped>
*, *::before, *::after {
  box-sizing: border-box;
}

.honeydipper__bulb .honey::before, .honeydipper::after, .honeydipper::before {
  content: "";
  display: block;
  position: absolute;
}

.intro {
  background: #ffffff;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.container {
  position: relative;
  width: 20rem;
  height: 20rem;
}

.honeypot {
  z-index: 2;
  position: absolute;
  bottom: 0;
  left: 4rem;
  width: 12rem;
  height: 12rem;
  border-radius: 100%;
  background-color: #E2C6B3;
  background-image: linear-gradient(transparent 35%, #D69142 35%, #D69142 40%, transparent 40%), linear-gradient(transparent 45%, #D69142 45%, #D69142 50%, transparent 50%), linear-gradient(transparent 55%, #D69142 55%, #D69142 60%, transparent 60%), linear-gradient(transparent 65%, #D69142 65%, #D69142 70%, transparent 70%);
  box-shadow: inset 0px 0px 12px 0px rgba(198, 143, 105, 0.4);
}
.honeypot__top {
  position: absolute;
  top: 0rem;
  left: 0rem;
  width: 12rem;
  height: 2rem;
  border-radius: 2.5rem;
  background: #E2C6B3;
  box-shadow: inset 0px 6px 12px 0px rgba(198, 143, 105, 0.4);
}

.honeypot__shadow {
  position: absolute;
  width: 12rem;
  height: 0.75rem;
  bottom: -0.25rem;
  left: 4rem;
  opacity: 0.4;
  background: #a4a4a4;
  border-radius: 50%;
}

.honeydipper {
  position: absolute;
  background: #8C705F;
  width: 13rem;
  height: 1rem;
  top: 10rem;
  left: 6rem;
  transform: rotateZ(-60deg);
  animation: dipper 10s cubic-bezier(0.4, 1, 0.83, 0.75) 1;
}
.honeydipper::before {
  left: 2rem;
  width: 2rem;
  height: 100%;
  background: rgba(242, 191, 89, 0.6);
}
.honeydipper::after {
  width: 2.5rem;
  height: 2.5rem;
  right: -1.5rem;
  top: -0.75rem;
  border-radius: 50%;
  background: #8C705F;
}
.honeydipper__bulb {
  position: absolute;
  width: 4.5rem;
  height: 3.5rem;
  top: -1.25rem;
  left: -2.5rem;
  background-color: #8C705F;
  background-image: linear-gradient(90deg, transparent 50%, #4D3E34 55%);
  background-size: 1rem;
  border-radius: 1.5rem;
}
.honeydipper__bulb .honey {
  z-index: 5;
  position: absolute;
  background: rgba(242, 191, 89, 0.6);
  border-radius: 1.5rem;
  bottom: 0;
  width: 100%;
  height: 100%;
}
.honeydipper__bulb .honey::before {
  width: 2.5rem;
  height: 0.25rem;
  background: #F2BF59;
  border-radius: 0% 0% 200% 200%;
  bottom: -0.125rem;
  left: 1.1rem;
}
.honeydipper__bulb .honey .drip {
  position: absolute;
  background: #F2BF59;
}
.honeydipper__bulb .honey .drip:nth-of-type(1) {
  width: 1.5rem;
  height: 1.5rem;
  bottom: -1.5rem;
  left: 1.5rem;
  border-radius: 0 0 1rem 1rem;
  transform-origin: top center;
  animation: drip-left 5s cubic-bezier(0.35, 0.71, 0.81, 0.39) 1;
  animation-delay: 2.5s;
}
.honeydipper__bulb .honey .drip:nth-of-type(2) {
  border-radius: 1rem;
  width: 1.5rem;
  height: 1.5rem;
  bottom: -1.5rem;
  left: 1.5rem;
  opacity: 1;
  animation: drip-right 5s cubic-bezier(0.35, 0.71, 0.81, 0.39) 1;
  animation-delay: 2.5s;
}

@keyframes dipper {
  0%, 100% {
    top: 10rem;
    left: 6rem;
    transform: rotateZ(-60deg);
  }
  10%, 90% {
    top: 8rem;
    left: 5rem;
    transform: rotateZ(-90deg);
  }
  25%, 75% {
    top: 1rem;
    left: 10rem;
    transform: rotateZ(0deg);
  }
}
@keyframes drip-left {
  0% {
    transform: scale(1);
  }
  25% {
    transform: scaleX(0.75) scaleY(1.5);
  }
  50% {
    transform: scaleX(0.5) scaleY(1.5);
  }
  75% {
    transform: scaleX(0) scaleY(2);
  }
  80% {
    transform: scaleX(0) scaleY(0.25);
  }
  100% {
    transform: scaleX(1) scaleY(1);
  }
}
@keyframes drip-right {
  0% {
    opacity: 1;
    transform: translateY(0) scale(0.25);
  }
  25% {
    opacity: 1;
    transform: translateY(50%) scale(0.25);
  }
  50% {
    opacity: 1;
    transform: translateY(100%) scale(1);
  }
  75% {
    opacity: 1;
    transform: translateY(200%) scale(1.25);
  }
  80% {
    opacity: 1;
    transform: translateY(500%);
  }
  100% {
    transform: translateY(800%);
    opacity: 0;
  }
}





  :root {
  --bg-color:#fb1;
}

.intro {
  overflow:hidden;  
}

.bee {
  width:50px;
  height:50px;
  background:black;
  border-radius:50% 75% 0% 75%;
  background:linear-gradient(-50deg, black 15px, goldenrod 15px, goldenrod 25px, black 25px, black 40px, goldenrod 40px, goldenrod 50px, black 50px);
  box-shadow:inset 0 0 0 2px black, inset 5px -5px 5px 5px rgba(139,69,19,.5), -10px 20px 35px saddlebrown;  
  position:absolute;
  left:50%;
  top:50%;
  transform:rotate(-20deg);
}
.bee:before {
  content:'';
  width:35px;
  height:35px;
  border-radius:75% 50% 75% 25%;
  background:radial-gradient(circle at 10px 15px, black 3px, goldenrod 3px, goldenrod 20px, black);
  box-shadow:0 0 0 2px black; 
  position:absolute;
  left:-22px;
  top:-15px;
  transform:rotate(30deg);
}
.bee:after {
  content:'';
  width:30px;
  height:30px;
  position:absolute;
  left:-33px;
  top:-28px;
  border-radius:50%;
  z-index:-1000;
  box-shadow:inset -2px 1px 0 black, 1px -2px 0 var(--bg-color), 3px -3px 0 black;
  animation:hair .33s linear infinite;
}
@keyframes hair {
  50% { transform:translateY(2px); }
}

.flip {
  /*   transition:.25s; */
  transform:rotate(20deg) scaleX(-1) !important;
}

.bee .wings {
  width:50px;
  height:50px;
  background:linear-gradient(to bottom left, black, transparent 50px);
  border-radius:50% 50% 50% 25%;
  position:absolute;
  left:25px;
  top:-25px;
  opacity:.5;
  transform-origin:left bottom;
  perspective:200px;
  animation:buzz .33s linear infinite;
}
@keyframes buzz {
  50% { transform: scale(.9) rotateY(90deg) rotateX(90deg); }
}

.bee .limbs {
  width:10px;
  height:10px;
  border-right:2px solid black;
  border-left:2px solid black;
  position:absolute;
  top:100%;
  left:25px;
}
.bee .limbs:before {
  content:'';
  width:100%;
  height:100%;
  border-right:2px solid black;
  border-left:2px solid black;
  position:absolute;
  top:-20px;
  left:-33px;
  transform:rotate(60deg);
}

.honey_trail {
  width:10px;
  height:10px;
  border-radius:50%;
  background:radial-gradient(circle, var(--bg-color) 45%, brown); 
  position:absolute;
  z-index:20000;
  animation:honey 2s linear .2s forwards;
}
@keyframes honey {
  100% { transform:translateY(300%) scale(.5); opacity:0; }
}
</style>
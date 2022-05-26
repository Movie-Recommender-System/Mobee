<template>
  <div class="container pt-5">
    <account-error-list v-if="authError"></account-error-list>
    <div class="body d-md-flex align-items-center justify-content-between">
        <div class="box-1 mt-md-0 mt-5">
            <img src="../assets/minions2.png"
                class="" alt="">
        </div>
        <div class=" box-2 ps-5 d-flex flex-column h-100">
          <div class="mt-5">
              <p class="mb-1 h-1">SignUp</p>
              <p class="text-muted mb-2">Create your own account to use the Mobee service.</p>
              <div class="d-flex flex-column ">
                  <p class="text-muted mb-2">Continue with...</p>
                  <div class="d-flex align-items-center">
                      <form @submit.prevent="signup(credentials)">
                        <div class="form-group">
                            <label>User Name</label>
                            <input  v-model="credentials.username" placeholder="User Name" class="form-control" type="text" id="username" required/>
                        </div>
                        <div class="form-group">
                            <label>Password</label>
                            <input v-model="credentials.password1" placeholder="Password" class="form-control" type="password" id="password1" required />
                        </div>
                        <div class="form-group">
                            <label>Password Confirmation</label>
                            <input v-model="credentials.password2" placeholder="Password Again" class="form-control" type="password" id="password2" required />
                        </div>

                        <button  type="submit" class="btn btn-secondary">Register</button>
                      </form>
                              </div>
                          </div>
                        </div>
                        <div class="mt-auto">
                <p class="footer text-muted mb-0 mt-md-0 mt-4">By register you agree with our
                    <span class="p-color me-1">terms and conditions</span>and
                    <span class="p-color ms-1">privacy policy</span>
                </p>
            </div>
        </div>
    </div>  
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif
}

.container {
    margin: 50px auto;
}

.body {
    position: relative;
    width: 720px;
    height: 440px;
    margin: 20px auto;
    border: 1px solid #dddd;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

.box-1 img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.box-2 {
    padding: 10px;
}

.box-1,
.box-2 {
    width: 50%;
}

.h-1 {
    font-size: 24px;
    font-weight: 700;
}

.text-muted {
    font-size: 14px;
}

.container .box {
    width: 100px;
    height: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 2px solid transparent;
    text-decoration: none;
    color: #615f5fdd;
}

.box:active,
.box:visited {
    border: 2px solid #ffa600;
}

.box:hover {
    border: 2px solid #ff9d00;
}

.btn.btn-primary {
    background-color: transparent;
    color: #ffb700;
    border: 0px;
    padding: 0;
    font-size: 12px;
}

.btn.btn-primary .fas.fa-chevron-right {
    font-size: 12px;
}

.footer .p-color {
    color: #ff8800;
}

.footer.text-muted {
    font-size: 10px;
}

.fas.fa-times {
    position: absolute;
    top: 20px;
    right: 20px;
    height: 20px;
    width: 20px;
    background-color: #f3cff379;
    font-size: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.fas.fa-times:hover {
    color: #ff0000;
}

@media (max-width:767px) {
    body {
        padding: 10px;
    }

    .body {
        width: 100%;
        height: 100%;
    }

    .box-1 {
        width: 100%;
    }

    .box-2 {
        width: 100%;
        height: 440px;
    }
}

</style>

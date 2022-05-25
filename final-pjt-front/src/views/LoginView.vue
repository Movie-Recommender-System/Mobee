<template>
  <div class="container">
    
    <div class="main1 container">

      <div class="row  justify-content-center p-3">
        <div class="col-md-6 col-sm-12 text-center text-align-center align-self-center">
          <h2>Application<br> Login Page</h2>
          <p>Login or register from here to access.</p>
        </div>
        <div class="col-md-6 col-sm-12">
          <div class="login-form">
            <form @submit.prevent="login(credentials)">
              <div class="form-group my-4 ">
                  <label class="fs-5 ">User Name</label>
                  <input id="username" v-model="credentials.username" type="text" class="form-control" placeholder="User Name" required>
              </div>
              <div class="form-group my-4">
                  <label class="fs-5 ">Password</label>
                  <input id="password" v-model="credentials.password" type="password" class="form-control" placeholder="Password" required>
              </div>
              <div class="row">
                <div class="col-6">
                  <button type="submit" class="col-6 btn btn-black bg-black text-white me-1" style="width:100%;">Login</button>
                </div>
                <div class="col-6">
                  <router-link :to="{name:'signup'}" >
                    <button type="submit" class="btn btn-secondary" style="width:100%;">Go Register</button>
                  </router-link>
                </div>
              </div>
              
            </form>
          </div>
        </div>
      </div>
    </div>
    
    <hr>
    <account-error-list v-if="authError"></account-error-list>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style scoped>

  
</style>

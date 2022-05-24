<template>
  <div>
    <div>
      <h2>Application<br> Login Page</h2>
      <p>Login or register from here to access.</p>
      
    </div>
    <div class="main1">
      <div class="col-md-6 col-sm-12">
        <div class="login-form">
          <form @submit.prevent="login(credentials)">
            <div class="form-group">
                <label>User Name</label>
                <input id="username" v-model="credentials.username" type="text" class="form-control" placeholder="User Name" required>
            </div>
            <div class="form-group">
                <label>Password</label>
                <input id="password" v-model="credentials.password" type="password" class="form-control" placeholder="Password" required>
            </div>
            <button type="submit" class="btn btn-black bg-black text-white">Login</button>
            <router-link :to="{name:'signup'}">
              <button type="submit" class="btn btn-secondary">Register</button>
            </router-link>
          </form>
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

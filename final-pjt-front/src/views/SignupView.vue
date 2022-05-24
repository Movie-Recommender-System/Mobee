<template>
  <div>

    <div>
      <h2>Application<br> Login Page</h2>
      <p>Login or register from here to access.</p>
      <account-error-list v-if="authError"></account-error-list>
      
    </div>
      <div class="col-md-6 col-sm-12">
        <div class="login-form">
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

<style></style>

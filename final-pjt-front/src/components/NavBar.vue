<template>
  <nav>
    <ul>
      <li>
        <router-link :to="{ name: 'movie' }">Movie</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'article' }">Community</router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'profile', params: { username } }">
          {{ currentUser.username }}'s page
        </router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </li>
      <li v-else>
        <a href="" @click.prevent="logout()">logout</a>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </li>
    </ul>
    
    </nav>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
      ...mapActions(['logout'])
    }
  }
</script>

<style>
  
</style>
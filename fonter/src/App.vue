<template>
  <nav-bar></nav-bar>
  <router-view></router-view>

  <div class="circle1"></div>
  <div class="circle2"></div>
</template>

<script>
import NavBar from 'content/nav-bar/NavBar.vue'
import * as func from '@/store/mutations-type.ts'
import { getStore } from 'network/login.js'

export default {
  name: 'App',
  data () {
    return {
    }
  },
  methods: {
    setStore (token) {
      getStore(token).then(res => {
        this.$store.commit(func.SETACCOUNT, res.data['account'])
        this.$store.commit(func.SETEMAIL, res.data['email'])
        this.$store.commit(func.SETNAME, res.data['name'])
        this.$store.commit(func.SETPASSWORD, res.data['password'])
      })
    }
  },
  components: {
    NavBar,
  },
  created () {
    this.$store.commit(func.GETTOKEN)
    if (this.$store.state.token) {
      this.setStore({ 'token': this.$store.state.token })
    }
  }
}
</script>

<style>
@import "assets/css/base.css";
</style>

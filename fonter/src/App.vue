<template>
  <nav-bar></nav-bar>
  <router-view></router-view>

  <div class="circle1"></div>
  <div class="circle2"></div>
</template>

<script>
import NavBar from 'content/nav-bar/NavBar.vue'
import * as func from '@/store/mutations-type.ts'

export default {
  name: 'App',
  data () {
    return {
    }
  },
  methods: {
  },
  components: {
    NavBar,
  },
  created () {
    this.$store.commit(func.GETTOKEN)
  }
}
</script>

<style>
@import "assets/css/base.css";
</style>

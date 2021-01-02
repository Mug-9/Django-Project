<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from 'content/nav-bar/NavBar.vue'

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
  }
}
</script>

<style>
@import "assets/css/base.css";
.app {
  position: relative;
  min-height: 100%;
}
</style>

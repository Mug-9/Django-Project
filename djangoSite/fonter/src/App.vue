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
      name: "1234",
      pwd: '1234',
    }
  },
  methods: {
    // submitForm (event) {
    //   console.log(this.name)
    //   let formData = new FormData()
    //   formData.append('name', this.name)
    //   formData.append('pwd', this.pwd)
    //   postLogin(formData).then(res => {
    //     console.log(res)
    //   })
    // }
  },
  components: {
    NavBar,
  }
}
</script>

<style>
@import "assets/css/base.css";
</style>

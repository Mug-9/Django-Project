<template>
  <div id="app">
    {{ this.content }}
  </div>
</template>

<script>
import { getBooks } from 'network/home'

export default {
  el: '#app',
  data () {
    return {
      content: "12",
    }
  },
  created () {
    getBooks().then(res => {
      console.log(res)
      this.content = res.data
    })
  }
}
</script>

<style>
</style>

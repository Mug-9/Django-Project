<template>
  <div id="app">
    <form>
      <input type="text" placeholder="login" v-model="name" />
      <input type="text" placeholder="pwd" v-model="pwd" />
      <input type="submit" value="登录" @click="submitForm" />
    </form>
    <!-- <button @click="submitForm">submit</button> -->
  </div>
</template>

<script>
import { getBooks } from 'network/home'
import { postLogin } from 'network/home'

export default {
  el: '#app',
  data () {
    return {
      name: "1234",
      pwd: '1234',
    }
  },
  created () {
    getBooks().then(res => {
      console.log(res)
      this.content = res.data
    })
  },
  methods: {
    submitForm (event) {
      console.log(this.name)
      let formData = new FormData()
      formData.append('name', this.name)
      formData.append('pwd', this.pwd)
      postLogin(formData).then(res => {
        console.log(res)
      })
    }
  }
}
</script>

<style>
</style>

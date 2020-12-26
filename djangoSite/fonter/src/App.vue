<template>
  <div id="app">

  </div>
</template>

<script>
  import {getBooks} from 'network/home'

  export default {
    created() {
      getBooks().then(res=> {
        console.log(res);
      })
    }
  }
</script>

<style>

</style>

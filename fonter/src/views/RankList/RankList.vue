<template>
  <div class="main">
    <div class="content">
      <online-list></online-list>
    </div>
  </div>
</template>

<script>
import OnlineList from './OnlineList.vue'
export default {
  name: "RankList",
  components: {
    OnlineList
  },
}
</script>

<style scoped>
</style>
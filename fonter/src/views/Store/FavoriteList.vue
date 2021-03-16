<template>
  <div>
    <el-steps
      direction="vertical"
      :active="length"
      v-loading="loading"
      v-if="!loading"
    >
      <el-step
        :title="item['time']"
        status="success"
        style="margin: 20px"
        v-for="item in logs"
        :key="item"
        class="step"
      >
        <template v-slot:icon>
          <img src="~@/assets/img/online-icons/log.svg" alt="" />
        </template>
        <template v-slot:description>
          <p style="font-size: 1.5em"> 收藏了 {{ item["msg"] }}</p>
        </template>
      </el-step>
    </el-steps>
  </div>
</template>

<script>
import { FavoriteList } from '@/network/get_bili.js'
export default {
  name: "FavoriteList",
  methods: {
    getFavorite () {
      let data = {
        token: this.$store.state.token
      }
      FavoriteList(data).then(res => {
        this.logs = res['list']
        this.loading = false
        this.length = this.logs.length
      })
    },
  },
  data () {
    return {
      logs: {},
      loading: true,
      length: 0
    }
  },
  mounted () {
    this.getFavorite()
  }
}
</script>

<style scoped>
.step img {
  width: 25px;
  height: 25px;
}
</style>
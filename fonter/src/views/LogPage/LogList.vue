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
        :status="calStatus(item['type'])"
        style="margin: 20px"
        v-for="item in logs"
        :key="item"
        class="step"
      >
        <template v-slot:icon>
          <img src="~@/assets/img/online-icons/log.svg" alt="" />
        </template>
        <template v-slot:description>
          <p style="font-size: 1.5em">{{ item["msg"] }}</p>
        </template>
      </el-step>
    </el-steps>
  </div>
</template>

<script>
import { OperatorLog } from '@/network/get_bili.js'
export default {
  name: "LogList",
  methods: {
    getLog () {
      let data = {
        token: this.$store.state.token
      }
      OperatorLog(data).then(res => {
        this.logs = res['list']
        this.loading = false
        this.length = this.logs.length
      })
    },
    calStatus (type) {
      if (type == 'like') {
        return 'finish'
      } else if (type == 'delete') {
        return 'error'
      } else if (type == 'comment') {
        return 'success'
      }
    }
  },
  data () {
    return {
      logs: {},
      loading: true,
      length: 0
    }
  },
  mounted () {
    this.getLog()
  }
}
</script>

<style scoped>
.step img {
  width: 25px;
  height: 25px;
}
</style>
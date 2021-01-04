<template>
  <div class="main">
    <div class="content">
      <echarts-time
        v-if="props_flag"
        echartsTime_id="echarts"
        echartsTime_width="1000px"
        echartsTime_height="800px"
        :echartsTime_data="onlineNumbers"
        :echartsTime_date="now_date"
        @dateChange="dateChange"
      ></echarts-time>
    </div>
  </div>
</template>

<script>
import { getOnlineNumbers } from 'network/onlineNumber.js'
import EchartsTime from './EchartsTime.vue'
import * as func from '@/store/mutations-type.ts'

export default {
  name: "Home",
  data () {
    return {
      onlineNumbers: {
        dates: [],
        times: [],
        numbers: [],
      },
      props_flag: false,
      now_date: new Date()
    }
  },
  computed: {
  },
  components: {
    EchartsTime
  },
  methods: {
    getNumbers () {
      this.onlineNumbers.dates = []
      this.onlineNumbers.times = []
      this.onlineNumbers.numbers = []
      let query_date = this.now_date.getFullYear() + '-' + (this.now_date.getMonth() + 1) + '-'
        + this.now_date.getDate()
      
      let data = {
        date: query_date,
      }
      if(this.$store.state.token) {
        data.token = this.$store.state.token
      }
      getOnlineNumbers(data).then(res => {
        let results = JSON.parse(res)
        for (let result of results) {
          this.onlineNumbers.dates.push(result.fields['date'])
          this.onlineNumbers.times.push(result.fields['time'])
          this.onlineNumbers.numbers.push(result.fields['number'])
        }
        this.props_flag = true
      })
    },
    dateChange (val) {
      this.now_date = val
      this.getNumbers()
    }
  },
  created () {
    this.getNumbers()
  },
}
</script>

<style scoped>
@import "~@/assets/css/home.css";
</style>
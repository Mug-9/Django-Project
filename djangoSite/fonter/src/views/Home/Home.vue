<template>
  <div class="main">
    <div class="content">
      <echarts-time
        v-if="props_flag"
        echartsTime_id="echarts"
        echartsTime_width="1000px"
        echartsTime_height="800px"
        :echartsTime_data="crowdAge"
        @dateChange="dateChange"
      ></echarts-time>
    </div>
  </div>
</template>

<script>
import { GetCrowd } from 'network/get_crowd.js'
import EchartsTime from './EchartsTime.vue'
import * as func from '@/store/mutations-type.ts'

export default {
  name: "Home",
  data () {
    return {
      crowdAge: {
        age: [],
        rate_b: [],
        rate_all: [],
        tgi: [],
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
      this.crowdAge.age = []
      this.crowdAge.rate_b = []
      this.crowdAge.rate_all = []
      let data = {}
      if(this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetCrowd(data).then(res => {
        let results = JSON.parse(res)
        console.log(results);
        for (let result of results) {
          
          if(result['word'] == 'b站官网') {
            for (let age of result['age']) {
              this.crowdAge.age.push(age['desc'])
              this.crowdAge.rate_b.push(age['rate'])
              this.crowdAge.tgi.push(age['tgi'])
            }
          }else {
            for (let age of result['age']) {
              this.crowdAge.rate_all.push(age['rate'])
            }
          }
        }
        console.log(this.crowdAge.tgi);
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
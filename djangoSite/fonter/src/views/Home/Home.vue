<template>
  <div class="main">
    <div class="content">
      <div class="echarts">
        <echarts-baidu-index
          v-if="baiduIndex_flag"
          echartsBaiduIndex_id="echarts_baidu_index"
          :echartsBaiduIndex_width="baiduIndexWidth"
          echartsBaiduIndex_height="600px"
          :echartsBaiduIndex_data="baiduIndex"
          @dateChange="dateChange"
        >
        </echarts-baidu-index>
      </div>
      <div class="echarts">
        <echarts-crowd-age
          v-if="crowdAge_flag"
          echartsBase_id="echarts_crowd_age"
          :echartsBase_width="crowd_width"
          echartsBase_height="400px"
          :echartsBase_data="crowdAge"
          @dateChange="dateChange"
        ></echarts-crowd-age>
        <el-divider v-show="isIndivdual" direction="vertical"></el-divider>
        <echarts-crowd-sex
          v-if="crowdAge_flag"
          echartsBase_id="echarts_crowd_sex"
          :echartsBase_width="crowd_width"
          echartsBase_height="400px"
          :echartsBase_data="crowdSex"
          @dateChange="dateChange"
        >
        </echarts-crowd-sex>
      </div>
    </div>
  </div>
</template>

<script>
import { GetCrowdAge } from 'network/get_crowd.js'
import { GetBaiduIndex } from 'network/get_baidu_index.js'
import EchartsBaiduIndex from './EchartsBaiduIndex.vue'
import EchartsCrowdAge from './EchartsCrowdAge.vue'
import * as func from '@/store/mutations-type.ts'
import EchartsCrowdSex from './EchartsCrowdSex.vue'

export default {
  name: "Home",
  data () {
    return {
      isIndivdual: true,
      screenWidth: document.body.clientWidth - 200,
      days: 7,
      crowdAge: {
      },
      baiduIndex: {
        date: [],
        userIndexes: {},
      },
      crowdSex: {
      },
      crowdAge_flag: false,
      baiduIndex_flag: false,
      now_date: new Date()
    }
  },
  computed: {
    crowd_width () {
      if ((this.screenWidth - 100) / 2 < 700) {
        this.isIndivdual = false
        return this.screenWidth + 'px'
      } else {
        this.isIndivdual = true
        return ((this.screenWidth - 100) / 2) + 'px'
      }
    },
    baiduIndexWidth () {
      return this.screenWidth + 'px'
    }

  },
  watch: {
  },
  components: {
    EchartsBaiduIndex,
    EchartsCrowdAge,
    EchartsCrowdSex
  },
  methods: {
    getCrowdAge () {
      this.crowdAge.age = []
      this.crowdAge.rate_b = []
      this.crowdAge.rate_all = []
      let data = {}
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetCrowdAge(data).then(res => {
        let results = JSON.parse(res)
        console.log(results)
        for (let index in results) {
          let result = results[index]
          console.log(result)
          if (index == 0) {
            this.crowdAge['b'] = result['b']
            this.crowdAge['all'] = result['all']
            this.crowdAge['tgi'] = result['tgi']
            this.crowdAge['desc'] = result['desc']
          } else {
            this.crowdSex['b'] = result['b']
            this.crowdSex['all'] = result['all']
            this.crowdSex['tgi'] = result['tgi']
            this.crowdSex['desc'] = result['desc']
          }
        }
        this.crowdAge_flag = true
      })
    },
    getBaiduIndex () {
      let data = {
        type: this.days == 0 ? 'live' : 'index',
        days: this.days,
      }
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetBaiduIndex(data).then(res => {
        let results = JSON.parse(res)
        let kinds = ['all', 'pc', 'wise']
        for (let result of results) {
          for (let kind of kinds) {
            this.baiduIndex.userIndexes[kind] = result[kind]
          }
          this.baiduIndex.date = result['date']
        }
        this.baiduIndex_flag = true
      })
    },
    dateChange (val) {
      this.days = val
      this.getBaiduIndex()
    }
  },
  created () {
    this.getCrowdAge()
    this.getBaiduIndex()
  },
  mounted () {
    window.onresize = () => {
      return (() => {
        this.screenWidth = (document.body.clientWidth - 200)
      })()
    }
  }
}
</script>

<style scoped>
@import "~@/assets/css/home.css";
</style>
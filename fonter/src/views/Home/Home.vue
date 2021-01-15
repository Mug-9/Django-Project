<template>
  <div class="main">
    <div class="content">
      <el-tabs type="border-card">
        <el-tab-pane>
          <template #label
            ><img src="~@/assets/img/index.svg" alt="" />
            <span> 趋势</span>
          </template>
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
            <general-table
              v-if="baiduIndex_flag"
              :general_table="generals"
            ></general-table>
          </div>
        </el-tab-pane>
        <el-tab-pane label="人群">
          <template #label>
            <img src="~@/assets/img/crowd.svg" alt="" />
            <span>人群</span>
          </template>

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
          <div class="echarts">
            <echarts-interest
              v-if="interest_flag"
              echartsBase_id="echarts_interest"
              :echartsBase_width="baiduIndexWidth"
              echartsBase_height="600px"
              :echartsBase_data="crowd_interests"
            >
            </echarts-interest>
          </div>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import { GetBaiduIndex, GetCrowd, GetInterest } from 'network/get_baidu_index.js'
import EchartsBaiduIndex from './EchartsBaiduIndex.vue'
import EchartsCrowdAge from './EchartsCrowdAge.vue'
import EchartsCrowdSex from './EchartsCrowdSex.vue'
import EchartsInterest from './EchartsInterest.vue'
import * as func from '@/store/mutations-type.ts'
import GeneralTable from './general-table.vue'

export default {
  name: "Home",
  components: {
    EchartsBaiduIndex,
    EchartsCrowdAge,
    EchartsCrowdSex,
    EchartsInterest,
    GeneralTable
  },
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
      general: {

      },
      crowdSex: {
      },
      crowd_interests: {
      },
      crowdAge_flag: false,
      baiduIndex_flag: false,
      interest_flag: false,
      now_date: new Date()
    }
  },
  computed: {
    generals () {
      return this.general['all'] == undefined ? "" : [{
        all_avg: this.general['all'].avg,
        wise_avg: this.general['wise'].avg,
        all_yoy: this.general['all'].yoy + '%',
        all_qoq: this.general['all'].qoq + '%',
        wise_yoy: this.general['wise'].yoy + '%',
        wise_qoq: this.general['wise'].qoq + '%',
      }]
    },
    crowd_width () {
      if ((this.screenWidth - 100) / 2 < 700) {
        this.isIndivdual = false
        return Math.max(500, this.screenWidth) + 'px'
      } else {
        this.isIndivdual = true
        return ((this.screenWidth - 100) / 2) + 'px'
      }
    },
    baiduIndexWidth () {
      return Math.max(500, this.screenWidth) + 'px'
    }

  },
  methods: {
    getCrowd () {
      this.crowdAge.age = []
      this.crowdAge.rate_b = []
      this.crowdAge.rate_all = []
      let data = {}
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetCrowd(data).then(res => {
        let results = JSON.parse(res)
        for (let index in results) {
          let result = results[index]
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
          if (result['word'] == 'index') {
            for (let kind of kinds) {
              this.baiduIndex.userIndexes[kind] = result[kind]
            }
            this.baiduIndex.date = result['date']
          } else {
            for (let kind of kinds) {
              this.general[kind] = result[kind]
            }
          }
        }
        this.baiduIndex_flag = true
      })
    },
    getInterest () {
      let data = {}
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetInterest(data).then(res => {
        let results = JSON.parse(res)
        let kinds = ['all', 'b', 'desc', 'tgi']
        for (let kind of kinds) {
          this.crowd_interests[kind] = results[kind]
        }
        this.interest_flag = true
      })
    },
    dateChange (val) {
      this.days = val
      this.getBaiduIndex()
    }
  },
  created () {
    this.getCrowd()
    this.getBaiduIndex()
    this.getInterest()
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
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
              echartsBase_id="echarts_baidu_index"
              :echartsBase_width="baiduIndexWidth"
              echartsBase_height="600px"
            >
            </echarts-baidu-index>
          </div>
          <div class="echarts">
            <echarts-feed-index
              v-if="baiduFeedIndex_flag"
              echartsBase_id="echarts_baidu_feedIndex"
              :echartsBase_width="baiduIndexWidth"
              echartsBase_height="600px"
              :echartsBase_data="baidu_feedIndex"
              @feedIndex_dateChange="feedIndex_dateChange"
              @feedIndex_cityChange="feedIndex_cityChange"
            >
            </echarts-feed-index>
          </div>
        </el-tab-pane>
        <el-tab-pane label="人群">
          <template #label>
            <img src="~@/assets/img/crowd.svg" alt="" />
            <span>人群</span>
          </template>

          <div class="echarts">
            <echarts-region
              echartsBase_id="echarts_region"
              :echartsBase_width="crowd_width"
              echartsBase_height="400px"
            >
            </echarts-region>
          </div>

          <div class="echarts">
            <echarts-crowd
              :echartsBase_width="crowd_width"
              echartsBase_height="400px"
            ></echarts-crowd>
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
import { GetCrowd, GetInterest, GetFeedIndex, GetNewIndex } from 'network/get_baidu_index.js'
import EchartsBaiduIndex from './EchartsBaiduIndex.vue'
import EchartsCrowd from './EchartsCrowd.vue'
import EchartsInterest from './EchartsInterest.vue'
import * as func from '@/store/mutations-type.ts'
import EchartsFeedIndex from './EchartsFeedIndex.vue'
import EchartsRegion from './EchartsRegion.vue'

export default {
  name: "Home",
  components: {
    EchartsBaiduIndex,
    EchartsCrowd,
    EchartsInterest,
    EchartsFeedIndex,
    EchartsRegion
  },
  data () {
    return {
      isIndivdual: true,
      screenWidth: document.body.clientWidth - 200,
      days: 7,
      crowdAge: {
      },
      general: {
      },
      crowdSex: {
      },
      crowd_interests: {
      },
      baidu_feedIndex: {
        days: 7,
        area: '全国',

      },
      feedIndex_general: {
      },
      newIndex_general: {

      },
      crowdAge_flag: false,
      baiduIndex_flag: false,
      interest_flag: false,
      baiduFeedIndex_flag: false,
      now_date: new Date()
    }
  },
  computed: {
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
    getFeedIndex () {
      let data = {
        days: this.baidu_feedIndex['days'],
        area: this.baidu_feedIndex['area'],
      }
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetFeedIndex(data).then(res => {
        GetNewIndex(data).then(res => {
          let results = JSON.parse(res)
          for (let result of results) {
            if (result['word'] == 'newIndex') {
              this.baidu_feedIndex['newIndex'] = result['newIndex']
            } else {
              this.baidu_feedIndex['newIndex_general'] = result
              this.baidu_feedIndex['newIndex_general']['title'] = '新闻指数'
            }
          }
          this.baiduFeedIndex_flag = true
        })
        let results = JSON.parse(res)
        for (let result of results) {
          if (result['word'] == 'feedIndex') {
            this.baidu_feedIndex['date'] = result['date']
            this.baidu_feedIndex['feedIndex'] = result['feedIndex']
          } else {
            this.baidu_feedIndex['feedIndex_general'] = result
            this.baidu_feedIndex['feedIndex_general']['title'] = '资讯指数'
          }
        }

      })


    },
    feedIndex_dateChange (val) {
      this.baidu_feedIndex['days'] = val
      this.getFeedIndex()
    },
    feedIndex_cityChange (val) {
      this.baidu_feedIndex['area'] = val
      this.getFeedIndex()
    },
    region_dateChange (val) {
      this.baidu_region['days'] = val
      this.getRegion()
    }
  },
  created () {
    this.getInterest()
    this.getFeedIndex()
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
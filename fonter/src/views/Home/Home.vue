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
              echartsBase_id="echarts_baidu_feedIndex"
              :echartsBase_width="baiduIndexWidth"
              echartsBase_height="600px"
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
              echartsBase_id="echarts_interest"
              :echartsBase_width="baiduIndexWidth"
              echartsBase_height="600px"
            >
            </echarts-interest>
          </div>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
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
      general: {
      },
      crowd_interests: {
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
      if ((this.screenWidth - 100) / 2 < 300) {
        this.isIndivdual = false
        return Math.max(300, (this.screenWidth - 100) / 2 < 300) + 'px'
      } else {
        this.isIndivdual = true
        return ((this.screenWidth - 100) / 2) + 'px'
      }
    },
    baiduIndexWidth () {
      return Math.max(600, this.screenWidth) + 'px'
    }
  },
  methods: {


    region_dateChange (val) {
      this.baidu_region['days'] = val
      this.getRegion()
    }
  },
  created () {
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
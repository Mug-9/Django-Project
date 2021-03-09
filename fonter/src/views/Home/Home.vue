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
              echartsBase_height="350px"
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
import { ElLoading } from 'element-plus'

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
      screenWidth: document.body.clientWidth * 0.7,
      days: 7,
      now_date: new Date()
    }
  },
  computed: {
    crowd_width () {
      if ((this.screenWidth) / 2 < 500) {
        return Math.max(500, (this.screenWidth) / 2 < 300) + 'px'
      } else {
        return ((this.screenWidth) / 2) + 'px'
      }
    },
    baiduIndexWidth () {
      return Math.max(700, this.screenWidth) + 'px'
    }
  },
  methods: {
  },
  created () {
  },
  mounted () {
    window.onresize = () => {
      return (() => {
        this.screenWidth = document.body.clientWidth * 0.7

      })()
    }
  }
}
</script>

<style scoped>
@import "~@/assets/css/views/Home/home.css";
@import "~@/assets/css/component/el-tab/el-tab.css";
</style>
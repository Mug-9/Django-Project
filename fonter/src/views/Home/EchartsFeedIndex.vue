<template>
  <div class="echarts-date">
    <div class="echarts-div">
      <echarts
        :echarts_id="echartsBase_id"
        :width="echartsBase_width"
        :height="echartsBase_height"
        :options="options"
      ></echarts>
    </div>
    <div class="days-div">
      <el-dropdown @command="feedIndex_dateChange">
        <el-button type="primary">
          {{ days + "   " }}<i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item command="7">近7天</el-dropdown-item>
            <el-dropdown-item command="30">近30天</el-dropdown-item>
            <el-dropdown-item command="60">近60天</el-dropdown-item>
            <el-dropdown-item command="90">近90天</el-dropdown-item>
            <el-dropdown-item command="180">近半年</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      <city-pick @cityChange="cityChange" class="city-pick"> </city-pick>
    </div>
  </div>

  <div class="table-div">
    <feed-index-general :general_table="echartsBase_data['feedIndex_general']">
    </feed-index-general>
    <feed-index-general :general_table="echartsBase_data['newIndex_general']">
    </feed-index-general>
  </div>
</template>

<script>
import Echarts from './Echarts'
import CityPick from '@/components/commons/select-city/city-pick.vue'

import FeedIndexGeneral from './feedIndexGeneral.vue'
export default {
  name: "EchartsBaiduFeedIndex",
  components: {
    Echarts,
    CityPick,
    FeedIndexGeneral
  },
  props: {
    echartsBase_id: {
      type: String
    },
    echartsBase_width: {
      type: String
    },
    echartsBase_height: {
      type: String
    },
    echartsBase_data: {
      type: Object
    },
    echartsBase_date: {
      type: Object,
    },
  },
  data () {
    return {
      echarts_width: this.echartsBase_width,
      days: "近7天",
      now_date: this.echartsBase_date,
      options: {
        title: {
          text: '百度资讯指数'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          }
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        legend: {
          data: ['资讯指数', '媒体指数'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: this.echartsBase_data['date'],
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#8a2be2'
            }
          },
        }],
        yAxis: [{
          type: 'value',
          name: '资讯指数',
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#ff7f50',
              width: 2,
              type: 'solid'
            }
          },
        }, {
          type: 'value',
          name: '媒体指数',
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#0000ff',
              width: 2,
              type: 'solid'
            }
          },
        }
        ],
        series: [
          {
            name: "资讯指数",
            type: "line",
            color: '#ff7f50',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: this.echartsBase_data['feedIndex'],
          },
          {
            name: "媒体指数",
            type: "line",
            color: '#0000ff',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            yAxisIndex: 1,
            data: this.echartsBase_data['newIndex'],
          },
        ]
      }
    }
  },
  watch: {
    'echartsBase_data': {
      handler (newV, oldV) {
        this.options.series[0].data = newV['feedIndex']
        this.options.xAxis[0].data = newV['date']
        this.options.series[1].data = newV['newIndex']
      },
      deep: true
    },
    echartsBase_width: {
      handler (newV, oldV) {
        this.echarts_width = newV
      },
      deep: true
    }
  },
  methods: {
    feedIndex_dateChange (command) {
      if (command == '180') {
        this.days = '近半年'
      } else {
        this.days = '近' + command + '天'
      }
      this.$emit('feedIndex_dateChange', command)
    },
    cityChange (val) {
      this.$emit('feedIndex_cityChange', val)

    }
  },
  mounted () {
  }
}
</script>

<style scoped>
@import "~@/assets/css/echarts_time.css";
.table-div {
  width: 95%;
  margin: 10px auto;
  display: flex;
}
.diver {
  display: inline-flex;
  left: 50%;
  height: 60px;
  widows: 5px;
  background-color: red;
}
</style>
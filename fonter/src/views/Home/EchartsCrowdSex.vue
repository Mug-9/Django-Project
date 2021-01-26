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
  </div>
</template>

<script>
import Echarts from './Echarts'
import DayPick from 'commons/time-pick/DayPick.vue'

export default {
  name: "EchartsCrowdAge",
  components: {
    Echarts,
    DayPick
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
  },
  data () {
    return {
      options: {
        title: {
          text: '年龄分布'
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
          data: ['b站', '全网', 'tgi'],
        },
        xAxis: [{
          type: 'category',
          axisTick: {
            alignWithLabel: true
          },
          data: this.echartsBase_data['desc'],
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#8a2be2'
            }
          },
        }],
        yAxis: [{
          type: 'value',
          name: '百分比',
          max: 100,
          min: 0,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#00a1d6',
              width: 2,
            }
          },
          axisLabel: {
            formatter: '{value} %'
          }
        }, {
          type: 'value',
          name: 'TGI指数',
          max: 200,
          min: 0,
          axisLine: {
            show: true,
            lineStyle: {
              color: '#d14a61',
              width: 2,
            }
          },
        },
        ],
        series: [{
          name: 'b站',
          type: 'bar',
          color: '#00a1d6',
          data: this.echartsBase_data['b']
        },
        {
          name: "全网",
          type: 'bar',
          data: this.echartsBase_data['all']
        },
        {
          name: "tgi",
          type: "line",
          smooth: 1,
          lineStyle: {
            width: 5
          },
          data: this.echartsBase_data['tgi'],
          yAxisIndex: 1,
          color: '#d14a61',
        }]
      }
    }
  },
  watch: {
  },
  methods: {
    dateChange (val) {
      this.now_date = val
      this.$emit('dateChange', val)
    },
  },
  mounted () {
  }
}
</script>

<style scoped>
@import "~@/assets/css/echarts_time.css";
</style>
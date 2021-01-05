<template>
  <div class="echarts-date">
    <div class="echarts-div">
      <echarts
        :echarts_id="echartsTime_id"
        :width="echartsTime_width"
        :height="echartsTime_height"
        :options="options"
      ></echarts>
    </div>
    <div class="day-pick-div" v-show="false">
      <day-pick :dayPick_date="now_date" @dateChange="dateChange"></day-pick>
    </div>
  </div>
</template>

<script>
import Echarts from './Echarts'
import DayPick from 'commons/time-pick/DayPick.vue'

export default {
  name: "EchartsTime",
  components: {
    Echarts,
    DayPick
  },
  props: {
    echartsTime_id: {
      type: String
    },
    echartsTime_width: {
      type: String
    },
    echartsTime_height: {
      type: String
    },
    echartsTime_data: {
      type: Object
    },
    echartsTime_date: {
      type: Object,
    }
  },
  data () {
    return {
      now_date: this.echartsTime_date,
      options: {
        title: {
          text: '性别分布'
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
          data: this.echartsTime_data.age
        }],
        yAxis: [{
          type: 'value',
          name: '百分比',
          max: 100,
          min: 0,
          axisLine: {
            lineStyle: {
              color: '#00a1d6'
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
            lineStyle: {
              color: '#d14a61'
            }
          },

        },
        ],
        series: [{
          name: 'b站',
          type: 'bar',
          color: '#00a1d6',
          data: this.echartsTime_data.rate_b
        },
        {
          name: "全网",
          type: 'bar',
          data: this.echartsTime_data.rate_all
        },
        {
          name: "tgi",
          type: "line",
          data: this.echartsTime_data.tgi,
          yAxisIndex: 1,
          color: '#d14a61',
        }]
      }
    }
  },
  watch: {
    'echartsTime_data.times': {
      handler (newV, oldV) {
        console.log(newV)
        this.options.xAxis.data = newV
        console.log(this.options.xAxis.data)
      }
    },
    'echartsTime_data.numbers': {
      handler (newV, oldV) {
        console.log(newV)
        this.options.series[0].data = newV
        console.log(this.options.series[0].data)
      }
    }
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
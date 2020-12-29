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
    <div class="day-pick-div">
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
          text: 'bilibili在线人数'
        },
        tooltip: {},
        legend: {
          data: ['人数']
        },
        xAxis: {
          data: this.echartsTime_data.times
        },
        yAxis: {},
        series: [{
          name: '人数',
          type: 'line',
          data: this.echartsTime_data.numbers
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
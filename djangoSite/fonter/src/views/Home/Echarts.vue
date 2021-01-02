<template>
  <div>
    <div :id="echarts_id" :style="style"></div>
  </div>
</template>

<script>
// const echarts = require('echarts')

import { inject } from "vue"

export default {
  name: "Echarts",
  inject: ["Echarts"],
  props: {
    echarts_id: {
      type: String,
    },
    width: {
      type: String,
      default: "1000px",
    },
    height: {
      type: String,
      default: "800px",
    },
    options: {
      type: Object,
      default () {
        return {
          title: {
            text: "vue-Echarts",
          },
          legend: {
            data: ["销量"],
          },
          xAxis: {
            data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
          },
          yAxis: [
            {
              type: "value",
            },
          ],
          series: [
            {
              name: "销量",
              type: "line",
              data: [5, 20, 36, 10, 10, 70],
            },
          ],
        }
      },
    },
  },
  data () {
    return {
      charts: "",
    }
  },
  computed: {
    style () {
      return {
        height: this.height,
        width: this.width,
      }
    },
  },
  watch: {
    options: {
      handler (newV, oldV) {
        console.log(newV)
        if (this.echarts) {
          if (newV) {
            this.echarts.clear()
            this.echarts.setOption(newV)
          } else {
            this.echarts.clear()
            this.echarts.setOption(oldV)
          }
        } else {
          this.init()
        }
      },
      deep: true,
    },
  },
  methods: {
    init () {
      this.echarts = this.Echarts.init(
        document.getElementById(this.echarts_id)
      )
      this.echarts.setOption(this.options)
    },
  },
  mounted () {
    this.init()
  },
};
</script>

<style scoped>
</style>
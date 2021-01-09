<template>
  <div>
    <div :id="echarts_id" :style="style"></div>
  </div>
</template>

<script>

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
      r_width: this.width
    }
  },
  computed: {
    style () {
      return {
        height: this.height,
        width: this.r_width,
      }
    },
  },
  watch: {
    options: {
      handler (newV, oldV) {
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
    width: {
      handler (newV, oldV) {
        this.r_width = newV
      }
    }
  },
  methods: {
    init () {
      this.echarts = this.Echarts.init(
        document.getElementById(this.echarts_id)
      )
      this.echarts.setOption(this.options)
      window.addEventListener('resize', () => { this.echarts.resize() })
    },
  },
  mounted () {
    this.init()
  },
};
</script>

<style scoped>
</style>
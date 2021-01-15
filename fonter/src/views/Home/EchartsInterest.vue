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

export default {
  name: "EchartsInterest",
  components: {
    Echarts,
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
      echarts_width: this.echartsBase_width,
      options: {

        title: {
          text: '兴趣分布'
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
          data: ['b站', '全网', 'TGI指数'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: this.echartsBase_data['desc'],
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
          name: '人群占比',
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
              type: 'solid'
            }
          },
          axisLabel: {
            formatter: '{value} %'
          }
        },
        {
          type: 'value',
          name: 'TGI指数',
          max: 200,
          min: 0,
          // nameTextStyle: {//y轴上方单位的颜色
          //   color: '#151515',
          // },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#d14a61',
              width: 2,
              type: 'solid'
            }
          },
        },
        ],
        series: [
          {
            name: "b站",
            type: "bar",
            color: '#00a1d6',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: this.echartsBase_data['b'],
          },
          {
            name: '全网',
            type: "bar",
            color: '#6495ed',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: this.echartsBase_data['all'],
          },
          {
            name: "TGI指数",
            type: "line",
            color: '#d14a61',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            yAxisIndex: 1,
            data: this.echartsBase_data['tgi'],
          },
        ]
      }
    }
  },
  watch: {
    echartsBase_width: {
      handler (newV, oldV) {
        this.echarts_width = newV
      },
      deep: true
    }
  },
  methods: {

  },
  mounted () {
  }
}
</script>

<style scoped>
@import "~@/assets/css/echarts_time.css";
</style>
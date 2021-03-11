<template>
  <div
    class="echarts-date"
    v-loading="echartsBase_data['loading']"
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.8)"
    element-loading-text="拼命加载中"
  >
    <div class="echarts-div">
      <echarts
        :echarts_id="echartsBase_id"
        :width="echarts_width"
        :height="echartsBase_height"
        :options="options"
      ></echarts>
    </div>
  </div>
</template>

<script>
import Echarts from '@/components/commons/Echarts/Echarts.vue'

export default {
  name: "EchartsBaiduIndex",
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
    }
  },
  data () {
    return {
      echarts_width: this.echartsBase_width,
      options: {
        title: {
          text: '视频数据曲线',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            animation: false
          }
        },
        grid: [{
          left: "20%",
          right: "20%",
          height: '35%'
        }, {
          left: "20%",
          right: "20%",
          height: '35%',
          top: '55%'
        }],
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        axisPointer: {
          link: { xAxisIndex: 'all' }
        },
        dataZoom: [
          {
            show: true,
            start: 30,
            end: 70,
            xAxisIndex: [0, 1]
          },
          {
            type: 'inside',
            start: 30,
            end: 70,
            xAxisIndex: [0, 1]
          }
        ],
        legend: {
          data: ['播放量', '投币', '点赞', '收藏', '弹幕', '评论'],
          left: 10
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: this.echartsBase_data['dateTime'],
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#8a2be2'
            }
          },
        },
        {
          gridIndex: 1,
          show: true,
          type: 'category',
          data: this.echartsBase_data['dateTime'],
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              width: 2,
              color: '#8a2be2'
            }
          },
          position: 'top'
        }],
        yAxis: [{
          type: 'value',
          name: '播放量',
          position: 'left',
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
        },
        {
          type: 'value',
          name: '点赞',
          position: 'left',
          offset: 50,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#5f9ea0',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          type: 'value',
          name: '投币',
          position: 'left',
          offset: 100,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#daa520',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          type: 'value',
          name: '收藏',
          position: 'right',
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#6b8e23',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          type: 'value',
          name: '弹幕',
          position: 'right',
          offset: 50,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#00ff7f',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          type: 'value',
          name: '评论',
          position: 'right',
          offset: 100,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#4169e1',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          gridIndex: 1,
          inverse: true,
          type: 'value',
          name: '播放量增长',
          position: 'left',
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
        },
        {
          gridIndex: 1,
          inverse: true,
          type: 'value',
          name: '点赞增长',
          position: 'left',
          offset: 50,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#5f9ea0',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          gridIndex: 1,
          inverse: true,
          type: 'value',
          name: '投币增长',
          position: 'left',
          offset: 100,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#daa520',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          gridIndex: 1,
          inverse: true,
          type: 'value',
          name: '收藏增长',
          position: 'right',
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#6b8e23',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          gridIndex: 1,
          inverse: true,
          type: 'value',
          name: '弹幕增长',
          position: 'right',
          offset: 50,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#00ff7f',
              width: 2,
              type: 'solid'
            }
          },
        },
        {
          gridIndex: 1,
          inverse: true,
          type: 'value',
          name: '评论增长',
          position: 'right',
          offset: 100,
          nameTextStyle: {//y轴上方单位的颜色
            color: '#151515',
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: '#ff4500',
              width: 2,
              type: 'solid'
            }
          },
        },
        ],
        series: [
          {
            name: "播放量",
            type: "line",
            color: '#ff7f50',
            smooth: 0,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['view'],
          },
          {
            name: '点赞',
            type: "line",
            color: '#5f9ea0',
            yAxisIndex: 1,
            smooth: 0,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['like'],
          },
          {
            name: "投币",
            type: "line",
            yAxisIndex: 2,
            color: '#daa520',
            smooth: 0,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['coin'],
          },
          {
            name: "收藏",
            type: "bar",
            yAxisIndex: 3,
            color: '#6b8e23',
            smooth: 0,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['favorite'],
          },
          {
            name: "弹幕",
            type: "bar",
            yAxisIndex: 4,
            color: '#00ff7f',
            smooth: 0,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['danmaku'],
          },
          {
            name: "评论",
            type: "bar",
            yAxisIndex: 5,
            color: '#4169e1',
            smooth: 0,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['reply'],
          },
          {
            name: "播放量增长",
            type: "line",
            color: '#ff7f50',
            smooth: 0,
            xAxisIndex: 1,
            yAxisIndex: 6,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['view_d'],
          },
          {
            name: '点赞增长',
            type: "line",
            color: '#5f9ea0',
            smooth: 0,
            xAxisIndex: 1,
            yAxisIndex: 7,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['like_d'],
          },
          {
            name: "投币增长",
            type: "line",
            color: '#daa520',
            smooth: 0,
            xAxisIndex: 1,
            yAxisIndex: 8,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['coin_d'],
          },
          {
            name: "收藏增长",
            type: "bar",
            color: '#6b8e23',
            smooth: 0,
            xAxisIndex: 1,
            yAxisIndex: 9,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['favorite_d'],
          },
          {
            name: "弹幕增长",
            type: "bar",
            color: '#00ff7f',
            smooth: 0,
            xAxisIndex: 1,
            yAxisIndex: 10,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['danmaku_d'],
          },
          {
            name: "评论增长",
            type: "bar",
            color: '#4169e1',
            smooth: 0,
            xAxisIndex: 1,
            yAxisIndex: 11,
            lineStyle: {
              width: 2
            },
            data: this.echartsBase_data['reply_d'],
          },
        ]
      }
    }
  },
  computed: {
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
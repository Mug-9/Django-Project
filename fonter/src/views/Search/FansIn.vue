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

  <div>
    <baidu-index-general
      v-if="!echartsBase_data['loading']"
      :general_table="echartsBase_data['general']"
    >
    </baidu-index-general>
  </div>
  <div v-if="!echartsBase_data['loading']">
    <comments :comment_data="commentData"> </comments>
  </div>
</template>

<script>
import Echarts from '@/components/commons/Echarts/Echarts.vue'


export default {
  name: "FansIn",
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
    },
  },
  data () {
    return {
      echarts_width: this.echartsBase_width,
      options: {
        title: {
          text: '粉丝增长趋势'
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
          data: ['粉丝数量', '粉丝增长数'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: this.echartsBase_data['fans_time'],
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
          name: '粉丝数量',
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
          name: '粉丝增长数',
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
            name: "粉丝数量",
            type: "line",
            color: '#0000ff',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            data: this.echartsBase_data['fans_list'],
          },
          {
            name: '粉丝增长数',
            type: "line",
            color: '#6495ed',
            smooth: 0.6,
            lineStyle: {
              width: 5
            },
            yAxisIndex: 1,
            data: this.echartsBase_data['fand_list'],
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
</style>
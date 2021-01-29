<template>
  <div class="echarts-date">
    <div class="echarts-div">
      <echarts
        v-if="!echartsBase_data['loading']"
        echarts_id="echartsAge"
        :width="echartsBase_width"
        :height="echartsBase_height"
        :options="options['Age']"
      ></echarts>
      <echarts
        v-if="!echartsBase_data['loading']"
        echarts_id="echartsSex"
        :width="echartsBase_width"
        :height="echartsBase_height"
        :options="options['Sex']"
      ></echarts>
    </div>
  </div>
</template>

<script>
import { GetCrowd } from 'network/get_baidu_index.js'
import Echarts from './Echarts'
import DayPick from 'commons/time-pick/DayPick.vue'

export default {
  name: "EchartsCrowdAge",
  components: {
    Echarts,
    DayPick
  },
  props: {
    echartsBase_width: {
      type: String
    },
    echartsBase_height: {
      type: String
    },
  },
  data () {
    return {
      echartsBase_data: {
        crowdAge: {},
        crowdSex: {},
        loading: true,
      },
      options: {
        Age: {
          title: {
            text: null
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
            data: null,
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
            data: null
          },
          {
            name: "全网",
            type: 'bar',
            data: null
          },
          {
            name: "tgi",
            type: "line",
            smooth: 1,
            lineStyle: {
              width: 5
            },
            data: null,
            yAxisIndex: 1,
            color: '#d14a61',
          }]
        },
        Sex: {
          title: {
            text: null
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
            data: null,
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
            data: null
          },
          {
            name: "全网",
            type: 'bar',
            data: null
          },
          {
            name: "tgi",
            type: "line",
            smooth: 1,
            lineStyle: {
              width: 5
            },
            data: null,
            yAxisIndex: 1,
            color: '#d14a61',
          }]
        },
      },

    }
  },
  computed: {
  },
  methods: {
    getCrowd () {
      let data = {}
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetCrowd(data).then(res => {
        let results = JSON.parse(res)
        for (let index in results) {
          let result = results[index]
          if (index == 0) {
            this.echartsBase_data['crowdAge']['b'] = result['b']
            this.echartsBase_data['crowdAge']['all'] = result['all']
            this.echartsBase_data['crowdAge']['tgi'] = result['tgi']
            this.echartsBase_data['crowdAge']['desc'] = result['desc']
          } else {
            this.echartsBase_data['crowdSex']['b'] = result['b']
            this.echartsBase_data['crowdSex']['all'] = result['all']
            this.echartsBase_data['crowdSex']['tgi'] = result['tgi']
            this.echartsBase_data['crowdSex']['desc'] = result['desc']
          }
        }
        this.options['Age'].title.text = "年龄分布"
        this.options['Age'].xAxis[0].data = this.echartsBase_data['crowdAge']['desc']
        this.options['Age'].series[0].data = this.echartsBase_data['crowdAge']['b']
        this.options['Age'].series[1].data = this.echartsBase_data['crowdAge']['all']
        this.options['Age'].series[2].data = this.echartsBase_data['crowdAge']['tgi']
        this.options['Sex'].title.text = "性别分布"
        this.options['Sex'].xAxis[0].data = this.echartsBase_data['crowdSex']['desc']
        this.options['Sex'].series[0].data = this.echartsBase_data['crowdSex']['b']
        this.options['Sex'].series[1].data = this.echartsBase_data['crowdSex']['all']
        this.options['Sex'].series[2].data = this.echartsBase_data['crowdSex']['tgi']
        this.echartsBase_data['loading'] = false
      })
    },
  },
  mounted () {
    this.getCrowd()
  }
}
</script>

<style scoped>
@import "~@/assets/css/echarts_time.css";
</style>
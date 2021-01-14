<template>
  <div class="main">
    <div class="content">
      <div class="echarts">
        <echarts-baidu-index
          v-if="baiduIndex_flag"
          echartsBaiduIndex_id="echarts_baidu_index"
          :echartsBaiduIndex_width="baiduIndexWidth"
          echartsBaiduIndex_height="600px"
          :echartsBaiduIndex_data="baiduIndex"
          @dateChange="dateChange"
        >
        </echarts-baidu-index>
        <el-table
          v-if="baiduIndex_flag"
          :data="general_table"
          class="general_table"
        >
          <el-table-column prop="all_avg" label="整体日均值"> </el-table-column>
          <el-table-column prop="wise_avg" label="移动日均值">
          </el-table-column>
          <el-table-column prop="all_yoy" label="整体同比">
            <template #default="scope">
              <span v-if="scope.row.all_yoy[0] == '-'">
                <font color="#19BE6B07">{{ scope.row.all_yoy }} </font>
              </span>
              <span v-else>
                <font color="red">{{ scope.row.all_yoy }} </font></span
              >
              <img
                v-if="scope.row.all_yoy[0] == '-'"
                src="~assets/img/dicline.svg"
                alt=""
              />
              <img v-else src="~assets/img/up.svg" alt="" />
            </template>
          </el-table-column>
          <el-table-column prop="all_qoq" label="整体环比">
            <template #default="scope">
              <span v-if="scope.row.all_qoq[0] == '-'">
                <font color="#19BE6B07">{{ scope.row.all_qoq }} </font>
              </span>
              <span v-else>
                <font color="red">{{ scope.row.all_qoq }} </font></span
              >
              <img
                v-if="scope.row.all_qoq[0] == '-'"
                src="~assets/img/dicline.svg"
                alt=""
              />
              <img v-else src="~assets/img/up.svg" alt="" />
            </template>
          </el-table-column>

          <el-table-column prop="wise_yoy" label="移动同比">
            <template #default="scope">
              <span v-if="scope.row.wise_yoy[0] == '-'">
                <font color="#19BE6B07">{{ scope.row.wise_yoy }} </font>
              </span>
              <span v-else>
                <font color="red">{{ scope.row.wise_yoy }} </font></span
              >
              <img
                v-if="scope.row.wise_yoy[0] == '-'"
                src="~assets/img/dicline.svg"
                alt=""
              />
              <img v-else src="~assets/img/up.svg" alt="" /> </template
          ></el-table-column>
          <el-table-column prop="wise_qoq" label="移动环比">
            <template #default="scope">
              <span v-if="scope.row.wise_qoq[0] == '-'">
                <font color="#19BE6B07">{{ scope.row.wise_qoq }} </font>
              </span>
              <span v-else>
                <font color="red">{{ scope.row.wise_qoq }} </font></span
              >
              <img
                v-if="scope.row.wise_qoq[0] == '-'"
                src="~assets/img/dicline.svg"
                alt=""
              />
              <img v-else src="~assets/img/up.svg" alt="" /> </template
          ></el-table-column>
        </el-table>
      </div>
      <div class="echarts">
        <echarts-crowd-age
          v-if="crowdAge_flag"
          echartsBase_id="echarts_crowd_age"
          :echartsBase_width="crowd_width"
          echartsBase_height="400px"
          :echartsBase_data="crowdAge"
          @dateChange="dateChange"
        ></echarts-crowd-age>
        <el-divider v-show="isIndivdual" direction="vertical"></el-divider>
        <echarts-crowd-sex
          v-if="crowdAge_flag"
          echartsBase_id="echarts_crowd_sex"
          :echartsBase_width="crowd_width"
          echartsBase_height="400px"
          :echartsBase_data="crowdSex"
          @dateChange="dateChange"
        >
        </echarts-crowd-sex>
      </div>
    </div>
  </div>
</template>

<script>
import { GetBaiduIndex, GetCrowd } from 'network/get_baidu_index.js'
import EchartsBaiduIndex from './EchartsBaiduIndex.vue'
import EchartsCrowdAge from './EchartsCrowdAge.vue'
import * as func from '@/store/mutations-type.ts'
import EchartsCrowdSex from './EchartsCrowdSex.vue'

export default {
  name: "Home",
  data () {
    return {
      isIndivdual: true,
      screenWidth: document.body.clientWidth - 200,
      days: 7,
      crowdAge: {
      },
      baiduIndex: {
        date: [],
        userIndexes: {},
      },
      general: {

      },
      crowdSex: {
      },
      crowdAge_flag: false,
      baiduIndex_flag: false,
      now_date: new Date()
    }
  },
  computed: {
    general_table () {
      return this.general['all'] == undefined ? "" : [{
        all_avg: this.general['all'].avg,
        wise_avg: this.general['wise'].avg,
        all_yoy: this.general['all'].yoy + '%',
        all_qoq: this.general['all'].qoq + '%',
        wise_yoy: this.general['wise'].yoy + '%',
        wise_qoq: this.general['wise'].qoq + '%',
      }]
    },
    crowd_width () {
      if ((this.screenWidth - 100) / 2 < 700) {
        this.isIndivdual = false
        return Math.max(500, this.screenWidth) + 'px'
      } else {
        this.isIndivdual = true
        return ((this.screenWidth - 100) / 2) + 'px'
      }
    },
    baiduIndexWidth () {
      return Math.max(500, this.screenWidth) + 'px'
    }

  },
  watch: {
  },
  components: {
    EchartsBaiduIndex,
    EchartsCrowdAge,
    EchartsCrowdSex
  },
  methods: {
    getCrowd () {
      this.crowdAge.age = []
      this.crowdAge.rate_b = []
      this.crowdAge.rate_all = []
      let data = {}
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetCrowd(data).then(res => {
        let results = JSON.parse(res)
        for (let index in results) {
          let result = results[index]
          if (index == 0) {
            this.crowdAge['b'] = result['b']
            this.crowdAge['all'] = result['all']
            this.crowdAge['tgi'] = result['tgi']
            this.crowdAge['desc'] = result['desc']
          } else {
            this.crowdSex['b'] = result['b']
            this.crowdSex['all'] = result['all']
            this.crowdSex['tgi'] = result['tgi']
            this.crowdSex['desc'] = result['desc']
          }
        }
        this.crowdAge_flag = true
      })
    },
    getBaiduIndex () {
      let data = {
        type: this.days == 0 ? 'live' : 'index',
        days: this.days,
      }
      if (this.$store.state.token) {
        data.token = this.$store.state.token
      }
      GetBaiduIndex(data).then(res => {
        let results = JSON.parse(res)
        console.log(results)
        let kinds = ['all', 'pc', 'wise']
        for (let result of results) {
          if (result['word'] == 'index') {
            for (let kind of kinds) {
              this.baiduIndex.userIndexes[kind] = result[kind]
            }
            this.baiduIndex.date = result['date']
          } else {
            for (let kind of kinds) {
              this.general[kind] = result[kind]
            }
          }
        }
        this.baiduIndex_flag = true
      })
    },
    dateChange (val) {
      this.days = val
      this.getBaiduIndex()
    }
  },
  created () {
    this.getCrowd()
    this.getBaiduIndex()
  },
  mounted () {
    window.onresize = () => {
      return (() => {
        this.screenWidth = (document.body.clientWidth - 200)
      })()
    }
  }
}
</script>

<style scoped>
@import "~@/assets/css/home.css";
</style>
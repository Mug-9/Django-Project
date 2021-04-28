<template>
  <div class="main">
    <div class="content">
      <div class="up">
        <div class="face_desc">
          <div class="face">
            <img
              class="face_img"
              src="http://i0.hdslb.com/bfs/face/93f3d5d1085357565a4c2e4ac151104ac3d783ac.jpg"
              alt=""
            />
            <p class="name">宝剑嫂</p>
          </div>
          <div class="desc">
            <p>认证信息： bilibili2020百大UP主</p>
            <p>账户简介： 努力做人民的好猪猪 【微博@宝剑嫂】</p>
          </div>
        </div>
        <div class="rank">
          <img src="~@/assets/img/up_data.png" alt="" />
        </div>
      </div>
      <div class="detail">
        <div class="total">
          <img class="img1" src="~@/assets/img/video_data.png" alt="" />
        </div>
        <div class="choose">
          <el-button>数据趋势</el-button>
          <el-button>历史作品监测</el-button>
          <el-button>活跃粉丝画像</el-button>
          <el-button type="primary">作品画像</el-button>
          <el-button>广告分析</el-button>
        </div>
        <div class="fanstu" v-show="false">
          <img src="~@/assets/img/粉丝性别分布.png" alt="" />
          <img class="img2" src="~@/assets/img/活跃粉丝年龄分布.png" alt="" />
          <img src="~@/assets/img/echarts(2).png" alt="" />
          <img src="~@/assets/img/echarts(3).png" alt="" />
          <img src="~@/assets/img/echarts(1).png" alt="" />
        </div>

        <div>
          <div class="fanstu">
            <p class="title">作品分布</p>
            <img src="~@/assets/img/echarts(4).png" alt="" />
            <img class="img2" src="~@/assets/img/echarts(5).png" alt="" />
          </div>
          <div class="fanstu">
            <p class="title">最多播放TOP3</p>
            <img src="~@/assets/img/echarts(7).png" alt="" />
          </div>
          <div class="fanstu">
            <p class="title">最低播放TOP3</p>
            <img src="~@/assets/img/echarts(8).png" alt="" />
          </div>
          <div class="fanstu">
            <p class="title">作品发布时间分布</p>
            <img src="~@/assets/img/echarts(6).png" alt="" />
          </div>
        </div>
        <div class="fanstu" v-show="false">
          <div class="abs">
            <p class="title3">推广数： <span class="num">15</span></p>

            <el-divider></el-divider>
            <div class="title4">
              美妆： <span class="red">13</span> 科技：<span class="red"
                >2
              </span>
            </div>
            <p></p>
          </div>
          <div class="jinqi">
            <p class="title3">近期推广</p>
            <el-divider></el-divider>
            <div class="daili">
              <div class="dailiItem">
                <p class="title">2020-12-11</p>
                <p class="title">
                  <span class="red">唐代女子风情万种</span> --
                  <span class="num">御泥坊</span>
                </p>
              </div>
              <div class="dailiItem">
                <p class="title">2020-10-21</p>
                <p class="title">
                  <span class="red">我去工厂啦！【膜法世家x宝剑嫂】</span>
                  --
                  <span class="num">膜法世家</span>
                </p>
              </div>
            </div>
            <div class="daili">
              <div class="dailiItem">
                <p class="title">2020-08-10</p>
                <p class="title">
                  <span class="red"
                    >挑战全脸芭比粉，没想到居然...还怪好看！</span
                  >
                  --
                  <span class="num">娇韵诗</span>
                </p>
              </div>
              <div class="dailiItem">
                <p class="title">2020-03-20</p>
                <p class="title">
                  <span class="red">八分钟教你变成娇俏小女人!</span> --
                  <span class="num">雅思兰黛</span>
                </p>
              </div>
            </div>
            <p>近期推广全为美妆类</p>
            <p class="title3">近期推广数据走势</p>
            <el-divider></el-divider>
            <echarts
              class="data2"
              echarts_id="abc4"
              width="600px"
              height="400px"
              :options="options"
            ></echarts>
            <p>
              近几期推广数据向好，最新一期推广数据最佳，现在是最佳的推广时期。
            </p>
            <p class="title3">近期推广数据</p>
            <el-divider></el-divider>
            <div class="data" v-for="item in items" :key="item">
              <online-item isShowComment="true">
                <template v-slot:slot-img>
                  <a :href="get_url(item)"><img :src="item['pic']" alt="" /></a>
                </template>
                <template v-slot:item-title>
                  <p>{{ item["title"] }}</p>
                </template>
                <template v-slot:item-bv>
                  <el-link
                    type="primary"
                    :href="get_url(item)"
                    :underline="false"
                  >
                    {{ item["bvid"] }}</el-link
                  >
                </template>
                <template v-slot:item-desc>
                  <el-input
                    type="textarea"
                    :autosize="{ minRows: 2, maxRows: 2 }"
                    v-model="item['desc']"
                    :disabled="true"
                  >
                  </el-input>
                </template>
                <template v-slot:item-author>
                  <a href=""></a><img :src="item['owner']['face']" alt="" />
                  {{ item["owner"]["name"] }}
                </template>
                <template v-slot:item-coin
                  >:{{ item["stat"]["coin"] }}
                </template>
                <template v-slot:item-like
                  >:{{ item["stat"]["like"] }}
                </template>
                <template v-slot:item-danmu
                  >:{{ item["stat"]["danmaku"] }}
                </template>
                <template v-slot:item-favorite>
                  :{{ item["stat"]["favorite"] }}
                </template>
                <template v-slot:item-reply
                  >:{{ item["stat"]["reply"] }}
                </template>
                <template v-slot:item-share
                  >:{{ item["stat"]["share"] }}
                </template>
                <template v-slot:item-view
                  >:{{ item["stat"]["view"] }}
                </template>
                <template v-slot:item-tname> {{ item["tname"] }} </template>
                <template v-slot:pubupdate>:{{ item["pubdate"] }} </template>
                <template v-slot:duration>{{ item["duration"] }}</template>
              </online-item>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Echarts from '@/components/commons/Echarts/Echarts.vue'
import onlineItem from 'commons/online-list/online-item.vue'
export default {
  name: "Detail",
  components: { onlineItem, Echarts },
  data () {
    return {
      items: [{
        aid: 970051991,
        bvid: "BV1Lp4y1k7pG",
        cid: 247985378,
        copyright: 1,
        ctime: 1603283832,
        desc: "喜欢这个视频的话一定要一键三连呀~~~",
        dimension: { width: 1920, height: 1080, rotate: 0 },
        height: 1080,
        rotate: 0,
        width: 1920,
        duration: 595,
        dynamic: "进来看我一人体验四份工作！！！原来我最适合当客服哈哈哈～",
        mission_id: 14567,
        no_cache: false,
        owner: {
          face: "http://i0.hdslb.com/bfs/face/93f3d5d1085357565a4c2e4ac151104ac3d783ac.jpg",
          mid: 113362335,
          name: "宝剑嫂",
        },
        pic: "http://i0.hdslb.com/bfs/archive/11a13219cf36b963ec612c18a53f7f4539b90aad.jpg",
        pubdate: "2020-10-21 20:37:12",
        rights: {
          autoplay: 1,
          bp: 0,
          clean_mode: 0,
          download: 1,
          elec: 0,
          hd5: 0,
          is_cooperation: 0,
          is_stein_gate: 0,
          movie: 0,
          no_background: 0,
          no_reprint: 1,
          pay: 0,
          ugc_pay: 0,
          ugc_pay_preview: 0,
        },
        stat: {
          aid: 970051991,
          argue_msg: "",
          coin: 3973,
          danmaku: 3194,
          dislike: 0,
          evaluation: "",
          favorite: 1662,
          his_rank: 0,
          like: 22661,
          now_rank: 0,
          reply: 969,
          share: 324,
          view: 247514,
        },
        state: 0,
        subtitle: { allow_submit: false, list: [] },
        allow_submit: false,
        list: [],
        tid: 21,
        title: "我去工厂啦！【膜法世家x宝剑嫂】",
        tname: "日常",
        user_garb: { url_image_ani_cut: "" },
        url_image_ani_cut: "",
        videos: 1,
      }, {
        aid: 97775739,
        bvid: "BV1hE411N7Q1",
        cid: 166785041,
        copyright: 1,
        ctime: 1584685283,
        desc: "微博@宝剑嫂↵雅诗兰黛白金养肤气垫！瑕疵皮！无滤镜巨高清测评！这次换了一个相机不高清你打我哈！↵整个妆容想营造一种氛围感，阳光，暖洋洋，妩媚，娇俏，女人味120分！↵希望大家喜欢这个视频！！",
        dimension: { width: 1920, height: 1080, rotate: 0 },
        duration: 563,
        dynamic: "进来，好看，真的！",
        mission_id: 12989,
        no_cache: false,
        owner: {
          face: "http://i0.hdslb.com/bfs/face/93f3d5d1085357565a4c2e4ac151104ac3d783ac.jpg",
          mid: 113362335,
          name: "宝剑嫂",
        },
        pic: "http://i0.hdslb.com/bfs/archive/f16d2035f92a138af3efdfed2d9854fee2a19edf.jpg",
        pubdate: "2020-03-20 19:00:20",
        rights: {
          autoplay: 1,
          bp: 0,
          clean_mode: 0,
          download: 1,
          elec: 0,
          hd5: 1,
          is_cooperation: 0,
          is_stein_gate: 0,
          movie: 0,
          no_background: 0,
          no_reprint: 1,
          pay: 0,
          ugc_pay: 0,
          ugc_pay_preview: 0,
        },
        stat: {
          aid: 97775739,
          argue_msg: "",
          coin: 12047,
          danmaku: 14173,
          dislike: 0,
          evaluation: "",
          favorite: 5559,
          his_rank: 0,
          like: 40088,
          now_rank: 0,
          reply: 3132,
          share: 1211,
          view: 387798,
        },
        state: 0,
        subtitle: { allow_submit: true, list: [] },
        allow_submit: true,
        list: [],
        tid: 157,
        title: "八分钟教你变成娇俏小女人！",
        tname: "美妆",
        user_garb: { url_image_ani_cut: "" },
        videos: 1,
      },],
      options: {
        title: {
          text: '近期视频数据走势'
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
          data: ['播放量', '点赞', '收藏'],
        },
        xAxis: [{
          show: true,
          type: 'category',
          data: ['八分钟教你变成娇俏小女人！', "微胖女生的夏天是什么样？玻璃唇哑光肌甜辣妆！", '月销30W+的爆款面膜！实话实说膜法世家全线测评！', "我去工厂啦！【膜法世家x宝剑嫂】", '唐 代 女 子 风 情 万 种',],
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
          name: '数据',
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
          name: '数据',
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
        ],
        series: [
          {
            name: "播放量",
            type: "line",
            color: '#0000ff',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            data: [338000, 310000, 383000, 248000, 661000],
          },
          {
            name: '点赞',
            type: "line",
            color: '#6495ed',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            yAxisIndex: 1,
            data: [40000, 29000, 32000, 23000, 59000],
          },
          {
            name: "收藏",
            type: "line",
            color: '#d14a61',
            smooth: 0,
            lineStyle: {
              width: 3
            },
            yAxisIndex: 1,
            data: [5559, 2343, 4159, 3973, 6216],
          },
        ]
      },
    }
  },
  methods: {
    get_url (item) {
      let bv = item['bvid']
      return item['redirect_url'] == undefined ? "https://www.bilibili.com/video/" + bv : item["redirect_url"]
    },
  }
}
</script>

<style scoped>
.content {
  display: flex;
}
.up {
  flex: 1;
}
.detail {
  flex: 3;
}
.desc {
  color: grey;
  margin: 10px 30px;
}
.face {
  display: flex;
  font-size: 1.5em;
  justify-content: center;
  margin: 20px;
}
.face_img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
.name {
  margin: auto 10px;
}
.de {
  display: flex;
}
.fans {
  flex: 1;
}
.rank {
  display: flex;
  margin: 20px 45px;
}
.rank img {
  width: 300px;
  height: 260px;
  border-radius: 5%;
}
.life {
  flex: 1;
}
.img2 {
  margin-left: 40px;
}
.img1 {
  width: 1300px;
}
.choose {
  display: flex;
  background: white;
  width: 1330px;
  margin: 10px 0px;
  padding: 0px 5px;
}
.title {
  margin: 10px;
}
.fanstu {
  background: white;
  padding: 5px;
}
.jinqi img {
  width: 300px;
  height: 200px;
}
.slot-items img {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  vertical-align: middle;
}
.slot-img img {
  width: 400px;
  height: 280px;
  border-radius: 1rem;
}
.num {
  color: green;
}
.red {
  color: red;
}
.title3 {
  font-weight: 500;
  font-size: 1.4em;
  margin: 10px;
}
.title4 {
  margin-bottom: 50px;
  margin-left: 50px;
}
.data2 {
  margin-left: 250px;
  margin-top: 30px;
}
.daili {
  display: flex;
}
.dailiItem {
  flex: 1;
}
</style>
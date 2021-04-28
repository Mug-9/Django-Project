<template>
  <div class="main">
    <div class="content">
      <div class="frame">
        <div class="type">
          <el-button class="button_type" type="primary">全部</el-button>
          <el-button class="button_type">动物圈</el-button>
          <el-button class="button_type">美食</el-button>
          <el-button class="button_type">国创</el-button>
          <el-button class="button_type">番剧</el-button>
          <el-button class="button_type">动画</el-button>
          <el-button class="button_type">数码</el-button>
          <el-button class="button_type">游戏</el-button>
          <el-button class="button_type">知识</el-button>
          <el-button class="button_type">生活</el-button>
          <el-button class="button_type">时尚</el-button>
          <el-button class="button_type">鬼畜</el-button>
          <el-button class="button_type">音乐</el-button>
          <el-button class="button_type">舞蹈</el-button>
          <el-button class="button_type">娱乐</el-button>
          <el-button class="button_type">记录片</el-button>
          <el-button class="button_type">资讯</el-button>
        </div>
      </div>
      <div class="rank" v-for="item in items" :key="item">
        <online-item isShowComment="true" class="item">
          <template v-slot:slot-img>
            <a :href="get_url(item)"><img :src="item['pic']" alt="" /></a>
          </template>
          <template v-slot:item-title>
            <p>{{ item["title"] }}</p>
          </template>
          <template v-slot:item-bv>
            <el-link type="primary" :href="get_url(item)" :underline="false">
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
          <template v-slot:item-coin>:{{ item["stat"]["coin"] }} </template>
          <template v-slot:item-like>:{{ item["stat"]["like"] }} </template>
          <template v-slot:item-danmu>:{{ item["stat"]["danmaku"] }} </template>
          <template v-slot:item-favorite>
            :{{ item["stat"]["favorite"] }}
          </template>
          <template v-slot:item-reply>:{{ item["stat"]["reply"] }} </template>
          <template v-slot:item-share>:{{ item["stat"]["share"] }} </template>
          <template v-slot:item-view>:{{ item["stat"]["view"] }} </template>
          <template v-slot:item-tname> {{ item["tname"] }} </template>
          <template v-slot:pubupdate>:{{ item["pubdate"] }} </template>
          <template v-slot:duration>{{ item["duration"] }}</template>
        </online-item>
        <div class="fen">
          <p>热点评分</p>
          <p class="fenshu">{{ item["fen"] }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import onlineItem from 'commons/online-list/online-item.vue'
export default {
  name: "SecHot",
  components: { onlineItem },
  data () {
    return {
      items: [{
        fen: 1434653,
        aid: 417544167,
        bvid: "BV1nV411H7ds",
        cid: 323853971,
        comment: { web_like: 0, web_reply: 0, replys: [], comment_id: "BV1nV411H7ds", is_like: 0, word: "comment" },
        comment_id: "BV1nV411H7ds",
        is_like: 0,
        replys: [],
        web_like: 0,
        web_reply: 0,
        word: "comment",
        copyright: 1,
        ctime: "2021-04-14 16:00:11",
        desc: "这次我们来到了全球知名度最高的酒店博览会，本来我们的目的是来长长见识，结果居然了解到了和我们生活最息息相关的秘辛！",
        dimension: { width: 1920, height: 1080, rotate: 0 },
        height: 1080,
        rotate: 0,
        width: 1920,
        duration: "0:8:42",
        dynamic: "王师傅白嫖参加展会，居然突然的正义执行？揭露外卖的秘辛！",
        echarts_data: {
          coin: [0, 2726],
          coin_d: [0, 2726],
          danmaku: [0, 800],
          danmaku_d: [0, 800],
          dateTime: ["2021-04-14 16:00:09", "2021-04-14 17:11:19"],
          favorite: [0, 832],
          favorite_d: [0, 2726],
          like: [0, 6522],
          like_d: [0, 6522],
          reply: [0, 383],
          reply_d: [0, 383],
          share: [0, 167],
          share_d: [0, 167],
          view: [0, "6.21万"],
          view_d: [0, "6.21万"],
        },
        mission_id: 16490,
        online_count: 3532,
        owner: {
          face: "http://i1.hdslb.com/bfs/face/b89330ff519e87ad61f8e78e7af7bc4cdc9ca181.jpg",
          mid: 452606628,
          name: "王师傅和小毛毛",
        },
        pic: "http://i1.hdslb.com/bfs/archive/f0207c9c76d0af3213e7bd30e9824cefc89c1c2c.jpg",
        pubdate: "2021-04-14 16:00:09",
        rights: {
          autoplay: 1,
          bp: 0,
          download: 0,
          elec: 0,
          hd5: 1,
          is_cooperation: 0,
          movie: 0,
          no_background: 0,
          no_reprint: 1,
          pay: 0,
          ugc_pay: 0,
          ugc_pay_preview: 0,
        },
        short_link: "https://b23.tv/BV1nV411H7ds",
        stat: {
          aid: 417544167,
          coin: 2726,
          danmaku: 800,
          dislike: 0,
          favorite: 832,
          his_rank: 0,
          like: 6522,
          now_rank: 0,
          reply: 383,
          share: 167,
          view: "6.21万",
        },
        state: 0,
        tid: 212,
        title: "你的外卖成本只要四元？料理包外卖内幕揭秘！",
        tname: "美食侦探",
        videos: 1
      }, {
        fen: 124653,
        aid: 417593765,
        bvid: "BV1xV411H7HY",
        cid: 323995082,
        dimension: { width: 1920, height: 1080, rotate: 0 },
        height: 1080,
        rotate: 0,
        width: 1920,
        duration: "0:18:39",
        dynamic: "",
        online_count: 6273,
        owner: {
          face: "http://i2.hdslb.com/bfs/face/f8f0fc4114bb06a87481abe12faa006a383cbe6d.jpg",
          mid: 346563107,
          name: "波士顿圆脸",
        },
        pic: "http://i0.hdslb.com/bfs/archive/b08a17b6d66d8ecdd7313aa600a36b646aa212ed.jpg",
        pubdate: "2021-04-14 13:35:33",
        rights: {
          autoplay: 1,
          bp: 0,
          download: 0,
          elec: 0,
          hd5: 0,
          is_cooperation: 0,
          movie: 0,
          no_background: 0,
          no_reprint: 1,
          pay: 0,
          ugc_pay: 0,
          ugc_pay_preview: 0,
        },
        short_link: "https://b23.tv/BV1xV411H7HY",
        stat: {
          aid: 417593765,
          coin: 6725,
          danmaku: 4557,
          dislike: 0,
          favorite: 2750,
          his_rank: 0,
          like: "2.91万",
          now_rank: 0,
          reply: 2390,
          share: 1026,
          view: "24.37万",
        },
        state: 0,
        tid: 203,
        title: "福岛核废水决定排海，FDA：农产品,先禁为敬",
        tname: "热点",
        videos: 1,
      }, {
        fen: 34653,
        aid: 587608318,
        bvid: "BV1GB4y1A7kA",
        cid: 322892889,
        comment: { web_like: 0, web_reply: 0, replys: [], comment_id: "BV1GB4y1A7kA", is_like: 0, word: "comment" },
        copyright: 1,
        ctime: "2021-04-11 21:17:52",
        desc: "魔法才能打败魔法。",
        dimension: { width: 1920, height: 1080, rotate: 0 },
        duration: "0:15:11",
        dynamic: "俄国的氢弹方案，目前看起来比福岛倒废水方案靠谱的多。↵刚好双方都有丰富的经验。",
        mission_id: 16881,
        online_count: 3395,
        owner: {
          face: "http://i1.hdslb.com/bfs/face/aaf33dced1941af0946f37c62f4b48fcaba9c9a2.jpg",
          mid: 37663924,
          name: "硬核的半佛仙人",
        },
        pic: "http://i2.hdslb.com/bfs/archive/15d78eab11967a72ab80630219b6ce81e7c45b3b.jpg",
        pubdate: "2021-04-11 21:17:52",
        rights: {
          autoplay: 1,
          bp: 0,
          download: 0,
          elec: 0,
          hd5: 1,
          is_cooperation: 0,
          movie: 0,
          no_background: 0,
          no_reprint: 1,
          pay: 0,
          ugc_pay: 0,
          ugc_pay_preview: 0,
        },
        short_link: "https://b23.tv/BV1GB4y1A7kA",
        stat: {
          aid: 587608318,
          coin: "6.40万",
          danmaku: "1.57万",
          dislike: 0,
          favorite: "3.4万",
          his_rank: 5,
          like: "19.25万",
          now_rank: 0,
          reply: "1.41万",
          share: "3.21万",
          view: "249.38万",
        },
        state: 0,
        tid: 124,
        title: "【半佛】氢弹可以解决核电站废水问题？",
        tname: "社科人文",
        videos: 1,
      }
      ]
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
.frame {
  background: white;
  width: 95%;
  margin: 10px auto;
}
.button_type {
  margin: 5px;
}
.slot-img img {
  width: 400px;
  height: 280px;
  border-radius: 1rem;
}
.slot-items img {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  vertical-align: middle;
}
.rank {
  display: flex;
}
.item {
  flex: 1;
}
.fen {
  margin: 20px;
  width: 100px;
  font-size: 1.2em;
}
.fenshu {
  margin-top: 80px;
  color: red;
}
</style>
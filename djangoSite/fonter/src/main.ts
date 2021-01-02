import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementPlus from "element-plus";
import "element-plus/lib/theme-chalk/index.css";

let Echarts: any = require("echarts");
import cookies from "vue-cookies";

const app = createApp(App);

app.provide("Echarts", Echarts);
app.provide("Cookies", cookies);
app
  .use(store)
  .use(router)
  .use(ElementPlus)
  .mount("#app");

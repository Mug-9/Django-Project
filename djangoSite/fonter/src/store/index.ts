import { createStore } from "vuex";
import * as func from "@/store/mutations-type";
import { locale } from "element-plus";

export default createStore({
  state: {
    email: "",
    password: "",
    cookies: "",
    account: "",
    token: "",
  },
  mutations: {
    [func.SETEMAIL](state, config) {
      state.email = config;
    },
    [func.SETPASSWORD](state, config) {
      state.password = config;
    },
    [func.SETACCOUNT](state, config) {
      state.account = config;
    },
    [func.SETTOKEN](state, config) {
      state.token = config;
      localStorage.token = config;
    },
    [func.GETTOKEN](state) {
      if (localStorage.getItem("expires") != null) {
        let limitDate = localStorage.getItem("expires");
        let nowDate = new Date();

        if (JSON.stringify(nowDate) > limitDate!) {
          window.localStorage.clear();
          state.token = "";
        } else if (!state.token && localStorage.getItem("token") != null) {
          state.token = localStorage.getItem("token")!;
        }
      }
      return state.token;
    },
    [func.CLEARTOKEN](state) {
      state.token = "";
    },
  },
  getters: {
    isLogin(state) {
      console.log(state.token);
      return !(state.token == "");
    },
  },
  actions: {},
  modules: {},
});

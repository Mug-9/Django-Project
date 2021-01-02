import { createStore } from "vuex";
import * as func from "@/store/mutations-type";

export default createStore({
  state: {
    isLogin: false,
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
  },
  actions: {},
  modules: {},
});

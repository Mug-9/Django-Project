import { createStore } from "vuex";
import * as func from "@/store/mutations-type";

export default createStore({
  state: {
    isLogin: true,
    email: "",
    password: "",
  },
  mutations: {
    [func.SETEMAIL](state, config) {
      state.email = config;
    },
    [func.SETPASSWORD](state, config) {
      state.password = config;
    },
  },
  actions: {},
  modules: {},
});

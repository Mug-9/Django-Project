import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const Home = () => import("views/Home/Home.vue");
const RankList = () => import("views/RankList/RankList.vue");
const Login = () => import("views/Login/Login.vue");
const Register = () => import("views/Register/Register.vue");

const routes: Array<RouteRecordRaw> = [
  {
    path: "",
    redirect: "/home",
  },
  {
    path: "/home",
    component: Home,
  },
  {
    path: "/ranklist",
    component: RankList,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/register",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

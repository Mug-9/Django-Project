import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const Home = () => import("views/Home/Home.vue");
const RankList = () => import("views/RankList/RankList.vue");
const Login = () => import("views/Login/Login.vue");
const Register = () => import("views/Register/Register.vue");
const Profile = () => import("views/Profile/Profile.vue");
const Log = () => import("views/LogPage/Profile.vue");
const Store = () => import("views/Store/Profile.vue");
const Search = () => import("views/Search/Search.vue");
const SearchV = () => import("views/SearchV/SearchV.vue");
const Detail = () => import("views/Detail/Detail.vue");
const SecHot = () => import("views/SecHot/SecHot.vue");
const HotDetail = () => import("views/HotDetail/HotDetail.vue");
const HotAnay = () => import("views/HotAnay/HotAnay.vue");

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
  {
    path: "/profile",
    component: Profile,
  },
  {
    path: "/log",
    component: Log,
  },
  {
    path: "/store",
    component: Store,
  },
  {
    path: "/search",
    component: Search,
  },
  {
    path: "/searchv",
    component: SearchV,
  },
  {
    path: "/Detail",
    component: Detail,
  },
  {
    path: "/SecHot",
    component: SecHot,
  },
  {
    path: "/HotDetail",
    component: HotDetail,
  },
  {
    path: "/HotAnay",
    component: HotAnay,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

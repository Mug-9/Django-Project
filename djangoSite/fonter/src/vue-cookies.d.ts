import Vue from 'vue'
import VueCookies from 'vue-cookies'

declare module 'vue/types/vue' {
  interface Vue{
    $cookies: VueCookies
  }
}
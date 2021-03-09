import { request } from './request'

export function formLogin (config) {
  return request({
    method: 'post',
    url: 'login',
    data: config,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function getToken () {
  return request({
    method: 'get',
    url: 'login',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function getStore (config) {
  return request({
    method: 'get',
    url: 'GetInfo',
    params: config,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function updateStore (config) {
  return request({
    method: 'get',
    url: 'UpdateInfo',
    params: config,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

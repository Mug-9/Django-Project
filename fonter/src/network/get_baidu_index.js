import { request } from './request'

export function GetBaiduIndex (data) {

  return request({
    method: 'get',
    url: 'GetBaiduIndex',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function GetCrowd (data) {

  return request({
    method: 'get',
    url: 'GetCrowd',
    params: {
      token: data,
    },
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function GetInterest (data) {

  return request({
    method: 'get',
    url: 'GetInterest',
    params: {
      token: data,
    },
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}


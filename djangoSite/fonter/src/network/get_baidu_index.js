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
export function GetBaiduIndexLive (data) {
  
  return request({
    method: 'get',
    url: 'GetBaiduIndex',
    params: {
      type: 'live',
      token: data,
    },
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}


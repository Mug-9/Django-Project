import { request } from './request'

export function GetCrowdAge (data) {
  
  return request({
    method: 'get',
    url: 'GetCrowd',
    params: {
      type: 'age',
      token: data,
    },
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}



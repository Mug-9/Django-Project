import { request } from './request'

export function GetCrowd (data) {
  
  return request({
    method: 'get',
    url: 'GetCrowd',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

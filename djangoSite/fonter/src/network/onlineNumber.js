import { request } from './request'

export function getOnlineNumbers (data) {
  
  return request({
    method: 'get',
    url: 'online_number',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

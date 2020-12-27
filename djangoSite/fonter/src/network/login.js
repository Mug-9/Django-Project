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

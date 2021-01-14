import { request } from './request'

export function formRegister (config) {
  return request({
    method: 'post',
    url: 'register',
    data: config,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

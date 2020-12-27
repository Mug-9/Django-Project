import { request } from './request'

export function getBooks () {
  return request({
    url: 'books'
  })
}

export function postLogin (config) {
  return request({
    method: 'post',
    url: 'books',
    data: config,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

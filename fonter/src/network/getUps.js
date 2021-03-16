import { request} from './request'

export function getUpRank(config) {
  return request({
    method: 'get',
    url: 'GetUpInfo',
    params: config,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function getFansIncreRank() {
  return request({
    method: 'get',
    url: 'GetFansIncre',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function getVideoIncreRank() {
  return request({
    method: 'get',
    url: 'GetVideoIncre',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}


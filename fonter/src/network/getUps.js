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

import { request} from './request'

export function OnlineList() {
  return request({
    method: 'get',
    url: 'OnlineList',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function HotList(data) {
  return request({
    method: 'get',
    url: 'HotList',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}
import { request } from './request'

export function OnlineList (data) {
  return request({
    method: 'get',
    url: 'OnlineList',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function HotList (data) {
  return request({
    method: 'get',
    url: 'HotList',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function PostComment (data) {
  return request({
    method: 'post',
    url: 'UpdateInfo',
    data: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function OperatorLog (data) {
  return request({
    method: 'get',
    url: 'OperatorLog',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function FavoriteList (data) {
  return request({
    method: 'get',
    url: 'GetFavorite',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function Search (data) {
  return request({
    method: 'get',
    url: 'Search',
    params: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

export function rSearch (data) {
  return request({
    method: 'post',
    url: 'Search',
    data: data,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

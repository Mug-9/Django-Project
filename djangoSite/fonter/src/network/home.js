import { request } from './request'

export function getBooks () {
  return request({
    url: 'api/books'
  })
}

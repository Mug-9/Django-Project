import axios from 'axios'
import qs from 'qs'


export function request (config) {
  const instance = axios.create({
    // baseURL: 'http://localhost:8888/api/',
    baseURL: 'http://123.56.252.111:8888/api/',
    timeout: 10000,
  })

  instance.interceptors.request.use(config => {
    if (config.method == "POST") {
      config.data = qs.stringify(config.data)
    }
    if (!(/^(get|head|options|trace)$/.test(config['method']))) {
      config['xsrfCookieName'] = 'csrftoken'
      config['xsrfHeaderName'] = 'X-CSRFTOKEN'
    }
    return config
  }, err => {
    console.log(err)
  })

  instance.interceptors.response.use(res => {
    return res.data

  }, err => {
    console.log(err)
  })

  return instance(config)
}

export function requestAll (config) {
  return axios.all(config)
}

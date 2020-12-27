import axios from 'axios'
import qs from 'qs'

export function request (config) {
  const instance = axios.create({
    baseURL: 'http://192.168.0.105:8888/api/',
    timeout: 5000,
  })

  instance.interceptors.request.use(config => {
    if (config.method == "POST") {
      config.data = qs.stringify(config.data)
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


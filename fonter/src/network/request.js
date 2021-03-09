import axios from 'axios'
import qs from 'qs'


export function request (config) {
  const instance = axios.create({
    baseURL: process.env.VUE_APP_API_URL,
    timeout: 15000,
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
    return err
  })

  instance.interceptors.response.use(res => {
    return res.data
  })

  // , err => {
  //   let data = {
  //     'message': 'error',
  //     'error': err
  //   }
  //   return data
  // }

  return instance(config)
}

export function requestAll (config) {
  return axios.all(config)
}

import axios from 'axios'

function useAxios() {
	const instance = axios.create({
		baseURL: 'http://127.0.0.1:8000/',
		timeout: 5000,
	})

	instance.interceptors.request.use(
		(config) => {
			const token = localStorage.getItem('user.token')
			if (token) {
				config.headers['token'] = 'Token ' + token
			}
			return config
		},
		(error) => {
			return Promise.reject(error)
		}
	)

	instance.interceptors.response.use(
		(response) => {
			return response.data
		},
		(error) => {
			if (error.response.status == 400) {
				// console.log('data :>> ', error.response.data)
				return error.response.data
			}
			return Promise.reject(error)
		}
	)

	return instance
}

export default useAxios

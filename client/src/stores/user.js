import { defineStore } from 'pinia'

export const useUserStore = defineStore({
	id: 'user',

	state: () => ({
		user: {
			isAuthenticated: false,
			id: null,
			name: null,
			email: null,
			token: null,
		},
	}),

	actions: {
		initStore() {
			console.log('initStore')
			const token = localStorage.getItem('user.token')
			if (token) {
				this.user.token = localStorage.getItem('user.token')
				this.user.email = localStorage.getItem('user.email')
				this.user.id = localStorage.getItem('user.id')
				this.user.name = localStorage.getItem('user.name')
				this.user.isAuthenticated = true

				console.log('用户' + this.user.name + '登录成功')
			}
		},

		setToken(data) {
			console.log('setToken', data)

			this.user.token = data.token
			this.user.email = data.email
			this.user.name = data.name
			this.user.id = data.user_id
			this.user.isAuthenticated = true

			localStorage.setItem('user.token', data.token)
			localStorage.setItem('user.email', data.email)
			localStorage.setItem('user.name', data.name)
			localStorage.setItem('user.id', data.user_id)

			console.log('用户的token已设置：' + this.user.token)
		},

		removeToken(user) {
			console.log('removeToken')

			this.user.token = null
			this.user.email = null
			this.user.name = null
			this.user.id = null
			this.user.isAuthenticated = null

			localStorage.setItem('user.token', '')
			localStorage.setItem('user.email', '')
			localStorage.setItem('user.name', '')
			localStorage.setItem('user.id', '')
		},
	},
})

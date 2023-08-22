<template>
	<div class="text-center p-10 lg:p-20">
		<h1 class="text-3xl text-white lg:text-6xl">登录</h1>
	</div>

	<div class="px-4 mx-auto lg:w-1/4">
		<div class="mb-5">
			<input
				type="text"
				class="w-full mt-2 px-4 py-2 rounded-xl focus:outline-none"
				placeholder="Email"
				v-model="user.email"
			/>
		</div>

		<div class="mb-5">
			<input
				type="password"
				class="w-full mt-2 px-4 py-2 rounded-xl focus:outline-none"
				placeholder="密码"
				v-model="user.password"
			/>
		</div>

		<div class="flex gap-5">
			<button
				@click="login"
				class="px-5 py-3 rounded-xl text-white bg-teal-800 hover:bg-teal-700"
			>
				登录
			</button>

			<button
				@click="toRegister"
				class="px-5 py-3 rounded-xl text-white bg-teal-800 hover:bg-teal-700"
			>
				没有账号？去注册
			</button>
		</div>
	</div>
</template>

<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'
import useAxios from '../composables/useAxios'

const userStore = useUserStore()
const router = useRouter()
const axios = useAxios()

const user = reactive({
	email: '',
	password: '',
})

function toRegister() {
	router.push({ name: 'signup' })
}

async function login() {
	const userForm = new FormData()
	userForm.append('email', user.email)
	userForm.append('password', user.password)

	await axios.post('auth/login/', userForm).then((res) => {
		console.log('res :>> ', res)
		userStore.setToken(res.user)
		router.push({ name: 'home' })
	})
}
</script>

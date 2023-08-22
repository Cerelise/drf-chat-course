<template>
	<div class="text-center p-10 lg:p-20">
		<h1 class="text-3xl text-white lg:text-6xl">注册</h1>
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
				type="text"
				class="w-full mt-2 px-4 py-2 rounded-xl focus:outline-none"
				placeholder="用户名"
				v-model="user.username"
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

		<div class="mb-5">
			<input
				type="password"
				class="w-full mt-2 px-4 py-2 rounded-xl focus:outline-none"
				placeholder="重复密码"
				v-model="user.repassword"
			/>
		</div>

		<div ref="errMsg" class="py-2 text-sm text-white"></div>

		<div class="flex gap-5">
			<button
				@click="signup"
				class="px-5 py-3 rounded-xl text-white bg-teal-800 hover:bg-teal-700"
			>
				注册
			</button>

			<button
				@click="toLogin"
				class="px-5 py-3 rounded-xl text-white bg-teal-800 hover:bg-teal-700"
			>
				已有账号？去登录
			</button>
		</div>
	</div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import useAxios from '../composables/useAxios'

const router = useRouter()
const axios = useAxios()

const user = reactive({
	email: '',
	username: '',
	password: '',
	repassword: '',
})

const errMsg = ref(null)

async function signup() {
	if (user.repassword !== user.password) {
		errMsg.value.innerHTML = '两次密码不一致，请重新输入！'
		errMsg.value.classList.add(
			'mb-5',
			'text-center',
			'bg-red-500',
			'rounded-lg'
		)
		return
	} else if (
		user.email.length == 0 ||
		user.username.length == 0 ||
		user.password.length == 0 ||
		user.repassword.length == 0
	) {
		errMsg.value.innerHTML = '表单未填写完整！'
		errMsg.value.classList.add(
			'mb-5',
			'text-center',
			'bg-red-500',
			'rounded-lg'
		)
		return
	} else {
		errMsg.value.innerHTML = ''
		errMsg.value.classList.add('hidden')
	}

	const userForm = new FormData()
	userForm.append('email', user.email)
	userForm.append('username', user.username)
	userForm.append('password', user.password)

	await axios.post('auth/signup/', userForm).then((res) => {
		const error = res.errors && res.errors.length > 0 ? res.errors[0] : null
		if (error) {
			errMsg.value.innerHTML = '该邮箱已被使用！'
			errMsg.value.classList.remove('hidden')
			errMsg.value.classList.add(
				'mb-5',
				'text-center',
				'bg-red-500',
				'rounded-lg'
			)
			return
		} else {
			router.push({ name: 'login' })
		}
	})
}

function toLogin() {
	router.push({ name: 'login' })
}
</script>

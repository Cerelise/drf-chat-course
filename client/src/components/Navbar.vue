<template>
	<nav class="flex items-center justify-between px-4 py-6 bg-teal-800">
		<div>
			<router-link to="/" class="text-xl text-white">Django-Chat</router-link>
		</div>

		<div
			v-if="!userStore.user.isAuthenticated"
			class="flex items-center space-x-4"
		>
			<router-link to="/login" class="text-white hover:text-gray-200"
				>登录</router-link
			>
			<router-link
				to="/signup"
				class="px-5 py-3 rounded-xl text-white bg-teal-600 hover:bg-teal-700"
				>注册</router-link
			>
		</div>

		<div v-else class="flex items-center space-x-4">
			<router-link to="/rooms" class="text-white hover:text-gray-200"
				>房间</router-link
			>
			<button
				@click="logout"
				class="px-5 py-3 rounded-xl text-white bg-teal-600 hover:bg-teal-700"
			>
				登出
			</button>
		</div>
	</nav>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'

const router = useRouter()
const userStore = useUserStore()

function logout() {
	userStore.removeToken()
	router.push({ name: 'home' })
}
</script>

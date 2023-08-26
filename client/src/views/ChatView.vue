<template>
	<main>
		<div class="p-10 text-center lg:p-20">
			<h1 class="text-3xl text-white lg:text-6xl">{{ roomStore.room.name }}</h1>
		</div>

		<div class="mx-4 p-4 bg-white rounded-xl lg:w-2/4 lg:mx-auto">
			<div
				class="chat-messages space-y-3 mb-3"
				id="chat-messages"
				ref="chatContainer"
			>
				<div v-for="msg in msgList" class="p-4 bg-gray-200 rounded-xl">
					<p class="font-semibold">{{ msg.username }}</p>
					<p>{{ msg.content }}</p>
				</div>
			</div>
		</div>

		<div class="mt-6 mx-4 p-4 bg-white rounded-xl lg:w-2/4 lg:mx-auto">
			<div class="flex">
				<input
					type="text"
					class="flex-1 mr-3 focus:outline-none"
					placeholder="请发送消息..."
					v-model="chatMsg"
				/>
				<button
					@click="sendMessage()"
					class="px-5 py-3 rounded-xl text-white bg-teal-600 hover:bg-teal-700"
				>
					发送
				</button>
			</div>
		</div>
	</main>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useUserStore } from '../stores/user'
import { useRoomStore } from '../stores/room'
import { onMounted, ref, nextTick } from 'vue'
import useAxios from '../composables/useAxios'

const userStore = useUserStore()
const roomStore = useRoomStore()
const route = useRoute()
const axios = useAxios()

const chatSocket = ref('')
const chatMsg = ref('')
const msgList = ref([])

const chatContainer = ref(null)

const room_slug = route.params.room_slug
roomStore.initStore(room_slug)

function initChatSocket() {
	chatSocket.value = new WebSocket('ws://127.0.0.1:8000/ws/' + room_slug + '/')

	chatSocket.value.onmessage = function (e) {
		console.log('onmessage')
		const msg = JSON.parse(e.data)
		if (msg.content) {
			msgList.value.push(msg)
			scrollToButtom()
		} else {
			alert('消息为空！')
			return
		}
	}

	chatSocket.value.onclose = function (e) {
		console.log('onclose')
	}
}

function sendMessage() {
	let msg = JSON.stringify({
		content: chatMsg.value,
		username: userStore.user.name,
		room: roomStore.room.slug,
	})
	chatSocket.value.send(msg)

	chatMsg.value = ''
}

function scrollToButtom() {
	nextTick(() => {
		if (chatContainer.value) {
			chatContainer.value.scrollTop = chatContainer.value.scrollHeight
		}
	})
}

onMounted(async () => {
	// 获取当前聊天室详情
	await axios.get(`/chat/${route.params.room_slug}/`).then((response) => {
		msgList.value = response.message_list
	})
	scrollToButtom()
	initChatSocket()
})
</script>

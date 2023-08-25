<template>
	<main>
		<div class="p-10 text-center lg:p-20">
			<h1 class="text-3xl text-white lg:text-6xl">{{ room_slug }}</h1>
		</div>

		<div class="mx-4 p-4 bg-white rounded-xl lg:w-2/4 lg:mx-auto">
			<div class="chat-messages space-y-3 mb-3">
				<div class="p-4 bg-gray-200 rounded-xl">
					<p class="font-semibold">sanapri</p>
					<p>hello</p>
				</div>
			</div>
			<div class="chat-messages space-y-3 mb-3">
				<div class="p-4 bg-gray-200 rounded-xl">
					<p class="font-semibold">cerelise</p>
					<p>hi</p>
				</div>
			</div>
		</div>

		<div class="mt-6 mx-4 p-4 bg-white rounded-xl lg:w-2/4 lg:mx-auto">
			<div class="flex">
				<input
					type="text"
					class="flex-1 mr-3 focus:outline-none"
					placeholder="请发送消息..."
				/>
				<button
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
import { onMounted, ref } from 'vue'

const route = useRoute()

const chatSocket = ref('')

const room_slug = route.params.room_slug

function initChatSocket() {
	chatSocket.value = new WebSocket('ws://127.0.0.1:8000/ws/' + room_slug + '/')

	chatSocket.value.onmessage = function (e) {
		console.log('onmessage')
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

onMounted(async () => {
	initChatSocket()
})
</script>

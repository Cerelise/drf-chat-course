<template>
	<main>
		<div class="p-10 text-center lg:p-20">
			<h1 class="text-3xl text-white lg:text-6xl">Rooms</h1>
		</div>

		<div class="w-full flex flex-wrap items-center">
			<div v-for="room in rooms" class="w-full p-3 lg:w-1/4">
				<div class="p-4 bg-white shadow rounded-xl text-center">
					<h2 class="mb-5 text-2xl font-semibold">{{ room.name }}</h2>
					<router-link
						:to="'chat' + room.get_absolute_url"
						class="px-5 py-3 block rounded-xl text-white bg-teal-600 hover:bg-teal-700"
						>加入房间</router-link
					>
				</div>
			</div>
		</div>
	</main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import useAxios from '../composables/useAxios'

const axios = useAxios()

const rooms = ref([])

function getRoomList() {
	axios.get('chat/').then((res) => {
		console.log(res)
		rooms.value = res.rooms
	})
}

onMounted(() => {
	getRoomList()
})
</script>

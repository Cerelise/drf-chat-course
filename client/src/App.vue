<script setup>
import Navbar from './components/Navbar.vue'
import { useUserStore } from './stores/user'

const userStore = useUserStore()

userStore.initStore()
</script>

<template>
	<Navbar />
	<RouterView />
</template>

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import RoomsView from '../views/RoomsView.vue'
import ChatView from '../views/ChatView.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: HomeView,
		},
		{
			path: '/login',
			name: 'login',
			component: LoginView,
		},
		{
			path: '/signup',
			name: 'signup',
			component: SignUpView,
		},
		{
			path: '/chat/:room_slug',
			name: 'chat',
			component: ChatView,
		},
		{
			path: '/rooms',
			name: 'rooms',
			component: RoomsView,
		},
	],
})

export default router

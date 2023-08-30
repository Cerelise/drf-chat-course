import { defineStore } from "pinia";
import useAxios from "../composables/useAxios";

const axios = useAxios();

export const useRoomStore = defineStore({
	id: "room",

	state: () => ({
		room: {
			name: null,
			slug: null,
			message_list: [],
		},
	}),

	actions: {
		async initStore(room_slug) {
			console.log("initStore");
			const token = localStorage.getItem("user.token");
			if (token) {
				await axios.get(`/chat/${room_slug}/`).then((response) => {
					console.log("response :>> ", response);
					this.room.name = response.room.name;
					this.room.slug = response.room.slug;
					this.room.message_list = response.message_list;
					console.log(this.room.message_list);
				});
			}
		},
	},
});

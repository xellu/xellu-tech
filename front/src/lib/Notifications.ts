import { writable } from "svelte/store";
import { type Writable } from "svelte/store";
import { playSound } from "./SoundManager";

export let notifyQueue: Writable<Notification[]> = writable([]);
let notifications: Notification[] = [];

notifyQueue.subscribe(value => {
    notifications = value;
})

export type Notification = {
    message: string,
    type: "info" | "success" | "warning" | "error",
    id: string
}

export function notify(message: string, type: "info" | "success" | "warning" | "error" = "info", expire: number = 5000) {
    const id = Math.random().toString(36).substring(7);
    notifications.push({ message, type, id });
    notifyQueue.set(notifications);

    playSound(["warning", "error"].includes(type) ? '/ping-error.mp3' : "/ping.mp3", 0.2)
    
    setTimeout(() => {
        notifications = notifications.filter(n => n.id !== id);
        notifyQueue.set(notifications);
    }, expire);
}
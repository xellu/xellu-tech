import { writable } from "svelte/store";
import { playSound } from "./sounds";

export let notifications: any = writable([]);
export let pingState: any = writable(false);

let ping = false
pingState.subscribe((value: any) => {
    ping = value;
});

export type Notification = {
    id: string,
    message: string,
    type: 'primary' | 'warning' | 'error' | 'success',
    expire: number
}

export function notify(message: string, type: 'primary' | 'warning' | 'error' | 'success' = 'primary', timeout: number = 5000) {
    let id = Math.random().toString(36).substring(7);

    notifications.update((n:any) => [...n, {id, message, type, expire: Date.now() + timeout }]);
    
    if (ping) {
        playSound("ping.mp3", 0.2);
    }

}
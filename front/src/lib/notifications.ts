import { writable } from "svelte/store";

export let notifications: any = writable([]);

export type Notification = {
    id: string,
    message: string,
    type: 'primary' | 'warning' | 'error' | 'success',
    timeout: number
}

export function notify(message: string, type: 'primary' | 'warning' | 'error' | 'success' = 'primary', timeout: number = 5000) {
    let id = Math.random().toString(36).substring(7);

    notifications.update((n:any) => [...n, {id, message, type, timeout }]);
}
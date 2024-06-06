import { type Writable } from "svelte/store";
import { writable } from "svelte/store";

export let emailInbox: Writable<Email[]> = writable([]);
let inbox: Email[] = [];

emailInbox.subscribe(value => {
    inbox = value;
})

export type Email = {
    subjet: string,
    content: string,
    author: Contact,
    read: boolean
}

export type Contact = {
    name: string,
    online: boolean
}

export const contacts: Contact[] = [
    {
        name: "Xel Lu",
        online: true
    },
    {
        name: "Rachel Johnson",
        online: true
    },
    {
        name: "James Roberts",
        online: true
    },
    {
        name: "Dan C. Smith",
        online: true
    }
]

export function sendEmail(email: Email) {
    inbox.push(email);
    emailInbox.set(inbox);
}

export function markAsRead(email: Email) {
    let index = inbox.findIndex(e => e == email);
    if (index == -1) { return }

    inbox[index].read = true;
    emailInbox.set(inbox);
}

export function deleteEmail(email: Email) {
    let index = inbox.findIndex(e => e == email);
    if (index == -1) { return }

    inbox.splice(index, 1);
    emailInbox.set(inbox);
}
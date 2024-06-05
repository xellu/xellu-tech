import { notify } from "./notifications"

export const contacts = [
    {
        name: "Xel Lu",
        online: true,
        send: () => {
            notify("Out of order", "warning", 10000)
        }
    },
    {
        name: "James Roberts",
        online: false,
        send: () => {
            notify("Unable to send: No Network Connectionr", "warning", 10000)
        }
    },
    {
        name: "Rachel Johnson",
        online: false,
        send: () => {
            notify("Unable to send: No Network Connection", "warning", 10000)
        }
    },
    {
        name: "Dan C.",
        online: true,
        send: () => {
            notify("Unable to send: No Network Connection", "error", 10000)
        }
    }
]
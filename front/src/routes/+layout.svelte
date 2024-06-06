<script lang="ts">
    import "../app.pcss";

    import { type Notification } from "$lib/Notifications";
    import { notifyQueue } from "$lib/Notifications";
    import { scale, slide } from "svelte/transition";

    let notifications: Notification[] = [];

    notifyQueue.subscribe(value => {
        notifications = value;
    });
    
    const notifyStates = {
        "success": {
            style1: "bg-success-500/10 text-success-500",
            style2: "bg-success-500/5 border-success-500/30",
            title: "Success"
        },
        "warning": {
            style1: "bg-warning-500/10 text-warning-500",
            style2: "bg-warning-500/5 border-warning-500/30",
            title: "Attention"
        },
        "error": {
            style1: "bg-error-500/10 text-error-500",
            style2: "bg-error-500/5 border-error-500/30",
            title: "System Failure"
        },
        "info": {
            style1: "bg-secondary-900/10 text-secondary-500",
            style2: "bg-secondary-900/5 border-secondary-500/30",
            title: "Notice"
        }
    }

</script>

<div class="fixed bottom-16 right-0 p-5">
    {#each notifications as n}
        <div class="{notifyStates[n.type].style2 || notifyStates.info.style2} border shadow-lg mb-2 w-56" transition:slide>
            <div class="flex items-center justify-between p-1 px-2 {notifyStates[n.type].style1 || notifyStates.info.style1}">
                <h4 class="h4">{notifyStates[n.type].title || notifyStates.info.title}</h4>
                <button class="text-xl" on:click={() => {
                    notifications = notifications.filter(notify => notify.id !== n.id);
                    notifyQueue.set(notifications);
                }}>[x]</button>
            </div>
            <p class="p-3" transition:scale>{n.message}</p>
        </div>
    {/each}
</div>

<slot />
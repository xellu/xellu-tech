<script lang="ts">
    import "../app.pcss";

    import { onMount, onDestroy } from 'svelte';
    import { notifications } from "$lib/notifications.ts";

    import { fade, slide } from 'svelte/transition';

    let notificationQueue: any = []

    let notificationDisplayed: string[] = []

    const stateMessages: any = {
        success: "Success",
        error: "Error",
        warning: "Attention",
        surface: "Notification",
    }

    const colors: any = {
        success: "0, 125, 0",
        error: "125, 0, 0",
        warning: "125, 125, 0",
        primary: "0, 50, 0",
    }

    let queueManagerInstance: any = null

    onMount(() => {
        notifications.subscribe((notifications: any) => {
            notifications.forEach((notification: any) => {
                if (!notificationDisplayed.includes(notification.id)) {
                    notificationQueue = [...notificationQueue, notification];
                    notificationDisplayed.push(notification.id)

                    console.info(`Queued notification: [${notification.type}] ${notification.id}`)
                }
            });
        })

        queueManagerInstance = setInterval(() => { queueManager() }, 100);
    })

    onDestroy(() => {
        clearInterval(queueManagerInstance)
    })

    function queueManager() {
        notificationQueue.forEach((notif: any) => {
            if (notif.expire < Date.now()) {
                removeNotification(notif.id)
            }
        })
    }

    function removeNotification(notifId: string) {
        notificationQueue = notificationQueue.filter((n: any) => n.id != notifId)
    }

</script>

<div class="fixed bottom-16 right-0 flex flex-col m-5" style="z-index: 999999999999999999999;" transition:fade>  
{#each notificationQueue as notif}
    <div class="w-64 backdrop-blur-sm mt-3 crt" transition:slide style="border: 1px solid rgb({colors[notif.type] || colors['primary']});">
        <div class="px-2 flex items-center justify-between select-none"
          style="background-color: rgba({colors[notif.type] || colors['primary']}, .8);">
        
            <h1 class="text-lg font-black text-surface-100">{stateMessages[notif.type] || 'Notification'}</h1>
            <button class="text-2xl" on:click={() => {
                removeNotification(notif.id)
            }}>x</button>
        </div>
        <div class="p-2 px-3" style="background-color: rgba({colors[notif.type] || colors['primary']}, .5);">
        
            <p>{notif.message}</p>
        </div>
    </div>
{/each}
</div>

<slot />
<script lang="ts">
    import "../app.pcss";

    import { onMount, onDestroy } from 'svelte';
    import { notifications } from "$lib/notifications.ts";

    import { slide } from 'svelte/transition';

    let currentNotification: any = null
    let notificationQueue: any = []
    let remaining: number = 0;

    let notificationDisplayed: string[] = []
    let notificationBlock: boolean = false

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
                    notificationQueue.push(notification);
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
        if (currentNotification != null)
            remaining = Math.floor((currentNotification.expire - Date.now()) / 1000) + 1;

        notificationQueue.forEach((notification: any) => {
            if (currentNotification == null && !notificationBlock) {
                currentNotification = notification;
                currentNotification.expire = Date.now() + notification.timeout;
            }

            if (currentNotification != null && Date.now() > currentNotification.expire) {
                removeNotification(notification.id);
            }
        })
    }

    function removeNotification(notifId: string) {
        notificationQueue = notificationQueue.filter((n: any) => n.id != notifId)
        currentNotification = null;

        notificationBlock = true;
        setTimeout(() => {
            notificationBlock = false;
        }, 500)
    }

</script>

{#if currentNotification}
<div class="w-screen h-screen flex items-center justify-center z-20 fixed left-0 top-0"> 
    <div class="min-w-56 max-w-96 backdrop-blur-sm" transition:slide style="border: 1px solid rgb({colors[currentNotification.type]});">
        <div class="px-2 flex items-center justify-between"
          style="background-color: rgba({colors[currentNotification.type]}, .8);">
        
            <h1 class="text-lg font-black text-surface-100">{stateMessages[currentNotification.state] || 'Notification'} ({remaining}s)</h1>
            <button class="text-2xl" on:click={() => {
                removeNotification(currentNotification.id)
            }}>x</button>
        </div>
        <div class="p-2 px-3" style="background-color: rgba({colors[currentNotification.type]}, .5);">
        
            <p>{currentNotification.message}</p>
        </div>
    </div>
</div>
{/if}

<slot />
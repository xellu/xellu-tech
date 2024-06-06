<script lang="ts">
    import { scale, slide } from "svelte/transition";
    import { apps } from "$lib/Apps";

    import { type Window } from "$lib/WindowManager";
    import { isTop, promoteWindow, closeWindow } from "$lib/WindowManager";
    import { onDestroy, onMount } from "svelte";

    export let self: Window;

    let active: boolean = isTop(self.appId);
    let eventLoopThread: any = null;

    let randomId = Math.random().toString(36).substring(7);
    let visible = false

    onMount(() => {
        eventLoopThread = setInterval(eventLoop, 100)
    })

    onDestroy(() => {
        if (eventLoopThread) {
            clearInterval(eventLoopThread)
        }
    })

    function eventLoop() {
        active = isTop(self.appId);

        visible = self.visible;

        let win = document.getElementById(randomId);
        if (win) {
            //get window width and height
            let width = win.offsetWidth;
            let height = win.offsetHeight;

            if (self.posX < 0) {
                self.posX = 0;
            }
            
            if (self.posY < 0) {
                self.posY = 0;
            }

            if (self.posX + width > window.innerWidth) {
                self.posX = window.innerWidth - width;
            }
            if (self.posY + height > window.innerHeight - 64) {
                self.posY = window.innerHeight - height - 64;
            }
        }
    }

    let dragTemp = {
        x: 0,
        y: 0
    }

    function saveToTemp(e: DragEvent) {
        dragTemp.x = e.layerX;
        dragTemp.y = e.layerY;
    }

    function handleDrag(e: DragEvent) {
        let x = e.clientX - dragTemp.x;
        let y = e.clientY - dragTemp.y;

        self.posX = x;
        self.posY = y;
    }

</script>

{#if visible}
<div class="bg-surface-500/50 border {active ? 'border-primary-900' : 'border-primary-900/50'} {self.visible ? 'fixed' : 'hidden'} duration-300 max-w-3xl min-w-56 backdrop-blur-md text-left crt"
    id="{randomId}" style="left: {self.posX}px; top: {self.posY}px; z-index: {self.posZ};"
    on:click={() => { if (!isTop(self.appId)) { promoteWindow(self) } }} on:keydown={null} role="checkbox" tabindex="0" aria-checked
    transition:scale
>

<button class="flex justify-between items-center px-2 {active ? 'bg-primary-500/10 text-primary-500' : 'bg-primary-500/5 text-primary-300'} text-lg w-full duration-300" draggable="true"  on:dragstart={(e) => saveToTemp(e)} on:dragend={(e) => handleDrag(e)}> 
        <p class="flex-grow text-left h4">❏ {apps[self.appId].title}</p>
        <div class="flex">
            <button class="p-1 text-xl" on:click={() => { self.visible = false; visible = false }}>[-]</button>
            <button class="p-1 text-xl" on:click={() => { if (!self.meta.locked) {
                self.visible = false
                visible = false
                setTimeout(() => { closeWindow(self) }, 500)
            }}}>[x]</button>
        </div>
    </button>

    <div class="overflow-y-scroll" style="max-height: 30rem;" transition:slide>
        <slot />
    </div>
</div>
{/if}
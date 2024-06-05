<script lang="ts">
    import { onMount } from "svelte";
    import { scale, slide } from "svelte/transition";

    import { playSound } from "$lib/sounds";

    export let self: any = {
        open: false,
        posX: 0,
        posY: 0,
        posZ: 0,
        onOpen: () => {}
    }

    export let windows: any = null;
    export let name: string = "Window";
    export let tray: any = {
        volume: false
    }
    export let locked: boolean = false;

    let pageId: string = Math.random().toString(36).substring(7);

    let active: boolean = false;

    let dragtemp = {
        x: 0,
        y: 0
    }

    function handleDrag(e: MouseEvent) {
        self.posX = e.clientX - dragtemp.x;
        self.posY = e.clientY - dragtemp.y;

        promoteToTop();

        let width = document.getElementById(pageId)?.clientWidth || 0;
        let height = document.getElementById(pageId)?.clientHeight || 0;
    }

    function saveToTemp(e: DragEvent) {
        dragtemp.x = e.layerX;
        dragtemp.y = e.layerY;
    }

    function isTop() {
        return self.posZ === getHighestZ();
    }

    function getHighestZ() {
        let highestZ = 0;
        Object.keys(windows).forEach((key: string) => {
            if (windows[key].posZ > highestZ && windows[key].open) {
                highestZ = windows[key].posZ;
            }
        })

        return highestZ;
    }

    function promoteToTop() {
        self.posZ = getHighestZ() + 1;
        if (tray.volume) { playSound("window-open.mp3", 0.01) }
    }

    self.onOpen = () => {
        self.open = true;
        promoteToTop()
    }

    let activeInterval: any = null;

    onMount(() => {
        activeInterval = setInterval(() => {
            active = isTop()

            let width = document.getElementById(pageId)?.clientWidth || 0;
            let height = document.getElementById(pageId)?.clientHeight || 0;

            if (self.posX < 0) { self.posX = 0 }
            if (self.posY < 0) { self.posY = 0 }

            if (self.posX > window.innerWidth - width) { self.posX = window.innerWidth - width - 5 }
            if (self.posY > window.innerHeight - height - 64) { self.posY = window.innerHeight - height - 69 }

        }, 200)
    })
</script>

{#if self.open}
<div class="bg-surface-500/50 border {active ? 'border-primary-900' : 'border-primary-900/50'} max-w-3xl min-w-56 fixed backdrop-blur-md duration-300 text-left crt"
    id="{pageId}" style="left: {self.posX}px; top: {self.posY}px; z-index: {self.posZ};"
    on:click={() => { if (!isTop()) { promoteToTop() } }} on:keydown={null} role="checkbox" tabindex="0" aria-checked
    transition:scale>

<button class="flex justify-between items-center px-2 {active ? 'bg-primary-500/10 text-primary-500' : 'bg-primary-500/5 text-primary-300'} text-lg w-full duration-300" draggable="true"  on:dragstart={(e) => saveToTemp(e)} on:dragend={(e) => handleDrag(e)}> 
        <p class="flex-grow text-left h4">❏ {name}</p>
        <button class="p-1 text-xl" on:click={() => { if (!locked) { self.open = false }}}>X</button>
    </button>

    <div class="overflow-y-scroll" style="max-height: 30rem;" transition:slide>
        <slot />
    </div>
</div>
{/if}
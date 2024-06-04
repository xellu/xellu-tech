<script lang="ts">
    import { onMount } from "svelte";
    import { scale } from "svelte/transition";

    export let self: any = {
        open: false,
        posX: 0,
        posY: 0,
        posZ: 0,
        onOpen: () => {}
    }

    export let windows: any = null;
    export let name: string = "Window";

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

        }, 500)
    })
</script>

{#if self.open}
<div class="bg-surface-500 border {active ? 'border-primary-900' : 'border-primary-900/50'} max-w-xl w-full fixed backdrop-blur-sm" id="{pageId}" style="left: {self.posX}px; top: {self.posY}px;" transition:scale>
    <button class="flex justify-between items-center px-2 {active ? 'bg-primary-500/10' : 'bg-primary-500/5'} text-lg w-full" draggable="true" on:click={() => promoteToTop()} on:mousedown={() => promoteToTop()} on:dragstart={(e) => saveToTemp(e)} on:dragend={(e) => handleDrag(e)}> 
        <p class="text-primary-500 flex-grow text-left h4">{name}</p>
        <button class="text-primary-500 p-1 text-xl" on:click={() => self.open = false}>X</button>
    </button>

    <div class="max-h-96 overflow-y-scroll">
        <slot />
    </div>
</div>
{/if}
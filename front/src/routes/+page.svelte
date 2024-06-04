<script lang="ts">
    import { onMount } from 'svelte';
    import { fade, scale } from 'svelte/transition';

    let photosensitiveWarning: boolean = true
    let transitionDelay: boolean = false
    
</script>

{#if photosensitiveWarning}
<div class="w-screen h-screen flex items-center justify-center flex-wrap gap-10" transition:scale>
    <img src="/WarningSign.png" alt="">
    <div class="flex justify-center flex-col gap-3 p-5">
        <h1 class="h1 font-black text-warning-500 max-w-xl w-full">ATTENTION</h1>
        <p class="max-w-xl w-full text-lg">
            This page contains flashing lights that may trigger seizures in small percentage of people, even without prior history of photosensitive epilepsy.
        </p>

        <button class="btn variant-filled-warning max-w-56 text-2xl font-bold" on:click={() => {
            photosensitiveWarning = false;
            transitionDelay = true
            setTimeout(
                () => {
                    transitionDelay = false;
                }, 1000) }}>Proceed</button>
    </div>
</div>
{:else if transitionDelay}
<div class="crt"></div>
{:else}
<div class="crt crt-open-animation p-5" transition:fade>
    
</div>
{/if}
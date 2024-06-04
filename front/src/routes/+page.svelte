<script lang="ts">
    import { onMount } from 'svelte';
    import { fade, scale } from 'svelte/transition';

    let photosensitiveWarning: boolean = false
    let transitionDelay = {
        state: true,
        crt: false
    }

    onMount(() => {
        if (localStorage.getItem('photosensitiveWarning') == undefined) {
            photosensitiveWarning = true
        }
        transitionDelay.state = false
    })
    
</script>

<svelte:head>
    <title>Xel Lu</title>
</svelte:head>

{#if photosensitiveWarning}

<div class="w-screen h-screen flex items-center justify-center flex-wrap gap-10" transition:fade>
    <img src="/WarningSign.png" alt="">
    <div class="flex justify-center flex-col gap-3 p-5">
        <h1 class="h1 font-black text-warning-500 max-w-xl w-full">ATTENTION</h1>
        <p class="max-w-xl w-full text-lg">
            This page contains flashing lights that may trigger seizures in small percentage of people, even without prior history of photosensitive epilepsy.
        </p>
        <p class="text-warning-900">If you continue, we will not prompt you again</p>

        <button class="btn variant-filled-warning max-w-56 text-2xl font-bold" on:click={() => {
            photosensitiveWarning = false;
            transitionDelay.state = true
            transitionDelay.crt = true

            localStorage.setItem('photosensitiveWarning', 'set')

            setTimeout(
                () => {
                    transitionDelay.state = false;
                }, 1000) }}>Proceed</button>
    </div>
</div>

{:else if transitionDelay.state}
<div class="crt-line"></div>

<div class="{transitionDelay.crt ? 'crt' : ''}"></div>
{:else}
<div class="crt-line"></div>

<div class="fixed top-0 left-0 w-screen h-screen select-none -z-50 flex items-center justify-center opacity-10">
    <img src="/icon.png" alt="" draggable="false">
</div>

<div class="crt tv-start p-5" transition:fade>
    <p>Hello World!</p>
</div>
{/if}
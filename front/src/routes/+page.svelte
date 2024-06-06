<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import { activeWindows, openWindow } from "$lib/WindowManager";
    import { apps } from "$lib/Apps";

    import { playSound, stopSound } from "$lib/SoundManager";

    import { fade } from "svelte/transition";

    let windows = [];

    let loaded: boolean = false;
    let soundEnabled: boolean = false;
    let photosensitiveWarning = {
        state: false,
        expire: 0,
        remaining: "10s"
    }

    let noiseSoundID: string | null = null;

    let imageFlicker = {
        last: Date.now(),
        interval: 5000,
    }

    activeWindows.subscribe(value => {
        windows = value;
    });

    let eventLoopThread: any = null

    onMount(() => {
        if (localStorage.getItem("photosensitiveWarning") === null) {
            photosensitiveWarning.state = true;
            photosensitiveWarning.expire = Date.now() + 10000
        }

        eventLoopThread = setInterval(eventLoop, 250)

        loaded = true
    });

    onDestroy(() => {
        if (eventLoopThread) {
            clearInterval(eventLoopThread)
        }

        if (noiseSoundID) {
            stopSound(noiseSoundID)
        }
    });

    function flicker(img: HTMLImageElement, disableRecursion: boolean = false) {
        let randomDelay = Math.floor(Math.random() * 200) + 50
        let randomRetry = 0;
        if (disableRecursion) {
            randomRetry = Math.floor(Math.random() * 100)
        }

        img.style.opacity = "0"

        playSound("/flicker.mp3", 0.1)

        setTimeout(() => {
            img.style.opacity = "1"

            if (!disableRecursion && Math.random() < 0.5) {
                setTimeout(() => {
                    flicker(img, true)
                }, randomRetry)
            }

        }, randomDelay)
    }

    function eventLoop() {
        //photosensitive warning
        if (photosensitiveWarning.state) {
            let remaining = Math.floor((photosensitiveWarning.expire - Date.now()) / 1000)
            if (remaining <= 0) {
                photosensitiveWarning.state = false
                localStorage.setItem("photosensitiveWarning", "true")
            } else {
                photosensitiveWarning.remaining = remaining.toString() + "s"
            }
        }

        if (!soundEnabled) { return }

        //image flicker
        if (Date.now() - imageFlicker.last > imageFlicker.interval) {
            imageFlicker.last = Date.now()
            //get 3-5 random images
            let images = document.querySelectorAll("img")
            let randomImages = []
            for (let i = 0; i < Math.floor(Math.random() * 3) + 3; i++) {
                randomImages.push(images[Math.floor(Math.random() * images.length)])
            }
            
            randomImages.forEach(img => {
                flicker(img)
            })
        }
    }
</script>

{#if loaded}

{#if photosensitiveWarning.state}
    <div class="w-screen h-screen flex items-center justify-center gap-10 flex-wrap" transition:fade>
        <img src="/WarningSign.png" alt="" class="h-44">
        <div class="max-w-96">
            <h1 class="h1 uppercase font-black text-warning-500">Attention</h1>
            <p class="text-lg">This page contains flashing lights that may trigger seizures in some people, even without prior history of photosensitive epilepsy.</p>
            <button class="mt-5 btn variant-filled-warning" on:click={() => {
                photosensitiveWarning.expire = 0;
            }}>I Understand</button>
        </div>
    </div>

{:else if !soundEnabled}
    <button class="w-screen h-screen flex flex-col gap-10 items-center justify-center crt" on:click={() => {
        soundEnabled = true
        noiseSoundID = playSound("/noise.mp3", 0.05, true)
    }}>
        <img src="/icon.png" alt="" class="w-64">
        <h1 class="h3 uppercase font-black text-primary-500">Click Anywhere to Enable Sound</h1>
    </button>
{:else}

<div class="w-screen h-screen flex flex-col gap-5 flex-wrap p-5 xl:p-10 crt select-none" transition:fade>
    {#each Object.keys(apps) as app}
        <button class="w-20 h-24" on:click={() => {
            openWindow(app)
        }}>
            <img src="{apps[app].icon}" alt="" class="h-20" draggable="false">
            <p class="lowercase text-center">{apps[app].title}</p>
        </button>
    {/each}
</div>

{/if}
{/if}
<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import { apps } from "$lib/Apps";

    import { playSound, stopSound } from "$lib/SoundManager";
    import { activeWindows, openWindow, getAllAppWindows } from "$lib/WindowManager";
    import { type Window, type AppWindow as AppWindowType } from "$lib/WindowManager";

    import { fade } from "svelte/transition";

    import AppWindow from "$lib/components/AppWindow.svelte";
    import { contacts, sendEmail } from "$lib/Email";

    let windows: Window[] = [];

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
    let taskbar: AppWindowType[] = []

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
        if (img.className.includes("no-flicker")) { return }
        
        let randomDelay = Math.floor(Math.random() * 200) + 50
        let randomRetry = 0;
        if (disableRecursion) {
            randomRetry = Math.floor(Math.random() * 100)
        }

        img.style.opacity = "0"


        setTimeout(() => {
            img.style.opacity = "1"
            playSound("/flicker.mp3", 0.1)

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

        //prevent in-game interactions if sound is disabled
        if (!soundEnabled) { return }

        //taskbar
        taskbar = getAllAppWindows()

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

<head>
    <title>Xel Lu</title>
</head>

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
        // noiseSoundID = playSound("/noise.mp3", 0.05, true)
        setTimeout(() => {
            sendEmail({
                author: contacts[0],
                subject: "Welcome!",
                content: "Welcome to your job!",
                read: false
            })
        }, 5000)
    }}>
        <img src="/icon.png" alt="" class="w-64" draggable="false">
        <h1 class="h3 uppercase font-black text-primary-500">Click Anywhere to Enable Sound</h1>
    </button>
{:else}

<!-- background image -->
<div class="fixed w-screen h-screen -z-10 flex items-center justify-center opacity-10">
    <img src="/icon.png" alt="" class="w-96 animate-pulse">
</div>

<!-- desktop -->
<div class="w-screen h-screen flex flex-col gap-5 flex-wrap p-5 xl:p-10 crt select-none" transition:fade>
    {#each Object.keys(apps) as app}
        {#if !apps[app].hidden}
            <div class="w-20 h-24" on:click={() => {
                openWindow(app)
            }} on:keydown={null} role="checkbox" tabindex="0" aria-checked>
                <img src="{apps[app].icon}" alt="" class="h-20" draggable="false">
                <p class="lowercase text-center">{apps[app].title}</p>
            </div>
        {/if}
    {/each}
</div>

<!-- taskbar -->
<div class="fixed w-screen z-20 left-0 bottom-0 h-16 p-3 flex items-center justify-between bg-primary-900/5 select-none">
    <div class="w-56">
        <button class="flex gap-3 items-center pl-2 crt" on:click={() => openWindow("userprofile")}>
            <img src="/User.png" alt="" class="w-6 rounded-full border border-primary-500 p-1 no-flicker">
            <p class="text-xl text-primary-500">Profile</p>
        </button>
    </div>

    <div class="flex gap-5">
        {#each taskbar as window}
            {#if !window.app.hidden}
                <button class="flex flex-col gap-3 items-center pl-2" on:click={() => openWindow(window.appId)}>
                    <img src="{window.app.icon}" alt="" class="w-8 h-8" draggable="false">
                    <div class="w-8 h-1 {window.open == 'open' ? 'bg-primary-500' : window.open == 'closed' ? '' : 'bg-primary-500/10'}"></div>
                </button>
            {/if}
        {/each}
    </div>

    <div class="w-56 flex items-center justify-end crt">
        <p class="pr-3 text-lg text-primary-500">9:40 PM</p>
    </div>
</div>

<!-- app windows -->
{#each windows as window}
    <AppWindow bind:self={window}>
        <svelte:component this={apps[window.appId].component} bind:self={window} />
    </AppWindow>
{/each}

{/if}
{/if}
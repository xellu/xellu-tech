<script lang="ts">
    import { notify } from '$lib/notifications';
    import { onMount, onDestroy } from 'svelte';
    import { fade } from 'svelte/transition';

    import AppWindow from "./window.svelte";
    import About from "./windows/about.svelte";
    import Projects from "./windows/projects.svelte";
    import Email from './windows/email.svelte';
    import Terminal from './windows/terminal.svelte';

    var audio: any = null;

    let photosensitiveWarning: boolean = false
    let photosensitiveExpire: number = Date.now() + 10000
    let photosensitiveRemaining: string = "10s"

    let transitionDelay = {
        state: true,
        crt: false
    }

    let mobileWarning: boolean = false

    let windows: any = {
        about: {
            open: false,
            posX: 200,
            posY: 100,
            posZ: 0,
            onOpen: () => {}
        },
        projects: {
            open: false,
            posX: 220,
            posY: 120,
            posZ: 0,
            onOpen: () => {}
        },
        email: {
            open: false,
            posX: 240,
            posY: 140,
            posZ: 0,
            onOpen: () => {}
        },
        terminal: {
            open: false,
            posX: 260,
            posY: 160,
            posZ: 0,
            onOpen: () => {}
        }
    }

    let tray: {time: string, volume: boolean} = {
        time: new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }),
        volume: false
    }

    let intervals: any = {
        time: null,
        flicker: null
    }

    onMount(() => {
        // flashing lights warning
        if (localStorage.getItem('photosensitiveWarning') == undefined) {
            photosensitiveWarning = true

            setTimeout(() => {
                photosensitiveWarning = false
                transitionDelay.state = true
                transitionDelay.crt = true

                localStorage.setItem('photosensitiveWarning', 'set')

                setTimeout(() => {
                    transitionDelay.state = false;
                }, 1000)
            }, photosensitiveExpire - Date.now())
        }
        transitionDelay.state = false

        // mobile device warning
        if (window.innerWidth < 1024) {
            mobileWarning = true

            setTimeout(() => {
                mobileWarning = false
            }, 3000)
        }
        
        // preload assets
        const images = ['/icon.png', '/AboutMe.png', '/Projects.png', '/Email.png', '/Terminal.png', '/User.png', '/Volume.png', '/VolumeMuted.png',
            '/Music.png', '/WarningSign.png', '/rotate.gif'];
        
        images.forEach(image => {
            const img = new Image();
            img.src = image;
        });   

        intervals.flicker = setInterval(() => {
            imageFlicker()
        }, 5000)

        // update time
        intervals.time = setInterval(() => {
            photosensitiveRemaining = ((photosensitiveExpire - Date.now()) / 1000).toFixed(0) + "s"

            tray.time = new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
        }, 1000)
    })

    onDestroy(() => {
        console.info("Unloading page")
        Object.keys(intervals).forEach(key => {
            clearInterval(intervals[key])
        })

        if (audio) {
            audio.pause();
            audio.currentTime = 0;
        }
    })

    function playNoise() {
        if (audio) {
            audio.pause();
            audio.currentTime = 0;
        }

        audio = new Audio('/noise.mp3');
        audio.loop = true;
        audio.volume = 0.05;
        audio.play();
    }

    function stopNoise() {
        if (audio) {
            audio.pause();
            audio.currentTime = 0;
        }
    }

    function imageFlicker() {
        if (photosensitiveWarning) return;

        const images = document.querySelectorAll('img');

        const randomImages = [];
        for (let i = 0; i < 3; i++) {
            const random = Math.floor(Math.random() * images.length);
            randomImages.push(images[random]);
        }

        randomImages.forEach(img => {
            img.style.opacity = "0";
            setTimeout(() => {
                img.style.opacity = "1";
                if (Math.floor(Math.random() * 2) == 1) {
                    setTimeout(() => {
                        img.style.opacity = "0";
                        setTimeout(() => {
                            img.style.opacity = "1";
                        }, Math.floor(Math.random() * 100))
                    }, Math.floor(Math.random() * 100))
                }
            }, Math.floor(Math.random() * 100))
        })
    }
    
</script>

<svelte:head>
    <title>Xel Lu</title>
</svelte:head>

<div class="{photosensitiveWarning ? '' : 'crt'}">
    {#if mobileWarning}
    <div class="w-screen h-screen flex items-center justify-center gap-3 flex-col bg-surface-900/90" transition:fade>
        <img src="/rotate.gif" alt="" class="w-32">
        <p class="px-5 text-center">Please rotate your mobile device sideways for better experience</p>
        <p class="px-5 text-center mt-10 text-secondary-500">We advise using a desktop for the best experience</p>
    </div>
    {/if}

    {#if photosensitiveWarning}

    <div class="w-screen h-screen flex items-center justify-center flex-wrap gap-10" transition:fade>
        <img src="/WarningSign.png" alt="">
        <div class="flex justify-center flex-col gap-3 p-5">
            <h1 class="h1 font-black text-warning-500 max-w-xl w-full">ATTENTION ({photosensitiveRemaining})</h1>
            <p class="max-w-xl w-full text-lg">
                This page contains flashing lights that may trigger seizures in small percentage of people, even without prior history of photosensitive epilepsy.
            </p>
            <p class="text-warning-900">If you continue, we will not prompt you again</p>

            <button class="btn variant-filled-warning max-w-56 text-2xl font-bold" on:click={() => {
                photosensitiveWarning = false;
                transitionDelay.state = true
                transitionDelay.crt = true

                localStorage.setItem('photosensitiveWarning', 'set')

                setTimeout(() => {
                    transitionDelay.state = false;
                }, 1000)
            }}>Proceed</button>
        </div>
    </div>

    {:else if transitionDelay.state}
    <!-- <div class="crt-line"></div> -->

    <div class="w-screen h-screen"></div>
    {:else}

    <!-- <div class="crt-line"></div> -->

    <div class="fixed top-0 left-0 w-screen h-screen select-none -z-50 flex items-center justify-center opacity-10" transition:fade>
        <img src="/icon.png" alt="" draggable="false" class="max-w-xl w-full p-5 animate-pulse">
    </div>

    <div class="tv-start w-screen h-screen" transition:fade>
        <div class="h-screen w-screen flex flex-col">
            <!-- desktop -->
            <div class="w-full flex-grow flex flex-col flex-wrap gap-5 p-5 lg:p-16 select-none">

                <button class="flex flex-col items-center justify-center max-w-16 max-h-24" on:click={() => windows.about.onOpen()}>
                    <img src="/AboutMe.png" alt="" class="w-16" draggable="false">
                    <p>about me</p>
                </button>

                <button class="flex flex-col items-center justify-center max-w-16 max-h-24" on:click={() => windows.projects.onOpen()}>
                    <img src="/Projects.png" alt="" class="w-16" draggable="false">
                    <p>projects</p>
                </button>

                <button class="flex flex-col items-center justify-center max-w-16 max-h-24" on:click={() => windows.email.onOpen()}>
                    <img src="/Email.png" alt="" class="w-16" draggable="false">
                    <p>contact</p>
                </button>

                <button class="flex flex-col items-center justify-center max-w-16 max-h-24" on:click={() => windows.terminal.onOpen()}>
                    <img src="/Terminal.png" alt="" class="w-16" draggable="false" >
                    <p>terminal</p>
                </button>
                
            </div>

            <div class="bg-surface-500 flex items-center justify-between p-3 px-5 w-full h-16">
                <!-- user -->
                <button class="flex items-center justify-between gap-3" on:click={() => { notify("FATAL SYSTEM FAILURE: auth.service is not responding", "error") }}>
                    <img src="/User.png" alt="USER" class="w-6 rounded-full border border-primary-500 p-1">
                    <p class="text-primary-500 text-xl">%user%</p>
                </button>

                <!-- time & tray -->
                <div class="flex items-center justify-center gap-5">
                    <button on:click={() => {
                        tray.volume = !tray.volume;
                        tray.volume ? playNoise() : stopNoise();
                    }}>
                        <img src="/{tray.volume ? 'Volume' : 'VolumeMuted'}.png" alt="VOLUME" class="w-6">
                    </button>

                    <p class="text-xl text-primary-500">{tray.time}</p>
                </div>
            </div>
        </div>
    </div>
    {/if}

    <AppWindow name="About Me" bind:self={windows.about} bind:windows={windows}>
        <About />
    </AppWindow>

    <AppWindow name="Projects" bind:self={windows.projects} bind:windows={windows}>
        <Projects />
    </AppWindow>

    <AppWindow name="Xel's E-Mail Client" bind:self={windows.email} bind:windows={windows}>
        <Email />
    </AppWindow>

    <AppWindow name="Terminal" bind:self={windows.terminal} bind:windows={windows}>
        <Terminal bind:self={windows.terminal} bind:windows={windows} />
    </AppWindow>
</div>

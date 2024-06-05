<script lang="ts">
    import { notify, pingState } from '$lib/notifications';
    import { onMount, onDestroy } from 'svelte';
    import { fade } from 'svelte/transition';
    import { playSound } from '$lib/sounds';
    import { contacts } from '$lib/contacts';

    import AppWindow from "./window.svelte";
    import About from "./windows/about.svelte";
    import Projects from "./windows/projects.svelte";
    import Email from './windows/email.svelte';
    import Terminal from './windows/terminal.svelte';
    import Tasks from './windows/tasks.svelte';
    import Files from './windows/files.svelte';
    import FileDisplay from './windows/filedisplay.svelte';

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
        todo: {
            open: true,
            posX: 400,
            posY: 200,
            posZ: 1,
            onOpen: () => {}
        },
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
        },
        files: {
            open: false,
            posX: 280,
            posY: 180,
            posZ: 0,
            onOpen: () => {}
        },
        fileDisplay: {
            open: false,
            posX: 300,
            posY: 200,
            posZ: 0,
            content: [],
            onOpen: () => {}
        }
    }

    let tasks: any = {
        readAbout: {
            title: "Read About the Company",
            description: "Take a look at what We've accomplished!",
            completed: false
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

    let inbox: {title: string, message: string, author: {name: string, online: boolean, send: Function}, unread: boolean}[] = []

    onMount(() => {

        windows.todo.posX = window.innerWidth - 350
        windows.todo.posY = 50

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
            '/Music.png', '/WarningSign.png', '/rotate.gif', "/Files.png", "/File.png", "/Folder.png", "/Tasks.png"];
        
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

        setTimeout(() => {
            inbox = inbox.concat({
                title: "Welcome to the company!",
                message: "We're glad to have you on board! Please take a look on the top right corner for your tasks. If you have any questions, feel free to ask!",
                author: contacts[1],
                unread: true
            })
            notify("You've got mail!")
        }, photosensitiveWarning ? 20000 : 10000)
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
        audio.volume = 0.02;
        audio.play();

        pingState.set(true)
    }

    function stopNoise() {
        if (audio) {
            audio.pause();
            audio.currentTime = 0;
        }

        pingState.set(false)
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
                if (tray.volume) playSound("flicker.mp3", 0.1)
                img.style.opacity = "1";
                if (Math.floor(Math.random() * 2) == 1) {
                    setTimeout(() => {
                        img.style.opacity = "0";
                        setTimeout(() => {
                            img.style.opacity = "1";
                            if (tray.volume) playSound("flicker.mp3", 0.1)
                        }, Math.floor(Math.random() * 200))
                    }, Math.floor(Math.random() * 200))
                }
            }, Math.floor(Math.random() * 200))
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
            <div class="w-full flex-grow flex flex-wrap gap-7 p-5 lg:p-16 select-none">
                <div class="flex flex-col gap-5">                    
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
                        <p>e-mail</p>
                    </button>

                    <button class="flex flex-col items-center justify-center max-w-16 max-h-24" on:click={() => windows.terminal.onOpen()}>
                        <img src="/Terminal.png" alt="" class="w-16" draggable="false" >
                        <p>terminal</p>
                    </button>

                    <button class="flex flex-col items-center justify-center max-w-16 max-h-24" on:click={() => windows.files.onOpen()}>
                        <img src="/Files.png" alt="" class="w-16" draggable="false" >
                        <p>files</p>
                    </button>                

                </div>
                
                <div class="flex flex-col gap-5"> 
                    <button class="flex flex-col items-center justify-center max-w-16 max-h-24" on:click={() => windows.todo.onOpen()}>
                        <img src="/Tasks.png" alt="" class="w-16" draggable="false" >
                        <p>tasks</p>
                    </button>
                </div>
                
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

    {#if !photosensitiveWarning && !mobileWarning && !transitionDelay.state}

    <AppWindow name="About Me" bind:self={windows.about} bind:windows={windows} bind:tray={tray}>
        <About />
    </AppWindow>

    <AppWindow name="Projects" bind:self={windows.projects} bind:windows={windows} bind:tray={tray}>
        <Projects />
    </AppWindow>

    <AppWindow name="E-Mail" bind:self={windows.email} bind:windows={windows} bind:tray={tray}>
        <Email bind:inbox={inbox} />
    </AppWindow>

    <AppWindow name="Terminal" bind:self={windows.terminal} bind:windows={windows} bind:tray={tray}>
        <Terminal bind:self={windows.terminal} bind:windows={windows} bind:tasks={tasks} bind:inbox={inbox} />
    </AppWindow>

    <AppWindow name="Tasks" bind:self={windows.todo} bind:windows={windows} bind:tray={tray} locked={true}>
        <Tasks bind:tasks={tasks} />
    </AppWindow>

    <AppWindow name="File Browser" bind:self={windows.files} bind:windows={windows} bind:tray={tray}>
        <Files bind:windows={windows} bind:tasks={tasks} bind:inbox={inbox} />
    </AppWindow>

    <AppWindow name="Notepad" bind:self={windows.fileDisplay} bind:windows={windows} bind:tray={tray}>
        <FileDisplay bind:content={windows.fileDisplay.content} />
    </AppWindow>
    
    {/if}

    
</div>

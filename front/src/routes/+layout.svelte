<script lang="ts">
    import "../app.pcss"

    import Highlighed from "$lib/components/Highlighed.svelte";

    import { instagram, github, discord } from "$lib/socials";

    import { onMount, onDestroy } from "svelte";
    import { getToastStore, initializeStores, Toast } from "@skeletonlabs/skeleton";

    import { AutoAuthenticate, AuthLogger } from '$lib/scripts/Auth';

    initializeStores();



    const toast = getToastStore();

    function onMove(event: MouseEvent) {
        let circle = document.getElementById("circle");
        if (!circle) return;
        
        let x = event.clientX - (circle.clientWidth / 2);
        let y = event.clientY - (circle.clientHeight / 2);

        if (x < 0) x = 0;
        if (y < 0) y = 0;
        if (x + circle.clientWidth > window.innerWidth) x = window.innerWidth - circle.clientWidth;
        if (y + circle.clientHeight > window.innerHeight) y = window.innerHeight - circle.clientHeight;

        circle.style.left = x + "px";
        circle.style.top = y + "px";
    }

    let page: {list: {name: string, path: string}[], active: string} = {
        list: [
            {
                name: "About",
                path: "/",
            },
            {
                name: "Blog",
                path: "/blog"
            },
            {
                name: "Image Host",
                path: "/host"
            }
        ],
        active: ""
    }

    let loops: any[] = []
    onMount(async () => {
        document.body.addEventListener("mousemove", onMove);

        let auth = await AutoAuthenticate();

        auth.state.loggedIn ? AuthLogger.ok(`Successfully authenticated (${auth.state.auto})`) : AuthLogger.warn(`Unable to authenticate: ${auth.state.error}`);
        if (auth.state.error && !auth.state.loggedIn) { //show error message
            toast.trigger({
                message: auth.state.error,
                background: "variant-glass-warning",
            })
        }

        loops.push(setInterval(() => {
            let current: string | null = null;
            
            page.list.forEach(p => {
                if (window.location.pathname.startsWith(p.path)) {
                    current = p.path;
                }
            })

            // console.log(window.location.pathname, current)

            if (current) {
                page.active = current;
            } else {
                page.active = "/";
            }
        }, 100))
    })

    onDestroy(() => {
        loops.forEach(l => clearInterval(l));
    })



</script>

<Toast />

<div id="circle"
    class="max-lg:hidden absolute w-[400px] h-[400px] -top-[500px] left-1/2 rounded-full -z-20 duration-150"
    style="background: radial-gradient(circle, rgba(var(--color-primary-500) / 0.2) 0%, rgba(var(--color-primary-500) / 0) 70%)"
></div>

<div class="flex flex-wrap max-md:flex-col lg:justify-between lg:gap-32 backdrop-blur-md">
    <!-- left side -->
    <div class="min-w-64 lg:w-1/5 lg:flex-grow flex flex-col lg:justify-between xl:items-end p-10 xl:pt-32 lg:min-h-screen gap-10">
        <!-- top -->
        <div class="max-w-96">
            <h1 class="h1 text-7xl text-primary-500 font-bold">
                <Highlighed>Xellu</Highlighed>
            </h1>
            <p class="text-lg">Full-Stack Developer</p>
            <p class="mt-5 text-surface-50 max-w-80">
                👋 Hello! I'm a <Highlighed>Developer</Highlighed> from Czechia,
                Living in Siberia, Russia. 
            </p>

            <div class="flex flex-col gap-2 mt-16">
                {#each page.list as p}                
                    <a href="{p.path}">
                        <button class="flex items-center gap-1 group">
                            <div class="h-px {p.path == page.active ? 'w-12 bg-tertiary-500' : 'w-6 bg-white group-hover:bg-tertiary-300 group-hover:w-12'} duration-300"></div>
                            <p class="{p.path == page.active ? 'text-tertiary-500' : ''} duration-300">{p.name}</p>
                        </button>
                    </a>
                {/each}
                
            </div>
        </div>

        <!-- bottom -->
        <div class="flex items-center xl:justify-center gap-5">
            <a href={instagram} target="_blank" rel="noopener noreferrer" draggable="false" class="opacity-50 hover:opacity-100 duration-200">
                <img src="/instagram.png" alt="instagram" class="h-8" draggable="false" />
            </a>
            <a href={github} target="_blank" rel="noopener noreferrer" draggable="false" class="opacity-50 hover:opacity-100 duration-200">
                <img src="/github.png" alt="github" class="h-8" draggable="false" />
            </a>
            <a href={discord} target="_blank" rel="noopener noreferrer" draggable="false" class="opacity-50 hover:opacity-100 duration-200">
                <img src="/discord.png" alt="discord" class="h-8" draggable="false" />
            </a>
        </div>

    </div>

    <!-- right side -->
    <div class="min-w-64 lg:w-1/3 flex-grow flex flex-col gap-3 xl:h-screen items-start p-10 xl:pt-32 overflow-y-scroll scroll-smooth">

        <!-- page content -->
        <div class="w-full xl:w-3/5">
            <slot></slot>
        </div>

    </div>
</div>   

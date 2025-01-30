<script lang="ts">
    import "../app.pcss"
    import "../markdown.pcss"

    import Highlighted from "$lib/components/Highlighted.svelte";
    import MouseCircle from "$lib/components/MouseCircle.svelte";

    import { instagram, github, discord } from "$lib/socials";

    import { onMount, onDestroy } from "svelte";
    import { getToastStore, initializeStores, Toast, Modal } from "@skeletonlabs/skeleton";

    import { AutoAuthenticate, AuthLogger } from '$lib/scripts/Auth';

    initializeStores();

    const ICONS = [
        "add",
        "arrow_right_alt",
        "edit",
        "delete",
        "error",
        "open_in_new",
        "cancel_schedule_send",
        "send",
        "check",
        "close",
        "keyboard_arrow_down",
        "expand_more",
    ].toSorted();

    const toast = getToastStore();

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
                path: "/panel"
            }
        ],
        active: ""
    }

    let loops: any[] = []
    onMount(async () => {
        let auth = await AutoAuthenticate();

        auth.state.loggedIn ? AuthLogger.ok(`Successfully authenticated (${auth.state.auto})`) : AuthLogger.warn(`Unable to authenticate: ${auth.state.error}`);
        if (auth.state.error && !auth.state.loggedIn) { //show error message
            toast.trigger({
                message: auth.state.error,
                background: "variant-soft-warning",
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

<svelte:head>
    <meta name="author" content="Xellu" />
    <meta name="description" content="A Personal blog page and invite-only image hosting" />
    <meta name="keywords" content="blog, posts, xellu, xellu.tech, image hosting" />

    <meta content="#33A4F7" data-react-helmet="true" name="theme-color" />

    <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names={ICONS}"
    />
</svelte:head>

<Toast />
<Modal />
<MouseCircle />

<div class="flex flex-wrap max-md:flex-col lg:justify-between lg:gap-32 backdrop-blur-md">
    <!-- left side -->
    <div class="min-w-64 lg:w-1/5 lg:flex-grow flex flex-col lg:justify-between xl:items-end p-10 xl:pt-32 lg:min-h-screen gap-10">
        <!-- top -->
        <div class="max-w-96">
            <h1 class="h1 text-7xl text-primary-500 font-bold">
                <Highlighted>Xellu</Highlighted>
            </h1>
            <p class="text-lg">Full-Stack Developer</p>
            <p class="mt-5 text-surface-50 max-w-80">
                👋 Hello! I'm a <Highlighted>Developer</Highlighted> from Czechia,
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

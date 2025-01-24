<script lang="ts">
    import Highlighed from "$lib/components/highlighed.svelte";

    import Bio from "$lib/pages/Bio.svelte";
    import Blog from "$lib/pages/Blog.svelte";

    import { instagram, github, discord } from "$lib/socials";

    import { slide } from "svelte/transition";
    import { onDestroy, onMount } from "svelte";

    let page: {list: {name: string, id: string, component: any, hidden?: true}[], active: string} = {
        list: [
            {
                name: "About",
                id: "bio",
                component: Bio
            },
            {
                name: "Blog",
                id: "blog",
                component: Blog
            }
        ],
        active: "bio"
    }

    let loops: any = []
    onMount(() => {
        loops.push(setInterval(() => {
            if (window.location.hash) {
                let hash = window.location.hash.slice(1);
                if (page.list.find(p => p.id == hash)) {
                    page.active = hash;
                }
            } else {
                page.active = "bio";
            }
        }, 100))
    })

    onDestroy(() => {
        loops.forEach((l: any) => clearInterval(l));
    })
</script>


<head>
    <title>Xellu</title>
</head>

<div class="flex flex-wrap max-md:flex-col lg:justify-between lg:gap-32">
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
                    {#if !p.hidden}
                    <button class="flex items-center gap-1 group" on:click={() => {
                        if (p.id == page.active) { return; }
                        
                        window.location.hash = p.id;
                    }}>
                        <div class="h-px {p.id == page.active ? 'w-12 bg-tertiary-500' : 'w-6 bg-white group-hover:bg-tertiary-300 group-hover:w-12'} duration-300"></div>
                        <p class="{p.id == page.active ? 'text-tertiary-500' : ''} duration-300">{p.name}</p>
                    </button>
                    {/if}
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
            {#each page.list as p}
                {#if p.id == page.active}
                    <div transition:slide>
                        <svelte:component this={p.component}></svelte:component>
                    </div>
                {/if}
            {/each}
        </div>

    </div>
</div>
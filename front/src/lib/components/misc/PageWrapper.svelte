<script lang="ts">
    import Highlighted from "$lib/components/Highlighted.svelte";

    import { onMount, onDestroy } from "svelte";
    import { instagram, github, discord } from "$lib/socials";

    export let title: string = "Xellu";
    export let subtitle: string | null = null

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
                name: "File Host",
                path: "/panel"
            }
        ],
        active: ""
    }

    let loops: any[] = []
    onMount(async () => {
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

<div class="flex flex-wrap max-md:flex-col lg:justify-between lg:gap-32 backdrop-blur-md">
    <!-- left side -->
    <div class="min-w-64 lg:w-1/5 lg:flex-grow flex flex-col lg:justify-between xl:items-end p-10 xl:pt-32 lg:min-h-screen gap-10">
        <!-- top -->
        <div class="max-w-96">
            <h1 class="h1 text-7xl text-primary-500 font-bold">
                <Highlighted>{title}</Highlighted>
            </h1>
            <p class="text-lg w-80">{subtitle == null ? 'Full-Stack Developer' : subtitle}</p>
            {#if subtitle == null}
                <p class="mt-5 text-surface-50 w-80">
                    👋 Hello! I'm a <Highlighted>Developer</Highlighted> from Czechia, Living in Siberia, Russia.
                </p>
            {/if}

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
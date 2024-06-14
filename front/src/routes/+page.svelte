<script lang="ts">
    import Highlighed from "$lib/components/highlighed.svelte";
    import Separator from "$lib/components/separator.svelte";

    import { instagram, github, youtube, discord } from "$lib/socials";
    import { projects } from "$lib/projects";
</script>

<head>
    <title>iohue</title>
</head>

<div class="w-screen flex items-center justify-center py-56 p-5">
    <div class="p-7 card max-w-xl w-full rounded-xl">
        
        <!-- profile -->
        <header class="h-56 flex flex-col items-center justify-center gap-5 w-full">
            <div class="flex items-center justify-center gap-10">
                <img src="/favicon.png" alt="profile icon" class="w-28 rounded-full">
                <div class="flex flex-col gap-3">
                    <p>👋 Hello! I am..</p>
                    <h1 class="h1 font-bold bg-gradient-to-bl from-primary-500 to-secondary-500 bg-clip-text text-transparent">
                        Iohue
                    </h1>
                </div>
            </div>

            <div class="flex items-center justify-center gap-3">
                <a href="{github}" target="_blank" class="hover:opacity-80 duration-150">
                    <img src="/github.png" alt="github" class="w-10" draggable="false">
                </a>
                <a href="{instagram}" target="_blank" class="hover:opacity-80 duration-150">
                    <img src="/instagram.png" alt="github" class="w-10" draggable="false">
                </a>
                <a href="{youtube}" target="_blank" class="hover:opacity-80 duration-150">
                    <img src="/youtube.png" alt="github" class="w-10" draggable="false">
                </a>
                
            </div>
        </header>

        <!-- about me -->
        <Separator>About Me</Separator>
        <p>
            I'm a <Highlighed>Full-Stack</Highlighed> Developer, from 🇨🇿 & 🇷🇺. 
            I'm passionate about <Highlighed from="from-tertiary-500" to="to-tertiary-600">Web</Highlighed> and <Highlighed from="from-error-500" to="to-error-600">Game</Highlighed> Development
        </p>

        <!-- current project -->
        <Separator>What I'm Doing</Separator>
        <p>
            I'm currently working on <Highlighed style="font-bold">Lime</Highlighed>, a Game Cheat Marketplace and Provider.
        </p>

        <div class="w-full flex justify-end">
            <a href="https://limeade.cool/" target="_blank">
                <button class="btn btn-sm variant-soft-primary mt-3">
                    Check it Out
                </button>
            </a>
        </div>

        <!-- past projects -->
        <Separator>My Work</Separator>
        <div class="flex flex-col gap-3">
            {#each projects as p}
                <div class="card variant-filled-surface p-5">
                    <div class="flex items-start justify-between">
                        <div>
                            <h3 class="h4 font-bold">{p.name}</h3>
                            <p class="text-sm">{p.description}</p>
                        </div>

                        <a href="{p.url}" target="_blank">
                            <button class="btn btn-sm variant-soft-tertiary rounded-md">Open</button>
                        </a>
                    </div>

                    <div class="flex flex-wrap gap-2 mt-2">
                        {#each p.tags as tag}
                            <span class="chip variant-soft-secondary">{tag}</span>
                        {/each}
                    </div>
                </div>
            {/each}

            <div class="flex justify-end">
                <a href="{github}" target="_blank">
                    <button class="btn btn-sm variant-filled-surface mt-3">
                        See More
                    </button>
                </a>
            </div>
        </div>

        <!-- contact me -->
        <Separator>Get In Touch</Separator> 
        <p>
            Feel free to reach out to me on <a href="{discord}" class="text-secondary-500 underline" target="_blank">Discord</a> or
            <a href="{instagram}" class="text-tertiary-500 underline" target="_blank">Instagram</a>
        </p>

    </div>
</div>
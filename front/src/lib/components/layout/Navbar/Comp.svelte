<script lang="ts">
    import { Grid } from "../../Grid";
    import Button from "../../Button.svelte";
    import { isOpen, highlightedElement, blockInteraction, URLS } from "./store";

    import { goto } from "$app/navigation";
    import { onMount } from "svelte";
    import { fade, slide } from "svelte/transition";
    import Mesh from "../../Mesh.svelte";

    let contactButton: boolean = $state(false);

    onMount(() => {
        if (!window.location.pathname.includes("/panel")) { contactButton = true; }
    })
</script>

<svelte:head>
    <style>
        @keyframes highlight {
            0%, 100% { background-color: white; }
            50% { background-color: var(--color-secondary-300); }
            
        }
        .bg-highlight {
            animation: highlight 2s infinite;
            border-left: 1px solid black;
            color: black;
        }
    </style>
</svelte:head>

<Grid.Root className="pt-32 pb-8">
    <Grid.Lines.All />

    <Grid.Duo className="lg:pr-3 lg:col-span-1! max-lg:col-span-3">
        <div class="w-full flex items-center z-40">
            <div class="w-12">
                <Button
                    label = "" icon = "menu"
                    onclick = {() => { isOpen.set(true) }}
                />
            </div>
            <a class="h-12 grow flex justify-center items-center max-lg:text-surface-950 max-lg:bg-primary-500 duration-150" draggable="false" href="/" title="Xellu">
                <h1 class="h2 pl-3 pt-1">Xellu</h1>
            </a>
        </div>
    </Grid.Duo>

    <div class="lg:col-span-1"></div>

    <Grid.DuoEx className="flex justify-end">
        {#if contactButton}
        <div class="lg:w-1/2 w-full max-lg:hidden">
            <Button
                label = "Contact Me" icon = "waving_hand"
                onclick={() => { goto('/contact') }}
            />
        </div>
        {/if}
    </Grid.DuoEx>
</Grid.Root>

{#if $isOpen}
    <div class="fixed w-screen h-screen bg-primary-500 z-50 top-0 left-0" transition:slide={{axis: "x"}}>
    <div transition:fade class="w-screen h-screen">
        <Grid.Root className="pt-32 pb-8">
            <Grid.Lines.All border="bright" />

            <Grid.Duo className="lg:pr-3 lg:col-span-1! max-lg:col-span-3">
                <div class="w-full flex items-center z-40">
                    <div class="w-12">
                        <Button
                            label = "" icon = "close"
                            variant = "filled"
                            onclick = {() => { isOpen.set(false) }}
                        />
                    </div>
                    <button class="h-12 grow flex justify-center items-center max-lg:text-surface-950 duration-150" onclick={() => {
                        goto("/");
                        isOpen.set(false);
                    }}>
                        <h1 class="h2 pl-3 pt-1 text-black">Xellu</h1>
                    </button>
                </div>
            </Grid.Duo>

            <div class="lg:col-span-1"></div>

            <Grid.DuoEx className="flex justify-end">
                <div class="lg:w-1/2 w-full max-lg:hidden">
                    <Button
                        label = "Contact Me" icon = "waving_hand"
                        variant = "filled"
                        onclick={() => { goto('/contact') }}
                    />
                </div>
            </Grid.DuoEx>
        </Grid.Root>

        <Grid.Root className="text-black max-lg:-mt-5">
            <Grid.Lines.Minimal border="bright" />

            <Grid.Full className="border-y border-surface-700 w-full flex flex-col">
                {#each URLS as link, i}
                    <button class="w-full h-24 lg:h-32 group  {i != 0 ? 'border-t border-surface-700' : ''} h1 font-sans font-black flex whitespace-nowrap" onclick={() => { 
                        goto(link.url);
                        isOpen.set(false);
                    }}>
                        <div class="{$blockInteraction ? ($highlightedElement == link.name ? 'w-0' : 'w-full') : 'group-hover:w-0 w-full'} duration-300 h-24 lg:h-32 flex items-center justify-center overflow-hidden uppercase"><span>{link.name}</span></div>
                        <div class="{$blockInteraction ? ($highlightedElement == link.name ? 'w-full' : 'w-0') : 'group-hover:w-full w-0'} duration-300 h-24 lg:h-32 flex items-center justify-center text-white bg-black overflow-hidden uppercase"><span>{link.name}</span></div>
                    </button>
                {/each}
            </Grid.Full>
        </Grid.Root>
        
        <Grid.Root className="lg:h-5 max-lg:hidden">
            <Grid.Lines.Minimal border="bright" />
            <Grid.Full>
                <Mesh direction="horizontal" className="w-full h-5"><div></div></Mesh>
            </Grid.Full>
        </Grid.Root>

        <Grid.Root className="max-lg:-mt-8">
            <Grid.Lines.Minimal border="bright" />

            <Grid.Full className="flex max-lg:px-5 lg:items-center lg:justify-evenly max-lg:flex-col p-5 border-surface-700 border-y duration-150 {$highlightedElement == 'socials' ? 'bg-highlight' : 'text-black'}  gap-3">
                <a href="https://github.com/xellu/" class="flex gap-3 items-center select-none group" draggable="false" target="_blank">
                    <img src="/brands/github.png" alt="" class="w-5 lg:w-8">
                    <p class="lg:text-xl font-semibold font-mono whitespace-nowrap group-hover:underline">/xellu</p>
                </a>

                <a href="https://www.instagram.com/xelluuu/" class="flex gap-3 items-center select-none group" draggable="false" target="_blank">
                    <img src="/brands/instagram.png" alt="" class="w-5 lg:w-8">
                    <p class="lg:text-xl font-semibold font-mono whitespace-nowrap group-hover:underline">@xelluuu</p>
                </a>

                <a href="https://discord.com/users/923528901219729430" class="flex gap-3 items-center select-none group" draggable="false" target="_blank">
                    <img src="/brands/discord.png" alt="" class="w-5 lg:w-8">
                    <p class="lg:text-xl font-semibold font-mono whitespace-nowrap group-hover:underline">@nejfake</p>
                </a>

                
                <!-- <p>{$highlightedElement || 'null'}</p> -->
            </Grid.Full>
        </Grid.Root>

        <Grid.Root className="h-full max-lg:-mt-5">
            <Grid.Lines.All border="bright" />

            <Grid.Full className="max-lg:-mt-5">
                <Mesh className="w-full h-screen"><div></div></Mesh>
            </Grid.Full>
        </Grid.Root>
    </div>
    </div>
{/if}
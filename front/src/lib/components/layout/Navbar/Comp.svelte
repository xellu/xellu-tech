<script lang="ts">
    import { Grid } from "../../Grid";
    import Button from "../../Button.svelte";
    import Mesh from "../../Mesh.svelte";
    import { Socials } from "$lib/stores/Bio";


    import { isOpen, highlightedElement, blockInteraction, URLS, externalUrl } from "./store";

    import { goto, preloadData } from "$app/navigation";
    import { onMount } from "svelte";
    import { fade, slide } from "svelte/transition";

    let contactButton: boolean = $state(false);
    let navToUrl = $derived(new URL($externalUrl, window.location.origin));


    onMount(() => {
        if (!window.location.pathname.includes("/panel") && !window.location.pathname.includes("/contact")) { contactButton = true; }

        const preloader = (e: MouseEvent) => {
            const parent = (e.target as HTMLElement).parentElement;
            if (!parent) return;
            const url = parent.getAttribute("data-preload-url");
            if (url) { preloadData(url); }
        };
        document.body.addEventListener("mousemove", preloader);
        return () => { document.body.removeEventListener("mousemove", preloader); }
    })
   
    $effect(() => {
        document.body.style.overflow = $isOpen ? 'hidden' : '';
    });
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

<Grid.Root className="pt-8 lg:pt-32 pb-8">
    <Grid.Lines.All />

    <Grid.Duo className="lg:pr-3 lg:col-span-1! max-lg:col-span-3">
        <div class="w-full flex items-center">
            <div class="w-12 fixed z-40 shadow-xl">
                <Button
                    label = "" icon = "menu"
                    onclick = {() => { isOpen.set(true) }}
                />
            </div>
            <a class="h-12 grow flex justify-center items-center max-lg:text-surface-950 max-lg:bg-primary-500 duration-150" draggable="false" href="/" title="Xellu">
                <h1 class="h2 pl-15 pt-1">Xellu</h1>
            </a>
        </div>
    </Grid.Duo>

    <div class="lg:col-span-1"></div>

    <Grid.DuoEx className="flex justify-end">
        {#if contactButton}
        <div class="lg:w-1/2 w-full max-lg:hidden">
            <Button
                label = "Contact Me" icon = "waving_hand"
                url = "/contact"
            />
        </div>
        {/if}
    </Grid.DuoEx>
</Grid.Root>

{#if $isOpen}
    <div class="fixed w-screen h-screen bg-primary-500 z-50 top-0 left-0" transition:slide={{axis: "x"}}>
    <div transition:fade class="w-screen h-screen">
        <Grid.Root className="pt-8 lg:pt-32 pb-8">
            <Grid.Lines.All border="bright" />

            <Grid.Duo className="lg:pr-3 lg:col-span-1! max-lg:col-span-3">
                <div class="w-full flex items-center z-40">
                    <div class="min-w-12">
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
                        onclick={() => { goto('/contact'); isOpen.set(false) }}
                    />
                </div>
            </Grid.DuoEx>
        </Grid.Root>

        <Grid.Root className="text-black" padding={true}>
            <Grid.Lines.Minimal border="bright" />

            <Grid.Full className="border-y border-surface-700">
                {#if $highlightedElement == "url"}
                    <div class="w-full bg-black text-white flex items-center justify-center text-3xl font-title" style="height: {128*URLS.length}px;" transition:slide>
                        <span>{window.location.origin == navToUrl.origin ? navToUrl.pathname.split('/')[navToUrl.pathname.split('/').length-1] || 'Home' : navToUrl.hostname}</span>
                    </div>
                {:else}
                    <div class="w-full flex flex-col" transition:slide>
                    {#each URLS as link, i}
                        <button class="w-full h-32 group  {i != 0 ? 'border-t border-surface-700' : ''} h1 font-sans font-black flex whitespace-nowrap"
                            data-preload-url={link.url}
                            onclick={() => { 
                                goto(link.url);
                                isOpen.set(false);
                        }}>
                            <div class="{$blockInteraction ? ($highlightedElement == link.name ? 'w-0' : 'w-full') : 'group-hover:w-0 w-full'} duration-300 h-32 flex items-center justify-center overflow-hidden uppercase"><span>{link.name}</span></div>
                            <div class="{$blockInteraction ? ($highlightedElement == link.name ? 'w-full' : 'w-0') : 'group-hover:w-full w-0'} duration-300 h-32 flex items-center justify-center text-white bg-black overflow-hidden uppercase"><span>{link.name}</span></div>
                        </button>
                    {/each}
                    </div>
                {/if}
            </Grid.Full>
        </Grid.Root>
        
        <Grid.Root className="lg:h-5 max-lg:hidden">
            <Grid.Lines.Minimal border="bright" />
            <Grid.Full>
                <Mesh direction="horizontal" className="w-full h-5"><div></div></Mesh>
            </Grid.Full>
        </Grid.Root>

        <Grid.Root>
            <Grid.Lines.Minimal border="bright" />

            <Grid.Full className="flex max-lg:px-5 lg:items-center lg:justify-evenly max-lg:flex-col p-5 border-surface-700 lg:border-t border-b duration-150 {$highlightedElement == 'socials' ? 'bg-highlight' : 'text-black'}  lg:gap-3">
                <a href="{Socials.github}" class="flex gap-3 items-center select-none group" draggable="false" target="_blank">
                    <img src="/brands/github.png" alt="" class="w-5 lg:w-8">
                    <p class="lg:text-xl font-semibold font-mono whitespace-nowrap group-hover:underline">/xellu</p>
                </a>

                <a href="{Socials.instagram}" class="flex gap-3 items-center select-none group" draggable="false" target="_blank">
                    <img src="/brands/instagram.png" alt="" class="w-5 lg:w-8">
                    <p class="lg:text-xl font-semibold font-mono whitespace-nowrap group-hover:underline">@xelluuu</p>
                </a>

                <a href="{Socials.discord}" class="flex gap-3 items-center select-none group" draggable="false" target="_blank">
                    <img src="/brands/discord.png" alt="" class="w-5 lg:w-8">
                    <p class="lg:text-xl font-semibold font-mono whitespace-nowrap group-hover:underline">@nejfake</p>
                </a>

                
                <!-- <p>{$highlightedElement || 'null'}</p> -->
            </Grid.Full>
        </Grid.Root>

        <Grid.Root className="h-full">
            <Grid.Lines.All border="bright" />

            <Grid.Full>
                <Mesh className="w-full h-screen"><div></div></Mesh>
            </Grid.Full>
        </Grid.Root>
    </div>
    </div>
{/if}
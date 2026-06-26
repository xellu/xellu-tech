<script lang="ts">
    import JBGlyph from "./JBGlyph.svelte";
    
    import { addIcon } from "$lib/stores/IconStore";
    import { onMount } from "svelte";

    let { name, className = "" }: {name: string, className?: string} = $props();

    onMount(() => {
        if (!name.startsWith("glyph:")) { addIcon(name) }
    })
</script>

<svelte:head>
    <style>
        @keyframes wave-anim {
            0%, 100% {
                rotate: -10deg
            }
            50% {
                rotate: 10deg
            }
        }

        .animate-wave {
            animation: wave-anim 2s infinite;
        }
    </style>
</svelte:head>

{#if name.startsWith("glyph:")}
    <JBGlyph {className} text={name.replace('glyph:', '')} />
{:else}
    <span class="material-symbols-sharp {className} {name == 'waving_hand' ? ' animate-wave' : ''}">{name}</span>
{/if}
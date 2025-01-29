<script lang="ts">
    import { ConicGradient, type ConicStop } from "@skeletonlabs/skeleton";

    export let center: boolean = true;
    export let centerY: boolean = false;
    
    export let error: string | null = null;

    const conicStops: ConicStop[] = [
        { color: 'transparent', start: 0, end: 1 },
        { color: 'rgb(var(--color-primary-500))', start: 90, end: 100 }
    ];
</script>

<div class="{center ? 'flex items-center justify-center w-full' : ''} {centerY ? 'h-screen': ''}">
    <div class="flex flex-col items-center">
        {#if error == null}
            <ConicGradient stops={conicStops} spin width="w-12" />
        
        <!-- error handler -->
        {:else}
            <span class="material-symbols-outlined text-error-500 text-5xl">error</span>
            <p class="text-error-500 opacity-50 font-bold text-xs uppercase my-5">{error}</p>
        {/if}
    </div>


</div>
<script lang="ts">
    import { Grid } from ".";
    import Mesh from "../Mesh.svelte";

    let { variant, label = undefined, height = "h-32" }:
        {
            variant: "empty" | "alt1" | "alt2" | "alt3" | "breakout"
            height?: string,
            label?: string}
    = $props()
</script>

<div class="max-lg:hidden">
{#if variant == "empty"}
    <Grid.Root className={height}>
        <Grid.Lines.Minimal />
        <Grid.Full className="border-y border-surface-800/80"><div></div>
        </Grid.Full>
    </Grid.Root>

{:else if variant == "alt1"}
<Grid.Root className={height}>
    <Grid.Lines.All />
</Grid.Root>
<Grid.Root className="pb-8">
    <Grid.Lines.All />
    <Grid.Lines.Minimal className="lg:hidden" />

    <Grid.Single className="border-y border-surface-800/80 flex flex-col ">
        <div class="w-full grow bg-[url(/mesh/diagonal-tb.png)] bg-repeat opacity-50 h-12"></div>
    </Grid.Single>
    <Grid.Single>
        <div class="px-3">
            <p class="text-surface-500 font-mono text-xs translate-y-12">{label}</p>
        </div>
    </Grid.Single>
    <Grid.Single className="flex items-center "><div class="w-full h-px bg-surface-800/80"></div></Grid.Single>
    <Grid.Single className="max-lg:border-t h-8 border-surface-800/80 "><div></div></Grid.Single>
    
</Grid.Root>
<Grid.Root className="{height} ">
    <Grid.Lines.All />
    
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
</Grid.Root>

{:else if variant == "alt2"}
<Grid.Root className={height}>
    <Grid.Lines.All />
</Grid.Root>
<Grid.Root className="pb-8 ">
    <Grid.Lines.All />
    
    <Grid.Single className="flex items-center "><div></div></Grid.Single>
    <Grid.Single className="flex items-center "><div class="w-full h-px bg-surface-800/80"></div></Grid.Single>
    <Grid.Single className="max-lg:border-t h-8 border-surface-800/80"><div></div></Grid.Single>
    <Grid.Single className="border-y border-surface-800/80 flex flex-col ">
        <div class="w-full grow bg-[url(/mesh/diagonal-tb.png)] bg-repeat opacity-50 h-12"></div>
    </Grid.Single>

</Grid.Root>
<Grid.Root className="h-8 ">
    <Grid.Lines.All />
    
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
    <Grid.Single>
        <div class="px-3">
            <p class="text-surface-500 font-mono text-xs -translate-y-10">{label}</p>
        </div>
    </Grid.Single>
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
</Grid.Root>

{:else if variant == "alt3"}
<Grid.Root className=h-8>
    <Grid.Lines.All />
</Grid.Root>
<Grid.Root className="pb-8">
    <Grid.Lines.All />
    
    <Grid.Single className="flex items-end ">
        <div class="px-3">
            <p class="text-surface-500 font-mono text-xs -translate-y-8">{label}</p>
        </div>
    </Grid.Single>
    <Grid.Single className="flex items-center "><div class="w-full h-px bg-surface-800/80"></div></Grid.Single>
    <Grid.Single className="max-lg:border-t {height} border-surface-800/80"><div></div></Grid.Single>
    <Grid.Single className="border-t border-surface-800/80 flex flex-col "><div></div></Grid.Single>

</Grid.Root>
<Grid.Root className="{height} ">
    <Grid.Lines.All />
    
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
</Grid.Root>


{:else if variant == "breakout"}
<Grid.Root className="pb-8">
    <Grid.Lines.All />
    <Grid.Lines.Minimal className="lg:hidden" />

    <Grid.Single className="flex items-center "><div class="w-full h-px bg-surface-800/80"></div></Grid.Single>
    <Grid.Single className="max-lg:border-t border-surface-800/80">
        <div class="w-full flex items-center gap-3 group text-xs text-surface-500 font-mono pt-16" id="gallery">
            {#if label}
                <div class="bg-surface-800/80 h-px w-12"></div>
                <p>{label}</p>
            {/if}
            <div class="bg-surface-800/80 h-px grow"></div>
        </div>
    </Grid.Single>
    <Grid.Single className="flex items-center "><div></div></Grid.Single>
    <Grid.Single className="border-y border-surface-800/80 flex flex-col ">
        <div class="w-full grow bg-[url(/mesh/diagonal-tb.png)] bg-repeat opacity-50"></div>
    </Grid.Single>
</Grid.Root>
<Grid.Root className="{height} ">
    <Grid.Lines.Minimal />
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
</Grid.Root>
{/if}
</div>

<div class="lg:hidden">
    <Grid.Root>
        <Grid.Lines.Minimal />
        <Grid.Full className="border-t {height} border-surface-800/80">
            {#if label}
            <div class="w-full flex items-center gap-3 group text-xs text-surface-500 font-mono pt-16" id="gallery">
                <div class="bg-surface-800/80 h-px w-12"></div>
                <p>{label}</p>
                <div class="bg-surface-800/80 h-px grow"></div>
            </div>
            {/if}
        </Grid.Full>
    </Grid.Root>
</div>
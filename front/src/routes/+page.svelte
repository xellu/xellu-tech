<script lang="ts">
    import { goto } from "$app/navigation";
  
    import Button from "$lib/components/Button.svelte";
    import { Grid } from "$lib/components/Grid";
    import Icon from "$lib/components/Icon.svelte";
  import { Navbar } from "$lib/components/layout/Navbar";
</script>

<Grid.Root className="pt-8">
    <Grid.Lines.All />

    <Grid.Single className="max-lg:hidden font-mono text-surface-500 text-xs">
        <a href="#about" class="w-full flex items-center gap-3 group">
            <div class="bg-surface-800/80 h-px w-12"></div>
            <p>0x01</p>
            <div class="bg-surface-800/80 h-px w-3"></div>
            <p class="italic group-hover:underline">About Me</p>
            <div class="bg-surface-800/80 h-px grow"></div>
        </a>
    </Grid.Single>
    
    <Grid.Single>
        <div class="flex items-center justify-between gap-5 px-5">
            <Icon name="waving_hand" style="font-size: 3rem;" />
            <h2 class="text-2xl font-semibold lg:text-end">Hey!<br> I'm Xel</h2>
        </div>
    </Grid.Single>

    <Grid.Single className="max-lg:hidden font-mono text-xs text-surface-500 flex items-center gap-3">
        <a href="#gallery" class="w-full flex items-center gap-3 group">
            <div class="bg-surface-800/80 h-px w-12"></div>
            <p>0x03</p>
            <div class="bg-surface-800/80 h-px w-3"></div>
            <p class="italic group-hover:underline">Gallery</p>
            <div class="bg-surface-800/80 h-px grow"></div>
        </a>
    </Grid.Single>
    
    <Grid.Single className="max-lg:hidden font-mono text-xs text-surface-500 flex items-center gap-3">
        <button class="w-full flex items-center gap-3 group" onclick={() => {
            Navbar.setOpen(true);
            Navbar.highlight("socials")
        }}>
            <div class="bg-surface-800/80 h-px w-12"></div>
            <p>0x04</p>
            <div class="bg-surface-800/80 h-px w-3"></div>
            <p class="italic group-hover:underline">Socials</p>
            <div class="bg-surface-800/80 h-px grow"></div>
        </button>
    </Grid.Single>
</Grid.Root>

<Grid.Root className="max-lg:hidden pt-5 pb-8">
    <Grid.Lines.All />
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single className="font-mono text-surface-500 flex items-center gap-3">
        <button class="w-full flex items-center gap-3 group text-xs" onclick={() => { Navbar.navigateTo("My Work") }}>
            <div class="bg-surface-800/80 h-px w-12"></div>
            <p>0x02</p>
            <div class="bg-surface-800/80 h-px w-3"></div>
            <p class="italic group-hover:underline">My Work</p>
            <div class="bg-surface-800/80 h-px grow"></div>
        </button>
    </Grid.Single>
</Grid.Root>
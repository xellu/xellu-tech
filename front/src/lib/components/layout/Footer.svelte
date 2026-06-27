<script lang="ts">
    import { Socials } from "$lib/stores/Socials";
    
    import { Grid } from "../Grid";
    import Button from "../Button.svelte";
    import { Navbar } from "./Navbar";

    import { goto } from "$app/navigation";
</script>

<Grid.Root className="h-32">
    <Grid.Lines.All />
</Grid.Root>

<Grid.Root className="pb-8 max-lg:hidden">
    <Grid.Lines.All className="max-lg:hidden" />
    <Grid.Lines.Minimal className="lg:hidden" />

    <Grid.Single className="border-y border-surface-800/80 flex flex-col max-lg:hidden">
        <div class="w-full grow bg-[url(/mesh/diagonal-tb.png)] bg-repeat opacity-50 h-12"></div>
    </Grid.Single>
    <Grid.Single className="flex items-center max-lg:hidden"><div></div></Grid.Single>
    <Grid.Single className="flex items-center max-lg:hidden"><div class="w-full h-px bg-surface-800/80"></div></Grid.Single>
    <Grid.Single className="max-lg:border-t h-8 border-surface-800/80"><div></div></Grid.Single>
    
</Grid.Root>
<Grid.Root className="pb-24 max-lg:hidden">
    <Grid.Lines.All />
    
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single className="border-t border-surface-800/80"><div></div></Grid.Single>
</Grid.Root>

<Grid.Root className="pb-8" padding={true}>
    <Grid.Lines.All />
    <Grid.Single>
        <h2 class="h2 text-center">Xellu</h2>
    </Grid.Single>
    <Grid.Single className="flex flex-col gap-1 font-mono text-surface-200">
        <div class="flex gap-3 items-center mb-3 text-xs">
            <div class="h-px w-12 bg-surface-800/80"></div>
            <p class="font-mono text-surface-500">// Socials</p>
            <div class="h-px grow bg-surface-800/80"></div>
        </div>
        <a href="{Socials.github}" title="GitHub" class="hover:underline px-5" target="_blank">0x0A: Github</a>
        <a href="{Socials.discord}" title="Discord" class="hover:underline px-5" target="_blank">0x0B: Discord</a>
        <a href="{Socials.instagram}" title="Instagram" class="hover:underline px-5" target="_blank">0x0C: Instagram</a>
    </Grid.Single>
    <Grid.Single className="z-10 flex flex-col lg:pt-2">
        <Button
            label = "About Me" icon = "person"
            onclick = {() => { Navbar.navigateTo("About Me") }}
        />
        <Button
            label = "My Work" icon = "design_services" className="-mt-px"
            onclick = {() => { Navbar.navigateTo("My Work") }}
        />
        <Button
            label = "Services" icon = "apps" className="-mt-px"
            onclick = {() => { Navbar.navigateTo("Services") }}
        />
        
    </Grid.Single>
    <Grid.Single>
        <Button
            label = "Contact Me" icon = "chat_bubble"
            variant = "mesh" onclick={() => { goto('/contact') }}
        />        
    </Grid.Single>
</Grid.Root>
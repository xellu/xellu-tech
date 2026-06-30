<script lang="ts">
    import { Grid } from "$lib/components/Grid";
    import Button from "$lib/components/Button.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";
    import CommissionsForm from "$lib/components/layout/CommissionsForm.svelte";
    import Icon from "$lib/components/Icon.svelte";
    import Embed from "$lib/components/Embed.svelte";
</script>

<svelte:head>
    <Embed
        title = "Services | Xellu" route="/services"
    />
</svelte:head>

<Grid.Divider variant="breakout" height="h-0" />

<Grid.Root className="py-16">
    <Grid.Lines.Sides />
    <Grid.Single><div></div></Grid.Single>
    <Grid.DuoEx className="flex flex-col gap-3 items-center justify-center">
        <h2 class="h1">Services</h2>
    </Grid.DuoEx>
</Grid.Root>

<Grid.Divider variant="continue" height="h-8" />

<Grid.Root className="lg:py-16">
    <Grid.Lines.Sides className="max-lg:hidden" />
    <Grid.Lines.Minimal className="lg:hidden" />

    <Grid.Single className="flex flex-col items-center mt-16 p-8">
        <div>
            <h3 class="font-bold text-2xl">Commissions</h3>
            <p class="font-serif text-surface-50">Need work done on the Web, Backend, or just a UI Sketch?</p>
        </div>
    </Grid.Single>

    <CommissionsForm />
    
    <Grid.Single className="max-lg:hidden">
        <!-- <p class="px-3 pb-1 italic font-mono text-xs text-surface-300 flex items-center justify-between">
            <span>/* XelTekk Users</span>
            <span>*/</span>
        </p>
        <Button
            label="Log In" icon="login" variant="mesh"
            url = "https://xeltekk.com/login"
        />
        <div class="pt-4 px-3">
            <a href="#social" class="italic font-mono text-xs text-surface-300 hover:underline w-full">&UpArrow; What's this? Click to learn more.</a>
        </div> -->
        <div></div>
    </Grid.Single>
</Grid.Root>


<Grid.Divider variant="continue" height="h-8" />
<Grid.Root className="h-32"> <Grid.Lines.All /> </Grid.Root>
<Grid.Divider variant="continue" height="h-8" />

<!-- <Grid.Root>
    <Grid.Lines.Sides className="max-lg:hidden" />
    <Grid.Lines.Minimal className="lg:hidden" />

    <Grid.Single className="flex flex-col items-center mt-16 p-8">
        <div id="social">
            <h3 class="font-bold text-2xl">XelTekk</h3>
            <p class="font-serif text-surface-50">Everything in one place.</p>
        </div>
    </Grid.Single>
    <Grid.DuoEx className="flex flex-col items-center mt-16 p-8">
        <div class="flex items-center justify-evenly w-full gap-5 select-none">
            {#each ["home_storage", "music_cast", "forum", "person_text"] as name}
                <Icon {name} style="font-size: 48px;" /> 
            {/each}
        </div>
        
        <p class="mt-8 font-serif text-surface-50">
            Social platform with file storage, music streaming, forums, private chats, and personal about-me pages.
        </p>

        <div class="mt-8 flex gap-4 w-full">
            <Button
                label = "Try Today" icon = "chevron_right"
                url = "https://xeltekk.com/" variant="filled"
            />
            <Button
                label = "Log In" icon = "login"
                url = "https://xeltekk.com/login" variant="mesh"
            />
        </div>
    </Grid.DuoEx>
</Grid.Root>

<Grid.Divider variant="continue" height="h-8" /> -->


<Footer />
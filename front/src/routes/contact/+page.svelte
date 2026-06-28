<script lang="ts">
    import Button from "$lib/components/Button.svelte";
    import { Grid } from "$lib/components/Grid";
    import Mesh from "$lib/components/Mesh.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";

    import CommissionsForm from "$lib/components/layout/CommissionsForm.svelte";
    import ContactForm from "$lib/components/layout/ContactForm.svelte";

    import { onMount } from "svelte";
    import { slide } from "svelte/transition";

    let page: "commissions" | "contact" = $state("contact")

    onMount(() => {
        if (window.location.hash == "#commissions") {
            page = "commissions"
        }
    })
</script>

<Grid.Divider variant="continue" height="h-8" />

<Grid.Root>
    <Grid.Lines.Sides className="max-lg:hidden" />
    <Grid.Lines.Minimal className="lg:hidden" />

    <Grid.Single className="lg:-mt-8">
        <Button
            label = "Message Me" icon = "chat_bubble" variant={page == "contact" ? 'filled' : 'outlined'}
            onclick = {() => { page = "contact"}}
        />
        <Mesh className="h-10! max-lg:hidden"><div></div></Mesh>
        <Button
            label = "Commissions" icon = "design_services" variant={page == "commissions" ? 'filled' : 'outlined'} className="max-lg:-mt-px"
            onclick = {() => { page = "commissions"}}
        />
        <Mesh className="h-24! lg:hidden border-b border-surface-800/80 flex items-center justify-center">
            <p class="capitalize text-center bg-black border border-surface-800/80 {page == 'commissions' ? 'w-26' : 'w-18'} duration-150">{page}</p>
        </Mesh>
    </Grid.Single>
    <Grid.DuoEx className="w-full flex flex-col">
        {#if page == "commissions"}
            <div transition:slide>
                <CommissionsForm />
            </div>
        {:else}
            <div transition:slide>
                <ContactForm />
            </div>
        {/if}
    </Grid.DuoEx>
    <Grid.Single className="max-lg:hidden bg-[url(/landing/bridge1.jpg)] bg-cover bg-center opacity-25 ml-px"><div></div></Grid.Single>
</Grid.Root>

<Grid.Divider variant="continue-alt" height="h-8" />

<Footer />
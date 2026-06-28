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
    <Grid.Lines.Sides />

    <Grid.Single>
        <Button
            label = "Message Me" icon = "chat_bubble" variant={page == "contact" ? 'filled' : 'outlined'}
            onclick = {() => { page = "contact"}} className="mt-4"
        />
        <Mesh className="h-10!"><div></div></Mesh>
        <Button
            label = "Commissions" icon = "design_services" variant={page == "commissions" ? 'filled' : 'outlined'}
            onclick = {() => { page = "commissions"}}
        />
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
</Grid.Root>

<Grid.Divider variant="continue" height="h-8" />

<Footer />
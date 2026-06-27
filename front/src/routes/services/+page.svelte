<script lang="ts">
    import { Grid } from "$lib/components/Grid";
    import Button from "$lib/components/Button.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";
    import CommissionsForm from "$lib/components/layout/CommissionsForm.svelte";

    import { goto } from "$app/navigation";
</script>

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
        <p class="px-3 pb-1 italic font-mono text-xs text-surface-300">// User Section</p>
        <Button
            label="Log In" icon="login" variant="mesh"
            onclick={() => { goto("/panel") }}
        />
    </Grid.Single>
</Grid.Root>


<Grid.Divider variant="continue" height="h-8" />


<Footer />
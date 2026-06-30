<script lang="ts">
    import { Grid } from "$lib/components/Grid";
    import Footer from "$lib/components/layout/Footer.svelte";
</script>

<Grid.Divider variant="breakout" height="h-8" />
<Grid.Root>
    <Grid.Lines.Minimal />
    <Grid.Full className="flex items-center justify-center flex-col h-64 px-5">
        <h2 class="h2 text-7xl">Grid API</h2>
        <p class="lg:hidden font-mono text-sm text-surface-300">// Use desktop for a better experience</p>
    </Grid.Full>
</Grid.Root>
<Grid.Divider variant="continue" height="h-8" />
<Grid.Divider variant="alt1" label="Entanglement Hazard" />
<Grid.Divider variant="alt3" label="Keep clear of rotating drivelines. Switch off engine before performing service." />
<Grid.Divider variant="continue-alt" height="h-8" />
<Grid.Divider variant="alt2" label="Industrial Panels" />
<Footer />
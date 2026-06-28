<script lang="ts">
    import { page } from "$app/state";
  import Button from "$lib/components/Button.svelte";

    import { Grid } from "$lib/components/Grid";
    import Mesh from "$lib/components/Mesh.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";
</script>

<Grid.Divider variant="continue" height="h-8" />

<Grid.Root>
    <Grid.Lines.Minimal />
    <Grid.DuoEx className="flex items-center justify-center border-b border-surface-800/80 border-">
        <h2 class="text-9xl font-black text-error-500">{page.status}</h2>
    </Grid.DuoEx>
    <Grid.Single className="border-surface-800/80 border-l"><div></div></Grid.Single>
    <Grid.Single>
        <Mesh className="col-span-1 border-b border-l border-surface-800/80 h-16 lg:h-48 w-full flex justify-center items-center">
            <p class="border border-surface-800/80 lg:px-3 p-1 bg-black lg:font-extrabold lg:uppercase lg:text-lg max-lg:text-xs">{page.error?.message}</p>
        </Mesh>
    </Grid.Single>
    <Grid.Single className="border-l border-surface-800/80"><div></div></Grid.Single>
</Grid.Root>
<Grid.Root>
    <Grid.Lines.All />
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single>
        <Button
            label = "Go Home" icon="glyph:->" className="mt-16" url="/"
        />
    </Grid.Single>
</Grid.Root>

<Grid.Root className="h-64">
    <Grid.Lines.All />
</Grid.Root>

<Grid.Divider variant="alt2" height="h-0" />
<Grid.Divider variant="alt3" height="h-16" />

<Grid.Root className="grow">
    <Grid.Lines.All />
</Grid.Root>

<Footer />

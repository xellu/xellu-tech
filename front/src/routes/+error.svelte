<script lang="ts">
    import { page } from "$app/state";

    import { Grid } from "$lib/components/Grid";
    import Mesh from "$lib/components/Mesh.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";
</script>

<!-- <h2 class="text-2xl">{page.status}</h2>
<p>{page.error?.message}</p> -->

<div class="flex flex-col min-h-screen">
    <Grid.Root className="h-16">
        <Grid.Lines.All />
    </Grid.Root>

    <Grid.Root>
        <Grid.Lines.Minimal />
        <Grid.DuoEx className="flex items-center justify-center border-y border-surface-800/80">
            <h2 class="text-9xl font-black text-error-500">{page.status}</h2>
        </Grid.DuoEx>
        <Grid.Single>
            <Mesh className="col-span-1 border-y border-l border-surface-800/80 h-16 lg:h-48 w-full flex justify-center items-center">
                <p class="border border-surface-800/80 lg:px-3 p-1 bg-black lg:font-extrabold lg:uppercase lg:text-lg max-lg:text-xs">{page.error?.message}</p>
            </Mesh>
        </Grid.Single>
        <Grid.Single className="border-l border-surface-800/80"><div></div></Grid.Single>
    </Grid.Root>

    <Grid.Root className="h-64">
        <Grid.Lines.All />
    </Grid.Root>
    
    <Grid.Root className="h-16">
        <Grid.Lines.Minimal />
        <Grid.Full className="border-y border-surface-800/80">
            <!-- <Mesh direction="none" className="w-full h-16"><div></div></Mesh> -->
            <div></div>
        </Grid.Full>
    </Grid.Root>

    <Grid.Root className="grow">
        <Grid.Lines.All />
    </Grid.Root>

    <Footer />
</div>
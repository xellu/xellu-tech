<script lang="ts">
    import { Grid } from "$lib/components/Grid";
    import Button from "$lib/components/Button.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";

    import { Projects } from "$lib/stores/Bio";
</script>

<Grid.Divider variant="alt3" height="h-0" />
<Grid.Root>
    <Grid.Lines.Minimal />
    <Grid.Full className="flex items-center justify-center py-16">
        <h2 class="h1 text-3xl lg:text-5xl 2xl:text-9xl">My Work</h2>
    </Grid.Full>
</Grid.Root>
<Grid.Divider variant="continue" height="h-8" />

{#each Projects as p, index}
    <Grid.Root>
        <Grid.Lines.Sides />
        <Grid.Single className="px-5 min-h-16 lg:min-h-44 border-surface-800/80 {index > 0 ? 'border-t' : 'max-lg:border-t'}">
            <h3 class="text-xl font-bold pt-3">{p.project.name}</h3>
            <p class="text-sm text-surface-500">{p.date} &mdash; {p.until || 'Present'}</p>

            <div class="flex gap-1 flex-wrap mt-3 select-none">
                {#each p.project.tags as tag}
                    <span class="bg-primary-500 text-black px-1 text-xs font-mono">{tag}</span>
                {/each}
            </div>
        </Grid.Single>
        <Grid.DuoEx className="border-surface-800/80 {index > 0 ? 'lg:border-t' : ''}">
            <p class="font-serif text-lg p-5">
                {p.project.description}
            </p>
        </Grid.DuoEx>
        <Grid.Single className="flex flex-col {p.project.links.length == 0 ? 'border-y bg-[url(/mesh/diagonal-bt.png)] bg-repeat min-h-12 items-center justify-center' : 'mt-px'} border-surface-800/80">
            {#if p.project.links.length == 0}
                <p class="bg-black px-1 text-sm text-surface-500 border border-surface-800/80">No Links Available</p>
            {/if}
            
            {#each p.project.links as link}
                <Button
                    label={link.name} icon="open_in_new" className="-mt-px"
                    variant = {p.until ? 'outlined' : 'filled'} url={link.url}
                />    
            {/each}
        </Grid.Single>
    </Grid.Root>
{/each}

<Grid.Divider variant="continue" height="h-12" />

<Footer />
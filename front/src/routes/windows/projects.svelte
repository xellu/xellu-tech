<script>
    import { Projects, FeaturedProjects } from "$lib/projects";

    let page = "featured";
</script>

<div class="p-3 w-96">
    <div class="flex gap-3 mb-5">
        <button class="w-16 btn btn-sm {page == 'featured' ? 'variant-filled-primary': 'variant-outline-primary'}"
            on:click = {() => page = 'featured'}
        >Featured</button>
        <button class="w-16 btn btn-sm {page == 'all' ? 'variant-filled-primary': 'variant-outline-primary'}"
            on:click = {() => page = 'all'}
        >All [{Projects.length}]</button>
        
        
    </div>

    {#if page == 'featured'}
    <div class="flex flex-col gap-3 w-full">
        {#each FeaturedProjects as project}
            <div class="flex flex-col">
                <div class="flex gap-3 items-center justify-between">
                    <h4 class="h4 text-tertiary-500">{project.title}</h4>
                    <a href={project.url ? '#' : project.url} target="_blank" class="select-none text-lg {project.url ? 'text-secondary-500' : 'text-warning-500'} hover:underline">
                        [ {project.url ? 'View' : 'Not Available'} ]
                    </a>
                </div>
                <p>{project.description}</p>
                <div class="flex gap-2 flex-wrap select-none">
                    {#each project.tags as tag}
                        <span class="bg-primary-500/10 text-primary-500 px-2">{tag}</span>
                    {/each}
                </div>
            </div>
        {/each}
    </div>
    {:else}
    <div class="flex flex-col gap-3 w-full">
        {#each Projects as project}
            <div class="flex flex-col">
                <div class="flex gap-3 items-center justify-between">
                    <h4 class="h4 text-tertiary-500">{project.title}</h4>
                    <a href={project.url ? '#' : project.url} target="_blank" class="select-none text-lg {project.url ? 'text-secondary-500' : 'text-warning-500'} hover:underline">
                        [ {project.url ? 'View' : 'Not Available'} ]
                    </a>
                </div>
                <p>{project.description}</p>
                <div class="flex gap-2 flex-wrap select-none">
                    {#each project.tags as tag}
                        <span class="bg-primary-500/10 text-primary-500 px-2">{tag}</span>
                    {/each}
                </div>
            </div>
        {/each}
    </div>
    {/if}
</div>
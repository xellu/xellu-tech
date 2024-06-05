<script lang="ts">
    export let tasks: any = {}
</script>

<div class="p-3 max-w-72">
    <p class="text-secondary-500">Welcome to our team %user%! We're glad you've decided joined us</p>
    
    <p class="my-3">Your Tasks:</p>

    <div class="flex flex-col">
        {#each Object.keys(tasks) as task}
            <div class="{tasks[task].completed ? 'bg-primary-500/10': 'bg-warning-500/10'} px-1">
                <div class="flex gap-2 items-center">
                    {#if tasks[task].completed}
                        <span class="text-primary-500">[√]</span>
                        <p class="text-primary-500">{tasks[task].title}</p>
                    {:else}
                        <span class="text-warning-500">[ ]</span>
                        <p class="text-warning-500">{tasks[task].title}</p>
                    {/if}
                </div>
                <p class="text-sm">{tasks[task].description}</p>
            </div>
        {/each}
    </div>
</div>
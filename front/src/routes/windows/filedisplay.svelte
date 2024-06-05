<script lang="ts">
    export let content: string[] = [];
</script>

<div class="p-2 px-3 max-w-xl">
    {#if typeof(content) == "string"}
        <p>{@html content}</p>
    {:else}
    
        {#if content.length == 0}
            <p>Empty File</p>
        {/if}

        {#each content as item}
            {#if item == ""}
                <br>
            {:else}
                <p>{@html item}</p>
            {/if}    
        {/each}
    {/if}
</div>
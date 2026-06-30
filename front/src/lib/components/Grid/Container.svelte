<script lang="ts">
    import { onMount, type Snippet } from "svelte";

    let {
        className = "", padding = false, children
    }:
    {
        className?: string,
        padding?: boolean
        children: Snippet<[]>
    
    } = $props();
</script>

<div class="grid grid-cols-3 lg:grid-cols-6 relative max-lg:px-5 {className} {padding ? 'max-lg:gap-5' : ''}">
    
    <div class="col-span-1 max-lg:hidden"></div>
    
    {@render children()}

    <div class="col-span-1 max-lg:hidden"></div>
</div>
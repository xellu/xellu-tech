<script lang="ts">
    let { border = "dim", className = "" }: {border?: "dim" | "bright", className?: string} = $props();
</script>

<div class="absolute inset-0 grid grid-cols-3 lg:grid-cols-6 pointer-events-none -z-10 max-lg:mx-5 max-lg:border-x {border == 'dim' ? 'border-x-surface-800/80' : 'border-x-surface-700'} {className}">
    <div></div>
    <div class="w-px h-full {border == 'dim' ? 'bg-surface-800/80' : 'bg-surface-700'}"></div>
    <div class="w-px h-full {border == 'dim' ? 'bg-surface-800/80' : 'bg-surface-700'}"></div>
    <div class="w-px h-full opacity-0 max-lg:hidden"></div>
    <div class="w-px h-full {border == 'dim' ? 'bg-surface-800/80' : 'bg-surface-700'} max-lg:hidden"></div>
    <div class="w-px h-full {border == 'dim' ? 'bg-surface-800/80' : 'bg-surface-700'} max-lg:hidden"></div>
</div>
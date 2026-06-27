<script>
    let { children, className = "" } = $props();
</script>

<div class="max-lg:col-span-3 lg:col-span-4 {className}">
    {@render children()}
</div>
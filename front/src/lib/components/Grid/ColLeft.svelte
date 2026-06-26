<script>
    let { children, className = "" } = $props();
</script>

<div class="col-span-2 {className}">
    {@render children()}
</div>
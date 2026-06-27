<script>
    let { children, className = "" } = $props();
</script>

<div class="col-span-3 {className}">
    {@render children()}
</div>
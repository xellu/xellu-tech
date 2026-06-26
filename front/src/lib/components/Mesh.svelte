<script lang="ts">
    import type { Snippet } from "svelte";

    let {
        children,
        direction = "diagonal-bt",
        className = "",
        outline = false
    }: {direction?: "horizontal" | "vertical" | "diagonal-bt" | "diagonal-tb", className?: string, outline?: boolean, children: Snippet<[]> } = $props()
</script>

<div class="{outline ? 'p-[1.5px] ' + className : ''}">
    <div class="{outline ? '' : className} bg-repeat" style="background: url(/mesh/{direction}.png);">
        {@render children()}
    </div>
</div>
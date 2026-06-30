<script lang="ts">
    let { text, className }: {className?: string, text: string} = $props()
</script>

<span class="{className} font-mono">{text}</span>
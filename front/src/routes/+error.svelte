<script lang="ts">
    import { page } from "$app/stores";
</script>

<h1 class="text-7xl text-tertiary-500">{$page.status}</h1>
<p class="text-sm font-bold uppercase text-tertiary-500 opacity-50">{$page.error?.message}</p>
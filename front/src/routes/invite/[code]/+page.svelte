<script lang="ts">
    import { page } from "$app/stores";
    import { onMount } from "svelte";

    import Embed from "$lib/components/Embed.svelte";

    let code: string;
    
    onMount(() => {
        code = $page.params.code;
    })
</script>

<svelte:head>
    <title>You've been Invited to Xellu's Image Hosting</title>

    <Embed
        title = "Invite to Xellu's Image Hosting"
        description = "You've been invited to use Xellu's Private image hosting service, free of charge."
        route = "/invite/{code}"
    />
</svelte:head>

<div class="max-w-xs w-full">
    <h1 class="h3 font-bold">You've been Invited</h1>

    <p class="text-sm opacity-70 mt-5">
        You've been invited to use Xellu's Private image hosting service, free of charge.
    </p>

    <a href="/auth?invite={code}&ref=/panel">
        <button class="btn glass-success mt-10 w-full">
            Accept
        </button>
    </a>
</div>
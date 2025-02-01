<script lang="ts">
    export let title: string | null = null;
    export let description: string | null = null;
    export let icon: "default" | "custom" | "customLarge" | "none" = "default"
    export let iconUrl: string = "";
    export let route: string = "/";
    export let color: string = "#33A4F7";
</script>

<meta name="title" content="{title}" />

{#if title} <meta property="og:title" content="{title}" /> {/if}
{#if description} <meta property="og:description" content="{description}" /> {/if}

{#if icon == "default"}
    <meta property="og:image" content="/favicon.png" />

{:else if icon == "custom"}
    <meta property="og:image" content="{iconUrl}" />

{:else if icon == "customLarge"}
    <meta property="og:image" content="{iconUrl}" />
    <meta name="twitter:card" content="summary_large_image">
{/if}

<meta property="og:url" content="https://xellu.tech{route}" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="xellu.tech" />
<meta content="{color}" data-react-helmet="true" name="theme-color" />
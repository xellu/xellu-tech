<script lang="ts">
    import { onMount } from "svelte";

    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    
    import Loader from "$lib/components/Loader.svelte";
    import Embed from "$lib/components/Embed.svelte";
  
    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;

        if (!UserState.loggedIn && !UserState.loading) {
            window.location.href = "/auth?ref=/panel"
        }
    })

    let greeting: string;
    let loading: boolean = true;
    onMount(() => {
        const time = new Date().getHours();
        if (time >= 0 && time < 12) {
            greeting = "Good morning"
        } else if (time >= 12 && time < 18) {
            greeting = "Good afternoon"
        } else {
            greeting = "Good evening"
        }

        loading = false;
    })
</script>

<svelte:head>
    <title>Image Hosting | Xellu</title>
    <Embed
        title = "Xellu's Image Hosting"
        description = "Private & secure image hosting for only a select few."
        route = "/panel"
    />
</svelte:head>

{#if UserState.loading || !UserState.loggedIn || loading}
    <Loader />
{:else}
    <p>{greeting} {User?.username}</p>
{/if}
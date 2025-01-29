<script lang="ts">
    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    
    import Loader from "$lib/components/Loader.svelte";

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;

        if (!UserState.loggedIn && !UserState.loading) {
            window.location.href = "/auth"
        }
    })
</script>

{#if UserState.loading}
    <Loader />
{:else if !UserState.loggedIn}
    <Loader error="You are not logged in." />
{:else}
    <p>hello world</p>
{/if}
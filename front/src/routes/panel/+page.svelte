<script lang="ts">
    import { Account, type AccountType, AuthState, type AuthStateType } from "$lib/scripts/Auth";
    import { onMount } from "svelte";

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;

        if (!UserState.loggedIn && !UserState.loading) {
            window.location.href = "/auth?ref=" + window.location.pathname
        }
    })
    let greeting: string;

    onMount(() => {
        const time = new Date().getHours();
        if (time >= 0 && time < 12) {
            greeting = "Good morning"
        } else if (time >= 12 && time < 18) {
            greeting = "Good afternoon"
        } else {
            greeting = "Good evening"
        }
    })
</script>

<div class="w-full flex flex-col items-center justify-center mt-32 lg:mt-64 text-tertiary-500">
    <p class="font-bold uppercase">{greeting}, {User?.username}</p>

    <!-- mobile -->
    <div class="mt-32 mb-8 lg:hidden">
        <span class="material-symbols-outlined scale-[500%]">arrow_outward</span>
    </div>
    <p class="lg:hidden text-sm max-w-56 text-center opacity-50">Click on the Menu icon and select a service</p>

    <!-- desktop -->
    <div class="mt-32 mb-10 max-lg:hidden">
        <span class="material-symbols-outlined scale-[500%]">arrow_back</span>
    </div>
    <p class="max-lg:hidden text-sm text-center opacity-50">Select a service from a list of the left</p>

    
</div>
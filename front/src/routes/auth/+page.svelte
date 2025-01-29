<script lang="ts">
    import { Account, AuthState, LogIn, Register, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    import { TabGroup, Tab, TabAnchor } from '@skeletonlabs/skeleton';
  
    import { onMount } from "svelte";

    let ref: string = "/";
    let tab: "login" | "register" = "login";

    //--- auth

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;
    })

    onMount(() => {
        const search = new URLSearchParams(window.location.search);
        const qRef = search.get("ref");
        if (qRef && !qRef.startsWith("//")) {
            ref = qRef;
        }
    })
</script>

<div class="glass rounded-xl p-3">

</div>
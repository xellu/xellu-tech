<script lang="ts">
    import UcHeading from "$lib/components/UCHeading.svelte";
    
    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;
    })
</script>

<UcHeading>Coming Soon&trade;</UcHeading>
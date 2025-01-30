<script lang="ts">
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
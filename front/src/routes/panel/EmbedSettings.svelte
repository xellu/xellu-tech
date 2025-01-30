<script lang="ts">
    import ColorPicker from 'svelte-awesome-color-picker';

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

<ColorPicker
    --cp-bg-color="rgba(var(--color-surface-400)/0.2)"
    --cp-text-color="rgba(var(--color-surface-100))"
    --cp-border-color="transparent"
    --cp-button-hover-color="rgba(var(--color-surface-400)/0.2)"
    --cp-input-color="rgba(var(--color-surface-400)/0.2)"
    --focus-color="transparent"
    textInputModes={["hex", "rgb"]}
    isAlpha={false}
/>
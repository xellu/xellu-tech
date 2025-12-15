<script lang="ts">
    import UCHeading from "$lib/components/UCHeading.svelte";
  import ChangePassword from "$lib/components/misc/ChangePassword.svelte";
    import ChangeUsername from "$lib/components/misc/ChangeUsername.svelte";

    
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

    const buttonStates = {
        uuidCopied: false,
        changeUsername: false,
        changePassword: false,
    }

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

<ChangeUsername bind:open={buttonStates.changeUsername} />
<ChangePassword bind:open={buttonStates.changePassword} />


<div class="w-full">
    <UCHeading>{greeting}, {User?.username}</UCHeading>
    <div class="flex flex-col gap-1 glass rounded-xl p-3 mt-4 mb-5">

        <p class="uppercase font-bold text-xs">Username</p>
        <div class="flex items-center justify-between">
            <p class="font-mono glass p-1 w-48 rounded-lg overflow-hidden text-ellipsis whitespace-nowrap">{User?.username}</p>
            <button class="btn btn-sm glass-tertiary w-16"
                on:click={() => { buttonStates.changeUsername = true }}
            >Edit</button>
        </div>

        <p class="uppercase font-bold text-xs">UUID</p>
        <div class="flex items-center justify-between">
            <p class="font-mono glass p-1 w-48 rounded-lg overflow-hidden text-ellipsis whitespace-nowrap text-xs">{User?._id}</p>
            <button class="btn btn-sm glass-tertiary w-16"
                on:click={() => {
                    navigator.clipboard.writeText(User?._id || "");
                    buttonStates.uuidCopied = true;
                    setTimeout(() => {
                        buttonStates.uuidCopied = false;
                    }, 1000);
                }}
            >
                {buttonStates.uuidCopied ? '👍' : 'Copy'}
            </button>
        </div>

        <div class="mt-3">
            <button class="btn btn-sm glass-tertiary"
                    on:click={() => { buttonStates.changePassword = true }}
            >Change Password</button>
        </div>
        
    </div>
    
</div>
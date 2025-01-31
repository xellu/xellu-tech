<script lang="ts">
    import UcHeading from "$lib/components/UCHeading.svelte";
    import ChangeUsername from "../../lib/components/misc/ChangeUsername.svelte";
    import UploadBox from "$lib/components/misc/UploadBox.svelte";

    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;
    })

    const buttonStates = {
        uuidCopied: false,
        changeUsername: false
    }

    
</script>

<ChangeUsername bind:open={buttonStates.changeUsername} />

<UcHeading>My Account</UcHeading>
<div class="flex flex-col gap-1 glass rounded-xl p-3 mt-1 mb-5">

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
    
</div>

<UcHeading>Upload</UcHeading>
<UploadBox />

<UcHeading>Statistics</UcHeading>
<p>Uploads: {User?.uploads.files.length}</p>
<p>Storage Used: {(User?.uploads.storageUsed || 0)/1024}kb</p>
<script lang="ts">
    import UcHeading from "$lib/components/UCHeading.svelte";
    import ChangeUsername from "../../lib/components/misc/ChangeUsername.svelte";
    import UploadBox from "$lib/components/misc/UploadBox.svelte";

    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    import { toDataUnit } from "$lib/scripts/Utils";

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    let storageUsed: number = 0;

    Account.subscribe((value) => {
        User = value;

        if (value) {
            storageUsed = Math.round((value.uploads.storageUsed / value.uploads.storageMax) * 100);
        }
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
<div class="mb-5 mt-1"> <UploadBox /> </div>

<UcHeading>Storage</UcHeading>
<div class="flex flex-col mt-1">
    <div class="flex items-center justify-between">
        <p class="text-xs">
            {toDataUnit(User?.uploads.storageUsed || 0)} out of {toDataUnit(User?.uploads.storageMax || 0)} used
            to store {User?.uploads.files.length} {User?.uploads.files.length == 1 ? 'file' : 'files'}
        </p>

        <p class="font-mono text-sm {storageUsed > 60 ? storageUsed > 90 ? 'text-error-500' : 'text-warning-500' : 'text-primary-500'}">
            {storageUsed}%
        </p>
    </div>

    <div class="mt-3 bg-surface-400/20 rounded-full overflow-hidden w-full">
        <div class="h-1.5 rounded-full min-w-1.5 {storageUsed > 60 ? storageUsed > 90 ? 'bg-error-500' : 'bg-warning-500' : 'bg-primary-500'}"
            style="width: {storageUsed}%;"></div>
    </div>
</div>
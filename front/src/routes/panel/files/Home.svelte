<script lang="ts">
    import UcHeading from "$lib/components/UCHeading.svelte";
    import UploadBox from "$lib/components/misc/UploadBox.svelte";
    import Gallery from "./Gallery.svelte";

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

    
</script>


<UcHeading>Upload</UcHeading>
<div class="mb-5 mt-1"> <UploadBox /> </div>

<UcHeading>Storage</UcHeading>
<div class="flex flex-col mt-1 mb-5">
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

<!-- <UcHeading>Gallery</UcHeading>
<div class="mt-1">
    <Gallery />
</div> -->
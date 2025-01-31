<script lang="ts">
    import UcHeading from "$lib/components/UCHeading.svelte";

    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    
    import { getModalStore, getToastStore } from "@skeletonlabs/skeleton";
    import { fade, scale } from "svelte/transition";

    const modal = getModalStore();
    const toast = getToastStore();

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
        changeUsername: {
            open: false,
            loading: false,
            username: "",
            password: ""
        }
    }

    async function changeUsername() {
        const r = await fetch(`/api/v2/account/username`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: buttonStates.changeUsername.username,
                password: buttonStates.changeUsername.password
            })
        });

        buttonStates.changeUsername.password = "";

        if (r.ok) {
            buttonStates.changeUsername.username = "";
            
            toast.trigger({
                message: "Username changed successfully",
                background: "variant-soft-success"
            });
            buttonStates.changeUsername.open = false;
        } else {
            let data = await r.json();
            toast.trigger({
                message: data.error || "An error occurred",
                background: "variant-soft-error"
            });
        }

    }
</script>

{#if buttonStates.changeUsername.open}
<div class="fixed w-full h-screen bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 top-0 left-0" transition:fade>
    <div class="glass rounded-xl p-3 flex flex-col gap-3 md:max-w-sm md:w-full" transition:scale>
        <UcHeading>Change Username</UcHeading>

        <input type="text" class="glass-input" bind:value={buttonStates.changeUsername.username} placeholder="New Username" />
        <input type="password" class="glass-input" bind:value={buttonStates.changeUsername.password} placeholder="Password" />

        <div class="flex gap-3">
            <button
                class="btn btn-sm glass-tertiary"
                on:click={async () => {
                    buttonStates.changeUsername.loading = true;
                    try { await changeUsername() } catch (e) { console.error(e) }
                    buttonStates.changeUsername.loading = false;
                }}
                disabled={buttonStates.changeUsername.loading}
            >Change</button>
            
            <button class="btn btn-sm glass" on:click={() => {
                buttonStates.changeUsername.open = false    
                buttonStates.changeUsername.username = "";
            }}>Cancel</button>
        </div>
    </div>
</div>
{/if}

<UcHeading>My Account</UcHeading>
<div class="flex flex-col gap-1 glass rounded-xl p-3 mt-1 mb-5">

    <p class="uppercase font-bold text-xs">Username</p>
    <div class="flex items-center justify-between">
        <p class="font-mono glass p-1 w-48 rounded-lg overflow-hidden text-ellipsis whitespace-nowrap">{User?.username}</p>
        <button class="btn btn-sm glass-tertiary w-16"
            on:click={() => { buttonStates.changeUsername.open = true }}
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

<UcHeading>Statistics</UcHeading>
<p>Uploads: {User?.uploads.files.length}</p>
<p>Storage Used: {(User?.uploads.storageUsed || 0)/1024}kb</p>
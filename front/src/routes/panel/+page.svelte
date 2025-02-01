<script lang="ts">
    import { onMount } from "svelte";
    import { slide } from "svelte/transition";

    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    
    import Loader from "$lib/components/Loader.svelte";
    import Embed from "$lib/components/Embed.svelte";
    import UCHeading from "$lib/components/UCHeading.svelte";

    import Home from "./Home.svelte";
    import Chat from "./Chat.svelte";
    import Gallery from "./Gallery.svelte";

    import UploadSettings from "./UploadSettings.svelte";    
    import EmbedSettings from "./EmbedSettings.svelte";
    import AccountSettings from "./AccountSettings.svelte";

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;

        if (!UserState.loggedIn && !UserState.loading) {
            window.location.href = "/auth?ref=/panel"
        }
    })

    let greeting: string;
    let loading: boolean = true;
    onMount(() => {
        const time = new Date().getHours();
        if (time >= 0 && time < 12) {
            greeting = "Good morning"
        } else if (time >= 12 && time < 18) {
            greeting = "Good afternoon"
        } else {
            greeting = "Good evening"
        }

        loading = false;
    })

    const tabs: {label: string, icon: string, component: any}[] = [
        {
            label: "Home",
            icon: "home",
            component: Home
        },
        {
            label: "Chat",
            icon: "forum",
            component: Chat
        },
        {
            label: "Gallery",
            icon: "photo_library",
            component: Gallery
        },
        {
            label: "Uploading",
            icon: "cloud_upload",
            component: UploadSettings
        },
        {
            label: "Embed",
            icon: "colors",
            component: EmbedSettings
        },
        {
            label: "Account",
            icon: "person",
            component: AccountSettings
        }
    ]
    let activeTab: number = 0;

</script>

<svelte:head>
    <title>File Hosting | Xellu</title>
    <Embed
        title = "Xellu's File Hosting"
        description = "Private & secure file hosting for only a select few."
        route = "/panel"
    />
</svelte:head>

{#if UserState.loading || !UserState.loggedIn || loading}
    <Loader />
{:else}
    <UCHeading>{greeting}, {User?.username}</UCHeading>

    <div class="grid grid-cols-2 md:grid-cols-3 gap-2 my-3">
       {#each tabs as tab, i}
            <button class="btn btn-sm flex items-center justify-center {activeTab == i ? 'glass-tertiary text-tertiary-500' : 'glass'}" on:click={() => activeTab = i}>
                <span class="material-symbols-outlined">{tab.icon}</span>
                <span>{tab.label}</span>
            </button>
       {/each}
    </div>

    <div class="mt-5">
        {#each tabs as tab, i}
            {#if activeTab == i}
                <div transition:slide>
                    <svelte:component this={tabs[activeTab].component} />
                </div>
            {/if}
        {/each}
    </div>

{/if}
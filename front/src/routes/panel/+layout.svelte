<script lang="ts">
    import UCHeading from "$lib/components/UCHeading.svelte";
    import Embed from "$lib/components/Embed.svelte";
    import Loader from "$lib/components/Loader.svelte";

    
    import { Account, type AccountType, AuthState, type AuthStateType } from "$lib/scripts/Auth";
    import { goto } from "$app/navigation";
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

    let currentUrl: string | null = null;
    let navOpen: boolean = false;
    let greeting: string;

    const Links = [
        {
            url: "/panel/music",
            name: "Music",
            icon: "music_cast"
        },
        {
            url: "/panel/files",
            name: "Storage",
            icon: "folder_open"
        }
    ]

    onMount(() => {
        currentUrl = window.location.pathname;
        const time = new Date().getHours();
        if (time >= 0 && time < 12) {
            greeting = "Good morning";
        } else if (time >= 12 && time < 18) {
            greeting = "Good afternoon";
        } else {
            greeting = "Good evening";
        }
    })

    function setPage(url: string) {
        goto(url);
        currentUrl = url;
    }
</script>

<Embed
    title = "Xellu"
    description = ""
    route = "/"
/>

<button
    class="fixed top-5 right-5 z-50 flex items-center justify-center w-16 aspect-square btn glass-tertiary rounded-xl lg:hidden"
    on:click={() => {
        navOpen = !navOpen;            
    }}
>
    <span class="material-symbols-outlined scale-150">
        menu
    </span>
</button>

<div class="flex w-screen h-screen">
    <div class="p-3 rounded-xl w-1/6 min-w-56 flex flex-col gap-5 m-5 mr-0 max-lg:fixed max-lg:w-4/5 z-40 {navOpen ? 'max-lg:left-0 max-lg:opacity-100 max-lg:backdrop-blur-lg max-lg:bg-tertiary-500/10' : 'max-lg:-left-full max-lg:opacity-0 max-lg:scale-50'} duration-300">
        <div class="w-full glass p-3 rounded-xl">
            <UCHeading>{UserState.loading ? 'Welcome' : `${greeting}, ${User?.username}`}</UCHeading>
        </div>
        
        <div class="flex items-center -mb-3 gap-3 opacity-70">
            <p class="text-xs text-tertiary-500 font-bold uppercase">Services</p>
            <div class="flex-grow h-px bg-gradient-to-r from-tertiary-500/80 to-tertiary-500/0"></div>
        </div>
        <div class="flex flex-col gap-3">
            {#each Links as l}
                <button on:click={() => {
                    if (l.url == currentUrl) {
                        setPage('/panel');
                        return;
                    }

                    setPage(l.url)
                }} class="flex gap-1 justify-start items-center btn {l.url == currentUrl ? 'glass-tertiary' : 'glass text-tertiary-500'} rounded-xl">
                    <span class="material-symbols-outlined">{l.icon}</span>
                    <p>{l.name}</p>
                </button>
            {/each}
        </div>
    </div>
    <!-- <div class="lg:w-1/6"></div> -->
    <div class="w-full max-h-screen overflow-y-scroll p-5 {UserState.loading ? 'flex items-center justify-center h-screen' : ''}">
        {#if UserState.loading}
            <Loader />
        {:else}
            <slot></slot>
        {/if}
    </div>
</div>
<script lang="ts">
    import { onMount } from "svelte";
    import { slide } from "svelte/transition";
    import { getToastStore } from "@skeletonlabs/skeleton";

    import { Account, AuthState, LogIn, Register, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    
    import Loader from "$lib/components/Loader.svelte";

    const toast = getToastStore();

    let ref: string = "/";
    let page: string = "login"

    const form = {
        username: "",
        password: "",
        
        //only for register
        inviteCode: "",
    }

    //--- auth

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;

        if (value.loggedIn) {
            onSuccess();
        }
    })

    onMount(() => {
        const search = new URLSearchParams(window.location.search);
        const qRef = search.get("ref");
        if (qRef && !qRef.startsWith("//")) {
            ref = qRef;
        }
    })

    function resolve(res: AuthStateType) {
        if (!res.loggedIn) {
            return toast.trigger({
                message: res.error || "Unknown error",
                background: "variant-soft-warning",
            })
        }
    }

    function onSuccess() {
        toast.trigger({
            message: `Welcome, ${User?.username}`,
            background: "variant-soft-success",
        })
        window.location.href = ref;
    }


</script>

<div class="w-full flex items-center justify-center">
    <div class="glass rounded-xl p-3 flex flex-col max-w-xs w-full">
        <h2 class="uppercase font-bold text-tertiary-500 font-heading-token">{page}</h2>
        
        <input type="text" placeholder="Username" bind:value={form.username} class="glass-input mt-3" />
        <input type="password" placeholder="Password" bind:value={form.password} class="glass-input mt-1" />
    
        {#if page == "register"}
            <div transition:slide class="w-full">
                <input type="text" placeholder="Invite Code" bind:value={form.inviteCode} class="glass-input w-full mt-3" />    

                <button class="btn variant-soft-tertiary mt-5 flex items-center justify-center gap-3 w-full" disabled={UserState.loading}
                    on:click={async () => {
                        let res = await Register(form.username, form.password, form.inviteCode);
                        resolve(res);
                    }}
                >
                    {#if UserState.loading}
                        <Loader center={false} scale="sm" variant="tertiary" />
                    {/if}

                    Sign Up
                </button>
            </div>

        {:else}
            <button class="btn variant-soft-tertiary mt-5 flex items-center justify-center gap-3"
                disabled={UserState.loading}
                transition:slide
                on:click={async () => {
                    let res = await LogIn(form.username, form.password);
                    resolve(res);
                }}
            >
                {#if UserState.loading}
                    <Loader center={false} scale="sm" variant="tertiary" />
                {/if}

                Log In
            </button>
        {/if}

        <button
            class="text-left mt-3 opacity-50 text-xs uppercase font-bold"
            on:click={() => {
                page = page == "login" ? "register" : "login";
            }}
            >
            {page == "login" ? "Don't have an account?" : "Already have an account?"}
        </button>
    
    
    </div>
</div>
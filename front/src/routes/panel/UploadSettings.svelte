<script lang="ts">
    import UcHeading from "$lib/components/UCHeading.svelte";
    import UploadBox from "$lib/components/misc/UploadBox.svelte";
    import Loader from "$lib/components/Loader.svelte";

    import { onMount } from "svelte";
    import { getModalStore, getToastStore, SlideToggle } from "@skeletonlabs/skeleton";

    import { Account, AuthState, PushSettings, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    import { constructDomain } from "$lib/scripts/Utils";

    const toast = getToastStore();
    const modal = getModalStore();

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    let availableDomains: string[] = [];
    const settings = {
        subDomain: "",
        domain: "",
        rawUrl: false
    }

    const colors = {
        bg: "#313338",
        embedBg: "#2b2d31",
        url: "#00aafc"
    }

    Account.subscribe((value) => {
        User = value;

        if (value) {
            settings.subDomain = value.settings.subDomain;
            settings.domain = value.settings.domain;
            settings.rawUrl = value.settings.rawUrl;
        }
    })

    AuthState.subscribe((value) => {
        UserState = value;
    })

    const buttonStates = {
        regenKey: false,
    }

    
    onMount(async () => {
        const r = await fetch("/api/v2/config/available-domains");
        const data = await r.json();
        
        availableDomains = data.domains;
    })

    async function updateConfig(options: {[key: string]: any}) {
        const r = await PushSettings(options);
        if (r.ok) { return console.debug("Config Updated") }
            
        toast.trigger({
            message: r.error?.message || "An error occurred",
            background: "variant-soft-error",
            action: {
                label: "Retry",
                response: () => updateConfig(options)
            }
        })
    }

    async function regenKey(confirm?: boolean | null) {
        buttonStates.regenKey = false;

        if (confirm === null) {
            return modal.trigger({
                title: "Are you sure?",
                body: `You're about to re-generate your API Key. This will invalidate the current one, and You'll need to update it in your configurations.`,
                
                modalClasses: "glass-warning",
                type: "confirm",

                buttonTextCancel: "No",
                buttonTextConfirm: "Yes",
                response(r) {
                    regenKey(r);
                },
            })
        }
        if (!confirm) { return }

        buttonStates.regenKey = true;

        try {
            const r = await fetch("/api/v2/config/regenerate", { method: "POST" });
            buttonStates.regenKey = false;

            if (r.ok) { return toast.trigger({ message: "API Key Regenerated", background: "variant-soft-success" }) }
            
            const data = await r.json();
            toast.trigger({
                message: data.error?.message || "An error occurred",
                background: "variant-soft-error",
                action: {
                    label: "Retry",
                    response: () => regenKey(confirm)
                }
            })
        } catch (err: any) {
            toast.trigger({
                message: err.message || "An error occurred",
                background: "variant-soft-error",
                action: {
                    label: "Retry",
                    response: () => regenKey(confirm)
                }
            })
            buttonStates.regenKey = false;
        }
    }
</script>


<UcHeading>Upload</UcHeading>
<div class="mb-5 mt-1"> <UploadBox /> </div>

<UcHeading>Authentication</UcHeading>
<div class="glass rounded-xl p-3 mt-1 mb-5">
    <div class="flex items-center justify-between">
        <p class="glass font-mono p-1 px-2 rounded-lg"> ********************* </p>
        <button
            class="btn btn-sm glass-error flex items-center justify-center w-24 h-8"
            disabled={buttonStates.regenKey}
            on:click={() => {
                regenKey(null);
            }}
        >
            {#if buttonStates.regenKey}
                <Loader scale="sm" variant="error" />
            {:else}
                Regenerate
            {/if}
        </button>
    </div>

    <div class="flex gap-3 flex-wrap mt-3">
        <a href="/api/v2/config/download/sharex" target="_blank">
            <button class="btn btn-sm glass-tertiary">ShareX Config</button>
        </a>
    </div>
</div>

<UcHeading>Domain</UcHeading>
<div class="mt-1 mb-5 flex flex-col gap-2">
    <div class="flex gap-1 w-full">
        <input
            type="text" placeholder="Subdomain"
            class="glass-input max-w-40"
            bind:value={settings.subDomain}
            on:change={() => updateConfig({ subDomain: settings.subDomain })}
        >

        <span class="mt-2">.</span>

        <select name="Domain" placeholder="Domain" class="glass-input flex-grow" on:change={() => updateConfig({ domain: settings.domain })}>
            {#each availableDomains as domain}
                <option value={domain}>{domain}</option>
            {/each}
        </select>
    </div>

    <SlideToggle
        name="Raw URL"
        size="sm"
        
        bind:checked={settings.rawUrl}
        on:change={() => { updateConfig({rawUrl: settings.rawUrl}) }}

        background="glass"
        active="glass-tertiary"
        rounded="rounded-lg"
    >
        <span class="text-sm uppercase font-bold opacity-80">Use Raw URLs</span>
    </SlideToggle>
</div>

<UcHeading>Preview</UcHeading>

<div class="p-3 rounded-xl mt-1" style="background-color: {colors.bg};">
    <div class="flex items-start gap-3 select-none">
        <img src="/favicon.png" alt="" class="w-12 rounded-full" draggable="false">
        <div class="overflow-hidden">
            <p class="capitalize font-bold">{User?.username}</p>
            <p class="hover:underline cursor-pointer text-ellipsis overflow-hidden" style="color: {colors.url}">
                {#if User?.settings.rawUrl} https://{constructDomain(User?.settings.domain || "xellu.tech", User?.settings.subDomain)}/api/v2/files/3335e4fe8342478aa94f2ab0692cdf00-An1iO7WZ.png
                {:else} https://{constructDomain(User?.settings.domain || "xellu.tech", User?.settings.subDomain)}/upload/An1iO7WZ {/if}
            </p>
        
        </div>
    </div>
    
</div>
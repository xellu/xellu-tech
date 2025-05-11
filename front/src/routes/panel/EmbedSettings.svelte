<script lang="ts">
    import ColorPicker from 'svelte-awesome-color-picker';

    import { SlideToggle } from '@skeletonlabs/skeleton';
    import { slide } from 'svelte/transition';
    import { getToastStore } from '@skeletonlabs/skeleton';

    import { Account, AuthState, PushSettings, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    import { constructDomain } from '$lib/scripts/Utils';

    import UcHeading from '$lib/components/UCHeading.svelte';

    const toast = getToastStore();
    const settings = {
        enabled: false,
        rawUrl: false,

        color: "#000000",
        title: "",
        description: "",
        siteName: ""
    }

    const colors = {
        bg: "#313338",
        embedBg: "#2b2d31",
        url: "#00aafc"
    }

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
        
        if (value) {
            settings.enabled = value.settings.embeds.enabled

            settings.title = value.settings.embeds.title
            settings.description = value.settings.embeds.description
            settings.siteName = value.settings.embeds.siteName
            settings.color = value.settings.embeds.color.toString() //if its a hex for some reason

            settings.rawUrl = value.settings.rawUrl
        }
    })

    AuthState.subscribe((value) => {
        UserState = value;
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
</script>

<div class="flex flex-col">
    <div class="mb-5 flex flex-col gap-2">
        <SlideToggle
            name="Enable Embeds"
            size="sm"
            
            bind:checked={settings.enabled}
            on:change={() => { updateConfig({'embeds.enabled': settings.enabled}) }}

            background="glass"
            active="glass-tertiary"
            rounded="rounded-lg"
        >
            <span class="text-sm uppercase font-bold opacity-80">Allow Embedding</span>
        </SlideToggle>

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

    {#if settings.enabled}
    <div transition:slide>
        <UcHeading>Style</UcHeading>

        <div class="glass rounded-xl p-3 mt-1 flex flex-col gap-3 mb-5">
            <div class="flex items-center gap-3">
                <input
                    type="text" class="glass-input w-2/3 min-w-32"
                    placeholder="Title" bind:value={settings.title}
                    on:change={() => { updateConfig({'embeds.title': settings.title}) }}
                />
                <input
                    type="text" class="glass-input w-12 flex-grow"
                    placeholder="Site Name" bind:value={settings.siteName}
                    on:change={() => { updateConfig({'embeds.siteName': settings.siteName}) }}
                />
            </div>
            <input
                type="text" class="glass-input"
                placeholder="Description" bind:value={settings.description}
                on:change={() => { updateConfig({'embeds.description': settings.description}) }}    
            />
            
            
            <ColorPicker
                --cp-bg-color="transparent"
                --cp-text-color="rgba(var(--color-surface-100))"
                --cp-border-color="transparent"
                --cp-button-hover-color="rgba(var(--color-surface-900)/0.2)"
                --cp-input-color="rgba(var(--color-surface-900)/0.2)"
                --focus-color="transparent"
                
                textInputModes={["hex"]}
                isAlpha={false}

                bind:hex={settings.color}
                on:input={() => {
                    const color = settings.color;
                    setTimeout(() => {
                        if (color === settings.color) {
                            updateConfig({'embeds.color': settings.color})
                        }
                    }, 1000);
                }}
            />
        </div>
    </div>
    {/if}

    <UcHeading>Preview</UcHeading>
    <div class="p-3 rounded-xl mt-1" style="background-color: {colors.bg};">
        <div class="flex items-start gap-3 select-none">
            <img src="/favicon.png" alt="" class="w-12 rounded-full" draggable="false">
            <div>
                <p class="capitalize font-bold">{User?.username}</p>
                {#if !settings.rawUrl} <p class="hover:underline cursor-pointer" style="color: {colors.url}">https://{constructDomain(User?.settings.domain || "xellu.xyz", User?.settings.subDomain)}/upload/An1iO7WZ</p> {/if}

                {#if settings.enabled && !settings.rawUrl}
                <div class="flex rounded overflow-hidden shadow-md">
                    <div class="min-h-32 min-w-1" style="background-color: {settings.color};"></div>
                    <div class="flex flex-col gap-1 p-3 min-w-52 text-surface-200" style="background-color: {colors.embedBg};">
                        {#if settings.siteName} <p class="text-xs">{settings.siteName}</p> {/if}
                        {#if settings.title} <p class="font-bold hover:underline cursor-pointer" style="color: {colors.url};">{settings.title}</p> {/if}
                        {#if settings.description} <p class="text-sm">{settings.description}</p> {/if}

                        <img src="/splash.png" alt="" class="rounded" draggable="false">
                    </div>
                </div>
                {:else}
                    <img
                        src="/splash.png" alt="" draggable="false"
                        class="rounded shadow-sm" 
                        title="{settings.rawUrl ? 'https://xellu.xyz/api/v2/files/7461595e95f347b6bccbb8e10b3760cf-An1iO7WZ.png' : 'https://xellu.xyz/upload/An1iO7WZ'}"
                    >
                {/if}
            </div>
        </div>
        
    </div>


</div>

<div>

</div>
<script lang="ts">
    import ColorPicker from 'svelte-awesome-color-picker';
    import { SlideToggle } from '@skeletonlabs/skeleton';
    import { slide } from 'svelte/transition';

    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";

    import UcHeading from '$lib/components/UCHeading.svelte';

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;
    })

    const settings = {
        enabled: false,

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
</script>

<div class="flex flex-col">
    <div class="mb-5">
        <SlideToggle
            name="Enabled"
            size="sm"
            
            bind:checked={settings.enabled}

            background="glass"
            active="glass-tertiary"
            rounded="rounded-lg"
        >
            <span class="text-sm uppercase font-bold opacity-80">Use Embedding</span>
        </SlideToggle>
    </div>

    <UcHeading>Style</UcHeading>

    <div class="glass rounded-xl p-3 mt-1 flex flex-col gap-3 mb-5" transition:slide>
        <div class="flex items-center gap-3">
            <input type="text" class="glass-input w-2/3 min-w-32" placeholder="Title" bind:value={settings.title} />
            <input type="text" class="glass-input w-12 flex-grow" placeholder="Site Name" bind:value={settings.siteName} />
        </div>
        <input type="text" class="glass-input" placeholder="Description" bind:value={settings.description} />
        
        
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
        />
    </div>

    <UcHeading>Preview</UcHeading>
    <div class="p-3 rounded-xl mt-1" style="background-color: {colors.bg};">
        <div class="flex items-start gap-3 select-none">
            <img src="/favicon.png" alt="" class="w-12 rounded-full" draggable="false">
            <div>
                <p class="capitalize font-bold">{User?.username}</p>
                <p class="hover:underline cursor-pointer" style="color: {colors.url}">https://xellu.tech/upload/An1iO7WZ</p>

                {#if settings.enabled}
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
                    <img src="/splash.png" alt="" class="rounded shadow-sm" draggable="false">
                {/if}
            </div>
        </div>
        
    </div>


</div>

<div>

</div>
<script lang="ts">
    import Icon from "./Icon.svelte";
    import { Navbar } from "./layout/Navbar";


    let {
        onclick = () => {},
        url = undefined,
        variant = "outlined",
        className = "",

        label = "",
        icon = null,

        disabled = false,
    }: {
        onclick?: Function,
        url?: string,
        variant?: "outlined" | "filled" | "mesh",
        className?: string,

        label?: string,
        icon?: string | null,
        disabled?: boolean
    } = $props();
</script>

{#if url} <a href="{url}" title={label} class="absolute -top-full sr-only">{label}</a> {/if}

<button
    onclick={() => {
        if (disabled) return;

        if (url) { Navbar.navigateTo(url) }
        onclick()
    }}
    disabled = {disabled}
    class="group max-lg:w-full lg:w-[calc(100%+1px)] {disabled ? 'opacity-70 cursor-not-allowed' : 'opacity-100'} {className}"
>    
    <div class="w-full h-12 {variant == 'filled' ? 'group-hover:bg-surface-700' : 'group-hover:bg-primary-500'} duration-150"></div>
    <div class="flex items-center {label == '' || icon == null ? 'justify-center' : 'justify-between px-4'} gap-5 w-full h-12 -mt-12 {disabled ? '' : 'group-hover:translate-x-2 group-hover:-translate-y-2 group-hover:shadow-2xl'} border duration-150 delay-75
        {variant == "outlined" ? 'border-surface-800/80 bg-surface-950' : ''}
        {variant == "filled" ? 'border-surface-800/80 bg-primary-500 text-black' : ''}
        {variant == 'mesh' ? 'border-surface-800/80 bg-[url(/mesh/diagonal-bt.png)] bg-repeat bg-surface-950/80 backdrop-blur-2xl duration-150' : ''}
    ">
        {#if label} <p class="font-semibold {variant == 'mesh' ? 'bg-black group-hover:bg-surface-800 duration-150 px-2 border border-surface-700' : ''}">{label}</p> {/if}
        {#if icon} <Icon name={icon} className={variant == 'mesh' ? 'bg-black group-hover:bg-surface-800 duration-150 p-1 border border-surface-700' : ''} /> {/if}
    </div>
</button>
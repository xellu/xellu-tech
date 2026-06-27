<script lang="ts">
  import Icon from "./Icon.svelte";



    let {
        onclick = () => {},
        variant = "outlined",
        className = "",

        label = "Button",
        icon = null,
    }: {
        onclick?: Function,
        variant?: "outlined" | "filled" | "mesh",
        className?: string,

        label?: string,
        icon?: string | null
    } = $props();
</script>

<button onclick={() => {onclick()}} class="group w-[calc(100%+1px)]">
    <div class="w-full h-12 {variant == 'filled' ? 'group-hover:bg-surface-700' : 'group-hover:bg-primary-500'} duration-150"></div>
    <div class="flex items-center {label == '' || icon == null ? 'justify-center' : 'justify-between px-4'} gap-5 w-full h-12 -mt-12 group-hover:translate-x-2 group-hover:-translate-y-2 group-hover:shadow-2xl border duration-150 delay-75 {className}
        {variant == "outlined" ? 'border-surface-800/80 bg-surface-950' : ''}
        {variant == "filled" ? 'border-surface-800/80 bg-primary-500 text-black' : ''}
        {variant == 'mesh' ? 'border-surface-800/80 bg-[url(/mesh/diagonal-bt.png)] bg-repeat bg-surface-950/80 backdrop-blur-2xl duration-150' : ''}
    ">
        {#if label} <p class="font-semibold {variant == 'mesh' ? 'bg-black group-hover:bg-surface-800 duration-150 px-2 border border-surface-700' : ''}">{label}</p> {/if}
        {#if icon} <Icon name={icon} className={variant == 'mesh' ? 'bg-black group-hover:bg-surface-800 duration-150 p-1 border border-surface-700' : ''} /> {/if}
    </div>
</button>
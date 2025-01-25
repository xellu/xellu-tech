<script lang="ts">
    export let onClick: any = () => {};
</script>

<button
    on:click={onClick}
    class="group uppercase text-sm font-bold flex items-center gap-3 hover:text-tertiary-500 duration-300"
>    
    <span class="group-hover:underline"><slot/></span>
    <span class="material-symbols-outlined mr-5 group-hover:mr-0 group-hover:ml-5 duration-300">arrow_right_alt</span>
</button>
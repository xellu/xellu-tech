<script lang="ts">
    import { slide } from "svelte/transition";
    
    import { Grid } from "../Grid";
    import Select from "../Select.svelte";
  import Button from "../Button.svelte";
    
    let form = $state({
        name: "",
        email: "",
        service: "",
        customService: null,
        budget: "",
        content: ""
    })
</script>

<Grid.DuoEx className="p-3 lg:p-8">
    <div id="commissions">
        <span class="text-xs text-surface-50 font-semibold mb-1">I go by...</span>
        <input type="text" class="input" placeholder="John Doe" bind:value={form.name}>

        <div class="h-5"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">My email is...</span>
        <input type="email" class="input" placeholder="j.doe@example.com" bind:value={form.email}>

        <div class="h-10"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">I need...</span>
        <Select placeholder="Select a service" bind:value={form.service} items={[
            {label: "Frontend/Web Development", value: "frontend"},
            {label: "Backend Development", value: "backend"},
            {label: "Fullstack Development", value: "fullstack"},
            {label: "UI Design", value: "ui"},
            {label: "Something else", value: "other"},
        ]} />
        {#if form.service == "other"}
        <div transition:slide>
            <div class="h-3"></div>
            <div class="flex">
                <input type="text" class="input" placeholder="What exactly?" bind:value={form.customService}>
            </div>
        </div>
        {/if}

        <div class="h-5"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">My budget is roughly...</span>
        <div class="flex">
            <div class="ig-cell preset-filled-surface-200-800 border border-surface-800">EUR</div>
            <input type="number" class="input" placeholder="100" bind:value={form.budget}>
        </div>

        <div class="h-10"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">To be specific...</span>
        <div class="flex">
            <textarea class="textarea min-h-24" placeholder="I want to build a..." rows={5} bind:value={form.content}></textarea>
        </div>

        <div class="flex justify-end">
            <Button
                label = "Send Inquiry" icon="send" className="mt-5 lg:w-1/2!" variant="filled"
            />
        </div>
    </div>
</Grid.DuoEx>


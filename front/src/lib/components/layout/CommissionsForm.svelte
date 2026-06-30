<script lang="ts">
    import { slide } from "svelte/transition";
    
    import { Grid } from "../Grid";
    import Select from "../Select.svelte";
    import Button from "../Button.svelte";
    import { toaster } from "$lib/stores/Toaster";
    
    let form = $state({
        name: "",
        email: "",
        service: "",
        customService: null,
        budget: "",
        content: ""
    })

    let showErrors: boolean = $state(false);
    let disabled: boolean = $state(false);

    async function send() {
        showErrors = true;
        if (!form.name || !form.email || !form.content || !form.email.includes(".") || !form.email.includes("@") || !form.budget || !form.service || (form.service == "other" && !form.customService)) { return }

        disabled = true;
        try {
            const r = await fetch("/api/v3/commissions", {
                method: "POST",
                body: JSON.stringify({
                    name: form.name,
                    email: form.email,
                    service: form.service,
                    customService: form.customService,
                    budget: parseInt(form.budget),
                    content: form.content
                })
            })
            disabled = false;

            if (r.ok) {
                form = {
                    name: "",
                    email: "",
                    service: "",
                    customService: null,
                    budget: "",
                    content: ""
                }
                showErrors = false;
                return toaster.success({
                    title: "Inquiry sent!"
                })
            }

            if (r.status <= 500) {
                let data = await r.json();
                toaster.error({
                    title: "Request Error",
                    description: data.error || "Unknown Error"
                })
            } else {
                toaster.error({title: "Request Error", description: r.statusText})
            }
        } catch (e) {
            toaster.error({
                title: "Network Error",
                description: `${e}`
            })
            disabled = false;
        }
        disabled = false;
    }
</script>

<Grid.DuoEx className="p-3 lg:p-8">
    <div id="commissions">
        <span class="text-xs text-surface-50 font-semibold mb-1">I go by...</span>
        <input type="text" class="input" placeholder="John Doe" bind:value={form.name}>
        {#if showErrors && form.name.length == 0} <div in:slide> <span class="text-xs text-error-500">Please provide a name</span> </div> {/if}
        {#if form.name.length > 64} <div in:slide> <span class="text-xs text-error-500">Name too long</span> </div> {/if}

        <div class="h-5"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">My email is...</span>
        <input type="email" class="input" placeholder="j.doe@example.com" bind:value={form.email}>
        {#if showErrors && form.email.length == 0} <div in:slide> <span class="text-xs text-error-500">Please provide your email</span> </div> {/if}
        {#if showErrors && (!form.email.includes("@") || !form.email.includes(".")) && form.email.length > 0} <div in:slide> <span class="text-xs text-error-500">Incorrect email format</span> </div> {/if}
        {#if form.email.length > 128} <div in:slide> <span class="text-xs text-error-500">Email too long</span> </div> {/if}

        <div class="h-10"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">I need...</span>
        <Select placeholder="Select a service" bind:value={form.service} items={[
            {label: "Frontend/Web Development", value: "frontend"},
            {label: "Backend Development", value: "backend"},
            {label: "Fullstack Development", value: "fullstack"},
            {label: "UI Design", value: "ui"},
            {label: "Something else", value: "other"},
        ]} />
        {#if showErrors && !form.service} <div in:slide> <span class="text-xs text-error-500">Please select a service</span> </div> {/if}
        {#if form.service == "other"}
        <div transition:slide>
            <div class="h-3"></div>
            <div class="flex">
                <input type="text" class="input" placeholder="What exactly?" bind:value={form.customService}>
            </div>
        </div>
        {#if showErrors && !form.customService} <div in:slide> <span class="text-xs text-error-500">What do you want me to do?</span> </div> {/if}
        {/if}

        <div class="h-5"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">My budget is roughly...</span>
        <div class="flex">
            <div class="ig-cell preset-filled-surface-200-800 border border-surface-800">EUR</div>
            <input type="number" class="input" placeholder="100" bind:value={form.budget}>
        </div>
        {#if showErrors && (!form.budget || isNaN(parseInt(form.budget)))} <div in:slide> <span class="text-xs text-error-500">Please provide a budget</span> </div> {/if}
        {#if showErrors && parseInt(form.budget) <= 0} <div in:slide> <span class="text-xs text-error-500">I don't work for free</span> </div> {/if}


        <div class="h-10"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">To be specific...</span>
        <div class="flex">
            <textarea class="textarea min-h-24" placeholder="I want to build a..." rows={5} bind:value={form.content}></textarea>
        </div>
        {#if showErrors && form.content.length == 0} <div in:slide> <span class="text-xs text-error-500">Please provide a message</span> </div> {/if}
        {#if form.content.length > 1024} <div in:slide> <span class="text-xs text-error-500">Message too long</span> </div> {/if}


        <div class="flex justify-end">
            <Button
                label = "Send Inquiry" icon="send" className="mt-5 lg:w-1/2!" variant="filled"
                onclick={send} {disabled}
            />
        </div>
    </div>
</Grid.DuoEx>


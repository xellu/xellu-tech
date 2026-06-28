<script lang="ts">    
    import { Grid } from "../Grid";
    import Button from "../Button.svelte";
    
    let form = $state({
        name: "",
        email: "",
        content: ""
    })
</script>

<!-- TODO: connect to api -->

<Grid.DuoEx className="p-3 lg:p-8">
    <div id="commissions">
        <span class="text-xs text-surface-50 font-semibold mb-1">Your Name</span>
        <input type="text" class="input" placeholder="John Doe" bind:value={form.name}>

        <div class="h-5"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">Email</span>
        <input type="email" class="input" placeholder="j.doe@example.com" bind:value={form.email}>

        <div class="h-10"></div>

        <span class="text-xs text-surface-50 font-semibold mb-1">Message</span>
        <div class="flex">
            <textarea class="textarea min-h-24" rows={5} bind:value={form.content}></textarea>
        </div>

        <div class="flex justify-end">
            <Button
                label = "Send Message" icon="send" className="mt-5 lg:w-1/2!" variant="filled"
            />
        </div>
    </div>
</Grid.DuoEx>


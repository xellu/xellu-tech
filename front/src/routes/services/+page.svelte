<script lang="ts">
    import { Grid } from "$lib/components/Grid";
    import Button from "$lib/components/Button.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";

    import { goto } from "$app/navigation";

    // let 
</script>

<Grid.Divider variant="breakout" height="h-0" />

<Grid.Root className="py-16">
    <Grid.Lines.Sides />
    <Grid.Single><div></div></Grid.Single>
    <Grid.DuoEx className="flex flex-col gap-3 items-center justify-center">
        <h2 class="h1">Services</h2>
    </Grid.DuoEx>
</Grid.Root>

<Grid.Divider variant="continue" height="h-8" />

<Grid.Root className="lg:py-16">
    <Grid.Lines.Sides />
    <Grid.Single className="flex flex-col items-center justify-center p-8">
        <div>
            <h3 class="font-bold text-2xl">Commissions</h3>
            <p class="font-serif text-surface-50">Need work done on the Web, Backend, or just a UI Sketch?</p>
        </div>
    </Grid.Single>
    <Grid.DuoEx className="p-8">
        <div>
            <span class="text-xs font-serif">Your Name</span>
            <input type="text" class="input" placeholder="John Doe">

            <div class="h-5"></div>

            <span class="text-xs font-serif">What do you need to be done?</span>
            <select name="commissionType" class="select">
                <option>Frontend/Web Development</option>
                <option>Backend Development</option>
                <option>Fullstack Development</option>
                <option>UI Design</option>
                <option>UI Sketch</option>
            </select>
            
            <div class="h-5"></div>

            <span class="text-xs font-serif">Budget</span>
            <input type="text" class="input" placeholder="100-200 EUR">

            
        </div>
    </Grid.DuoEx>
    <Grid.Single className="max-lg:hidden">
        <p class="px-3 pb-1 italic font-mono text-xs text-surface-300">// User Section</p>
        <Button
            label="Log In" icon="login" variant="mesh"
            onclick={() => { goto("/panel") }}
        />
    </Grid.Single>
</Grid.Root>

<Grid.Divider variant="continue" height="h-8" />


<Footer />
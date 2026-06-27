<script lang="ts">
    import { goto } from "$app/navigation";
  
    import Button from "$lib/components/Button.svelte";
    import { Grid } from "$lib/components/Grid";
  import Icon from "$lib/components/Icon.svelte";
</script>

<Grid.Root className="pt-16">
    <Grid.Lines.All />

    <Grid.DuoEx>
        <div class="flex items-center gap-5 px-5">
            <Icon name="waving_hand" style="font-size: 5rem;" />
            <h2 class="lg:text-2xl font-semibold">What's up!<br> I'm Xel</h2>
        </div>
    </Grid.DuoEx>
    <Grid.DuoEx>
        <p>Hello World!</p>
    </Grid.DuoEx>
</Grid.Root>
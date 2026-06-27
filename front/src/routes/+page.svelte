<script lang="ts">
    import { goto } from "$app/navigation";
  
    import Button from "$lib/components/Button.svelte";
    import { Grid } from "$lib/components/Grid";
    import Icon from "$lib/components/Icon.svelte";
  import { Navbar } from "$lib/components/layout/Navbar";
  import Mesh from "$lib/components/Mesh.svelte";
</script>

<!-- Quick Links -->
<Grid.Root className="pt-8">
    <Grid.Lines.All />

    <Grid.Single className="max-lg:hidden font-mono text-surface-500 text-xs">
        <a href="#about" class="w-full flex items-center gap-3 group">
            <div class="bg-surface-800/80 h-px w-12"></div>
            <p>0x01</p>
            <div class="bg-surface-800/80 h-px w-3"></div>
            <p class="italic group-hover:underline">About Me</p>
            <div class="bg-surface-800/80 h-px grow"></div>
        </a>
    </Grid.Single>
    
    <Grid.Single>
        <div class="flex items-center justify-between gap-5 px-5">
            <Icon name="waving_hand" style="font-size: 3rem;" />
            <h2 class="text-2xl font-semibold lg:text-end">Hey!<br> I'm Xel</h2>
        </div>
    </Grid.Single>

    <Grid.Single className="max-lg:hidden font-mono text-xs text-surface-500 flex items-center gap-3">
        <a href="#gallery" class="w-full flex items-center gap-3 group">
            <div class="bg-surface-800/80 h-px w-12"></div>
            <p>0x03</p>
            <div class="bg-surface-800/80 h-px w-3"></div>
            <p class="italic group-hover:underline">Gallery</p>
            <div class="bg-surface-800/80 h-px grow"></div>
        </a>
    </Grid.Single>
    
    <Grid.Single className="max-lg:hidden font-mono text-xs text-surface-500 flex items-center gap-3">
        <button class="w-full flex items-center gap-3 group" onclick={() => {
            Navbar.setOpen(true);
            Navbar.highlight("socials")
        }}>
            <div class="bg-surface-800/80 h-px w-12"></div>
            <p>0x04</p>
            <div class="bg-surface-800/80 h-px w-3"></div>
            <p class="italic group-hover:underline">Socials</p>
            <div class="bg-surface-800/80 h-px grow"></div>
        </button>
    </Grid.Single>
</Grid.Root>

<Grid.Root className="max-lg:hidden pt-5 pb-8">
    <Grid.Lines.All />
    <Grid.Single><div></div></Grid.Single>
    <Grid.Single className="font-mono text-surface-500 flex items-center gap-3">
        <button class="w-full flex items-center gap-3 group text-xs" onclick={() => { Navbar.navigateTo("My Work") }}>
            <div class="bg-surface-800/80 h-px w-12"></div>
            <p>0x02</p>
            <div class="bg-surface-800/80 h-px w-3"></div>
            <p class="italic group-hover:underline">My Work</p>
            <div class="bg-surface-800/80 h-px grow"></div>
        </button>
    </Grid.Single>
</Grid.Root>

<!-- About Me -->
<Grid.Root>
    <Grid.Lines.All className="max-lg:hidden" />
    <Grid.Lines.Minimal className="lg:hidden" />

    <Grid.Single className="flex flex-col gap-3 max-lg:border-t border-surface-800/80">
        <div class="w-full flex items-center gap-3 group text-xs text-surface-500 font-mono pt-16" id="about">
            <div class="bg-surface-800/80 h-px grow"></div>
            <p>// About Me</p>
            <div class="bg-surface-800/80 h-px w-12"></div>
        </div>

    </Grid.Single>

    <Grid.Single className="max-lg:hidden border-b border-surface-800/80"><div></div></Grid.Single>

    <Grid.Single  className="max-lg:hidden border-y border-l border-surface-800/80 flex flex-col">
        <div class="w-full grow bg-[url(/landing/pole2.jpg)] bg-center bg-cover opacity-10"></div>
    </Grid.Single>
    
    <Grid.Single className="max-lg:hidden border-y border-surface-800/80">
        <Mesh className="w-full h-24 opacity-50"><div></div></Mesh>
    </Grid.Single>
</Grid.Root>

<Grid.Root>
    <Grid.Lines.Minimal />

    <Grid.Single className="pt-5 -mr-px border-r border-surface-800/80">
        <div class="border-y border-surface-800/80">
            <Mesh className="w-full p-5" direction="diagonal-tb">
                <div class="p-1.5 bg-black border border-surface-700"><img src="/landing/avatar.jpg" alt="" class="w-full select-none" draggable="false"></div>
            </Mesh>
        </div>
    </Grid.Single>
    <Grid.DuoEx className="p-5 flex flex-col justify-between">
        <p class="font-serif text-surface-50 lg:pt-5">
            Hey, I'm <span class="text-white">Xel</span>! <br>
            I've been coding since 2019, starting with Python, since then I took up web development and UI design around 2022, and I've been doing fullstack ever since then.
            <br><br>

            Fast-forward to now, and I'm freelancing and making a <a href="https://github.com/xellu/nautica-api" target="_blank" class="hover:underline font-bold text-white">backend development platform</a>.
            I've also taken up photography, you can check my pics in <a href="#gallery" class="hover:underline text-white font-bold">the gallery</a> below.
            <br><br>
            

            With that being said, I'm always looking for any opportunities to work on interesting projects, to learn new things and collaborations. So if you need something done, hit me up!
        </p>
        <div class="flex gap-5 mt-5 max-2xl:flex-col">
            <Button label="My Work" icon="design_services" variant="mesh" onclick={() => { Navbar.navigateTo("My Work") }} />
            <Button label="Message Me" icon="chat_bubble" onclick={() => { goto("/contact") }} />
            
        </div>
    </Grid.DuoEx>
    <Grid.Single className="lg:border-l border-surface-800/80 flex flex-col">
        <div class="w-full grow bg-[url(/landing/bus-snowstorm.jpg)] bg-center bg-cover opacity-25"></div>
    </Grid.Single>
</Grid.Root>

<Grid.Root> <Grid.Full className="border-t border-surface-800/80"><div></div></Grid.Full> </Grid.Root>

<div class="h-screen"></div>
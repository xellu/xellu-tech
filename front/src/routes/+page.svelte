<script lang="ts">
    import Highlighed from "$lib/components/highlighed.svelte";
    import Separator from "$lib/components/separator.svelte";

    import { instagram, github, discord, email } from "$lib/socials";
    import { projects } from "$lib/projects";

    let  active: string = "about";
    let intervals: any[] = []

    function onMove(event: MouseEvent) {
        let circle = document.getElementById("circle");
        if (!circle) return;
        
        let x = event.clientX - (circle.clientWidth / 2);
        let y = event.clientY - (circle.clientHeight / 2);
    
        if (x < 0) x = 0;
        if (y < 0) y = 0;
        if (x + circle.clientWidth > window.innerWidth) x = window.innerWidth - circle.clientWidth;
        if (y + circle.clientHeight > window.innerHeight) y = window.innerHeight - circle.clientHeight;

        circle.style.left = x + "px";
        circle.style.top = y + "px";
    }

</script>

<style lang="postcss">
    p a {
        @apply font-semibold;
        @apply text-surface-50;
    }

    p a:hover {
        @apply underline;
    }

</style>

<head>
    <title>Xellu</title>
</head>
<div id="circle" class="max-lg:hidden absolute w-[300px] h-[300px] -top-[500px] left-1/2 rounded-full bg-primary-500/10 duration-150"></div>

<div class="flex flex-wrap max-md:flex-col lg:justify-between lg:gap-32 z-10 backdrop-blur-3xl" on:mousemove={onMove}>
    <!-- left side -->
    <div class="min-w-64 lg:w-1/5 lg:flex-grow flex flex-col lg:justify-between xl:items-end p-10 xl:pt-32 lg:min-h-screen gap-10">
        <!-- top -->
        <div class="max-w-96">
            <h1 class="h1 text-7xl text-primary-500 font-bold">
                <Highlighed>Xellu</Highlighed>
            </h1>
            <p class="text-lg">Full-Stack Developer</p>
            <p class="mt-5 text-surface-50 max-w-80">
                👋 Hello! I'm a <Highlighed>developer</Highlighed> from Czechia,
                Living in Siberia, Russia. 
            </p>

            <div class="flex flex-col gap-2 mt-16 max-lg:hidden">
                <a href="#about" class="flex items-center gap-3 group" on:click={() => active = "about"}>
                    <div class="h-px bg-white {active == "about" ? 'w-24' : 'w-8 group-hover:w-24'} group-hover:bg-tertiary-500 duration-300"></div>
                    <span class="group-hover:text-tertiary-500 duration-300">About Me</span>
                </a>

                <a href="#projects" class="flex items-center gap-3 group" on:click={() => active = "projects"}>
                    <div class="h-px bg-white {active == "projects" ? 'w-24' : 'w-8 group-hover:w-24'} group-hover:bg-tertiary-500 duration-300"></div>
                    <span class="group-hover:text-tertiary-500 duration-300">Projects</span>
                </a>

                <a href="#contact" class="flex items-center gap-3 group" on:click={() => active = "contact"}>
                    <div class="h-px bg-white {active == "contact" ? 'w-24' : 'w-8 group-hover:w-24'} group-hover:bg-tertiary-500 duration-300"></div>
                    <span class="group-hover:text-tertiary-500 duration-300">Contact</span>
                </a>

                
            </div>
        </div>

        <!-- bottom -->
        <div class="flex items-center xl:justify-center gap-5">
            <a href={instagram} target="_blank" rel="noopener noreferrer" draggable="false" class="opacity-50 hover:opacity-100 duration-200">
                <img src="/instagram.png" alt="instagram" class="h-8" draggable="false" />
            </a>
            <a href={github} target="_blank" rel="noopener noreferrer" draggable="false" class="opacity-50 hover:opacity-100 duration-200">
                <img src="/github.png" alt="github" class="h-8" draggable="false" />
            </a>
            <a href={discord} target="_blank" rel="noopener noreferrer" draggable="false" class="opacity-50 hover:opacity-100 duration-200">
                <img src="/discord.png" alt="discord" class="h-8" draggable="false" />
            </a>
        </div>

    </div>

    <!-- right side -->
    <div class="min-w-64 lg:w-1/3 flex-grow flex flex-col gap-3 xl:h-screen items-start p-10 xl:pt-32 overflow-y-scroll scroll-smooth">

        <div class="w-full xl:w-3/5">
            <Separator> <span id="about">About Me</span> </Separator>
            <p class="text-surface-200">
                <!-- how i started -->
                In 2019, I tried coding in Python, and I liked it. I started learning web development around 2022, and I've been doing it since then.
                I also worked on the backend side of things, using Python and Node.js.

                <br><br>
                <!-- what i do now -->
                Nowadays, I'm working on my projects, and also Freelancing. I'm also learning new tech and improving my skills.
                Lately, I've been working on a <a href="https://limeade.cool/" target="_blank">game marketplace</a> with a few of my friends.

                <br><br>

                <!-- what i want to do -->
                I'm looking for any opportunities to work on interesting projects, and to learn new things. I'm also open to collaborations.
                <br><br>
                If you want work with me, or just chat, hit me up on <a href={discord} target="_blank">Discord</a>.
            </p>

            <div class="h-5"></div>
            <Separator> <span id="projects">My Projects</span> </Separator>
            <div class="flex flex-col gap-3">
                {#each projects as project}
                    <div class="group hover:bg-surface-300/5 p-5 rounded-xl duration-300 border-t border-t-white/0 hover:border-t-white/10">
                        <div class="flex justify-between">
                            <h2 class="text-lg font-semibold group-hover:text-tertiary-500 duration-300">{project.name}</h2>

                            <p class="text-sm uppercase font-semibold text-surface-300">{project.date.replaceAll("-", "—")}</p>
                        </div>
                        <p class="text-surface-200 w-4/5 mt-3">{project.description}</p>

                        {#if project.links.length > 0}
                        <div class="flex gap-3 flex-wrap my-5">
                            {#each project.links as link}
                                <a href="{link.url}" target="_blank" class="flex gap-2 items-center opacity-75 hover:opacity-100 duration-150">
                                    <img src="/link.png" alt="{link.name}" class="h-5" />
                                    <span>{link.name}</span>
                                </a>
                            {/each}
                        </div>
                        {/if}

                        <div class="flex gap-3 flex-wrap mt-5">
                            {#each project.tags as tag}
                                <span class="chip variant-soft-tertiary">{tag}</span>
                            {/each}
                        </div>
                    </div>
                {/each}
            </div>

            <div class="h-5"></div>
            <Separator> <span id="contact">Get in Touch</span> </Separator>

            <p class="text-surface-200">
                If you want to work with me, or just chat, feel free to reach out to me on <a href={discord} target="_blank">Discord</a>, or send me an <a href={email} target="_blank">email</a>.
            </p>

            <div class="mt-32">
                <p class="text-surface-200 text-sm">
                    Written in <a href="https://vscode.dev/" target="_blank">Visual Studio Code</a>.
                    Built with <a href="https://svelte.dev/" target="_blank">SvelteKit</a>, <a href="https://tailwindcss.com/" target="_blank">Tailwind CSS</a>, and <a href="https://skeleton.dev/" target="_blank">Skeleton</a>.
                    Deployed on <a href="https://cloud.oracle.com/" target="_blank">Oracle Cloud Infrastructure</a>.
                    Inspired by <a href="https://brittanychiang.com/" target="_blank">Brittany Chiang</a>.
                </p>
            </div>


        </div>

    </div>
</div>
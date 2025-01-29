<script lang="ts">
    import Separator from "$lib/components/Separator.svelte";

    import { projectTimeline } from "$lib/projects";
    import { discord, email } from "$lib/socials";
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

<div>
    <Separator> <span id="about">About Me</span> </Separator>
    <p class="text-surface-200 pl-3">
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

    <!-- my projects -->
    <Separator> <span id="projects">My Projects</span> </Separator>
    <div class="flex flex-col">
        {#each projectTimeline as entry, i}
            <div class="flex gap-3 group">
                <!-- timeline -->
                <div class="flex flex-col gap-1 items-center justify-center max-sm:w-1/4 w-56">
                    <div class="w-px min-h-5 flex-grow {i == 0 ? 'bg-gradient-to-t from-white/50 via-transparent to-transparent' : 'bg-white/50'}"></div>
                    <div class="max-md:text-center font-heading-token">
                        <p class="text-sm font-black uppercase group-hover:text-tertiary-500 duration-300">{entry.until ? `From ${entry.date}` : entry.date}</p>
                        {#if entry.until}
                            <p class="text-xs font-bold uppercase opacity-50 group-hover:text-tertiary-500 duration-300">To {entry.until}</p>
                        {/if}
                    </div>
                    <div class="w-px min-h-5 flex-grow {i == projectTimeline.length-1 ? 'bg-gradient-to-b from-white/50 via-transparent to-transparent': 'bg-white/50'}"></div>
                </div>

                <!-- project card -->
                <div class="p-3 rounded-xl w-full my-3 glass-group flex flex-col">
                    <h2 class="text-lg font-semibold group-hover:text-tertiary-500 duration-300 font-heading-token">{entry.project.name}</h2>
                    <p class="text-surface-200 w-4/5 mt-3 text-sm mb-5">{entry.project.description}</p>

                    {#if entry.project.links.length > 0}
                    <div class="flex gap-3 flex-wrap mb-3">
                        {#each entry.project.links as link}
                            <a href="{link.url}" target="_blank" class="flex gap-2 items-center opacity-70 hover:opacity-100 hover:text-primary-400 duration-150 text-xs uppercase font-bold">
                                <span class="material-symbols-outlined text-sm">open_in_new</span>
                                <span>{link.name}</span>
                            </a>
                        {/each}
                    </div>
                    {/if}

                    <div class="flex gap-3 flex-wrap">
                        {#each entry.project.tags as tag}
                            <span class="chip variant-soft-tertiary">{tag}</span>
                        {/each}
                    </div>
                </div>
            </div>
        {/each}
    </div>
    <div class="h-5"></div>

    <!-- contact info -->
    <Separator> <span id="contact">Get in Touch</span> </Separator>

    <p class="text-surface-200">
        If you want to work with me, or just chat, feel free to <a href={discord} target="_blank">reach out to me on Discord</a>, or <a href={email} target="_blank">send me an email</a>.
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
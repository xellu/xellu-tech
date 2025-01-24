<script lang="ts">
    import Separator from "$lib/components/separator.svelte";

    import { discord } from "$lib/socials";
</script>

<div>
    <Separator> <span id="about">About Me</span> </Separator>

    <p class="text-surface-200 pl-3 h-56 transparent-gradient-mask select-none">
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

    <a href="#bio" class="flex items-center gap-3 duration-300 group hover:gap-10 hover:text-tertiary-500 -mt-4 w-full z-30 p-3">
        <p class="group-hover:underline">More About Me</p>
        <span class="material-symbols-outlined">trending_flat</span>
    </a>

    <div class="h-5"></div>
</div>
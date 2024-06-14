<script lang="ts">
    import Highlighed from "$lib/components/highlighed.svelte";
    import Separator from "$lib/components/separator.svelte";

</script>

<head>
    <title>iohue</title>
</head>

<div class="w-screen flex items-center justify-center py-56 p-5">
    <div class="p-5 card max-w-xl w-full">
        
        <!-- profile -->
        <header class="h-56 flex flex-col items-center justify-center gap-5 w-full">
            <div class="flex items-center justify-center gap-10">
                <img src="/favicon.png" alt="profile icon" class="w-28 rounded-full">
                <div class="flex flex-col gap-3 items-center">
                    <p>👋 Hello! My name is</p>
                    <h1 class="h1 font-bold text-secondary-500">
                        Iohue
                    </h1>
                </div>
            </div>

            <div class="flex items-center justify-center gap-3">
                <p>s</p>
                <p>o</p>
                <p>c</p>
                <p>i</p>
                <p>a</p>
                <p>l</p>
                <p>s</p>
            </div>
        </header>

        <!-- about me -->
        <Separator>About Me</Separator>
        <!-- some text -->
        <p class="px-5">
            I'm a <Highlighed>Full-Stack</Highlighed> Developer with a passion for creating
            <Highlighed from="from-tertiary-500" to="to-tertiary-600">beautiful</Highlighed> and
            <Highlighed from="from-error-500" to="to-error-600">functional</Highlighed> applications.
        </p>


    </div>
</div>
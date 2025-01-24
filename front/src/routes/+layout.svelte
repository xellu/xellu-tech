<script lang="ts">
    import "../app.pcss"

    import { onMount } from "svelte";
    import { getToastStore, initializeStores, Toast } from "@skeletonlabs/skeleton";

    import { AutoAuthenticate, AuthLogger } from '$lib/scripts/Auth';

    initializeStores();



    const toast = getToastStore();

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

    onMount(async () => {
        document.body.addEventListener("mousemove", onMove);

        let auth = await AutoAuthenticate();

        auth.state.loggedIn ? AuthLogger.ok(`Successfully authenticated (${auth.state.auto})`) : AuthLogger.warn(`Unable to authenticate: ${auth.state.error}`);
        if (auth.state.error && !auth.state.loggedIn) { //show error message
            toast.trigger({
                message: auth.state.error,
                background: "variant-glass-warning",
            })
        }
    })


</script>

<Toast />

<div id="circle"
    class="max-lg:hidden absolute w-[400px] h-[400px] -top-[500px] left-1/2 rounded-full -z-20 duration-150"
    style="background: radial-gradient(circle, rgba(var(--color-primary-500) / 0.2) 0%, rgba(var(--color-primary-500) / 0) 70%)"
></div>

<div class="backdrop-blur-md">
    <slot></slot>   
</div>

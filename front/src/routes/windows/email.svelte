<script lang="ts">
    import { notify } from "$lib/notifications";
</script>

<div class="h-96 flex">
    <div class="flex flex-col w-44 bg-primary-900/5 h-96 gap-2">
        <p class="px-2">Contacts</p>
        <button class="btn btn-sm variant-soft-secondary m-2">
            <p class="text-left w-full">Xel Lu</p>
        </button>

        <div class="flex-grow"></div>
        <div class="bg-primary-900/5 p-2">
            <p>Welcome %user%</p>
        </div>
    </div>

    <div class="w-96 flex-grow p-3 flex flex-col">
        <h4 class="h4">Message</h4>
        <textarea class="textarea variant-soft-primary outline-none border-none resize-none p-1 px-2" rows="5"></textarea>
    
        <h4 class="h4 mt-5">Your E-Mail</h4>
        <input type="email" class="variant-soft-primary input p-1 px-2 outline-none border-none">
        
        <div class="flex-grow"></div>

        <button class="btn variant-soft-secondary" on:click={() => notify("Guess what? OUT OF ORDER! Now get this, IM. TOO. LAZY. TO. MAKE. AN. API. So yea just send it to me@xello.blue", "error", 10000)}>Send -&gt</button>
    </div>

</div>
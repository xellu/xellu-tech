<script lang="ts">
    import { notify } from "$lib/notifications";
    import { onMount, onDestroy } from "svelte";
    import { contacts } from "$lib/contacts";

    let selectedContact: any = null
    
    export let inbox: any[] = []
    let selectedMessage: any = null

    let message: string = ""
    let email: string = ""
    function reset() {
        message = ""
        email = ""  
    }

    let page = "inbox"
</script>

<div class="h-96 flex">
    <div class="flex flex-col w-44 bg-primary-900/5 h-96 gap-2">
        <p class="px-2">Contacts</p>
        {#each contacts as contact}
            <button class="btn btn-sm {selectedContact == contact ? 'variant-soft-secondary' : 'variant-soft-primary'} mx-2" on:click={() => { 
                if (selectedContact != contact) {
                    selectedContact = contact
                    page = "write"
                    reset()
                } else {
                    selectedContact = null
                    page = "inbox"
                }
             }}>
                <div class="flex gap-2 items-center justify-start w-full">
                    <div class="w-2 h-2 {contact.online ? 'bg-success-500' : 'bg-error-500'}" title="{contact.online ? 'online' : 'offline'}"></div>
                    <p class="text-left">{contact.name}</p>
                </div>
            </button>
        {/each}

        <div class="flex-grow"></div>
        <div class="bg-primary-900/20 p-2">
            <p>Welcome %user%</p>
        </div>
    </div>

    <div class="w-96 flex-grow p-3 flex flex-col overflow-y-scroll">
        {#if page == "write"}
            <h4 class="h4">Message {selectedContact.name}</h4>
            <textarea class="textarea variant-soft-primary outline-none border-none resize-none p-1 px-2" rows="5" bind:value={message}></textarea>
        
            {#if selectedContact == contacts[0]}
                <h4 class="h4 mt-5">Your E-Mail</h4>
                <input type="email" class="variant-soft-primary input p-1 px-2 outline-none border-none" bind:value={email}>
                <p class="text-sm">This contact form is working, and not related to the story</p>
            {/if}

            <div class="flex-grow"></div>

            <button class="btn variant-soft-secondary" on:click={() => {
                selectedContact.send()
                reset()
            }}>Send -&gt</button>
        {:else if page == "inbox"}
            {#if inbox.length == 0}
                <p>No mail here! You're caught up!</p>
            {:else}
                <h4 class="h4">Inbox</h4>
            {/if}
            
            <div class="flex flex-col-reverse">
            {#each inbox as mail}
                <button class="m-1 p-2 bg-primary-500/10" on:click={() => {
                    selectedMessage = mail
                    page = "message"
                    mail.unread = false
                }}>
                    <h6 class="h6 w-full text-left text-secondary-500">{#if mail.unread}<span class="animate-text-flashing">NEW</span>{/if} {mail.title}</h6>
                    <p class="w-full text-left">From {mail.author.name}</p>
                </button>
            {/each}
            </div>
        {:else if page == "message"}
            <button class="btn btn-sm variant-soft-primary w-20 py-1 mb-3" on:click={() => page = "inbox"}>
                &lt- Return
            </button>

            <h3 class="h3">{selectedMessage.title}</h3>
            <p class=" italic">sent from <span class="text-secondary-500">{selectedMessage.author.name}</span></p>
            <pre class="font-vt whitespace-normal mt-3">{selectedMessage.message}</pre>

            <div class="flex-grow"></div>
        {:else}
            <p>Page not found</p>
        {/if}
    </div>

</div>
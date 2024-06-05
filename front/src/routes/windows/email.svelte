<script lang="ts">
    import { notify } from "$lib/notifications";

    const contacts = [
        {
            name: "Xel Lu",
            online: true,
            send: () => {
                notify("Out of order", "error", 10000)
                reset()
            }
        },
        {
            name: "James Roberts",
            online: false,
            send: () => {
                notify("Out of order", "warning", 10000)
                reset()
            }
        },
        {
            name: "Rachel Johnson",
            online: false,
            send: () => {
                notify("Out of order", "success", 10000)
                reset()
            }
        },
        {
            name: "Dan C. %user.last_name%",
            online: false,
            send: () => {
                notify("Out of order", "primary", 10000)
                reset()
            }
        }
    ]

    let selectedContact: any = null
    
    let inbox: any[] = []
    let selectedMessage: any = null

    let message: string = ""
    let email: string = ""
    function reset() {
        message = ""
        email = ""  
    }
</script>

<div class="h-96 flex">
    <div class="flex flex-col w-44 bg-primary-900/5 h-96 gap-2">
        <p class="px-2">Contacts</p>
        {#each contacts as contact}
            <button class="btn btn-sm {selectedContact == contact ? 'variant-soft-secondary' : 'variant-soft-primary'} mx-2" on:click={() => { 
                if (selectedContact != contact) {
                    selectedContact = contact
                    reset()
                } else {
                    selectedContact = null
                }
             }}>
                <p class="text-left w-full">{contact.name}</p>
            </button>
        {/each}

        <div class="flex-grow"></div>
        <p class="animate-text-flashing text-center">NOTICE: out of order</p>
        <div class="bg-primary-900/20 p-2">
            <p>Welcome %user%</p>
        </div>
    </div>

    <div class="w-96 flex-grow p-3 flex flex-col">
        {#if selectedContact == null}
            {#if inbox.length == 0}
                <p>No mail here! You're caught up!</p>
            {/if}
            
            {#each inbox as mail}
                <div class="m-1 bg-primary-500/10">
                    <h6 class="h6">{mail.title}</h6>
                    <p>From {mail.author}</p>
                </div>
            {/each}
        {:else}
            <h4 class="h4">Message {selectedContact.name}</h4>
            <textarea class="textarea variant-soft-primary outline-none border-none resize-none p-1 px-2" rows="5" bind:value={message}></textarea>
        
            <h4 class="h4 mt-5">Your E-Mail</h4>
            <input type="email" class="variant-soft-primary input p-1 px-2 outline-none border-none" bind:value={email}>
            
            <div class="flex-grow"></div>

            <button class="btn variant-soft-secondary" on:click={() => {
                selectedContact.send()
            }}>Send -&gt</button>
        {/if}
    </div>

</div>
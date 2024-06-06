<script lang="ts">
    import { type Window } from "$lib/WindowManager";
    import { type Email, type Contact } from "$lib/Email";
    import { emailInbox, contacts } from "$lib/Email";
    import { notify } from "$lib/Notifications";

    export let self: Window;
    self

    let inbox: Email[] = []

    emailInbox.subscribe(value => {
        inbox = value;
    });

    let page: "inbox" | "read" | "compose" = "inbox";

    let selectedContact: Contact | null = null;
    let selectedEmail: Email | null = null;
</script>

<div class="flex h-80">
    <div class="w-44 flex flex-col p-2 bg-primary-900/10">
        <p class="m-1 mx-2">Contacts</p>
        {#each contacts as contact}
            <button class="flex gap-1 items-center btn btn-sm {contact == selectedContact ? 'variant-soft-primary' : ''}" on:click={() => {
                if (contact == selectedContact) {
                    page = "inbox"
                    selectedContact = null;
                } else {
                    page = "compose"
                    selectedContact = contact;
                }
            }}>
                <div class=""></div>
                <p class="w-full text-left">{contact.name}</p>
            </button>
        {/each}
    </div>
    <div class="w-96 h-80 overflow-y-scroll p-3">
        {#if page == "inbox"}
            <h3 class="h3 px-2">Inbox</h3>

            <div class="mt-3 flex flex-col-reverse gap-3">
                {#each inbox as email}
                    <button class="bg-primary-900/10 p-2 px-3" on:click={() => {
                        page = "read"
                        selectedEmail = email
                        email.read = true
                    }}>
                        <h4 class="h4 w-full text-left text-secondary-500">{#if !email.read}<span class="animate-text-flashing">[NEW]</span>{/if} {email.subject}</h4>
                        <p class="w-full text-left">from {email.author.name}</p>
                    </button>
                {/each}
            </div>

        {:else if page == "read"}
            {#if selectedEmail == null}
                <p class="text-error-500 p-2">No e-mail selected</p>
            {:else}
                <h3 class="h3 px-2">{selectedEmail.subject}</h3>
                <p class="text-secondary-500 px-2">from {selectedEmail.author.name}</p>

                <pre class="font-vt mt-3 p-2">{@html selectedEmail.content}</pre>
            {/if}
        {:else if page == "compose"}
            {#if selectedContact == null}
                <h3 class="h3 px-2">Compose</h3>
                <p class="text-error-500 mt-3">No contact selected</p>
            {:else}
                <div class="flex flex-col gap-2">
                    <h3 class="h3 px-2">Compose</h3>

                    <p class="text-secondary-500">Message {selectedContact.name}</p>    
                    <textarea class="input p-2 px-3 resize-none crt outline-none !bg-primary-900/10" rows="5"></textarea>

                    <button class="btn btn-sm variant-soft-secondary" on:click={() => {
                        setTimeout(() => {
                            notify("Temporary domain resolution failure, try again later", "error")
                        }, 500)
                    }}>
                        Send -&gt
                    </button>
                </div>
            {/if}
        {:else}
            <h3 class="h3 px-2">404 Not Found</h3>
            <p class="px-2">Requested page was not found</p>
        {/if}
    </div>
</div>


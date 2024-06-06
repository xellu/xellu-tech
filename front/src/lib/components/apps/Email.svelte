<script lang="ts">
    import { type Window } from "$lib/WindowManager";
    import { type Email, type Contact } from "$lib/Email";
    import { emailInbox, contacts } from "$lib/Email";

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
    <div class="w-96 h-80 overflow-y-scroll">
        {#if page == "inbox"}
            <h3 class="h3 px-2">Inbox</h3>
        {:else if page == "compose"}
            <h3 class="h3 px-2">Compose</h3>
        {:else}
            <h3 class="h3 px-2">404 Not Found</h3>
            <p class="px-2">Requested page was not found</p>
        {/if}
    </div>
</div>


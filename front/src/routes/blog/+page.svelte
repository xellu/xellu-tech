<script lang="ts">
    import { onMount } from "svelte";
    import { LoadNext, Posts, type PostType } from "$lib/scripts/Blog";
    import { Account, type AccountType } from "$lib/scripts/Auth";
    
    let User: AccountType | null = null;
    Account.subscribe(value => {
        User = value;
    });

    let loading: boolean = true
    let posts: PostType[] = []
    let page: "posts" | "new" = "posts";

    Posts.subscribe(value => {
        posts = value;
    });

    onMount(async () => {
        await LoadNext();

        loading = false;
    })
</script>

{#if User?.admin}
    <button class="btn btn-sm variant-soft-tertiary flex items-center justify-center gap-2">
        <span>stylus_note</span>
        <span>New Post</span>
    </button>
{/if}

<p>loading: {loading}</p>
<p>posts: {posts.length == 0 ? '(empty)' : posts}</p>
<p>user.admin: {User?.admin}</p>
<p>user.username: {User?.username}</p>
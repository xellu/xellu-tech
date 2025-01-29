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

    Posts.subscribe(value => {
        posts = value;
    });

    onMount(async () => {
        await LoadNext();

        loading = false;
    })
</script>

{#if User?.admin}
    <p>hello world</p>
{/if}

<p>loading: {loading}</p>
<p>posts: {posts.length == 0 ? '(empty)' : posts}</p>
<p>user.admin: {User?.admin}</p>
<p>user.username: {User?.username}</p>
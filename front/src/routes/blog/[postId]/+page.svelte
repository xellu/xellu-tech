<script lang="ts">

    import "../../../markdown.pcss";

    import { onMount } from "svelte";
    import { getToastStore } from "@skeletonlabs/skeleton";

    import Loader from "$lib/components/Loader.svelte";
    import ArrowButton from "$lib/components/ArrowButton.svelte";
    import Embed from "$lib/components/Embed.svelte";
    
    import type { PostType } from "$lib/scripts/Blog";
    import { toAgo } from "$lib/scripts/Utils";

    const toast = getToastStore();

    export let data;
    const { props } = data;

    let post: PostType | undefined;
    let error: string | null | undefined;

    $: post = props.post;
    $: error = props.error;

    onMount(() => {
        console.log(post, error)
    })
</script>

<svelte:head>
    <title>{post ? (post?.title || 'Blog Post') : 'Blog Post'} | Xellu</title>

    <Embed
        title = "{post ? post?.title : 'Blog Post'} by {post ? post?.author : 'Unknown'}"
        description = "{post ? post?.brief : 'No data'}"
        route = "/blog/{post ? post?._id : ''}"
    />
</svelte:head>

{#if !post && !error}
    <Loader />
{:else if error}
    <Loader error={error} />
{:else}
    <div class="flex items-center justify-between">
        <h1 class="h3 font-bold overflow-hidden text-ellipsis whitespace-nowrap">{post?.title}</h1>
    
        <a href="/blog">
            <ArrowButton>Return</ArrowButton>
        </a>
    </div>
    <p class="text-sm opacity-50">{post?.lastModified == null ? `Posted` : `Edited`} by <span class="capitalize font-bold">{post?.author}</span> {post?.lastModified == null ? toAgo((post?.createdAt || 0) * 1000) : toAgo(post?.lastModified * 1000)}</p>

    <div class="h-px w-full bg-surface-300/10 my-10"></div>

    <div class="markdown">
        {@html post?.content}
    </div>
{/if}

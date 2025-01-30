<script lang="ts">
    import "../../../markdown.pcss";

    import { page } from "$app/state";
    import { onMount } from "svelte";
    import { getToastStore } from "@skeletonlabs/skeleton";

    import Loader from "$lib/components/Loader.svelte";
    import ArrowButton from "$lib/components/ArrowButton.svelte";
    
    import type { PostType } from "$lib/scripts/Blog";
    import { toAgo, MarkdownParser } from "$lib/scripts/Utils";

    const toast = getToastStore();

    let post: PostType | null = null;
    let error: string | null = null;

    onMount(async () => {
        const postId = page.params.postId;

        const r = await fetch(`/api/v2/blog/post/${postId}`);
        const data = await r.json();

        if (!r.ok) {
            error = data.error || "Unknown error";
            return toast.trigger({
                message: error as string,
                background: "variant-soft-warning",
            })
        }

        post = data.post as PostType;
        post.content = MarkdownParser(post.content);
    })
</script>

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

    <div class="mt-5 markdown">
        {@html post?.content}
    </div>
{/if}

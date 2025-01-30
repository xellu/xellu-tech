<script lang="ts">
    import Loader from "$lib/components/Loader.svelte";
    import BlogPostCard from "$lib/components/BlogPostCard.svelte";

    import { onMount } from "svelte";
    import { slide } from "svelte/transition";
    import { getToastStore } from "@skeletonlabs/skeleton";

    import { LoadNext, Posts, type PostType } from "$lib/scripts/Blog";
    import { Account, type AccountType } from "$lib/scripts/Auth";
    
    const toast = getToastStore();

    let User: AccountType | null = null;
    Account.subscribe(value => {
        User = value;
    });

    let loading: boolean = true
    let posts: PostType[] = []
    let page: "posts" | "new" = "posts";
    let reachedEnd: boolean = false;

    let newPost: {_id: string | null, title: string, brief: string, content: string, previewOpen:boolean, saving: {state: boolean, error: boolean}} = {
        _id: null,
        title: "",
        brief: "",
        content: "",

        previewOpen: false,
        saving: {
            state: false,
            error: false,
        }
    }

    async function SavePost(): Promise<{ok: boolean, error?: string}> {
        if (!newPost.title || !newPost.brief || !newPost.content) {
            return { ok: false, error: "Missing Fields" };
        }

        let r: Response;
        if (newPost._id == null) {
            r = await fetch("/api/v2/blog/create", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title: newPost.title,
                    brief: newPost.brief,
                    content: newPost.content,
                })
            })
        } else {
            r = await fetch(`/api/v2/blog/post/${newPost._id}`, {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title: newPost.title,
                    brief: newPost.brief,
                    content: newPost.content,
                })
            })
        }

        if (!r.ok) {
            let e = await r.json();
            return { ok: false, error: e.error || r.statusText };
        }

        return { ok: true };
    }

    Posts.subscribe(value => {
        posts = value;
    });

    onMount(async () => {
        await LoadNext();

        loading = false;
    })
</script>

<svelte:head>
    <title>Blog Posts | Xellu</title>
</svelte:head>

{#if User?.admin}
    <button class="btn btn-sm {page === "posts" ? 'glass' : 'glass-tertiary'} flex items-center justify-center mb-5"
        on:click={() => {
            page = page === "posts" ? "new" : "posts";
            newPost = {
                _id: null,
                title: "",
                brief: "",
                content: "",

                previewOpen: false,
                saving: {
                    state: false,
                    error: false,
                }
            }
        }}
    >
        <span class="material-symbols-outlined duration-500 {page === 'posts' ? '' : 'rotate-[135deg]' }">add</span>
        <span>{page === "posts" ? 'New Post' : 'Cancel'}</span>
    </button>
{/if}

{#if page === "new"}
    <div transition:slide>
        <h2 class="uppercase font-bold text-tertiary-500">{newPost._id == null ? 'New Post' : 'Edit Post'}</h2>

        <div class="glass max-w-sm w-full rounded-xl p-3 mt-1 flex flex-col gap-1">    
            <input type="text" placeholder="Title" bind:value={newPost.title} class="glass-input w-2/3" />
            <input type="text" placeholder="Brief summary" bind:value={newPost.brief} class="glass-input" />
            
            <textarea placeholder="Content" bind:value={newPost.content} class="glass-input h-32 mt-3" />
        </div>

        <button class="btn btn-sm mt-2 flex items-center justify-center {newPost.saving.error ? 'glass-error' : 'glass-tertiary'}" disabled={newPost.saving.state || (!newPost.title || !newPost.brief || !newPost.content)}
            on:click={async () => {
                newPost.saving.state = true;
                newPost.saving.error = false;

                let res = await SavePost();

                newPost.saving.state = false;

                if (!res.ok) {
                    newPost.saving.error = true;
                    setTimeout(() => {
                        newPost.saving.error = false;
                    }, 1000);
                    return toast.trigger({
                        message: res.error || "Unknown error",
                        background: "variant-soft-error",
                    })
                }

                toast.trigger({
                    message: newPost._id == null ? "Post created" : "Post updated",
                    background: "variant-soft-success",
                })

                page = "posts";

                setTimeout(() => {
                    window.location.reload();
                }, 1000);
            }}
        >
            {#if newPost.saving.state} <Loader center={false} scale="sm" variant="tertiary" />
            {:else if newPost.saving.error} <span class="material-symbols-outlined">cancel_schedule_send</span>
            {:else} <span class="material-symbols-outlined">send</span>
            {/if}
            <span>{newPost._id == null ? 'Post' : 'Save'}</span>
        </button>

        <!-- preview -->
        <button class="flex items-center justify-start uppercase text-sm font-bold text-tertiary-400 mt-3"
            on:click={() => {
                newPost.previewOpen = !newPost.previewOpen;
            }}
        >
            <p>Preview</p>
            <span class="material-symbols-outlined duration-300 {newPost.previewOpen ? 'rotate-180' : ''}">keyboard_arrow_down</span>
        </button>

        {#if newPost.previewOpen}
            <div transition:slide class="border-t border-t-surface-400/20 mt-1 pt-5 max-w-sm w-full">
                {#if !newPost.title || !newPost.brief || !newPost.content}
                    <Loader error="Unable to preview: Missing Fields" />
                {:else}
                    <BlogPostCard post={{ //yea i have to do all this buffoonery cause i have to convert it to PostType 🥲
                        _id: newPost._id,
                        title: newPost.title,
                        brief: newPost.brief,
                        content: newPost.content,
            
                        lastModified: newPost._id == null ? null : parseInt((new Date()).getTime().toString())/1000,
                        createdAt: parseInt((new Date()).getTime().toString())/1000,
            
                        author: User?.username || "Unknown",
                    }} />
                {/if}
            </div>
        {/if}
    </div>
{:else if loading}
    <Loader />
{:else}
    <div transition:slide>
        <!-- <p>loading: {loading}</p>
        <p>posts: {posts.length == 0 ? '(empty)' : posts}</p>
        <p>user.admin: {User?.admin}</p>
        <p>user.username: {User?.username}</p> -->

        {#each posts as post}
            <BlogPostCard
                post={post}
                
                adminTools={User?.admin}
                onEdit={(p) => {
                    newPost = {
                        _id: p._id,
                        title: p.title,
                        brief: p.brief,
                        content: p.content,

                        previewOpen: false,
                        saving: {
                            state: false,
                            error: false,
                        }
                    }

                    page = "new";
                }}
            />
        {/each}

        {#if !reachedEnd}
            <button class="btn btn-sm glass flex items-center justify-center mt-5 w-full"
                transition:slide
                on:click={async () => {
                    const r = await LoadNext();
                    reachedEnd = r.reachedEnd || false;

                    if (!r.ok) {
                        return toast.trigger({
                            message: r.error || "Unknown error",
                            background: "variant-soft-error",
                        })
                    }
                }}
            >
                <span class="material-symbols-outlined">expand_more</span>
                <span>Load More</span>
            </button>
        {:else}
            <p class="text-center mt-5 opacity-50 text-xs uppercase font-bold" transition:slide>
                You've reached the end
            </p>
        {/if}
    </div>
{/if}

import { writable, type Writable } from "svelte/store";

type PostType = {
    _id: string,

    createdAt: number,
    lastModified: null | number,

    title: string,
    brief: string,
    content: string,
}

let NextPage: number = 1
const Posts: Writable<PostType[]> = writable<PostType[]>([]); //

async function LoadNext(): Promise<{ok: boolean, error?: string}> {
    if (NextPage < 0) {
        return {ok: true} //end of posts
    }

    const r = await fetch(`/api/v2/blog/posts?page=${NextPage}`)
    if (!r.ok) {
        return {ok: false, error: `Unable to update posts: ${r.status} ${r.statusText}`}
    }

    //wah wah boring ass code
    let data = await r.json()
    let newPosts: PostType[] = data.posts

    if (newPosts.length == 0) { NextPage == -1 }
    else { NextPage++ }

    //add new posts to Posts store
    Posts.update((value) => {
        value = value.concat(newPosts)
        return value
    })

    return {ok: true}
}

export {
    type PostType,

    Posts,
    LoadNext
}
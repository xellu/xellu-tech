import { type PostType } from "$lib/scripts/Blog";

let post: PostType | null = null;
let error: string | null = null;


export const load = async ({ params }) => {
    const postId = params.postId;

    const r = await fetch(`http://127.0.0.1/api/v2/blog/post/${postId}`);
    const data = await r.json();

    if (!r.ok) {
        error = data.error || "Unknown error";
        return { props: { error: error } };
    }

    post = data.post as PostType;

    return { 
        props: {
            post: post
        }
    };
};

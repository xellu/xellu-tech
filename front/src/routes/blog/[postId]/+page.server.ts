import { type PostType } from "$lib/scripts/Blog";

let post: PostType | null = null;
let error: string | null = null;


export const load = async ({ params }) => {
    const postId = params.postId;

    const r = await fetch(`http://127.0.0.1:5000/api/v2/blog/post/${postId}`);
    if (!r.ok) {
        return {
            props: {
                post: {
                    _id: "(none)",
                    createdAt: Date.now(),
                    lastModified: null,
                    
                    title: `${r.status} ${r.statusText}`,
                    brief: "Failed to load post",
                    content: "# Failed to load post",

                    author: "System"
                }
            }
        }
    }

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

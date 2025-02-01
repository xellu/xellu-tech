export const load = async ({ params }) => {
    const alias = params.alias;

    const r = await fetch(`http://127.0.0.1/api/v2/files/embed/${alias}`);
    const data = await r.json();

    if (!r.ok) {
        return { props: { error: data.error || "Unknown error", alias: alias} };
    }

    return { 
        props: {
            data: data,
            alias: alias
        }
    };
};

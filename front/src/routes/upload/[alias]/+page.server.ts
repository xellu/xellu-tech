export const load = async ({ params }) => {
    const alias = params.alias;

    const r = await fetch(`http://127.0.0.1/api/v2/files/embed/${alias}`);
    let data = null;
    try {
        data = await r.json();
    } catch (err) {
        return {
            props: {
                error: `${err}`,
                alias: alias,
            }
        }
    }

    if (!r.ok || data == null) {
        return { props: { error: data.error || "Unknown error", alias: alias} };
    }

    return { 
        props: {
            data: data,
            alias: alias
        }
    };
};

import Container from "./Container.svelte";

import ColDuo from "./ColDuo.svelte";
import ColDuoExpandable from "./ColDuoExpandable.svelte";
import ColAll from "./ColAll.svelte";
import ColSingle from "./ColSingle.svelte";
import LinesAll from "./LinesAll.svelte";
import LinesMinimal from "./LinesMinimal.svelte";

export const Grid = {
    Root: Container,

    Single: ColSingle,
    Duo: ColDuo,
    DuoEx: ColDuoExpandable,
    Full: ColAll,
    
    Lines: {
        All: LinesAll,
        Minimal: LinesMinimal
    }
}
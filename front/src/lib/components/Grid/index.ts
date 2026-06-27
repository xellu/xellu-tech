import Container from "./Container.svelte";

import ColDuo from "./ColDuo.svelte";
import ColDuoExpandable from "./ColDuoExpandable.svelte";
import ColTrio from "./ColTrio.svelte";
import ColAll from "./ColAll.svelte";
import ColSingle from "./ColSingle.svelte";

import Divider from "./Divider.svelte";
import LinesAll from "./LinesAll.svelte";
import LinesMinimal from "./LinesMinimal.svelte";

export const Grid = {
    Root: Container,

    Single: ColSingle,
    Duo: ColDuo,
    DuoEx: ColDuoExpandable,
    Trio: ColTrio,
    Full: ColAll,

    Divider: Divider,
    
    Lines: {
        All: LinesAll,
        Minimal: LinesMinimal
    }
}
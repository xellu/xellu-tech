import Container from "./Container.svelte";

import ColLeft from "./ColLeft.svelte";
import ColRight from "./ColRight.svelte";
import ColBoth from "./ColBoth.svelte";
import LinesAll from "./LinesAll.svelte";
import LinesMinimal from "./LinesMinimal.svelte";

export const Grid = {
    Root: Container,
    Left: ColLeft,
    Right: ColRight,
    Stretch: ColBoth,
    Lines: {
        All: LinesAll,
        Minimal: LinesMinimal
    }
}
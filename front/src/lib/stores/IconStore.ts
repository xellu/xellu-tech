import { writable, type Writable } from "svelte/store";

export const Icons: Writable<string[]> = writable([]);

export function addIcon(name: string) {
    Icons.update((v) => {
        if (v.includes(name)) { return v }
        
        v.push(name)
        return v.toSorted()
    })
}
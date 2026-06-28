import { goto, preloadData } from "$app/navigation";
import Comp from "./Comp.svelte";
import { isOpen, highlightedElement, URLS, blockInteraction, externalUrl, type NavbarElements, type LinkType } from "./store";

import { toaster } from "$lib/stores/Toaster";

export const Navbar = {
    Root: Comp,
    
    setOpen: (value: boolean) => { isOpen.set(value) },
    highlight: (value: NavbarElements) => {
        blockInteraction.set(true) //block mouse hover events

        setTimeout(() => { highlightedElement.set(value); }, 300) //delay highlight
        setTimeout(() => { highlightedElement.set(null); blockInteraction.set(false); }, 2300) //remove hl and block
    },
    navigateTo: async (url: string, newTab?: boolean) => {
        isOpen.set(true);
        blockInteraction.set(true) //block mouse hover

        let hlElement: LinkType | null = null;
        URLS.forEach((l) => {
            if ((url.startsWith(l.url) && l.url != "/") || url == l.url) {
                hlElement = l.name
            }
        })
        // console.log(hlElement)

        setTimeout(() => {
            highlightedElement.set(hlElement || "url")
            if (hlElement == null) { externalUrl.set(url) }
        }, 300)

        const start = Date.now();
        
        const external = !url.startsWith("/")
        let error: boolean = false;

        if (!external) {
            try { await preloadData(url); }
            catch (e) {
                console.error(e)
                error = true;
            }
        }

        const timeout = (Date.now() - start) > 700 ? 0 : 700 - (Date.now() - start);
        // console.log(timeout)
        
        if (error) setTimeout(() => { toaster.error({title: "Failed to open page"}) }, 300)

        if (!error) setTimeout(() => { newTab || external ? window.open(url) : goto(url) }, timeout)
        
        setTimeout(() => { //close navbar
            highlightedElement.set(null)
            isOpen.set(false)
            blockInteraction.set(false)
            externalUrl.set("")
        }, timeout+300)
    },

    isOpen: isOpen,
    highlightedElement: highlightedElement
}
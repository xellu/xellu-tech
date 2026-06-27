import { goto } from "$app/navigation";
import Comp from "./Comp.svelte";
import { isOpen, highlightedElement, URLS, blockInteraction, type NavbarElements, type UrlType } from "./store";

export const Navbar = {
    Root: Comp,
    
    setOpen: (value: boolean) => { isOpen.set(value) },
    highlight: (value: NavbarElements) => {
        blockInteraction.set(true) //block mouse hover events

        setTimeout(() => { highlightedElement.set(value); }, 300) //delay highlight
        setTimeout(() => { highlightedElement.set(null); blockInteraction.set(false); }, 2300) //remove hl and block
    },
    navigateTo: (value: UrlType) => {
        isOpen.set(true);
        blockInteraction.set(true) //block mouse hover
        setTimeout(() => { highlightedElement.set(value) }, 300)

        //open url
        setTimeout(() => { 
            let url: string | null = null;
            URLS.forEach((l) => {
                if (l.name == value) { url = l.url }
            })
            if (url) { goto(url) }
        }, 800)

        setTimeout(() => { //close navbar
            highlightedElement.set(null)
            isOpen.set(false)
            blockInteraction.set(false)
        }, 1000)
    },

    isOpen: isOpen,
    highlightedElement: highlightedElement
}
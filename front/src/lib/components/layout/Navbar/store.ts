import { writable, type Writable } from "svelte/store";

export const isOpen: Writable<boolean> = writable(false);
export const blockInteraction: Writable<boolean> = writable(false);
export const highlightedElement: Writable<NavbarElements> = writable(null); 

export const URLS = [
    {name: "About Me", url: "/"},
    {name: "My Work", url: "/work"},
    {name: "Services", url: "/services"}
]

export type UrlType = typeof URLS[number]['name'];
export type NavbarElements = UrlType | "socials" | null;

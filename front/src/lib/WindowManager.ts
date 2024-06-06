import { writable, type Writable } from "svelte/store";

import { logger } from "$lib/Logger";
import { apps } from "./Apps";
import { playSound } from "./SoundManager";

export let activeWindows: Writable<Window[]> = writable([]);

let windows: Window[] = [];

let startX = 200;
let startY = 200;

activeWindows.subscribe(value => {
    windows = value;
})

export type Window = {
    posX: number,
    posY: number,
    posZ: number,
    visible: boolean,

    appId: string,
    meta: any
}

export function getMaxZ() {
    let max = 0;
    windows.forEach(win => {
        if (win.posZ > max) {
            max = win.posZ;
        }
    })
    return max;
}

export function isTop(appId: string) {
    let top = 0;
    windows.forEach(win => {
        if (win.appId == appId && win.posZ > top && win.visible) {
            top = win.posZ;
        }
    })

    return top == getMaxZ();
}

export function promoteWindow(win: Window) {
    openWindow(win.appId, win.meta);
}

export function closeWindow(win: Window) {
    windows = windows.filter(window => window != win);

    activeWindows.set(windows);
}

export function openWindow(appId: string, meta:any = {}) {
    if (!Object.keys(apps).includes(appId)) { return }

    playSound("/window-open.mp3", 0.01)

    let exists: boolean = false;

    windows.forEach(win => {
        if (win.appId == appId) {
            win.posZ = getMaxZ() + 1;
            win.visible = true;
            exists = true;

            logger.success(`Window with appId [${appId}] promoted to top`)
            activeWindows.set(windows);
        }
    })

    if (exists) { return }

    windows.push({
        posX: startX,
        posY: startY,
        posZ: getMaxZ() + 1,
        visible: true,

        appId: appId,
        meta: meta
    })

    logger.success(`Opened window with appId [${appId}]`)

    startX += 20;
    startY += 20;

    if (startX > 400) { startX = 200 }
    if (startY > 400) { startY = 200 }
    activeWindows.set(windows);
}
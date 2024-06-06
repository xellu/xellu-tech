import { writable, type Writable } from "svelte/store";
import { type App } from "./Apps";

import { logger } from "$lib/Logger";
import { apps } from "./Apps";
import { playSound } from "./SoundManager";

export let activeWindows: Writable<Window[]> = writable([]);
export let allApps: Writable<AppWindow[]> = writable([]);

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

export type AppWindow = {
    app: App,
    appId: string,
    open: "open" | "hidden" | "closed"
}

export function getAllAppWindows(): AppWindow[] {
    let all: AppWindow[] = [];

    Object.keys(apps).forEach(app => {
        let open: "open" | "hidden" | "closed" = "closed";

        windows.forEach(win => {
            if (win.appId == app) {
                open = win.visible ? "open" : "hidden";
            }
        })

        all.push({
            app: apps[app],
            appId: app,
            open
        })
    })

    return all;
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

export function isOpen(appId: string): boolean {
    let open = false;
    windows.forEach(win => {
        if (win.appId == appId && win.visible) {
            open = true;
        }
    })

    return open;
}

export function isVisible(appId: string): boolean {
    let visible: boolean = false;
    windows.forEach(win => {
        if (win.appId == appId && win.visible) {
            visible = true;
        }
    })
    return visible;
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
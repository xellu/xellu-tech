import AboutMe from "./components/AboutMe.svelte"

export const apps: {about: App, projects: App, email: App} | any = { //had to add 'any' to stop vscode from bitching
    about: {
        title: "About Me",
        icon: "/AboutMe.png",
        component: AboutMe,
    },
    projects: {
        title: "Projects",
        icon: "/Projects.png",
        component: null,
    },
    email: {
        title: "E-Mail",
        icon: "/Email.png",
        component: null,
    },
    userprofile: {
        title: "User Profile",
        icon: "/User.png",
        component: null,
        hidden: true
    }
}

export type App = {
    title: string,
    icon: string,
    component?: any,
    hidden?: boolean,
}
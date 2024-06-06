import AboutMe from "./components/apps/AboutMe.svelte"
import Projects from "./components/apps/Projects.svelte"
import Email from "./components/apps/Email.svelte"

export const apps: {about: App, projects: App, email: App} | any = { //had to add 'any' to stop vscode from bitching
    about: {
        title: "About Me",
        icon: "/AboutMe.png",
        component: AboutMe,
    },
    projects: {
        title: "Projects",
        icon: "/Projects.png",
        component: Projects,
    },
    email: {
        title: "E-Mail",
        icon: "/Email.png",
        component: Email,
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
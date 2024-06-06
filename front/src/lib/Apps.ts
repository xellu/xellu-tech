export const apps: {about: App, projects: App, email: App} | any = { //had to add 'any' to stop vscode from bitching
    about: {
        title: "About Me",
        icon: "/AboutMe.png",
    },
    projects: {
        title: "Projects",
        icon: "/Projects.png",
    },
    email: {
        title: "E-Mail",
        icon: "/Email.png",
    },
}

export type App = {
    title: string,
    icon: string
}
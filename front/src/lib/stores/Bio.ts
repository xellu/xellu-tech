export const Socials = {
    discord: "https://discord.com/users/923528901219729430",
    instagram: "https://www.instagram.com/xelluuu/",
    github: "https://github.com/xellu/"
}

export type Project = {
    date: string,
    until?: string,
    project: {
        name: string,
        description: string,
        links: {
            name: string,
            url: string
        }[],
        tags: string[]
    }
}

export const Projects: Project[] = [
    {
        date: "Spring 2025",
        project: {
            name: "Nautica 3",
            description: "A Platform for Backend development. Providing managed runtime, file-based routing, many built-in services, features and its own package ecosystem.",
            links: [{
                name: "Source Code",
                url: "https://github.com/xellu/nautica-api"
            }],
            tags: ["Python"]
        }
    },
    {
        date: "Spring 2025",
        until: "Winter 2025",
        project: {
            name: "Clockwork SMP",
            description: "A Modded Minecraft Survival Server with over 500 members as of July 2025. Featuring a seamless system for managing whitelists, moderation and more.",
            links: [
                // {
                //     name: "Discord Server",
                //     url: "https://discord.gg/Bk37q2kaEc"
                // }
            ],
            tags: ["Java", "Python"]
        }
    },
    {
        date: "Summer 2024",
        until: "Spring 2025",
        project: {
            name: "Veinyard",
            description: "A Freelancing project, a Roblox Script marketplace.",
            links: [
                {
                    name: "Website",
                    url: "https://veinyard.com/"
                }
            ],
            tags: ["Svelte", "TypeScript", "TailwindCSS", "Python", "Nginx"]
        }
    },
    // {
    //     date: "Summer 2024",
    //     until: "Spring 2025",
    //     project: {
    //         name: "Lime",
    //         description: "A Game Cheat & Mod Marketplace and development, with focus on bypasses and user experience. Featuring a web dashboard for configuring cheat clients over the internet. Over 85 users & 11 paying customers, as of August 2024.",
    //         links: [
    //             // {
    //             //     name: "Website",
    //             //     url: "https://limeade.cool"
    //             // }
    //         ],
    //         tags: ["Svelte", "TypeScript", "TailwindCSS", "Python", "Nginx"]
    //     }    
    // },
    {
        date: "Winter 2024",
        until: "Summer 2024",
        project: {
            name: "XelCraft",
            description: "A Voxel-based Sandbox Game, similar to Minecraft, made with the Godot Engine. Has a chunk-based world system. Made for fun, and to learn game development. ",
            links: [
                {
                    name: "Source Code",
                    url: "https://github.com/xellu/xelcraft"
                },
            ],
            tags: ["C#", "Godot Engine", "3D Game"]
        }
    },
    {
        date: "Summer 2023",
        until: "Winter 2023",
        project: {
            name: "DoorsMC",
            description: "A Minecraft server network with custom plugins, minigames, and website, including backend systems for managing the network and players. Never released, Source code was lost.",
            links: [
                {
                    name: "Devlog #1",
                    url: "https://www.youtube.com/watch?v=fnN9afioqis"
                },
                {
                    name: "Devlog #2",
                    url: "https://www.youtube.com/watch?v=cJskgQsoX-0"
                }
            ],
            tags: ["Java", "Spigot", "Svelte", "TypeScript", "Python"]
        }
    },
    {
        date: "Summer 2021",
        until: "Spring 2022",
        project: {
            name: "Euphoria",
            description: "Advanced Discord Self-bot with over 100+ commands and features, including a Nitro Sniper, Plugin System, and more. Source code taken down due to Discord's Terms of Service.",
            links: [],
            tags: ["Python", "Discord API", "Automation"]
        }
    }
    
]
// export const projects = [
//     {
//         name: "MDBB",
//         description: "A Base for Discord Bots, with an Event, Plugin and Command System.",
//         date: "Mid - Late 2024",
//         links: [
//             {
//                 name: "Source Code",
//                 url: "https://github.com/xellu/mdbb"
//             }
//         ],
//         tags: ["Python", "Discord API"]
//     },
//     {
//         name: "Lime",
//         description: "A Game Cheat & Mod Marketplace and development, with focus on bypasses and user experience. Featuring a web dashboard for configuring cheat clients over the internet. Over 85 users & 11 paying customers, as of August 2024.",
//         date: "2024 - 2025",
//         links: [
//             {
//                 name: "Website",
//                 url: "https://limeade.cool"
//             }
//         ],
//         tags: ["Svelte", "TypeScript", "TailwindCSS", "Python", "Nginx"]
//     },
//     {
//         name: "XelCraft",
//         description: "A Voxel-based Sandbox Game, similar to Minecraft, made with the Godot Engine. Has a chunk-based world system. Made for fun, and to learn game development. ",
//         date: "2023 - 2024",
//         links: [
//             {
//                 name: "Source Code",
//                 url: "https://github.com/xellu/xelcraft"
//             }
//         ],
//         tags: ["C#", "Godot Engine", "3D Game"]
//     },
//     {
//         name: "DoorsMC",
//         description: "A Minecraft server network with custom plugins, minigames, and website, including backend systems for managing the network and players. Never released, Source code was lost.",
//         date: "Mid - Late 2023",
//         links: [],
//         tags: ["Java", "Spigot", "Svelte", "TypeScript", "Python"]
//     },
//     {
//         name: "Xello.Blue - Image Hosting",
//         description: "A Simple Image Hosting Service, with a web dashboard and API for uploading and managing images. Originally made for personal use, later made invite-only. Over 8,000 images uploaded, and 75+ users.",
//         date: "2022 - 2023",
//         links: [],
//         tags: ["Python", "HTML", "CSS", "JavaScript", "Flask"]
//     },
//     {
//         name: "Euphoria",
//         description: "Advanced Discord Self-bot with over 100+ commands and features, including a Nitro Sniper, Plugin System, and more. Source code taken down due to Discord's Terms of Service.",
//         date: "2021 - 2022",
//         links: [],
//         tags: ["Python", "Discord API", "Automation"]
//     }
    
// ]

export type Timeline = {
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

export const projectTimeline: Timeline[] = [
    {
        date: "Summer 2024",
        until: "Spring 2025",
        project: {
            name: "Lime",
            description: "A Game Cheat & Mod Marketplace and development, with focus on bypasses and user experience. Featuring a web dashboard for configuring cheat clients over the internet. Over 85 users & 11 paying customers, as of August 2024.",
            links: [
                {
                    name: "Website",
                    url: "https://limeade.cool"
                }
            ],
            tags: ["Svelte", "TypeScript", "TailwindCSS", "Python", "Nginx"]
        }    
    },
    {
        date: "Fall 2024",
        project: {
            name: "MDBB",
            description: "A Base for Discord Bots, with an Event, Plugin and Command System.",
            links: [
                {
                    name: "Source Code",
                    url: "https://github.com/xellu/mdbb"
                }
            ],
            tags: ["Python", "Discord API"]
        }
    },
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
            links: [],
            tags: ["Java", "Spigot", "Svelte", "TypeScript", "Python"]
        }
    },
    {
        date: "Summer 2022",
        until: "Winter 2023",
        project: {
            name: "Xello.Blue Image Host",
            description: "A Simple Image Hosting Service, with a web dashboard and API for uploading and managing images. Originally made for personal use, later made invite-only. Over 8,000 images uploaded, and 75+ users.",
            links: [],
            tags: ["Python", "HTML", "CSS", "JavaScript", "Flask"]
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
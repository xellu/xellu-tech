export const directories: any = {
    apps: {
        _type: "dir",
        "about.app": {
            _type: "file",
            content: ["<span class='text-warning-500'>Unable to display contents</span>"]
        },
        "projects.app": {
            _type: "file",
            content: ["<span class='text-warning-500'>Unable to display contents</span>"]
        },
        "email.app": {
            _type: "file",
            content: ["<span class='text-warning-500'>Unable to display contents</span>"]
        },
        "terminal.app": {
            _type: "file",
            content: ["<span class='text-warning-500'>Unable to display contents</span>"]
        },
        
    },
    user: {
        _type: "dir",
        default: {
            _type: "dir",
            home: {
                _type: "dir",
                documents: {
                    _type: "dir",
                    "about.txt": {
                        _type: "file",
                        content: [
                            "This is a guide to XelOS, the operating system that powers LIME Corporation's devices.", 
                            "XelOS is a proprietary operating system developed by LIME Corp. in early 1960's.", "",
                            "The system was designed to be optimized for the company's hardware, and is not available for public use.", "",
                            "To get started, type 'help' to see a list of available commands.",
                            "For more information, visit our website at www.limecorp.com", "",
                            "- James Roberts, 15th of April, 1982"
                        ]
                    },
                    "license.txt": {
                        _type: "file",
                        content: [
                            "XelOS is a proprietary operating system developed by LIME Corporation.",
                            "All rights reserved. Unauthorized use is strictly prohibited.",
                            "For more information, visit our website at www.limecorp.com", "",
                            "- James Roberts, 12th of April, 1982"
                        ]
                    },
                    lime: {
                        _type: "dir",
                        "about.txt": {
                            _type: "file",
                            content: [
                                "LIME Corporation is a multinational technology company that specializes in researching and developing new technologies for the U.S. government.",
                                "The company was founded in the post-war era by a group of scientists and engineers who had worked on the Manhattan Project.", "",
                                "While the company is best known for its work in the defense industry, it has also made significant contributions to the fields of computer science, telecommunications, and space exploration.",
                                "", "- Rachel Johnson, 3rd of May, 1983", "", "", "", "", "DO NOT TRUST THEM!", "THE OASIS PROJECT IS REAL!", "It is believed that the real reason why the Space Exploration programme (Oasis) was shut down was because of the discovery of a new planet, which was kept secret from the public.",
                                "The planet was named 'NG-1' and was said to be the first planet discovered outside of our solar system. It was said to be habitable and was believed to be the key to the future of humanity.",
                                "However, after the 1st manned mission to the planet, the crew was never heard from again. The mission was said to be a failure and the planet was deemed uninhabitable.",
                                "The truth is that the crew discovered that the planet was already inhabited by an advanced civilization. The crew was captured and taken prisoner by the inhabitants of the planet.",
                                "The crew was never heard from again and the planet was declared off-limits by the U.S. government. The Oasis project was shut down and all records of the mission were destroyed.",
                                "The truth about the planet and the crew was kept secret from the public and the crew was declared missing in action. The crew was never officially declared dead and their families were never told the truth about what happened to them.",
                                "Everyone who worked on the Oasis project was sworn to secrecy and the truth about the planet and the crew was never revealed to the public.",
                                "THEY'RE COMING FOR US"
                            ]
                        },
                    }
                }
            }
        }
    }
}
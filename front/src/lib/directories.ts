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
        "todo.app": {
            _type: "file",
            content: ["<span class='text-warning-500'>Unable to display contents</span>"]
        }
        
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
                            "XelOS is a proprietary operating system developed by LIME Corp. in late 1970's.", "",
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
                    }
                },
                company: {
                    _type: "dir",
                    "about.txt": {
                        _achievement: "readAbout",
                        _type: "file",
                        content: [
                            "LIME Corporation is a multinational technology company that specializes in researching and developing new technologies for the U.S. government.",
                            "The company was founded in the post-war era by a group of scientists and engineers who had worked on the Manhattan Project.", "",
                            "While the company is best known for its work in the defense industry, it has also made significant contributions to the fields of computer science, telecommunications, and space exploration.",
                            "", "- Rachel Johnson, 3rd of May, 1983", "", "", "", "", "DO NOT TRUST THEM!", "THE OASIS PROJECT IS REAL!"
                        ]
                    },
                }
            }
        }
    }
}
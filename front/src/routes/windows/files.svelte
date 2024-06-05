<script lang="ts">
    import { directories } from "$lib/directories";
    import { notify } from "$lib/notifications";
    import { contacts } from "$lib/contacts";

    export let windows: any = null;
    export let tasks: any = {}
    export let inbox: any[] = []

    let pwd: string[] = ["user", "default", "home"]    
    let previousPwd: string[][] = [pwd]

    


    function getFiles(): any[] {

        try {
            let path: string[] = pwd;
            let dir: any = null;

            // console.log(`new path: ${path}`)

            let failed: boolean = false
            path.forEach((p :string) => {
                // console.log(`crawling path: ${p}`)
                if (dir == null) {
                    dir = directories[p]
                    if (!dir) {
                        failed = true
                    }
                } else {
                    if (!dir[p]) {
                        failed = true
                    }

                    dir = dir[p]
                }
            })

            if (typeof(dir) != "object" || failed) {
                return [{name: "<span class='text-warning-500'>Directory not found</span>", type: "error"}]
            }

            let output: any[] = []
            Object.keys(dir).forEach((key) => {
                if (key.startsWith("_")) return
                output.push({name: key, type: dir[key]._type, data: dir[key]})
            })

            return output
        } catch (e) {
            console.error(`getFiles error: ${e}`)
            return [{name: `<span class='text-error-500'>Unable to list directory: ${e}</span>`, type: 'error'}]
        }
    }

    function changeDir(dir: string) {
        let temp: string[] = pwd;

        if (dir == "..") {
            if (pwd.length > 1) {
                pwd = pwd.slice(0, pwd.length - 1)
            }
        } else {
            if (dir == "/") {
                return [{name: "<span class='text-error-500'>Root access denied</span>", type: "error"}]
            } else if (dir.startsWith("/")) {
                pwd = dir.split("/").filter((p) => p != "")
                return []
            }

            let path = [...pwd, ...dir.split("/").filter((p) => p != "")]
            let _dir = directories
            let failed: boolean = false

            path.forEach((p :string) => {
                if (_dir == null) {
                    failed = true
                }

                if (_dir[p] == undefined) {
                    failed = true
                }
                
                _dir = _dir[p]
            })

            if (failed) {
                return [{name: "<span class='text-warning-500'>Directory not found</span>", type: "error"}]
            }
            pwd = path
        }

        previousPwd.push(temp);
        return []
    }

    function readFile(file: string) {
        let ls = getFiles()

        if (ls.filter((f) => f.name == file).length == 0) {
            return [`<span class='text-error-500'>File not found</span>`]
        }

        let data: any = {content: [`<span class='text-error-500'>File not found</span>`]}
        ls.forEach((f) => {
            if (f.name == file) {
                data = f.data
            }
        })

        if (data._achievement) {
            if (!tasks[data._achievement].completed) {
                tasks[data._achievement].completed = true
                setTimeout(() => { notify("Task completed", "success", 5000) }, 2000)

                if (data._achievement == "readAbout") {
                    setTimeout(() => {
                    inbox = inbox.concat({
                        title: "What was that?",
                        message: "You did not see that! Who put that there? Doesn't matter, just ignore it, okay? It isn't anything important.",
                        author: contacts[1],
                        unread: true
                    })
                    notify("You've got mail!")
                    directories.user.default.home.company["about.txt"].content = ["THEY ARE COMING"]
                }, 10000)
            }
            } 
        }

        return data.content
    }

    let files: any[] = getFiles()
    let bookmarks: any = {
        Home: "/user/default/home",
        Documents:  "/user/default/home/documents",
        Company: "/user/default/home/company",
        Apps: "/apps"
    }

    const icons: any = {
        dir: "Folder.png",
        file: "File.png",
        error: "WarningSign.png"
    }
</script>

<div class="flex flex-row h-96">
    <div class="w-44 flex flex-col gap-1 p-2 bg-primary-900/5">
        {#each Object.keys(bookmarks) as bookmark}
            <button class="btn btn-sm {`/${pwd.join('/')}` == bookmarks[bookmark] ? 'variant-soft-primary' : ''}" on:click={() => {
                changeDir(bookmarks[bookmark])
                files = getFiles()
            }}>
                <p class="w-full text-left">{bookmark}</p>
            </button>
        {/each}
    </div>
    <div class="flex flex-col" style="width: 700px;" >
        <div class="flex flex-row gap-3 p-1 bg-primary-900/5">
            <button class="btn btn-sm variant-soft-primary py-0" on:click={() => {
                if (previousPwd.length > 1) {
                    pwd = previousPwd[previousPwd.length - 1]
                    previousPwd = previousPwd.slice(0, previousPwd.length - 1)
                    files = getFiles()
                }
            }}>&lt-</button>
        </div>
        <div class="flex flex-row gap-3 flex-wrap p-5">
            
            {#each files as f}
                <button class="w-16 h-20 flex flex-col" on:click={() => {
                    if (f.type == "dir") {
                        let output = changeDir(f.name)
                        if (output.length == 0) {
                            files = getFiles()
                        } else {
                            files = output
                        }
                    }

                    if (f.type == "file" && f.name.endsWith(".app")) {
                        setTimeout(() => {
                            windows[f.name.replace(".app", "")].onOpen()
                        }, 50)
                    } else if (f.type == "file") {
                        windows["fileDisplay"].content = readFile(f.name)
                        setTimeout(() => {
                            windows["fileDisplay"].onOpen()
                        }, 50)
                    }
                }}>
                    <img src="{icons[f.type]}" alt="" class="w-16 max-h-16">
                    <p class="w-16 whitespace-nowrap text-ellipsis overflow-hidden text-center" title="{f.name}">{@html f.name}</p>
                </button>
            {/each}
        </div>
    </div>
</div>

<script lang="ts">
    import { onDestroy, onMount } from 'svelte';
    import { directories } from '$lib/directories';

    export let self: any = {
        open: false
    }

    export let windows: any = null

    const default_message = ["Running XelOS [Build 4-6-1984/f6eb9a3]", "(c) LIME Corporation, All Rights Reserved"]
    let history = default_message
    let pwd = ["user", "default", "home"]

    const commands: any = {
        help: () => {
            return [
                "",
                "Available commands:",
                "-  help - Display this help message",
                "-  ls - List files and directories",
                "-  cd &ltdir&gt - Change directory",
                "-  cat &ltfile&gt - Display file contents",
                "-  clear - Clear the terminal screen",
                "-  about - Display information about XelOS",
                "-  license - Display the XelOS license agreement",
                "-  start &ltapp&gt - Start an application",
                "-  exit - Exit the terminal"
            ]
        },
        pwd: () => {
            return ["/"+pwd.join("/")]
        },
        ls: (_path: string | null = null) => {
            try {
                let path: string[] = pwd
                let dir: any = null;

                console.log(pwd)

                if (_path) {
                    if (_path == "/") {
                        let output: string[] = []
                        Object.keys(directories).forEach((key) => {
                            if (key.startsWith("_")) return
                            output.push(directories[key]._type == "dir" ? `<span class="text-secondary-500">${key}/</span>` : key)
                        })

                        return [output.join("   ")]
                    } else if (_path.startsWith("/")) {
                        path = _path.split("/").filter((p) => p != "")
                    } else {
                        path = [...pwd, ..._path.split("/").filter((p) => p != "")]
                    }
                }

                let failed: boolean = false
                path.forEach((p :string) => {
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
                    return ["<span class='text-warning-500'>Directory not found</span>"]
                }

                let output: string[] = []
                Object.keys(dir).forEach((key) => {
                    if (key.startsWith("_")) return
                    output.push(dir[key]._type == "dir" ? `<span class="text-secondary-500">${key}/</span>` : key)
                })

                return [output.join("   ")]
            } catch (e) {
                return [`<span class='text-error-500'>Unable to list directory: ${e}</span>`]
            }
        },
        cd: (dir: string) => {
            if (dir == "..") {
                if (pwd.length > 1) {
                    pwd = pwd.slice(0, pwd.length - 1)
                }
            } else {
                if (dir == "/") {
                    return ["<span class='text-error-500'>Root access denied</span>"]
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
                    return ["<span class='text-warning-500'>Directory not found</span>"]
                }
                pwd = path
            }

            return []
        },
        clear: () => {
            history = default_message
            return []
        },
        cat: (file: string) => {
            let path = [...pwd, ...file.split("/").filter((p) => p != "")]
            let _dir = directories

            path.forEach((p :string) => {
                if (_dir == null) {
                    return ["<span class='text-warning-500'>File not found</span>"]
                }

                if (!_dir[p]) {
                    return ["<span class='text-warning-500'>File not found</span>"]
                }

                _dir = _dir[p]
            })

            if (_dir._type != "file") {
                return ["<span class='text-warning-500'>File not found</span>"]
            }

            return _dir.content
        },
        about: () => {
            processCommand("cat /user/default/home/documents/about.txt")
        },
        license: () => {
            processCommand("cat /user/default/home/documents/license.txt")
        },
        exit: () => {
            self.open = false
        },
        start: (app: string) => {
            if (windows[app]) {
                windows[app].onOpen()
                return ["<span class='text-success-500'>Application started</span>"]
            } else {
                return ["<span class='text-error-500'>Application not found</span>"]
            }
        }
        
    }


    let input = "";

    function processCommand(command: string) {
        let args = command.split(" ");
        let cmd = args[0];
        
        if (cmd in commands) {
            let results = commands[cmd](...args.slice(1));
            if (!results) return;

            let offset = 0;
            results.forEach((entry: string) => {
                setTimeout(() => {
                    history = [...history, entry];
                }, offset);
                offset += Math.floor(Math.random() * 50) + 50;
            });
        } else {
            history = [...history, `<span class='text-error-500'>Command not found: ${cmd}</span>`];
        }
    }

    function handleInput(event: KeyboardEvent) {
        if (event.key === "Enter") {
            history = [...history, `<span class='text-surface-400'>/${pwd.join("/")}> ${input}</span>`];
            processCommand(input);
            input = "";

            let cmd = document.getElementById("console");
            if (!cmd) { return }

            cmd.scrollTop = cmd.scrollHeight;
        }
    }

    let activeInterval: any = null;
    onMount(() => {
        activeInterval = setInterval(() => {
            let cmd = document.getElementById("console");
            if (!cmd) { return }

            if (cmd.scrollHeight - cmd.scrollTop < cmd.clientHeight + 50) {
                cmd.scrollTop = cmd.scrollHeight;
            }
        }, 100)
    });

    onDestroy(() => {
        clearInterval(activeInterval)
    })
</script>

<div class="p-3 scroll-smooth" style="width: 600px;">
    <div class="flex flex-col opacity-80 h-80 overflow-y-scroll" id="console">
        {#each history as item}
        <div>
            {#if item == ""}
                <p class="opacity-0 select-none">-</p>
            {:else}
                <p>{@html item}</p>
            {/if}
        </div>
        {/each}
        <div class="flex text-surface-400 w-full">
            <p class="whitespace-nowrap pr-1">/{pwd.join("/")}&gt</p>
            <div class="w-full">
                <input type="text" class="outline-none !bg-transparent w-full border-b border-b-surface-400"
                    on:keydown={handleInput} bind:value={input} />
            </div>
        </div>
        
    </div>
</div>
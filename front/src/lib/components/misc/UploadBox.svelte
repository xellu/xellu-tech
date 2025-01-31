<script lang="ts">
    import { getToastStore } from "@skeletonlabs/skeleton";
    import { slide } from "svelte/transition";

    const toast = getToastStore();

    let file: File | null = null;
    let progress: number = -1;

    const fileIcons = [
        {
            ext: ["png", "jpg", "jpeg", "gif", "webp"],
            icon: "image"
        },
        {
            ext: ["mp4", "webm", "avi", "mkv", "flv", "mov"],
            icon: "movie"
        },
        {
            ext: ["mp3", "wav", "flac", "ogg", "m4a"],
            icon: "music_note"
        },
        {
            ext: ["zip", "rar", "7z", "tar", "gz", "xz", "bz2", "rar4"],
            icon: "package"
        },
        {
            ext: [
                "js", "ts", "cjs", "html", "css", "pcss", "postcss", "tsx", "py", "pyw", "env", "php", "json", "jsonc",
                "bson", "db", "sql", "sh", "bat", "cmd", "ps1", "psm1", "psd1", "ps1xml", "pssc", "xml", "yaml", "yml", "toml",
                "ini", "cfg", "conf", "md", "markdown", "rst", "txt", "log", "csv", "tsv", "dat", "data", "bin", "exe", "dll",
                "lib", "obj", "o", "a", "so", "dylib", "dll", "pdb", "class", "jar", "war", "ear", "java", "kt", "kts", "ktm",
                "go", "rs", "rb", "r", "lua", "pl", "pm", "tcl", "awk", "sed", "asm", "s", "h", "hpp", "cpp", "cxx", "cc", "cs"
            ],
            icon: "code_blocks"
        }
    ]

    function handleClickEvent() {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = '*';
        input.onchange = (e) => {
            file = input.files?.[0] || null;
            try { upload() }
            catch (e) { 
                progress = -1;
                toast.trigger({
                    message: "Upload failed",
                    background: "variant-soft-error"
                })
            }

            input.remove();
        }

        input.click();
    }

    async function upload() {
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', `/api/v2/files/upload`, true);

        xhr.upload.onprogress = (event) => {
            if (event.lengthComputable) {
                progress = (event.loaded / event.total) * 100;
            }
        };

        xhr.onload = () => {
            const data = JSON.parse(xhr.responseText);
            if (xhr.status >= 200 && xhr.status < 300) {
                setTimeout(() => {
                    progress = -1;
                    file = null;
                }, 1000);
                toast.trigger({
                    message: "Link copied to clipboard",
                    background: "variant-soft-success"
                });
                navigator.clipboard.writeText(data.url);
            } else {
                setTimeout(() => {
                    progress = -1;
                    file = null;
                }, 1000);
                toast.trigger({
                    message: data.error || "Upload failed",
                    background: "variant-soft-error"
                });
            }
        };

        xhr.onerror = () => {
            setTimeout(() => {
                progress = -1;
                file = null;
            }, 1000);
            toast.trigger({
                message: "Upload failed",
                background: "variant-soft-error"
            });
        };

        xhr.send(formData);
    }
</script>

<button class="glass rounded-xl p-3 flex flex-col group items-center justify-center cursor-pointer w-full"
    on:drop={(e) => {
        if (progress !== -1) return;
        if (!e.dataTransfer?.files) return;

        e.preventDefault();
        file = e.dataTransfer?.files[0] || null;
        try { upload() }
        catch (e) { 
            progress = -1;
            file = null;
            toast.trigger({
                message: "Upload failed",
                background: "variant-soft-error"
            })
        }
    }}
    on:dragover={(e) => e.preventDefault()}
    on:click={() => {
        if (progress !== -1) return;
        handleClickEvent();
    }}
>
    <span class="material-symbols-outlined text-5xl opacity-70 group-hover:opacity-100 duration-300">
        {file ? (fileIcons.find(i => i.ext.includes(file?.name.split('.').pop() || "")) || {icon: 'draft'}).icon : 'upload'}
    </span>
    <p class="uppercase text-xs opacity-70 group-hover:opacity-100 duration-300 max-w-72 overflow-hidden text-ellipsis whitespace-nowrap mt-3">
        {file ? file.name : 'Drag and drop files here to upload'}
    </p>
    {#if progress >= 0}
    <div class="w-full bg-surface-400/50 rounded-full overflow-hidden mt-2" transition:slide>
        <div class="{progress == 100 ? 'bg-success-500 animate-pulse' : 'bg-primary-500'} h-1.5 duration-150 rounded-full min-w-1.5" style="width: {Math.round(progress)}%"></div>
    </div>
    {/if}
</button>
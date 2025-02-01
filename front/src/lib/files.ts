type FileType = {
    ext: string[],
    icon: string,
    category: string
}

const fileTypes: FileType[] = [
    {
        ext: ["png", "jpg", "jpeg", "gif", "webp"],
        icon: "image",
        category: "Images"
    },
    {
        ext: ["mp4", "webm", "avi", "mkv", "flv", "mov"],
        icon: "movie",
        category: "Videos"
    },
    {
        ext: ["mp3", "wav", "flac", "ogg", "m4a"],
        icon: "music_note",
        category: "Music"
    },
    {
        ext: ["zip", "rar", "7z", "tar", "gz", "xz", "bz2", "rar4"],
        icon: "package",
        category: "Archives"
    },
    {
        ext: [
            "js", "ts", "cjs", "html", "css", "pcss", "postcss", "tsx", "py", "pyw", "env", "php", "json", "jsonc",
            "bson", "db", "sql", "sh", "bat", "cmd", "ps1", "psm1", "psd1", "ps1xml", "pssc", "xml", "yaml", "yml", "toml",
            "ini", "cfg", "conf", "md", "markdown", "rst", "txt", "log", "csv", "tsv", "dat", "data", "bin", "exe", "dll",
            "lib", "obj", "o", "a", "so", "dylib", "dll", "pdb", "class", "jar", "war", "ear", "java", "kt", "kts", "ktm",
            "go", "rs", "rb", "r", "lua", "pl", "pm", "tcl", "awk", "sed", "asm", "s", "h", "hpp", "cpp", "cxx", "cc", "cs"
        ],
        icon: "code_blocks",
        category: "Code"
    }
]

const getFileType = (fileName: string): FileType => {
    for (let i = 0; i < fileTypes.length; i++) {
        const type = fileTypes[i];
        for (let j = 0; j < type.ext.length; j++) {
            if (fileName.endsWith("." + type.ext[j])) {
                return type;
            }
        }
    }
    return {
        ext: ["*"],
        icon: "draft",
        category: "Other"
    };
}

export {
    type FileType,

    fileTypes,
    getFileType
}
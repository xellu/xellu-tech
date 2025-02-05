<script lang="ts">
    import Embed from '$lib/components/Embed.svelte';
    import Loader from '$lib/components/Loader.svelte';
    import UcHeading from '$lib/components/UCHeading.svelte';
  
    import TextFile from '$lib/components/previews/TextFile.svelte';

    import { getFileType, getFileExtension } from '$lib/files';
    import { toAgo, toDataUnit } from '$lib/scripts/Utils';

    import { getToastStore } from '@skeletonlabs/skeleton';

    const toast = getToastStore();

    export let data;
    const { props } = data;

    type RemoteAliasLookup = {
        fileUrl: string,
        fileName: string,
        size: number,
        uploadedAt: number,
        
        embed: {
            enabled: boolean
            title: string,
            description: string | null,
            siteName: string | null
            color: string
        },
        author: {
            "_id": string,
            "username": string
        }
    }

    let file: RemoteAliasLookup;
    let error: string | null | undefined;
    let alias: string;

    $: file = props.data;
    $: error = props.error;
    $: alias = props.alias;
</script>

<svelte:head>
    <title>{file ? `${getFileExtension(file.fileName)} file uploaded by ${file.author.username}` : ''}</title>

    <!-- {#if file && file.embed.enabled}
        <Embed
            title={file.embed.title}
            description={file.embed.description}
            siteName={file.embed.siteName}
            color={file.embed.color}
            
            icon="customLarge"
            iconUrl={file.fileUrl}
            route={`https://xellu.tech/upload/${alias}`}
        />
    {:else if file && getFileType(file.fileName)}
        <Embed
            title={null}
            description={null}
            siteName={null}
            color="#000"
            disable={true}

            icon="customLarge"
            iconUrl={file.fileUrl}
            route={`https://xellu.tech/upload/${alias}`}
        />
    {/if} -->

    {#if !file}
        <Embed
            title = "File not found"
            description = "The file you are looking for does not exist or has been removed."
            color = "#FF442F"
            icon="none"    
        />
    {:else if file.embed.enabled}
        <Embed
            title = {file.embed.title || null}}
            description = {file.embed.description || null}
            siteName = {file.embed.siteName || null}
            color = {file.embed.color}

            icon = {getFileType(file.fileName).format == "video" ? "video" : "customLarge"}
            iconUrl = {file.fileUrl}
            route = {`https://xellu.tech/upload/${alias}`}
        />
    {:else}
        <Embed
            siteName = {null}
            disable = {true}

            icon = {getFileType(file.fileName).format == "video" ? "video" : "customLarge"}
            iconUrl = {file.fileUrl}
            route = {`https://xellu.tech/upload/${alias}`}
        />
    {/if}
</svelte:head>

<div class="w-full h-screen flex items-center justify-center flex-col">
    {#if !file && !error}
        <Loader />
    {:else if error}
        <Loader error={error} />
    {:else}
        <div class="flex items-center justify-between p-3">
            <div>

                <!-- details -->
                <div class="flex items-end justify-between mb-3 max-md:flex-col max-md:px-1">
                    <div class="flex items-center gap-3">
                        <UcHeading>{file.fileName}</UcHeading>
                        <span class="badge variant-filled-tertiary font-mono">{toDataUnit(file.size)}</span>
                        <div class="flex items-center text-sm select-none opacity-70">
                            <span class="material-symbols-outlined scale-75">person</span>
                            <span>{file.author.username} • {toAgo(file.uploadedAt*1000)}</span>
                        </div>
                    </div>

                    <div class="flex items-center gap-2 glass px-2 text-tertiary-500 py-0.5 rounded-xl">
                        <button class="p-1 aspect-square w-8 btn" on:click={() => {
                            navigator.clipboard.writeText(window.location.href);
                            toast.trigger({
                                message: 'Link copied to clipboard',
                                background: 'variant-soft-success'
                            });
                        }}>
                            <span class="material-symbols-outlined">share</span>
                        </button>
                        <a href="{file.fileUrl}" target="_blank" rel="noopener noreferrer">
                            <button class="p-1 aspect-square w-8 btn">
                                <span class="material-symbols-outlined">download</span>
                            </button>
                        </a>
                    </div>
                </div>

                <!-- preview -->
                <div class="flex aspect-video rounded-xl overflow-hidden glass w-[90vw] md:w-[512px] lg:w-[896px] p-3">
                    <div class="flex-grow"></div>
                    
                    <!-- file previews -->
                    
                    <!-- image -->
                    {#if getFileType(file.fileName).format === 'image'}
                        <img src={file.fileUrl} alt={file.fileName} class="object-cover" />
                    
                    <!-- video -->
                    {:else if getFileType(file.fileName).format === 'video'}
                        <video src={file.fileUrl} controls class="object-cover">
                            <track kind="captions" />
                        </video>
                    
                    <!-- audio -->
                    {:else if getFileType(file.fileName).format === 'audio'}
                        <div class="h-full flex items-center justify-center">
                            <audio src={file.fileUrl} controls class="object-cover" />
                        </div>

                    <!-- text -->
                    {:else if getFileType(file.fileName).format === 'text'}
                        <TextFile downloadUrl={file.fileUrl} name={file.fileName} />

                    <!-- preview unavailable -->
                    {:else}
                        <div class="h-full flex flex-col items-center justify-center text-white/70">
                            <span class="material-symbols-outlined text-9xl">{getFileType(file.fileName).icon}</span>
                            <p class="uppercase font-bold text-sm">No preview available</p>
                        </div>
                    {/if}
                    <div class="flex-grow"></div>
                </div>

            </div>
        </div>
    {/if}
</div>
<script lang="ts">
    import Loader from "$lib/components/Loader.svelte";
    import UcHeading from "$lib/components/UCHeading.svelte";
    import GalleryDisplay from "$lib/components/misc/GalleryDisplay.svelte";

    import { onMount } from "svelte";
    import { slide } from "svelte/transition";
    import { getToastStore } from "@skeletonlabs/skeleton";

    import { Account, AuthState, type AuthStateType, type AccountType } from "$lib/scripts/Auth";
    import { toDataUnit, toAgo } from "$lib/scripts/Utils";
    import { getFileType, getFileExtension, fileTypes, getCategoryIcon } from "$lib/files";
    import { Logger } from "$lib/scripts/Logger";

    const toast = getToastStore();
    const logger = new Logger("Gallery");

    let User: AccountType | null;
    let UserState: AuthStateType = { loggedIn: false, loading: true};

    Account.subscribe((value) => {
        User = value;
    })

    AuthState.subscribe((value) => {
        UserState = value;
    })

    let loading = true;
    type FileLookup = {
        fullName: string,
        originalName: string,
        contentType: string,

        size: number,
        uploadedAt: number,
    }

    let categories: {[key: string]: FileLookup[]} = {}
    let selectedCategory: string = "*";
    let allCategories: string[] = [];

    let shownFiles: FileLookup[] = [];
    let cache: {expire: number, data: FileLookup[]};

    let refreshGallery: any = () => {};

    async function loadUploads(): Promise<FileLookup[]> {
        const r = await fetch("/api/v2/files/gallery")
        if (r && r.status !== 200) {
            toast.trigger({
                message: r.status == 429 ? "You are being rate limited, try again later" : "Failed to load uploads",
                background: "variant-soft-error"
            })   
        }

        const data = await r.json();

        return data.files as FileLookup[];
    }

    function sortFilesByCategory() {
        categories = {};

        cache.data.forEach((file) => {
            const category = getFileType(file.fullName).category;

            if (!categories[category]) {
                categories[category] = [];
            }

            categories[category].push(file);
        })
    }

    function loadCategories() {
        fileTypes.forEach((type) => {
            if (type.category && !allCategories.includes(type.category)) {
                allCategories.push(type.category);
            }
        })
        allCategories = allCategories; //force reactivity
    }

    function processShownFiles() {
        shownFiles = [];
        if (selectedCategory == "*") {
            for (const key in categories) {
                shownFiles.push(...categories[key]);
            }
        } else {
            shownFiles = categories[selectedCategory] || [];
        }

        shownFiles.sort((a, b) => {
            return b.uploadedAt - a.uploadedAt;
        })

        refreshGallery();
    }

    onMount(async () => {
        loadCategories();

        const cached = localStorage.getItem("galleryCache");
        if (cached && JSON.parse(cached).expire > Date.now()) {
            cache = JSON.parse(cached);
            logger.ok("Loaded data from cache");
        } else {
            const data = await loadUploads();

            cache = {expire: Date.now() + 1000 * 60 * 3, data: data}; //3 minutes
            localStorage.setItem("galleryCache", JSON.stringify(cache));
            logger.ok("Loaded data from api");
        }

        sortFilesByCategory();
        processShownFiles();
        loading = false;
    })
</script>
{#if !loading}
<div class="my-6">
    <UcHeading>Categories to Browse</UcHeading>
    <div class="grid grid-cols-2 md:grid-cols-3 gap-2 mt-3" transition:slide>
        {#each allCategories as c}
            <button class="btn btn-sm {selectedCategory == c ? 'text-tertiary-500' : selectedCategory == '*' ? '' : 'opacity-60'} duration-300 flex-grow" on:click={() => {
                selectedCategory == c ? selectedCategory = "*" : selectedCategory = c;

                processShownFiles();
            }}>
                    <span class="material-symbols-outlined">{getCategoryIcon(c)}</span>
                    <p class="text-xs font-semibold uppercase w-32 text-left">{c}</p>
            </button>
        {/each}
    </div>

    <div class="{selectedCategory == '*' ? 'opacity-0' : 'opacity-60'} duration-150 select-none mt-1">
        <p class="text-xs ml-3">Click on an already selected category to clear the filter</p>
    </div>
</div>
{/if}


<div>
    {#if loading}
        <div class="w-full"> <Loader variant="tertiary" /> </div>
    {:else}
    
        <!-- <p><span class="text-tertiary-500">present:</span> {Object.keys(categories)}</p>
        <p><span class="text-tertiary-500">all:</span> {allCategories}</p>
        <p><span class="text-tertiary-500">selected:</span> {selectedCategory}</p> -->

        <GalleryDisplay files={shownFiles} bind:refresh={refreshGallery} />
    {/if}
</div>

<!-- uhh ill finish this l8ter -->
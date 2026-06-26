<script lang="ts">
	import './layout.css';

	import Navbar from "$lib/components/layout/Navbar.svelte";
	
	let { children } = $props();
	import { addIcon, Icons } from '$lib/stores/IconStore';
	
</script>

<svelte:head>
	<link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names={$Icons}"
    />
</svelte:head>

<Navbar />

{@render children()}

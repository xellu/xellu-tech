<script lang="ts">
	import './layout.css';

	import { Navbar } from '$lib/components/layout/Navbar';
	import { Icons } from '$lib/stores/IconStore';

	import { toaster } from '$lib/stores/Toaster';
	import { Toast } from '@skeletonlabs/skeleton-svelte';
	
	let { children } = $props();
</script>

<svelte:head>
	<link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names={$Icons}"
    />
</svelte:head>

<Navbar.Root />

{@render children()}

<Toast.Group {toaster}>
	{#snippet children(toast)}
		<Toast toast={toast}>
			<Toast.Message>
			<Toast.Title>{toast.title}</Toast.Title>
			<Toast.Description>{toast.description}</Toast.Description>
			</Toast.Message>
			<Toast.CloseTrigger />
		</Toast>
	{/snippet}
</Toast.Group>
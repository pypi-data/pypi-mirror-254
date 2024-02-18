<script lang="ts">
	import Copy from "./Copy.svelte";
	import RemoveTags from "./RemoveTags.svelte";
    import { createEventDispatcher } from 'svelte';

	export let value: string;
	export let show_copy_button: boolean = false;
    export let show_remove_tags_button: boolean = false;
    const dispatch = createEventDispatcher()

</script>

<div>
    {#if show_remove_tags_button}
        <RemoveTags on:clear={() => dispatch("clear")}/>
    {/if}
    {#if show_copy_button}
        <Copy {value} />
    {/if}
</div>

<style>
	div {
		display: flex;
		position: absolute;
		top: var(--block-label-margin);
		right: var(--block-label-margin);
		align-items: center;

		z-index: var(--layer-2);
		transition: 150ms;
		box-shadow: var(--shadow-drop);
		border: 1px solid var(--border-color-primary);
		border-top: none;
		border-right: none;
		border-radius: var(--block-label-right-radius);
		background: var(--block-label-background-fill);
		overflow: hidden;
		color: var(--block-label-text-color);
		font: var(--font);
		font-size: var(--button-small-text-size);
	}
</style>
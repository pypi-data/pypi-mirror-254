<script lang="ts">
	import { Check } from "@gradio/icons";
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher()
</script>
 
<button
    on:click={() => dispatch('clear')}
    title="Remove highlights"
    aria-roledescription="Remove highlights"
    aria-label="Remove highlights"
>
    <Check />
</button>

<style>
	button {
		position: relative;
		cursor: pointer;
		padding: 5px;
		width: 22px;
		height: 22px;
        background-color: green;
	}
</style>
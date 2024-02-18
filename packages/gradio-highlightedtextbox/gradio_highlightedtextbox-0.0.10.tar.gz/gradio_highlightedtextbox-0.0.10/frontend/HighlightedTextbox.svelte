<script lang="ts">
	import {
		beforeUpdate,
		afterUpdate,
		createEventDispatcher,
	} from "svelte";
	import BlockTitleWithHighlights from "./BlockTitleWithHighlights.svelte";
	import Widgets from "./Widgets.svelte";
	import type { SelectData } from "@gradio/utils";
	import { get_next_color } from "@gradio/utils";
	import { correct_color_map, getParentCursorPosition, getNodeAndOffset } from "./utils";

	const browser = typeof document !== "undefined";
	export let value: [string, string | null][] = [];
    export let value_is_output: boolean = false;
	export let label: string;
	export let legend_label: string;
	export let info: string | undefined = undefined;
	export let show_label = true;
	export let show_legend = false;
	export let show_legend_label = false;
	export let container = true;
	export let color_map: Record<string, string> = {};
	export let show_copy_button = false;
	export let show_remove_tags_button = false;
    export let disabled: boolean;
	
	let el: HTMLDivElement;
	let el_text: string = "";
	let marked_el_text: string = "";
	let ctx: CanvasRenderingContext2D;
	let current_color_map: Record<string, string> = !color_map || Object.keys(color_map).length === 0 ? {} : color_map;
	let _color_map: Record<string, { primary: string; secondary: string }> = {};
	let copied = false;
	let tags_removed = false;
	let timer: ReturnType<typeof setTimeout>;
    let can_scroll: boolean;
	let tagged_text: string = "";

	function set_color_map(): void {
		// if a label in the color map is not in the value, remove it from the color map
		for (let label in current_color_map) {
			if (!value.map(([_, label]) => label).includes(label)) {
				delete current_color_map[label];
			}
		}
		if (value.length > 0) {
			for (let [_, label] of value) {
				if (label !== null && !(label in current_color_map)) {
					let color = get_next_color(Object.keys(current_color_map).length);
					current_color_map[label] = color;
				}
			}
		}
		_color_map = correct_color_map(current_color_map, browser, ctx);
	}

	function set_text_from_value(as_output: boolean): void {
		if (value.length > 0 && as_output) {
			el_text = value.map(([text, _]) => text).join("");
			marked_el_text = value.map(([text, category]) => {
				if (category !== null) {
					return `<mark class="hl ${category}" style="background-color:${_color_map[category].secondary}">${text}</mark>`;
				} else {
					return text;
				}
			}).join("");
			tagged_text = value.map(([text, category]) => {
				if (category !== null) {
					return `<${category}>${text}</${category}>`;
				} else {
					return text;
				}
			}).join("");
		}
	}

	$: set_color_map();
	$: set_text_from_value(true);

	const dispatch = createEventDispatcher<{
		change: [string, string | null][];
		input: [string, string | null][];
		submit: undefined;
		blur: undefined;
		select: SelectData;
		focus: undefined;
		clear: undefined;
	}>();

    beforeUpdate(() => {
		can_scroll = el && el.offsetHeight + el.scrollTop > el.scrollHeight - 100;
	});

	function handle_change(): void {
		checkAndRemoveHighlight();
		set_value_from_marked_span();
		dispatch("change", value);
		if (!value_is_output) {
			dispatch("input", value);
		}
	}
	afterUpdate(() => {
		set_color_map();
		set_text_from_value(value_is_output);
		value_is_output = false;
	});

	function set_value_from_marked_span(): void {
		let new_value: [string, string | null][] = [];
		let text = "";
		let category = null;
		let in_tag = false;
		let tag = "";
		// Replace &nbsp;, &amp;, &lt;, &gt; with their corresponding characters
		let clean_marked_text = marked_el_text.replace(/&nbsp;|&amp;|&lt;|&gt;/g, function(m) {
			return {"&nbsp;":" ", "&amp;":"&", "&lt;":"<", "&gt;":">"}[m];
		});
		for (let i = 0; i < clean_marked_text.length; i++) {
			let char = clean_marked_text[i];
			if (char === "<") {
				in_tag = true;
				if (text) {
					new_value.push([text, category]);
				}
				text = "";
				category = null;
			} else if (char === ">") {
				in_tag = false;
				if (tag.slice(0, 4) === "mark") {
					let match = /class="hl ([^"]+)"/.exec(tag);
					category = match ? match[1] : null;
				}
				tag = "";
			} else if (in_tag) {
				tag += char;
			} else {
				text += char;
			}
		}
		if (text) {
			new_value.push([text, category]);
		}
		value = new_value;
	}

	function handle_remove_tags(): void {
		marked_el_text = el_text;
		handle_change();
		tags_removed = true;
		dispatch("clear");
	}

	// Method to remove highlight if cursor is inside
	function checkAndRemoveHighlight() {
		const selection = window.getSelection();
		const cursorPosition = selection.anchorOffset;
		if (selection.rangeCount > 0) {
			var currParent = selection.getRangeAt(0).commonAncestorContainer.parentElement;
			if (currParent && currParent.tagName.toLowerCase() === 'mark') {
				const text = currParent.textContent;
				// replace the mark tag with its text content
				var textContainer = currParent.parentElement;
				var newTextNode = document.createTextNode(text);
				textContainer.replaceChild(newTextNode, currParent);
				marked_el_text = textContainer.innerHTML;
				// set the cursor position to the same position as before
				var range = document.createRange()
				var newSelection = window.getSelection()
				const newCursorPosition = cursorPosition + getParentCursorPosition(textContainer)
				var nodeAndOffset = getNodeAndOffset(textContainer, newCursorPosition);
				range.setStart(nodeAndOffset.node, nodeAndOffset.offset);
				range.setEnd(nodeAndOffset.node, nodeAndOffset.offset);
				newSelection.removeAllRanges();
				newSelection.addRange(range);
			}
		}
	}
</script>

<label class:container for="highlighted-textbox">
	<BlockTitleWithHighlights {show_label} {show_legend} {show_legend_label} {legend_label} {_color_map} {info}>{label}</BlockTitleWithHighlights>
	<Widgets
		{show_copy_button}
		show_remove_tags_button={show_remove_tags_button && !tags_removed}
		value={tagged_text}
		on:clear={handle_remove_tags}
	/>
    {#if disabled}
        <div 
            class="textfield"
            data-testid="highlighted-textbox"
            contenteditable="false"
            bind:this={el}
            bind:textContent={el_text}
            bind:innerHTML={marked_el_text}
        />
    {:else}
<div
	class="textfield"
	data-testid="highlighted-textbox"
	contenteditable="true"
	role="textbox"
	tabindex="0"
	bind:this={el}
	bind:textContent={el_text}
	bind:innerHTML={marked_el_text}
	on:blur
	on:keypress
	on:select
	on:scroll
	on:input={handle_change}
	on:focus
	on:change={handle_change}
/>
    {/if}
</label>

<style>
	label {
		display: block;
		width: 100%;
	}

	.container {
		display: flex;
		flex-direction: column;
		gap: var(--spacing-sm);
	}

	.textfield {
		box-sizing: border-box;
		outline: none !important;
		box-shadow: var(--input-shadow);
		padding: var(--input-padding);
		border-radius: var(--radius-md);
		background: var(--input-background-fill);
		background-color: transparent;
		font-weight: var(--input-text-weight);
		font-size: var(--input-text-size);
		width: 100%;
		line-height: var(--line-sm);
		word-break: break-word;
		border: var(--input-border-width) solid var(--input-border-color);
		cursor: text;
		white-space: break-spaces;
	}

	.textfield:focus {
		box-shadow: var(--input-shadow-focus);
		border-color: var(--input-border-color-focus);
	}

	:global(mark) {
		border-radius: 3px;
	}
</style>
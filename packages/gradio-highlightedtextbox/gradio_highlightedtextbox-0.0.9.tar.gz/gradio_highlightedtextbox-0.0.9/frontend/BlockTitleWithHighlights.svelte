<script lang="ts">
	export let show_label = true;
    export let show_legend = true;
    export let show_legend_label = true;
    export let legend_label: string | undefined = "Highlights:";
    export let _color_map: Record<string, { primary: string; secondary: string }> = {};
	export let info: string | undefined = undefined;
</script>

<div class="title-container">
    <span
        class:sr-only={!show_label}
        class:hide={!show_label}
        class:has-info={info != null}
        data-testid="block-info"
    >
        <slot />
    </span>
    {#if Object.keys(_color_map).length !== 0}
        <span
            class="legend-separator"
            class:hide={!show_legend || !show_label}
            class:has-info={info != null}
        >
        ·
        </span>
        <div
            class="category-legend"
            data-testid="highlighted-text:category-legend"
            class:hide={!show_legend}
        >
            <span class:hide={!show_legend_label} class:has-info={info != null}>
                {legend_label}
            </span>
            {#each Object.entries(_color_map) as [category, color], i}
                <!-- svelte-ignore a11y-no-static-element-interactions -->
                <div class="category-label" style={"background-color:" + color.secondary} class:has-info={info != null}>
                    {category}
                </div>
            {/each}
        </div>
    {/if}
</div>
{#if info}
    <div class="title-with-highlights-info">
        {info}
    </div>
{/if}

<style>
	span.has-info {
		margin-bottom: var(--spacing-xs);
	}
	span:not(.has-info) {
		margin-bottom: var(--spacing-lg);
	}
	span {
		display: inline-block;
		position: relative;
		z-index: var(--layer-4);
		border: solid var(--block-title-border-width)
			var(--block-title-border-color);
		border-radius: var(--block-title-radius);
		background: var(--block-title-background-fill);
		padding: var(--block-title-padding);
		color: var(--block-title-text-color);
		font-weight: var(--block-title-text-weight);
		font-size: var(--block-title-text-size);
		line-height: var(--line-sm);
	}

	.hide {
		display: none !important;
	}

    .category-legend {
		display: flex;
		flex-wrap: wrap;
		gap: var(--spacing-sm);
		color: black;
	}

	.category-label {
		border-radius: var(--radius-xs);
		padding-right: var(--size-2);
		padding-left: var(--size-2);
		font-weight: var(--weight-semibold);
	}

    .category-label.has-info {
		margin-bottom: var(--spacing-xs);
	}
	.category-label:not(.has-info) {
		margin-bottom: var(--spacing-lg);
	}

	.title-container {
        display: flex;
    }

    .legend-separator {
        margin: 0 var(--spacing-md) 0 var(--spacing-md);
    }

    .title-with-highlights-info {
		margin-bottom: var(--spacing-xs);
		color: var(--block-info-text-color);
		font-weight: var(--block-info-text-weight);
		font-size: var(--block-info-text-size);
		line-height: var(--line-sm);
    }
</style>

<svelte:options accessors={true} />

<script context="module" lang="ts">
	export { default as Webcam } from "./shared/Webcam.svelte";
	export { default as BaseImageUploader } from "./shared/ImageUploader.svelte";
	export { default as BaseStaticImage } from "./shared/ImagePreview.svelte";
	export { default as BaseExample } from "./Example.svelte";
	export { default as BaseImage } from "./shared/Image.svelte";
</script>

<script lang="ts">
	import type { Gradio, SelectData } from "@gradio/utils";
	import StaticImage from "./shared/ImagePreview.svelte";

	import { Block, BlockLabel } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { FileData } from "@gradio/client";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { Image } from "@gradio/icons";
	import { normalise_file } from "@gradio/client";

	type sources = "upload" | "webcam" | "clipboard" | null;

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: FileData | null = null;
	$: _value = normalise_file(value, root, proxy_url);
	export let label: string;
	export let show_label: boolean;
	export let show_download_button: boolean;
	export let root: string;
	export let proxy_url: null | string;

	export let height = 600;
	export let width: number | undefined;

	export let _selectable = false;
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let show_share_button = false;
	export let sources: ("clipboard" | "webcam" | "upload")[] = [
		"upload",
		"clipboard",
		"webcam"
	];
	export let interactive: boolean;
	export let streaming: boolean;
	export let pending: boolean;
	export let mirror_webcam: boolean;

	export let gradio: Gradio<{
		change: never;
		error: string;
		edit: never;
		stream: never;
		drag: never;
		upload: never;
		clear: never;
		select: SelectData;
		share: ShareData;
	}>;

	$: url = _value?.url;
	$: url, gradio.dispatch("change");

	let values: null | FileData[] = [];
	$: if (_value) { values.unshift(_value) };
	let dragging: boolean;
</script>

<Block 
	{visible}
	variant={"solid"}
	border_mode={dragging ? "focus" : "base"}
	padding={false}
	{elem_id}
	{elem_classes}
	{height}
	{width}
	allow_overflow={false}
	{container}
	{scale}
	{min_width}
	>
<div class="wrapper">
	{#if show_label}
	<BlockLabel
		{show_label}
		Icon={Image}
		float={false}
		label={label || "ImageFeed"}
	/>
{/if}

{#each values as _value (_value)}

<div class="image-component-wrapper">
	<Block
		{visible}
		variant={"solid"}
		border_mode={dragging ? "focus" : "base"}
		padding={false}
		{elem_id}
		{elem_classes}
		height={null}
		{width}
		allow_overflow={true}
		{container}
		{scale}
		{min_width}
	>
		<StaticImage
			on:select={({ detail }) => gradio.dispatch("select", detail)}
			on:share={({ detail }) => gradio.dispatch("share", detail)}
			on:error={({ detail }) => gradio.dispatch("error", detail)}
			value={_value}
			{label}
			show_label={false}
			{show_download_button}
			selectable={_selectable}
			{show_share_button}
			i18n={gradio.i18n}
		/>		
	</Block>
</div>


{/each}
</div>
</Block>

<style>
	.wrapper {
		overflow: auto;
		display: flex;
		position: relative;
		flex-direction: column;
		align-items: start;
		width: 100%;
		height: 100%;
	}
	.image-component-wrapper {
		margin-top: 1rem !important;
		margin-bottom: 1rem !important;
		width: 96%;
		margin-left: auto;
		margin-right: auto;
	}
</style>
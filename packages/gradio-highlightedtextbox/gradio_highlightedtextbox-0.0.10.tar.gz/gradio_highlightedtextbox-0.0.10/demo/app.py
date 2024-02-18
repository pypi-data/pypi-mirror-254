import gradio as gr
from gradio_highlightedtextbox import HighlightedTextbox


def convert_tagged_text_to_highlighted_text(
    tagged_text: str,
    tag_id: str | list[str],
    tag_open: str | list[str],
    tag_close: str | list[str],
) -> list[tuple[str, str | None]]:
    return HighlightedTextbox.tagged_text_to_tuples(
        tagged_text, tag_id, tag_open, tag_close
    )


def convert_highlighted_text_to_tagged_text(
    highlighted_text: dict[str, str | list[tuple[str, str | None]]],
    tag_id: str | list[str],
    tag_open: str | list[str],
    tag_close: str | list[str],
) -> str:
    return HighlightedTextbox.tuples_to_tagged_text(
        highlighted_text["data"], tag_id, tag_open, tag_close
    )


def show_info(
    highlighted_text: dict[str, str | list[tuple[str, str | None]]],
    tag_id: str | list[str],
    tag_open: str | list[str],
    tag_close: str | list[str],
    msg: str,
) -> None:
    gr.Info(
        f"{msg}: {HighlightedTextbox.tuples_to_tagged_text(highlighted_text['data'], tag_id, tag_open, tag_close)}"
    )


initial_text = "It is not something to be ashamed of: it is no different from the <a>personal fears</a> and <b>dislikes</b> of other things that <c>manny peopl</c> have."

with gr.Blocks() as demo:
    gr.Markdown("### Parameters to control the highlighted textbox:")
    with gr.Row():
        tag_id = gr.Dropdown(
            choices=["Error A", "Error B", "Error C"],
            value=["Error A", "Error B", "Error C"],
            multiselect=True,
            allow_custom_value=True,
            label="Tag ID",
            show_label=True,
            info="Insert one or more tag IDs to use in the highlighted textbox.",
        )
        tag_open = gr.Dropdown(
            choices=["<a>", "<b>", "<c>"],
            value=["<a>", "<b>", "<c>"],
            multiselect=True,
            allow_custom_value=True,
            label="Tag open",
            show_label=True,
            info="Insert one or more tags to mark the beginning of a highlighted section.",
        )
        tag_close = gr.Dropdown(
            choices=["</a>", "</b>", "</c>"],
            value=["</a>", "</b>", "</c>"],
            multiselect=True,
            allow_custom_value=True,
            label="Tag close",
            show_label=True,
            info="Insert one or more tags to mark the end of a highlighted section.",
        )
    gr.Markdown(
        """
### Example:

The following text is tagged using the parameters above to mark spans that will be highlighted.

Both the tagged text and the highlighted text are editable, so you can see how the changes in one affect the other.

Highlights will disappear if the highlighted text is edited. Modals will appear upon focus, change, and blur events on the highlighted text.
"""
    )
    with gr.Row():
        tagged = gr.Textbox(
            initial_text,
            interactive=True,
            label="Tagged text",
            show_label=True,
            info="Tagged text using the format above to mark spans that will be highlighted.",
        )
        high = HighlightedTextbox(
            convert_tagged_text_to_highlighted_text(
                tagged.value, tag_id.value, tag_open.value, tag_close.value
            ),
            interactive=True,
            label="Highlighted text",
            info="Textbox containing editable text with custom highlights.",
            show_legend=True,
            show_label=True,
            legend_label="Legend:",
            show_legend_label=True,
            show_remove_tags_button=True,
            show_copy_button=False,
        )

    # Functions

    tagged.input(
        fn=convert_tagged_text_to_highlighted_text,
        inputs=[tagged, tag_id, tag_open, tag_close],
        outputs=high,
    )
    high.input(
        fn=convert_highlighted_text_to_tagged_text,
        inputs=[high, tag_id, tag_open, tag_close],
        outputs=tagged,
    )
    high.focus(
        fn=show_info,
        inputs=[high, tag_id, tag_open, tag_close, gr.State("Focus")],
        outputs=None,
    )
    high.blur(
        fn=show_info,
        inputs=[high, tag_id, tag_open, tag_close, gr.State("Blur")],
        outputs=None,
    )
    high.clear(
        fn=show_info,
        inputs=[high, tag_id, tag_open, tag_close, gr.State("Remove tags")],
        outputs=None,
    )
    high.change(
        fn=show_info,
        inputs=[high, tag_id, tag_open, tag_close, gr.State("Change")],
        outputs=None,
    )

if __name__ == "__main__":
    demo.launch()

from string import Template


class Templates:
    PROMPT_TEMPLATE_FIX_TEXT = Template(
        """Fix all typos and casing and punctuation in this text, but preserve all new line characters:

    $text

    Return only the corrected text."""
    )

    PROMPT_TEMPLATE_GENERATE_TEXT = Template(
        """Generate a snarky paragraph with 3 sentences about the following topic:

    $text

    Return only the corrected text."""
    )

    PROMPT_TEMPLATE_SUMMARIZE_TEXT = Template(
        """Summarize the following text in 3 sentences:

    $text

    Return only the corrected text."""
    )

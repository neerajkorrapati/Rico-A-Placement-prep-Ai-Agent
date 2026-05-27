import re


def clean_markdown_json(raw_text: str) -> str:
    """
    Removes ```json ... ``` markdown wrappers.
    """

    match = re.search(
        r"```(?:json)?\s*([\s\S]*?)\s*```",
        raw_text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return raw_text.strip()
"""Create workflow annotations and logs for a GitHub Actions workflow run."""


from typing import Literal as _Literal

from actionman.protocol import Stringable as _Stringable


def debug(message: _Stringable, print_: bool = True) -> str:
    """Create a debug log.

    Parameters
    ----------
    message : actionman.protocol.Stringable
        The log message.
    print_ : bool, default: True
        Whether to directly print the debug log.

    Returns
    -------
    str
        The debug log.

    References
    ----------
    - [GitHub Docs: Workflow Commands for GitHub Actions: Setting a debug message](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-debug-message)
    """
    output = f"::debug:: {message}"
    if print_:
        print(output, flush=True)
    return output


def annotation(
    typ: _Literal["debug", "notice", "warning", "error"],
    message: _Stringable,
    title: _Stringable = "",
    filename: _Stringable = "",
    line_start: int = 0,
    line_end: int = 0,
    column_start: int = 0,
    column_end: int = 0,
    print_: bool = True,
) -> str:
    """Create a notice, warning, or error annotation.

    Parameters
    ----------
    typ : {"notice", "warning", "error"}
        The type of annotation to create.
    message : actionman.protocol.Stringable
        The annotation message.
    title : actionman.protocol.Stringable, optional
        The annotation title.
    filename : actionman.protocol.Stringable, optional
        Path to a file in the repository to associate the message with.
    line_start : int, optional
        The starting line number in the file specified by the 'filename' argument,
        to associate the message with.
    line_end : int, optional
        The ending line number in the file specified by the 'filename' argument,
        to associate the message with.
    column_start : int, optional
        The starting column number in the line specified by the 'line_start' argument,
        to associate the message with.
    column_end : int, optional
        The ending column number in the line specified by the 'line_start' argument,
        to associate the message with.
    print_ : bool, default: True
        Whether to directly print the annotation.

    Returns
    -------
    str
        The annotation.

    References
    ----------
    - [GitHub Docs: Workflow Commands for GitHub Actions: Setting a notice message](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-notice-message)
    - [GitHub Docs: Workflow Commands for GitHub Actions: Setting a warning message](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-warning-message)
    - [GitHub Docs: Workflow Commands for GitHub Actions: Setting an error message](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-error-message)
    """
    args = locals()
    output = f"::{typ} "
    args_added = False
    for arg_name, github_arg_name in (
        ("title", "title"),
        ("filename", "file"),
        ("line_start", "line"),
        ("line_end", "endLine"),
        ("column_start", "col"),
        ("column_end", "endColumn"),
    ):
        if args[arg_name]:
            output += f"{github_arg_name}={args[arg_name]},"
            args_added = True
    output = output.removesuffix("," if args_added else " ")
    output += f"::{message}"
    if print_:
        print(output, flush=True)
    return output


def group(title: _Stringable, details: _Stringable, print_: bool = True) -> str:
    """Create an expandable log group.

    Parameters
    ----------
    title : actionman.protocol.Stringable
        The title of the log group.
    details : actionman.protocol.Stringable
        The details of the log group.
    print_ : bool, default: True
        Whether to directly print the log group.

    Returns
    -------
    str
        The log group.

    References
    ----------
    - [GitHub Docs: Workflow Commands for GitHub Actions: Grouping log output](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#grouping-log-output)
    """
    start = group_open(title, print_=False)
    end = group_close(print_=False)
    output = f"{start}\n{details}\n{end}"
    if print_:
        print(output, flush=True)
    return output


def group_open(title: _Stringable, print_: bool = True) -> str:
    """Open an expandable log group.

    Parameters
    ----------
    title : actionman.protocol.Stringable
        The title of the log group.
    print_ : bool, default: True
        Whether to directly print the log group.

    Returns
    -------
    str
        The log group's opening tag.

    References
    ----------
    - [GitHub Docs: Workflow Commands for GitHub Actions: Grouping log output](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#grouping-log-output)
    """
    output = f"::group::{title}"
    if print_:
        print(output, flush=True)
    return output


def group_close(print_: bool = True) -> str:
    """Close an expandable log group.

    Parameters
    ----------
    print_ : bool, default: True
        Whether to directly print the log group.

    Returns
    -------
    str
        The log group's closing tag.

    References
    ----------
    - [GitHub Docs: Workflow Commands for GitHub Actions: Grouping log output](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#grouping-log-output)
    """
    output = "::endgroup::"
    if print_:
        print(output, flush=True)
    return output

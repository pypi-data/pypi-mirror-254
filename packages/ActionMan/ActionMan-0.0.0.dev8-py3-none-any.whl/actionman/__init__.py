"""ActionMan

Use workflow commands for GitHub Actions from Python.
"""


import io as _io
import sys as _sys

from actionman import exception, log, environment_variable, step_output, step_summary


if hasattr(_sys.stdout, 'buffer'):
    # Wrap the standard output stream to change its encoding to UTF-8,
    # which is required for writing unicode characters (e.g., emojis) to the console in Windows.
    # However, this works in standard Python environments where sys.stdout is a regular file object;
    # in environments like Jupyter, sys.stdout is already set up to handle Unicode,
    # and does not need to be (and cannot be) wrapped in this way.
    _sys.stdout = _io.TextIOWrapper(_sys.stdout.buffer, encoding='utf-8')

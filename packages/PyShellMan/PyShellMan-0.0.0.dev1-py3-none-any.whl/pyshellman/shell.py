import subprocess as _subprocess
from pathlib import Path as _Path

from pyshellman import exception as _exception
from pyshellman.output import ShellOutput as _ShellOutput


def run(
    command: list[str],
    cwd: str | _Path | None = None,
    raise_execution: bool = True,
    raise_exit_code: bool = True,
    raise_stderr: bool = False,
    text_output: bool = True,
) -> _ShellOutput:
    cmd_str = " ".join(command)
    try:
        process = _subprocess.run(command, text=text_output, cwd=cwd, capture_output=True)
    except FileNotFoundError:
        if raise_execution:
            raise _exception.PyShellManExecutionError(command=cmd_str)
        return _ShellOutput(command=cmd_str)
    out = process.stdout.strip() if text_output else process.stdout
    err = process.stderr.strip() if text_output else process.stderr
    code = process.returncode
    if code != 0 and raise_exit_code:
        raise _exception.PyShellManNonZeroExitCodeError(command=cmd_str, code=code, output=out, error=err)
    if err and raise_stderr:
        raise _exception.PyShellManStderrError(command=cmd_str, code=code, output=out, error=err)
    return _ShellOutput(command=cmd_str, output=out or None, error=err or None, code=code)

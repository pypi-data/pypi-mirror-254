class PyShellManError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
        return


class PyShellManExecutionError(PyShellManError):
    """Exception raised for errors in the execution of a command."""
    def __init__(self, command: str):
        self.command = command
        message = f"Shell command '{command}' could not be executed."
        super().__init__(message)
        return


class PyShellManNonZeroExitCodeError(PyShellManError):
    """Exception raised for non-zero exit code in the execution of a command."""
    def __init__(
        self,
        command: str,
        code: int,
        output: str | bytes | None = None,
        error: str | bytes | None = None
    ):
        self.command = command
        self.code = code
        self.output = output
        self.error = error

        error_details = ""
        if error:
            error_details = f"Error:\n{error}\n{'='*50}\n"
        if output:
            error_details += f"Output:\n{output}"
        message = f"Shell command '{command}' failed with exit code {code} "
        if error_details:
            message += f"and the following output:\n{error_details}"
        else:
            message += "and no output."
        super().__init__(message)
        return


class PyShellManStderrError(PyShellManError):
    """Exception raised for non-empty stderr in the execution of a command."""

    def __init__(
        self,
        command: str,
        code: int,
        output: str | bytes | None = None,
        error: str | bytes | None = None
    ):
        self.command = command
        self.code = code
        self.output = output
        self.error = error

        error_details = f"Error:\n{error}\n{'=' * 50}\n"
        if output:
            error_details += f"Output:\n{output}"
        message = (
            f"Shell command '{command}' failed with exit code {code} "
            f"and the following output:\n{error_details}"
        )
        super().__init__(message)
        return

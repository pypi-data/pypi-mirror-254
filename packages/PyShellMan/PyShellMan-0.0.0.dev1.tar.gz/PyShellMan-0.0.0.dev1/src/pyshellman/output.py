from typing import NamedTuple as _NamedTuple


class ShellOutput(_NamedTuple):
    command: str
    code: int | None = None
    output: str | bytes | None = None
    error: str | bytes | None = None

    @property
    def executed(self) -> bool:
        return self.code is not None

    @property
    def succeeded(self) -> bool:
        return self.code == 0

    @property
    def details(self) -> dict[str, str | bytes | int]:
        details = {"Command": self.command, "Executed": self.executed}
        if self.executed:
            details["Exit Code"] = self.code
        if self.output:
            details["Output"] = self.output
        if self.error:
            details["Error"] = self.error
        return details

    @property
    def summary(self) -> str:
        if not self.executed:
            return f"Command could not be executed."
        if not self.succeeded:
            return f"Command failed with exit code {self.code}."
        return f"Command executed successfully."

    def __str__(self):
        return "\n".join([f"{key}: {value}" for key, value in self.details.items()])

import sys
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.enum import INQUIRERPY_KEYBOARD_INTERRUPT
from InquirerPy.utils import get_style
from rich.console import Console

console = Console()

PRIMARY = "#e5c07b"
SECONDARY = "#61afef"
MUTED = "#abb2bf"

clack_style = get_style({
    "questionmark": f"{PRIMARY} bold",
    "question": f"{PRIMARY} bold",
    "answermark": f"{SECONDARY}",
    "answered_question": f"{PRIMARY} bold",
    "answer": f"{MUTED}",
    "pointer": f"{SECONDARY} bold",
    "highlighted": f"{SECONDARY} bold",
    "selected": f"{SECONDARY} bold",
    "instruction": f"{MUTED}",
}, False)


class BackRequest(Exception):
    """Raised when the user requests to go back one prompt with Esc."""


BACK_KEYBINDINGS = {"skip": [{"key": "escape"}]}

def _version() -> str:
    try:
        from importlib.metadata import version
        return version("operator-use")
    except Exception:
        return ""

def print_banner():
    ver = _version()
    ver_str = f"  [dim]v{ver}[/dim]" if ver else ""
    console.print()
    console.print(f"               [bold {PRIMARY}]OPERATOR[/bold {PRIMARY}]{ver_str}", justify="left")
    console.print()

def print_start(title: str = "Initial Setup"):
    ver = _version()
    ver_str = f" [dim]v{ver}[/dim]" if ver else ""
    console.print(f"┌ [bold {PRIMARY}]Operator[/bold {PRIMARY}]{ver_str} [bold {PRIMARY}]{title}[/bold {PRIMARY}]")
    console.print("│")

def print_step(n: int, total: int, title: str, hint: str = "") -> None:
    """Print a numbered step header."""
    console.print(f"[bold {PRIMARY}]│[/bold {PRIMARY}]")
    step_label = f"[dim]Step {n}/{total}[/dim]"
    console.print(f"[bold {SECONDARY}]◆[/bold {SECONDARY}] {step_label}  [bold {PRIMARY}]{title}[/bold {PRIMARY}]")
    if hint:
        console.print(f"[bold {PRIMARY}]│[/bold {PRIMARY}]  [dim]{hint}[/dim]")


def print_info(title: str, info_dict: dict):
    console.print(f"[bold {SECONDARY}]◇[/bold {SECONDARY}] [bold {PRIMARY}]{title}[/bold {PRIMARY}]")
    console.print("│")
    for k, v in info_dict.items():
        console.print(f"│ [bright_black]{k}:[/bright_black] [white]{v}[/white]")
    console.print("│")

def select(message: str, choices: list, is_last: bool = False) -> str:
    console.print(f"[bold {PRIMARY}]│[/bold {PRIMARY}]")

    formatted_choices = []
    for c in choices:
        formatted_choices.append(Choice(c, f"o {c}"))

    result = inquirer.select(
        message=message,
        choices=formatted_choices,
        qmark="◆",
        amark="◇",
        pointer="◉", # The active pointer replaces the margin slot before the Choice item
        instruction=" ",
        style=clack_style,
        keybindings=BACK_KEYBINDINGS,
        mandatory=False,
    ).execute()

    if result == INQUIRERPY_KEYBOARD_INTERRUPT:
        console.print("└ Cancelled.")
        sys.exit(1)
    if result is None:
        raise BackRequest()

    return result

def text_input(message: str, is_password: bool = False, is_last: bool = False, default: str = "") -> str:
    console.print(f"[bold {PRIMARY}]│[/bold {PRIMARY}]")

    if is_password:
        result = inquirer.secret(
            message=message,
            qmark="◆",
            amark="◇",
            style=clack_style,
            keybindings=BACK_KEYBINDINGS,
            mandatory=False,
        ).execute()
    else:
        kwargs = dict(message=message, qmark="◆", amark="◇", style=clack_style)
        if default:
            kwargs["default"] = default
        kwargs["keybindings"] = BACK_KEYBINDINGS
        kwargs["mandatory"] = False
        result = inquirer.text(**kwargs).execute()

    if result == INQUIRERPY_KEYBOARD_INTERRUPT:
        console.print("└ Cancelled.")
        sys.exit(1)
    if result is None:
        raise BackRequest()

    return result

def confirm(message: str, is_last: bool = False) -> bool:
    console.print(f"[bold {PRIMARY}]│[/bold {PRIMARY}]")

    result = inquirer.confirm(
        message=message,
        qmark="◆",
        amark="◇",
        default=True,
        style=clack_style,
        keybindings=BACK_KEYBINDINGS,
        mandatory=False,
    ).execute()

    if result == INQUIRERPY_KEYBOARD_INTERRUPT:
        console.print("└ Cancelled.")
        sys.exit(1)
    if result is None:
        raise BackRequest()

    return result

def print_end():
    console.print(f"[bold {PRIMARY}]│[/bold {PRIMARY}]")
    console.print(f"└ [bold {SECONDARY}]Setup complete![/bold {SECONDARY}] [dim]Restart operator to apply changes.[/dim]")
    console.print()

def print_end_first_install():
    console.print(f"[bold {PRIMARY}]│[/bold {PRIMARY}]")
    console.print(f"└ [bold {SECONDARY}]Setup complete![/bold {SECONDARY}] Starting your agent now...")
    console.print()
    console.print("  [dim]To start Operator next time, install it permanently:[/dim]")
    console.print(f"    [bold {SECONDARY}]uv tool install operator-use[/bold {SECONDARY}]")
    console.print("  [dim]Then just type:[/dim]  [bold]operator[/bold]")
    console.print()

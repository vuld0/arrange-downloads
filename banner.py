import pyfiglet
from rich.console import Console


console = Console()


def script_banner():
    ascii_art = pyfiglet.figlet_format("# ARRANGE DOWNLOADS")
    console.print(f"[bold green]{ascii_art}[/bold green]")
    console.print("#" * 55, style="bold green")
    console.print("#" * 9, "Simple script to arrange your downloads", "#" * 9, style="bold green")
    console.print("#" * 55, style="bold green")
    print()




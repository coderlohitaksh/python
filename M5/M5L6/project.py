from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import time

console = Console()

# ---------- Styling ----------
class C:
    SELECT = "bold cyan"
    NORMAL = "white"
    TITLE = "bold blue"
    INPUT = "cyan"
    RESULT = "bold magenta"
    ERROR = "bold red"

# ---------- Gradient Title ----------
def gradient_text(text):
    t = Text()
    for i, ch in enumerate(text):
        t.append(ch, style=f"rgb(0,{150+i*2},255)")
    return t

def draw_title():
    title = [
        "███╗   ███╗ █████╗ ████████╗██╗  ██╗",
        "████╗ ████║██╔══██╗╚══██╔══╝██║  ██║",
        "██╔████╔██║███████║   ██║   ███████║",
        "██║╚██╔╝██║██╔══██║   ██║   ██╔══██║",
        "██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║",
        "╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝"
    ]

    console.clear()
    for line in title:
        console.print(gradient_text(line))
    console.print("\n[bold cyan]MATH CORE TERMINAL[/bold cyan]\n")

# ---------- Math Core ----------
class MathCore:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set(self, a, b):
        self.a = a
        self.b = b

    def mod(self):
        if self.b == 0:
            return None
        return self.a % self.b

    def gcd(self):
        x, y = abs(self.a), abs(self.b)
        while y:
            x, y = y, x % y
        return x

    def lcm(self):
        if self.a == 0 or self.b == 0:
            return 0
        return abs(self.a * self.b) // self.gcd()

# ---------- Roman ----------
class Roman:
    def convert(self, num):
        if num is None:
            return "Invalid"
        if num <= 0:
            return "Undefined"

        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syb = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        r = ""
        i = 0
        while num > 0:
            r += syb[i] * (num // val[i])
            num %= val[i]
            i += 1
        return r

# ---------- Menu ----------
def menu(options):
    console.print("[bold yellow]Select an option:[/bold yellow]\n")

    table = Table(show_header=False, box=None)
    table.add_column("Index", style="cyan", width=6)
    table.add_column("Option", style="white")

    for i, opt in enumerate(options):
        table.add_row(str(i), opt)

    console.print(table)

    return IntPrompt.ask("\nEnter choice", default=0)

# ---------- Input ----------
def get_numbers():
    a = IntPrompt.ask("[cyan]Enter A[/cyan]")
    b = IntPrompt.ask("[cyan]Enter B[/cyan]")
    return a, b

# ---------- Main ----------
def main():
    options = [
        "Remainder",
        "GCD",
        "LCM",
        "Roman",
        "Change Numbers",
        "Show History",
        "Clear History",
        "Exit"
    ]

    draw_title()
    a, b = get_numbers()

    core = MathCore(a, b)
    roman = Roman()
    history = []

    while True:
        draw_title()
        choice = menu(options)

        console.clear()
        draw_title()

        if choice == 0:
            r = core.mod()
            history.append(f"{core.a}%{core.b}={r}")
            console.print(Panel(f"[{C.RESULT}]Remainder: {r}[/]"))

        elif choice == 1:
            g = core.gcd()
            history.append(f"GCD={g}")
            console.print(Panel(f"[{C.RESULT}]GCD: {g}[/]"))

        elif choice == 2:
            l = core.lcm()
            history.append(f"LCM={l}")
            console.print(Panel(f"[{C.RESULT}]LCM: {l}[/]"))

        elif choice == 3:
            r = core.mod()
            rr = roman.convert(r)
            history.append(f"Roman={rr}")
            console.print(Panel(f"[{C.RESULT}]Roman: {rr}[/]"))

        elif choice == 4:
            a, b = get_numbers()
            core.set(a, b)

        elif choice == 5:
            if not history:
                console.print("[red]History Empty[/red]")
            else:
                console.print(Panel("\n".join(history), title="History"))

        elif choice == 6:
            history.clear()
            console.print("[red]History Cleared[/red]")

        elif choice == 7:
            console.print("[bold green]Goodbye![/bold green]")
            break

        else:
            console.print("[red]Invalid choice[/red]")

        Prompt.ask("\nPress Enter to continue")

# ---------- Run ----------
if __name__ == "__main__":
    main()
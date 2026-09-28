import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

ART = """
     _   _ _____ ______ ______ _____ _____   _   __ ___________     
    | | | |_   _|___  / |  _  \  _  /  __ \| | / /|  ___| ___ \    
    | | | | | |    / /  | | | | | | | /  \/| |/ / | |__ | |_/ /    
    | | | | | |   / /   | | | | | | | |    |    \ |  __||    /     
    \ \_/ /_| |_ / /___ | |/ /\ \_/ / \__/\| |\  \| |___| |\ \     
     \___/ \___/\_____/ |___/  \___/ \____/\_| \_/\____/\_| \_|    
"""


def docker_ps():
    """Fetches and parses docker ps command output."""
    command = (
        'docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Ports}}"'
    )
    output = os.popen(command).read().strip()
    lines = output.split("\n")[1:]  # Skip header line
    nested_data = []
    for line in lines:
        if line.strip():
            row = line.split()
            nested_data.append(row)
    return nested_data


def docker_system_df():
    """Fetches and parses docker system df command output."""
    command = (
        "docker system df --format "
        '"table {{.Type}}\t{{.TotalCount}}\t{{.Active}}\t{{.Size}}"'
    )
    output = os.popen(command).read().strip()
    lines = output.split("\n")[1:]  # Skip header line
    data = []
    for line in lines:
        if line.strip():
            parts = line.split()
            if len(parts) >= 4:
                size = parts[-1]
                active = parts[-2]
                total = parts[-3]
                type_name = " ".join(parts[:-3])
                data.append([type_name, total, active, size])
    return data


def main():
    """Renders the ASCII banner and Docker tables to the console."""
    panel = Panel.fit(ART, border_style="cyan", padding=(1, 2))
    console.print(panel, justify="center")

    # Render Docker PS Table
    data = docker_ps()
    table = Table(title="Docker PS INFO", title_style="white")
    table.add_column(
        "[green]Container_ID[/green]",
        justify="right",
        style="cyan",
        no_wrap=True,
    )
    table.add_column(
        "[green]Image[/green]", justify="right", style="cyan", no_wrap=True
    )
    table.add_column(
        "[green]Name[/green]", justify="right", style="cyan", no_wrap=True
    )
    table.add_column(
        "[green]Port[/green]", justify="right", style="cyan", no_wrap=True
    )
    table.add_column(
        "[green]Additional Port[/green]",
        justify="right",
        style="cyan",
        no_wrap=True,
    )

    for row in data:
        table.add_row(*[f"[cyan]{cell}[/cyan]" for cell in row])

    console.print(table, justify="center")

    # Render Docker System DF Table
    df_data = docker_system_df()
    df_table = Table(title="Docker System DF", title_style="white")
    df_table.add_column(
        "[green]Type[/green]", justify="left", style="cyan", no_wrap=True
    )
    df_table.add_column(
        "[green]Total[/green]", justify="right", style="cyan", no_wrap=True
    )
    df_table.add_column(
        "[green]Active[/green]", justify="right", style="cyan", no_wrap=True
    )
    df_table.add_column(
        "[green]Size[/green]", justify="right", style="cyan", no_wrap=True
    )

    for row in df_data:
        df_table.add_row(*[f"[cyan]{cell}[/cyan]" for cell in row])

    console.print(df_table, justify="center")


if __name__ == "__main__":
    main()
from rich.console import Console
from rich.table import Table
from rich.table import Text
from rich.panel import Panel
import os

console = Console()


art = """
     _   _ _____ ______ ______ _____ _____  _   __ ___________     
    | | | |_   _|___  / |  _  \  _  /  __ \| | / /|  ___| ___ \   
    | | | | | |    / /  | | | | | | | /  \/| |/ / | |__ | |_/ /   
    | | | | | |   / /   | | | | | | | |    |    \ |  __||    /    
    \ \_/ /_| |_ / /___ | |/ /\ \_/ / \__/\| |\  \| |___| |\ \    
     \___/ \___/\_____/ |___/  \___/ \____/\_| \_/\____/\_| \_|    
"""

panel = Panel.fit(
    art,
    border_style="cyan",
    padding=(1, 2)
)

console.print(panel, justify="center")

def docker_ps():
    output = os.popen('docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Ports}}"').read().strip()
    lines = output.strip().split('\n')
    lines = lines[1:]
    nested_data = []
    for line in lines:
        row = line.split()
        nested_data.append(row)
    return nested_data


def docker_system_df():
    output = os.popen('docker system df --format "table {{.Type}}\t{{.TotalCount}}\t{{.Active}}\t{{.Size}}"').read().strip()
    lines = output.split('\n')[1:]  # Skip header
    data = []
    for line in lines:
        if line.strip():
            parts = line.split()
            if len(parts) >= 4:
                size = parts[-1]
                active = parts[-2]
                total = parts[-3]
                type_name = ' '.join(parts[:-3])
                data.append([type_name, total, active, size])
    return data


data = docker_ps()
table = Table(title="Docker PS INFO", title_style="white")
table.add_column("[green]Container_ID[/green]", justify="right", style="cyan", no_wrap=True)
table.add_column("[green]Image[/green]", justify="right", style="cyan", no_wrap=True)
table.add_column("[green]Name[/green]", justify="right", style="cyan", no_wrap=True)
table.add_column("[green]Port[/green]", justify="right", style="cyan", no_wrap=True)
table.add_column("[green]Additional Port[/green]", justify="right", style="cyan", no_wrap=True)

for row in data:
    table.add_row(*[f"[cyan]{cell}[/cyan]" for cell in row])


console.print(table, justify="center")



df_data = docker_system_df()
df_table = Table(title="Docker System DF", title_style="white")
df_table.add_column("[green]Type[/green]", justify="left", style="cyan", no_wrap=True)  # left for long names
df_table.add_column("[green]Total[/green]", justify="right", style="cyan", no_wrap=True)
df_table.add_column("[green]Active[/green]", justify="right", style="cyan", no_wrap=True)
df_table.add_column("[green]Size[/green]", justify="right", style="cyan", no_wrap=True)

for row in df_data:
    df_table.add_row(*[f"[cyan]{cell}[/cyan]" for cell in row])

console.print(df_table, justify="center")
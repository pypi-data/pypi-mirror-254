from datetime import datetime, date
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.terminal_theme import MONOKAI


def write_project_info(project_info: dict, report: bool) -> None:
    out = f"""
:speech_balloon: Description: {project_info['description']}
:computer: Language: {project_info['language']}
:house: Homepage: {project_info['homepage']}
:100: Source Rank: {project_info['rank']}
:star: Stars: {project_info['stars']}
:link: Repository URL: {project_info['repository_url']}
:copyright::copyright: Respositoy License: {project_info['repository_license']}
:vs: Latest Release Version: {project_info['latest_release_number']}
:clock3: Latest Release Time: {datetime.strptime(project_info['latest_release_published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')}
:vs: Latest Stable Release Version: {project_info['latest_stable_release_number']}
:clock3: Latest Stable Release Time: {datetime.strptime(project_info['latest_stable_release_published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')}
:chart_with_upwards_trend: Dependents: {project_info['dependent_repos_count']}
:busts_in_silhouette: Contributions: {project_info['contributions_count']}
"""

    console = Console(record=True)
    console.print(
        Panel.fit(out, border_style="green", title=project_info["name"]),
        justify="center",
    )
    if report:
        report_path = (
            Path()
            .absolute()
            .joinpath(
                f"{date.today().strftime('%Y-%m-%d')} dexpo {project_info['name']}.svg"
            )
        )
        console.save_svg(report_path, theme=MONOKAI)
        console.print("Report file was written: ", report_path)

import os
import re
import string
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Optional

import click
import git
from git.exc import GitCommandError
from packaging.version import InvalidVersion
from packaging.version import parse as parse_version
from pyproject_parser import PyProject
from ruamel.yaml import YAML


def _get_toml_config(defaults: dict) -> Optional[dict]:
    try:
        toml_file: PyProject = PyProject.load(
            os.path.join(os.getcwd(), "pyproject.toml")
        )
        return {**defaults, **toml_file.tool["pre-commit-update"]}
    except (FileNotFoundError, KeyError):
        return None


def _get_color(text: str, color: str) -> str:
    return click.style(str(text), fg=color)


def _get_yaml_file_contents(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as f:
        content: str = f.read()
    return content


def _set_yaml_file_contents(file_path: str, yaml_doc: YAML, data: Any) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        yaml_doc.dump(data, f)


def _get_target_tag(tags: list, all_versions: bool) -> str:
    if all_versions:
        return tags[0]
    for t in tags:
        if not any(v in t for v in ("a", "b", "rc")):
            return t
    return tags[0]


def _get_parsed_tags(repo: dict) -> list:
    url: str = repo["repo"]
    try:
        remote_tags: list = (
            git.cmd.Git()
            .ls_remote("--exit-code", "--tags", url, sort="v:refname")
            .split("\n")
        )
        tags: list = []
        for tag in remote_tags:
            parsed_tag: str = re.split(r"\t+", tag)[1]
            if parsed_tag.endswith("^{}"):
                continue
            parsed_tag = parsed_tag.replace("refs/tags/", "")
            tags.append(parsed_tag)
        return tags
    except GitCommandError as ex:
        if ex.status == 2:
            message = f"No tags found for repo: {url}"
        else:
            message = f"Failed to list tags for repo: {url}"
        raise Exception(message)


def _get_repo_head_hash(repo: dict) -> str:
    url: str = repo["repo"]
    return git.cmd.Git().ls_remote("--exit-code", url, "HEAD").split()[0]


def _is_a_hash(ver: str) -> bool:
    # The minimum length for an abbreviated hash is 4:
    # <https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreabbrev>.
    if len(ver) < 4:
        return False
    else:
        # Credit goes to Levon (https://stackoverflow.com/users/1209279/levon)
        # for this idea: <https://stackoverflow.com/a/11592279/7593853>.
        return all(character in string.hexdigits for character in ver)


def _get_target_ver(repo: dict, tags: list, all_versions: bool) -> str:
    current_ver: str = repo["rev"]
    if current_ver in tags:
        return _get_target_tag(tags, all_versions)
    elif _is_a_hash(current_ver):
        return _get_repo_head_hash(repo)
    return current_ver


def run(
    dry_run: bool, all_versions: bool, verbose: bool, exclude: tuple, keep: tuple
) -> None:
    os.environ["GIT_TERMINAL_PROMPT"] = "0"
    try:
        yaml: YAML = YAML()
        yaml.indent(sequence=4)
        yaml.preserve_quotes = True
        file_path: str = os.path.join(os.getcwd(), ".pre-commit-config.yaml")
        yaml_str: str = _get_yaml_file_contents(file_path)
        data: Any = yaml.load(yaml_str)
        no_update: list = []
        to_update: list = []
        ignored: list = []
        kept: list = []

        with ThreadPoolExecutor(max_workers=10) as pool:
            tasks: list = []
            for i in range(len(data["repos"])):
                repo: dict = data["repos"][i]
                tasks.append(pool.submit(_get_parsed_tags, repo))

        for i, repository in enumerate(data["repos"]):
            if not repository["repo"].startswith("http"):
                continue
            repo = data["repos"][i]
            repo_name: str = repo["repo"].split("/")[-1]
            tag_versions: list = tasks[i].result()
            try:
                tag_versions.sort(key=parse_version)
            except InvalidVersion:
                pass
            tag_versions.reverse()
            target_ver: str = _get_target_ver(repo, tag_versions, all_versions)
            if repo_name in exclude:
                ignored.append(
                    f"{repo_name} - {_get_color(repo['rev'] + ' ★', 'magenta')}"
                )
                continue
            if repo_name in keep:
                if repo["rev"] != target_ver:
                    kept.append(
                        f"{repo_name} - {_get_color(repo['rev'] + ' -> ' + target_ver + ' ◉', 'blue')}"
                    )
                else:
                    kept.append(
                        f"{repo_name} - {_get_color(repo['rev'] + ' ◉', 'blue')}"
                    )
                continue
            if repo["rev"] != target_ver:
                to_update.append(
                    f"{repo_name} - {_get_color(repo['rev'], 'yellow')} -> {_get_color(target_ver + ' ✘', 'red')}"
                )
                data["repos"][i]["rev"] = target_ver
            else:
                no_update.append(
                    f"{repo_name} - {_get_color(repo['rev'] + ' ✔', 'green')}"
                )

        if verbose:
            for output in (ignored, kept, no_update):
                if not output:
                    continue
                click.echo("\n".join(output))

        if to_update:
            click.echo("\n".join(to_update))
            if not dry_run:
                _set_yaml_file_contents(".pre-commit-config.yaml", yaml, data)
                click.echo(_get_color("Changes detected and applied", "green"))
            else:
                raise click.ClickException(_get_color("Changes detected", "red"))
        else:
            click.echo(_get_color("No changes detected", "green"))

    except Exception as ex:
        sys.exit(str(ex))


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "-d",
    "--dry-run",
    is_flag=True,
    show_default=True,
    default=False,
    help="Dry run only checks for the new versions without updating",
)
@click.option(
    "-a",
    "--all-versions",
    is_flag=True,
    show_default=True,
    default=False,
    help="Include the alpha/beta versions when updating",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    show_default=True,
    default=False,
    help="Display the complete output",
)
@click.option(
    "-e",
    "--exclude",
    multiple=True,
    default=(),
    help="Exclude specific repo(s) by the `repo` url trim",
)
@click.option(
    "-k",
    "--keep",
    multiple=True,
    default=(),
    help="Keep the version of specific repo(s) by the `repo` url trim (still checks for the new versions)",
)
@click.pass_context
def cli(
    ctx: click.Context,
    dry_run: bool,
    all_versions: bool,
    verbose: bool,
    exclude: tuple,
    keep: tuple,
):
    defaults: dict = {p.name: p.default for p in ctx.command.params}
    is_default: bool = defaults == ctx.params

    if not is_default:
        run(dry_run, all_versions, verbose, exclude, keep)
        return

    toml_params: Optional[dict] = _get_toml_config(defaults)
    if toml_params:
        run(**toml_params)
        return

    run(**defaults)


if __name__ == "__main__":
    cli()

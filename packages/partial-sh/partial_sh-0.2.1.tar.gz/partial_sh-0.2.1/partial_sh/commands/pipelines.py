from collections import defaultdict
from pathlib import Path

import typer
from langchain.pydantic_v1 import BaseModel
from typing_extensions import Annotated

from ..store import PipelineInfo, PipelineStore

app = typer.Typer(no_args_is_help=False)

# Constants
ID_WIDTH = 13
NAME_WIDTH = 50
NAME_LIMIT = 27
ELLIPSIS = "..."


class PipelinesOutput(BaseModel):
    """Represents the output structure for pipelines."""

    location: Path
    pipelines: list[PipelineInfo]


def display_pipelines(pipelines_output: PipelinesOutput, all_: bool = True):
    """Displays the pipeline information in a formatted table.

    Args:
        pipelines_output (PipelinesOutput): The output object containing pipeline information.
        all (bool): If True, display all pipelines. If False, display only the latest pipeline for each name.
    """
    pipelines_path = pipelines_output.location
    pipeline_infos = pipelines_output.pipelines

    print(f"Location: {pipelines_path}\n")

    if not pipeline_infos:
        print("No pipelines to display.")
        return

    # Constants for formatting column widths
    NAME_WIDTH = 50
    ID_WIDTH = 13
    FILENAME_WIDTH = 50
    DATE_WIDTH = 20

    header = f"{'PIPELINE NAME':<{NAME_WIDTH}}{'ID':<{ID_WIDTH}}{'FILENAME':<{FILENAME_WIDTH}}{'LAST UPDATED':<{DATE_WIDTH}}"
    print(header)
    print("-" * len(header))

    # Group pipelines by name
    pipelines_by_name = defaultdict(list)
    for pipeline in pipeline_infos:
        pipelines_by_name[pipeline.name].append(pipeline)

    for name, pipelines in pipelines_by_name.items():
        # Sort pipelines by updated_at in descending order
        pipelines = sorted(pipelines, key=lambda x: x.updated_at, reverse=True)

        # Get the most recent pipeline
        latest_pipeline = pipelines[0]
        updated_at_str = (
            latest_pipeline.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            if latest_pipeline.updated_at
            else "N/A"
        )

        # Print the pipeline name and latest pipeline info
        print(
            f"{name:<{NAME_WIDTH}}{latest_pipeline.id:<{ID_WIDTH}}{latest_pipeline.filename+' ' or '':<{FILENAME_WIDTH}}{updated_at_str}"
        )

        # If all is True, print the remaining pipelines in the group, indented under the pipeline name
        if all_:
            for pipeline in pipelines[1:]:
                updated_at_str = (
                    pipeline.updated_at.strftime("%Y-%m-%d %H:%M:%S")
                    if pipeline.updated_at
                    else "N/A"
                )
                print(
                    f"{'':<{NAME_WIDTH}}{pipeline.id:<{ID_WIDTH}}{pipeline.filename+' ' or '':<{FILENAME_WIDTH}}{updated_at_str}"
                )

    print("-" * len(header))


def retrieve_pipelines_data(config_path: Path) -> PipelinesOutput:
    """Retrieves pipeline data from the given configuration path."""
    pipelines_path = config_path / "pipelines"
    store = PipelineStore(path=pipelines_path)

    try:
        store.refresh()
    except Exception as e:
        print(f"Error refreshing the pipeline store: {e}")
        return PipelinesOutput(location=pipelines_path, pipelines=[])

    return PipelinesOutput(location=store.path, pipelines=store.pipeline_infos)


@app.callback(invoke_without_command=True)
def list_pipelines(
    ctx: typer.Context,
    json_output: Annotated[
        bool,
        typer.Option(
            "--json",
            "-j",
            help="Show the output in JSON format",
        ),
    ] = False,
    all_: Annotated[
        bool,
        typer.Option(
            "--all",
            "-a",
            help="Show all pipelines, not just the latest pipeline for each name",
        ),
    ] = False,
):
    """
    List all the available pipelines.
    """
    config_path = Path(ctx.obj["config_path"])
    pipelines_output = retrieve_pipelines_data(config_path)

    if json_output:
        print(pipelines_output.json(indent=4))
    else:
        display_pipelines(pipelines_output, all_)

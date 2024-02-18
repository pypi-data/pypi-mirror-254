from pathlib import Path

import typer
from typing_extensions import Annotated

from ..store import PipelineStore

app = typer.Typer(no_args_is_help=True)

config_path: Path = Path.home() / ".config" / "partial"
pipelines_path = config_path / "pipelines"


def display_pipeline(name, filepath, pipeline_data):
    print(f"Pipeline: {name}\nFile: {filepath}\n-------------------")

    # Info
    print(f"ID: {pipeline_data['id']}")
    print(f"Created at: {pipeline_data['created_at']}")
    print(f"Updated at: {pipeline_data['updated_at']}")
    print("")
    # Print instructions
    print("Instructions:")
    for i, instruction in enumerate(pipeline_data["instructions"], 1):
        print(f"  {i}. {instruction['instruction']} (Mode: {instruction['mode']})")

    # Print codes
    print("\nCode:")
    for name, code in pipeline_data["code"].items():
        print(f"- {name}:\n\n    {code.replace('\n', '\n    ')}")

    # Other details
    print(f"\nRepeat: {pipeline_data['repeat']}")


@app.callback(invoke_without_command=True)
def show(
    name_or_id: Annotated[
        str,
        typer.Argument(
            help="Name or ID of the pipeline to show",
        ),
    ],
    json_output: Annotated[
        bool,
        typer.Option(
            "--json",
            "-j",
            help="Show the output in JSON format",
        ),
    ] = False,
):
    """
    Show the pipelien content
    """
    store = PipelineStore(path=pipelines_path)
    store.refresh()

    pipeline = store.get_by_id(name_or_id) or store.get_by_name(name_or_id)
    if pipeline is None:
        print(f"Pipeline not found: {name_or_id}")
        raise typer.Exit(1)

    if json_output:
        print(pipeline.json(indent=4))
        return

    display_pipeline(
        pipeline.name, store.path / pipeline.filename, pipeline.content.dict()
    )

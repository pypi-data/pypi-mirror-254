from collections import defaultdict
from pathlib import Path

import typer
from langchain.pydantic_v1 import BaseModel
from typing_extensions import Annotated

from ..store import ShapeInfo, ShapeStore

app = typer.Typer(no_args_is_help=False)

# Constants
ID_WIDTH = 13
NAME_WIDTH = 50
NAME_LIMIT = 27
ELLIPSIS = "..."


class ShapesOutput(BaseModel):
    """Represents the output structure for shapes."""

    location: Path
    shapes: list[ShapeInfo]


def display_shapes(shapes_output: ShapesOutput, all_: bool = True):
    """Displays the shape information in a formatted table.

    Args:
        shapes_output (ShapesOutput): The output object containing shape information.
        all_ (bool): If True, display all shapes. If False, display only the latest shape for each name.
    """
    shapes_path = shapes_output.location
    shape_infos = shapes_output.shapes

    print(f"Location: {shapes_path}\n")

    if not shape_infos:
        print("No shapes to display.")
        return

    # Constants for formatting column widths
    NAME_WIDTH = 50
    ID_WIDTH = 13
    FILENAME_WIDTH = 50
    DATE_WIDTH = 20

    header = f"{'SHAPE NAME':<{NAME_WIDTH}}{'ID':<{ID_WIDTH}}{'FILENAME':<{FILENAME_WIDTH}}{'LAST UPDATED':<{DATE_WIDTH}}"
    print(header)
    print("-" * len(header))

    # Group shapes by name
    shapes_by_name = defaultdict(list)
    for shape in shape_infos:
        shapes_by_name[shape.name].append(shape)

    for name, shapes in shapes_by_name.items():
        # Sort shapes by updated_at in descending order
        shapes = sorted(shapes, key=lambda x: x.updated_at, reverse=True)

        # Get the most recent shape
        latest_shape = shapes[0]
        updated_at_str = (
            latest_shape.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            if latest_shape.updated_at
            else "N/A"
        )

        # Print the shape name and latest shape info
        print(
            f"{name:<{NAME_WIDTH}}{latest_shape.id:<{ID_WIDTH}}{latest_shape.filename+' ' or '':<{FILENAME_WIDTH}}{updated_at_str}"
        )

        # If all_ is True, print the remaining shapes in the group, indented under the shape name
        if all_:
            for shape in shapes[1:]:
                updated_at_str = (
                    shape.updated_at.strftime("%Y-%m-%d %H:%M:%S")
                    if shape.updated_at
                    else "N/A"
                )
                print(
                    f"{'':<{NAME_WIDTH}}{shape.id:<{ID_WIDTH}}{shape.filename+' ' or '':<{FILENAME_WIDTH}}{updated_at_str}"
                )

    print("-" * len(header))


def retrieve_shapes_data(config_path: Path) -> ShapesOutput:
    """Retrieves shape data from the given configuration path."""
    shapes_path = config_path / "shapes"
    store = ShapeStore(path=shapes_path)

    try:
        store.refresh()
    except Exception as e:
        print(f"Error refreshing the shape store: {e}")
        return ShapesOutput(location=shapes_path, shapes=[])

    return ShapesOutput(location=store.path, shapes=store.shape_infos)


@app.callback(invoke_without_command=True)
def list_shapes(
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
            help="Show all shapes, not just the latest shape for each name",
        ),
    ] = False,
):
    """
    List all the available shapes.
    """
    config_path = Path(ctx.obj["config_path"])
    shapes_output = retrieve_shapes_data(config_path)

    if json_output:
        print(shapes_output.json(indent=4))
    else:
        display_shapes(shapes_output, all_)

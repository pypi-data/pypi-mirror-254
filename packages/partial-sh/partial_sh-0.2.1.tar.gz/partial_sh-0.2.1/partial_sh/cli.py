import logging

from .commands.config import app as config_app
from .commands.main import app as main_app
from .commands.pipelines import app as pipelines_app
from .commands.setup import app as setup_app
from .commands.show import app as show_app
from .commands.store import app as store_app

main_app.add_typer(setup_app, name="setup", no_args_is_help=False, help="Setup partial")
main_app.add_typer(config_app, name="config", no_args_is_help=False, help="Config")
main_app.add_typer(store_app, name="store", no_args_is_help=False, help="Store")
main_app.add_typer(pipelines_app, name="pipelines", help="Pipelines")
main_app.add_typer(show_app, name="show", help="Show the content of a pipeline")


def main():
    main_app()


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    main()

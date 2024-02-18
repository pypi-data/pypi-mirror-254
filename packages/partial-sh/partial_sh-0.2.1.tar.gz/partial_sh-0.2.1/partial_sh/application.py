import json
import logging
import sys

from .process import process_line

logger = logging.getLogger(__name__)


def print_data_output(output: str | dict):
    if isinstance(output, dict):
        logger.info("Output is a dict")
        output = json.dumps(output)
    else:
        logger.info("Output is a string")

    print(output, file=sys.stdout, flush=True)


def print_info(info: str, *args, **kwargs):
    """
    Print info to stderr, to avoid interfering with the output.
    """
    print(info, *args, **kwargs, file=sys.stderr)


class Application:
    llm = None
    sandbox = None
    store = None
    quiet = False

    def __init__(self, llm, sandbox, store, quiet=False):
        self.llm = llm
        self.sandbox = sandbox
        self.store = store
        self.quiet = quiet

    def terminate(self):
        if self.sandbox:
            self.sandbox.close()

    def process(
        self,
        lines,
        pipeline,
    ):
        logger.info("Process data")
        for idx, line in enumerate(lines):
            logger.info("Processing line: %s", idx)
            for ri in range(pipeline.repeat):
                logger.info("Repeat Iteration: %s", ri)
                if self.quiet is False and sys.stdout.isatty() is False:
                    print_info(f"Processing line: {idx} Repeat Iteration: {ri}")
                output = process_line(
                    llm=self.llm,
                    sandbox=self.sandbox,
                    line=line,
                    pipeline=pipeline,
                    store=self.store,
                )
                print_data_output(output)

        logger.info("Data processed")

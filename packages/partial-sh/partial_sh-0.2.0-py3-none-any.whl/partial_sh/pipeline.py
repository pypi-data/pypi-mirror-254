import logging
import re
from datetime import datetime
from pathlib import Path
from uuid import uuid4

import typer
from langchain.pydantic_v1 import BaseModel

from .instruction import InstructionMetadata, Modes

logger = logging.getLogger(__name__)


def prepare_key(s):
    s = s.lower().replace(" ", "_")
    # Remove special characters except for underscore
    return re.sub(r"[^a-z0-9_]", "", s)


class InvalidJson(Exception):
    pass


class PipelineConfigFile(BaseModel):
    id: str
    name: str | None = None
    created_at: str
    updated_at: str
    instructions: list[InstructionMetadata]
    code: dict[str, str] = {}
    repeat: int = 1


class Pipeline:
    id: str
    name: str | None = None
    created_at: str
    updated_at: str
    instructions: list[InstructionMetadata] = []
    code: dict[str, str] = {}
    repeat: int = 1
    regenerate: bool = False

    def __init__(self):
        pass

    def new(
        self,
        name: str,
        instructions: list[str],
        code: dict[str, str] = {},
        repeat: int = 1,
        regenerate: bool = False,
        mode: Modes | None = None,
    ):
        self.id = str(uuid4())
        self.name = name
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
        self.instructions = [
            InstructionMetadata(instruction=instruction, mode=mode)
            for instruction in instructions
        ]
        self.code = code
        self.repeat = repeat
        self.regenerate = regenerate
        return self

    def get_prep_name(self):
        # If name is not provided, use the first instruction
        if self.name is None or self.name == "":
            first_instruction = (self.instructions or [None])[0]
            if (
                first_instruction is None
                or first_instruction.instruction is None
                or first_instruction.instruction == ""
            ):
                return None
            prep_name = first_instruction.instruction
        else:
            prep_name = self.name

        return prepare_key(prep_name)[:50]

    def get_slug(self):
        key = self.id.split("-")[0]

        prep_name = self.get_prep_name()
        if prep_name is None:
            return key
        key = self.id.split("-")[0] + "__" + prep_name
        return key

    def load_from_file(self, file: Path):
        """
        Load pipeline from json file.
        """
        if file.is_file():
            try:
                pipeline_config = PipelineConfigFile.parse_file(file)
            except ValueError as e:
                e = InvalidJson(
                    f"Error parsing pipeline json file is invalid: {file.absolute()}\n{e}"
                )
                raise typer.Exit(e)
        self.id = pipeline_config.id
        self.created_at = pipeline_config.created_at
        self.updated_at = pipeline_config.updated_at
        self.instructions = pipeline_config.instructions
        self.code = pipeline_config.code
        self.repeat = pipeline_config.repeat
        return self

    def save_to_file(self, file: Path):
        """
        Save pipeline to json file.
        """
        pipeline_config = PipelineConfigFile(
            id=self.id,
            name=self.name,
            created_at=self.created_at,
            updated_at=datetime.now().isoformat(),
            instructions=self.instructions,
            code=self.code,
            repeat=self.repeat,
        )
        with open(file, "w") as f:
            json_content = pipeline_config.json(indent=4)
            f.write(json_content)

    def lookup_code(self, instruction: str):
        key = prepare_key(instruction)
        return self.code.get(key)

    def save_code(self, instruction: str, code: str):
        key = prepare_key(instruction)
        self.code[key] = code
        return self

    def remove_code(self, instruction: str):
        key = prepare_key(instruction)
        self.code.pop(key)
        return self

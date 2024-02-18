import logging
import os
from datetime import datetime
from pathlib import Path

from langchain.pydantic_v1 import BaseModel, ValidationError

from .pipeline import PipelineConfigFile

logger = logging.getLogger(__name__)


class PipelineInfo(BaseModel):
    id: str
    name: str
    filename: str | None = None
    content: PipelineConfigFile | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class PipelineStore:
    path: Path
    pipeline_infos: list[PipelineInfo] = []

    def __init__(self, path: Path):
        self.path = path

    def refresh(self):
        self.pipeline_infos = []
        self.list()

    def list(self):
        for filename in os.listdir(self.path):
            if filename.endswith(".json"):
                pipeline_name = filename[:-5].split("__")
                if len(pipeline_name) < 2:
                    continue
                pipeline_id = pipeline_name[0]
                pipeline_name = pipeline_name[1]

                # Get when file was created
                created_at = datetime.fromtimestamp(
                    os.path.getctime(self.path / filename)
                )
                # created_at = created_at.isoformat()
                # Get when file was last modified
                updated_at = datetime.fromtimestamp(
                    os.path.getmtime(self.path / filename)
                )
                # updated_at = updated_at.isoformat()

                self.pipeline_infos.append(
                    PipelineInfo(
                        id=pipeline_id,
                        name=pipeline_name,
                        filename=filename,
                        created_at=created_at,
                        updated_at=updated_at,
                    )
                )
        return self.pipeline_infos

    def find_pipeline_file(self, pipeline_arg: str) -> Path:
        """
        Find the pipeline file based on the pipeline argument.
        """
        # Refresh the pipeline store
        self.refresh()
        # Check if the pipeline argument is already a file
        pipeline_file = Path(pipeline_arg)
        if pipeline_file.is_file():
            return pipeline_file

        # If not a file, try to find it in the pipeline store
        pipeline_file = self.get_filepath_by_id(
            pipeline_arg
        ) or self.get_filepath_by_name(pipeline_arg)

        if not pipeline_file or not pipeline_file.is_file():
            # Handle the error as appropriate for your application
            return None

        return pipeline_file

    def get_filepath_by_id(self, id: str):
        for pipeline_info in self.pipeline_infos:
            if pipeline_info.id.startswith(id.split("-")[0]):
                filename = pipeline_info.filename
                pipeline_path = self.path / filename
                return pipeline_path
        return None

    def get_filepath_by_name(self, name: str):
        for pipeline_info in self.pipeline_infos:
            if pipeline_info.name.startswith(name):
                filename = pipeline_info.filename
                pipeline_path = self.path / filename
                return pipeline_path
        return None

    def get_by_id(self, id: str):
        for pipeline_info in self.pipeline_infos:
            if pipeline_info.id.startswith(id.split("-")[0]):
                filename = pipeline_info.filename
                pipeline_path = self.path / filename
                with open(pipeline_path, "r") as f:
                    try:
                        pipeline = PipelineConfigFile.parse_raw(f.read())
                    except ValidationError:
                        logger.error("Error parsing file %s", filename)
                        return None
                pipeline_info.content = pipeline
                return pipeline_info
        return None

    def get_by_name(self, name: str) -> PipelineInfo | None:
        matching_pipelines = [p for p in self.pipeline_infos if p.name.startswith(name)]

        # Sort pipelines by updated_at in descending order and get the most recent one
        if matching_pipelines:
            latest_pipeline = max(
                matching_pipelines, key=lambda p: p.updated_at or datetime.min
            )

            filename = latest_pipeline.filename
            pipeline_path = self.path / filename
            with open(pipeline_path, "r") as f:
                try:
                    pipeline = PipelineConfigFile.parse_raw(f.read())
                except ValidationError:
                    logger.error("Error parsing file %s", filename)
                    return None
            latest_pipeline.content = pipeline
            return latest_pipeline
        else:
            return None

"""Models for the SCC AI Services Client."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class BaseTask(BaseModel):
    """Base Model for transcribe tasks"""

    id: int
    owner_id: int
    source_language: str
    state: str
    task_id: str
    time_created: datetime
    time_received: Optional[datetime]
    time_updated: Optional[datetime]


class TranscribeTask(BaseTask):
    """Base Model for transcribe tasks"""

    url: str
    transcribe_translate_task_id: Optional[int]


class TranscribeTaskResult(TranscribeTask):
    """Base Model for transcribe tasks with result"""

    result: Optional[dict]


class TranscribeTranslateTask(BaseTask):
    """Base Model for combined transcribe translate tasks"""

    time_finished: Optional[datetime]
    target_languages: List[str]
    transcribe_task: List[TranscribeTask]


class TranscribeTranslateTaskResult(TranscribeTranslateTask):
    """Base Model for transcribe-translate tasks with result"""

    time_finished: Optional[datetime]
    result: Optional[dict]


class TranslateTask(BaseTask):
    """Base Model for translate tasks"""

    time_finished: Optional[datetime]
    text: str
    task_id: int
    transcribe_translate_task_id: Optional[int]


class TranslateTaskResult(TranslateTask):
    """Base Model for translate tasks with result"""

    time_finished: Optional[datetime]
    result: Optional[dict]


class NewTranscribeTask(BaseModel):
    """Base Model for transcribe tasks"""

    url: str
    source_language: str


class NewTranscribeTranslateTask(BaseModel):
    """Base Model for transcribe translate tasks"""

    url: str
    source_language: str
    target_languages: List[str]


class NewTranslateTask(BaseModel):
    """Base Model for translate tasks"""

    text: str
    source_language: str
    target_languages: List[str]


class User(BaseModel):
    """Base Model for users"""

    id: int
    username: str
    full_name: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
    transcribe_tasks: Optional[List[TranscribeTask]]
    translate_tasks: Optional[List[TranslateTask]]
    transcribe_translate_tasks: Optional[List[TranscribeTranslateTask]]

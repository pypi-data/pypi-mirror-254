"""Models for the SCC AI Services Client."""

from datetime import datetime
from typing import Dict, List, Optional
import uuid

from pydantic import AnyHttpUrl, BaseModel, EmailStr


class Error(BaseModel):
    """Base Model for errors"""

    error: str

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


class TranscribeWordElem(BaseModel):
    """Base Model for transcribe word elements"""

    word: str
    start: float
    end: float
    score: float


class TranscribeSegmentElem(BaseModel):
    """Base Model for transcribe segment elements"""

    start: float
    end: float
    text: str
    words: List[TranscribeWordElem]


class TranscribeTaskResultTranscriptElem(BaseModel):
    """Base Model for transcribe task results"""

    segments: List[TranscribeSegmentElem]
    word_segments: List[TranscribeWordElem]


class TranscribeTaskResultElem(BaseTask):
    """Base Model for transcribe task results"""

    source_language: str
    transcript: TranscribeTaskResultTranscriptElem
    vtt: str
    status: str


class TranscribeTaskResultWithoutResultElem(BaseTask):
    url: AnyHttpUrl
    task_id: uuid.UUID
    source_language: str
    state: str
    transcribe_translate_task_id: Optional[int]


class TranscribeTaskResult(TranscribeTaskResultWithoutResultElem):
    """Base Model for transcribe tasks with result"""

    result: Optional[TranscribeTaskResultElem] | Error


class TranscribeTranslateTask(BaseTask):
    """Base Model for combined transcribe translate tasks"""

    time_finished: Optional[datetime]
    target_languages: List[str]
    transcribe_task: List[TranscribeTask]


class TranslateTask(BaseTask):
    """Base Model for translate tasks"""

    time_finished: Optional[datetime]
    text: str
    task_id: int
    transcribe_translate_task_id: Optional[int]


class TranslateTaskResultWithoutResultElement(BaseTask):
    """Base Model for translate tasks without result element."""

    target_languages: List[str]
    text: str
    task_id: int
    transcribe_translate_task_id: Optional[int]
    time_finished: Optional[datetime]


class TranslateTaskResult(TranslateTaskResultWithoutResultElement):
    """Base Model for translate tasks with result"""

    result: Optional[dict[str, str]] | Error


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

class TranscribeTranslateTaskResultElement(BaseModel):
    """Base Model for transcribe-translate task result element."""
    transcript: TranscribeTaskResultTranscriptElem
    vtt: Dict[str, str]

class TranscribeTranslateTaskResult(BaseTask):
    """Base Model for transcribe-translate tasks with result"""

    target_languages: List[str]
    url: AnyHttpUrl
    task_id: uuid.UUID

    transcribe_task: List[TranscribeTaskResultWithoutResultElem]
    translate_task: List[TranslateTaskResultWithoutResultElement]
    time_finished: Optional[datetime]
    result: TranscribeTranslateTaskResultElement | Error

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

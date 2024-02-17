"""This is a manually created client for the SCC AI Services API.
Docs: https://test.ai-services.scc.kit.edu/docs
"""

# pylint: disable=broad-exception-raised

from typing import List
from loguru import logger
from pydantic import TypeAdapter
import requests


from scc_whisper_api_client import config
from scc_whisper_api_client.models import (
    NewTranscribeTask,
    NewTranscribeTranslateTask,
    NewTranslateTask,
    TranscribeTask,
    TranscribeTaskResult,
    TranscribeTranslateTask,
    TranscribeTranslateTaskResult,
    TranslateTask,
    TranslateTaskResult,
    User,
)


class SCCClient:
    """
    SCCClient is a client for interacting with the SCC AI Services API.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
        api_base_url (str): The base URL of the SCC AI Services API.
        version_path (str, optional): The version path of the API. Defaults to "v1".

    Attributes:
        username (str): The username for authentication.
        password (str): The password for authentication.
        api_base_url (str): The base URL of the SCC AI Services API.
        access_token (str): The access token for authentication.
        session (requests.Session): The session object for making API requests.

    """

    def __init__(
        self, username, password, api_base_url, version_path="v1", verify=True
    ):
        self.username = username
        self.password = password
        self.api_base_url = api_base_url
        if not self.api_base_url.endswith("/"):
            self.api_base_url += "/"
        if "/api" not in self.api_base_url:
            self.api_base_url = self.api_base_url + f"api/{version_path}/"
        self.access_token = None
        self.session = None
        self.verify = verify

    def login(self):
        """Login to the SCC AI Services API and set the access token."""
        self.session = requests.Session()
        url = self.api_base_url + "login/access-token"
        logger.debug(f"loggign in to {url}")
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
        }
        logger.debug(data)
        headers = {"Authorization": "Basic Og=="}
        res = self.session.post(
            self.api_base_url + "login/access-token",
            headers=headers,
            data=data,
            verify=self.verify,
        )
        if res.ok:
            self.access_token = res.json()["access_token"]
            self.session.headers.update(
                {"Authorization": f"Bearer {self.access_token}"}
            )
            self.session.verify = self.verify
        else:
            logger.critical(f"Could not login: {res.text}")
            raise Exception(f"Could not login: {res.text}")

    def get_user_info(self):
        """Get user info"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.get(self.api_base_url + "users/me")
        if res.ok:
            user = res.json()
            u = User(**user)
            return u
        return None

    def get_transcribe_tasks(self):
        """Get transcribe tasks"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.get(self.api_base_url + "transcribe/")
        if res.ok:
            transcribe_task_list_model = TypeAdapter(List[TranscribeTask])
            return transcribe_task_list_model.validate_python(res.json())
        logger.warning(f"Could not get transcribe tasks: {res.text}")
        return None

    def get_transcribe_task(self, task_id: str) -> TranscribeTaskResult:
        """Get transcribe task"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.get(self.api_base_url + f"transcribe/{task_id}")
        if res.ok:
            return TranscribeTaskResult(**res.json())
        logger.warning(f"Could not get transcribe task: {res.text}")
        return None

    def add_transcribe_task(self, task: NewTranscribeTask) -> TranscribeTaskResult:
        """Post a new transcrib task"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.post(
            self.api_base_url + "transcribe/", json=task.model_dump()
        )
        res = self.session.post(
            self.api_base_url + "transcribe/", json=task.model_dump()
        )
        if res.ok:
            return TranscribeTaskResult(**res.json())
        logger.error(f"Could not add transcribe task: {res.text}")
        raise Exception(f"Could not add transcribe task: {res.text}")

    def get_translate_tasks(self):
        """Get translate tasks"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.get(self.api_base_url + "translate/")
        if res.ok:
            translate_task_list_model = TypeAdapter(List[TranslateTask])
            return translate_task_list_model.validate_python(res.json())
        logger.warning(f"Could not get translate tasks: {res.text}")
        return None

    def get_translate_task(self, task_id: int) -> TranslateTaskResult:
        """Get translate task"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.get(self.api_base_url + f"translate/{task_id}")
        if res.ok:
            return TranslateTaskResult(**res.json())
        logger.warning(f"Could not get translate task: {res.text}")
        return None

    def add_translate_task(self, task: NewTranslateTask) -> TranslateTaskResult:
        """Post a new translate task"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.post(
            self.api_base_url + "translate/", json=task.model_dump()
        )
        if res.ok:
            print(res.json())
            return TranslateTaskResult(**res.json())

    def get_transcribe_translate_tasks(self):
        """Get transcribe translate tasks"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.get(self.api_base_url + "transcribe-translate/")
        if res.ok:
            transcribe_translate_task_list_model = TypeAdapter(
                List[TranscribeTranslateTask]
            )
            return transcribe_translate_task_list_model.validate_python(res.json())
        logger.warning(f"Could not get transcribe translate tasks: {res.text}")
        return None

    def get_transcribe_translate_task(
        self, task_id: str
    ) -> TranscribeTranslateTaskResult:
        """Get transcribe translate task"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.get(self.api_base_url + f"transcribe-translate/{task_id}")
        if res.ok:
            return TranscribeTranslateTaskResult(**res.json())
        logger.warning(f"Could not get transcribe translate task: {res.text}")
        return None

    def add_transcribe_translate_task(
        self, task: NewTranscribeTranslateTask
    ) -> TranscribeTranslateTaskResult:
        """Post a new transcribe translate task"""
        if not self.access_token:
            logger.error("No access token set. Please login first.")
            return None
        res = self.session.post(
            self.api_base_url + "transcribe-translate/", json=task.model_dump()
        )
        if res.ok:
            return TranscribeTranslateTaskResult(**res.json())


def main():
    """Main function"""
    client = SCCClient(
        username=config.SCC_USERNAME,
        password=config.SCC_PASSWORD,
        api_base_url=config.SCC_API_BASE_URL,
        verify=config.SCC_VERIFY_SSL,
    )
    client.login()
    # logger.info(pformat(client.get_user_info().dict()))
    # logger.info(pformat(client.get_transcribe_translate_tasks()))
    translate_task = NewTranslateTask(
        text="Hallo Welt", source_language="de", target_languages=["en", "fr"]
    )
    transcribe_task = NewTranscribeTask(
        url="https://media.bibliothek.kit.edu/campus/2023/DIVA-2023-283_mp4.mp4",
        source_language="de",
        target_languages=["en", "fr"],
    )
    res = client.add_transcribe_task(transcribe_task)
    logger.info(res.model_dump_json())
    # logger.info(pformat(client.add_translate_task(translate_task).dict()))

    # logger.info(pformat(client.get_translate_task(475022794)))


if __name__ == "__main__":
    main()

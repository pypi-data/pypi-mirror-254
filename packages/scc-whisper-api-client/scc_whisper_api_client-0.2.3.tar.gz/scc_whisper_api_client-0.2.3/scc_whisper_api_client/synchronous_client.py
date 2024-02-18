"""This is a manually created *synchronous* client for the SCC AI Services API.
Docs: https://test.ai-services.scc.kit.edu/docs
"""

# pylint: disable=broad-exception-raised

from time import sleep
from typing import Callable
from loguru import logger
from scc_whisper_api_client import config
from scc_whisper_api_client.client import SCCClient
from scc_whisper_api_client.models import (
    NewTranscribeTask,
    NewTranscribeTranslateTask,
    NewTranslateTask,
    TranscribeTaskResultElem,
    TranscribeTranslateTaskResultElement,
)


class SCCSyncClient(SCCClient):
    """Synchronous client for the SCC AI Services API"""

    def _sync_wrapper(
        self, add_func: Callable, get_func: Callable, max_tries=None, max_wait_time=None
    ) -> dict:
        """Wrapper for synchronous calls"""
        PAUSE_TIME = 5
        if max_tries is None:
            max_tries = config.SYNC_MAX_RETRIES
        if max_wait_time is None:
            max_wait_time = config.SYNC_MAX_WAIT_TIME_SEC
            max_tries = max_wait_time // PAUSE_TIME
        task_res = add_func()
        logger.info(task_res.model_dump_json())
        if task_res.task_id:
            result = None
            c = 0
            while not result:
                sleep(
                    1 + c * PAUSE_TIME
                )  # sleep a bit (and then same more) to give the task time to start
                res = get_func(task_res.task_id)
                logger.info(f"Task {task_res.task_id} state: {res.state}")
                if res.state in ["SUCCESS", "FAILURE"]:
                    result = res.result
                else:
                    logger.info(
                        f"Task {task_res.task_id} not finished yet; {max_tries - c} tries left."
                    )
                    if c > max_tries:
                        raise Exception(
                            f"Task {task_res.task_id} not finished after {max_tries} tries."
                        )
                    c += 1
            return result

    def run_transcribe_task(
        self, task: NewTranscribeTask, max_tries=None, max_wait_time=None
    ) -> TranscribeTaskResultElem:
        """Synchronous wrapper for transcribe task"""

        def add_func():
            return self.add_transcribe_task(task)

        def get_func(task_id):
            return self.get_transcribe_task(task_id)

        return self._sync_wrapper(add_func, get_func, max_tries, max_wait_time)

    def run_translate_task(
        self, task: NewTranslateTask, max_tries=None, max_wait_time=None
    ) -> dict[str, str]:
        """Synchronous wrapper for translate task"""

        def add_func():
            return self.add_translate_task(task)

        def get_func(task_id):
            return self.get_translate_task(task_id)

        return self._sync_wrapper(add_func, get_func, max_tries, max_wait_time)

    def run_transcribe_translate_task(
        self, task: NewTranscribeTranslateTask, max_tries=None, max_wait_time=None
    ) -> TranscribeTranslateTaskResultElement:
        """Synchronous wrapper for translate task"""

        def add_func():
            return self.add_transcribe_translate_task(task)

        def get_func(task_id):
            return self.get_transcribe_translate_task(task_id)

        return self._sync_wrapper(add_func, get_func, max_tries, max_wait_time)


def main():
    """Main function"""
    client = SCCSyncClient(
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
        # url="https://media.bibliothek.kit.edu/campus/2023/DIVA-2023-283_mp4.mp4xxx",
        source_language="de",
        target_languages=["en", "fr"],
    )
    res = client.run_transcribe_task(transcribe_task)
    logger.info(res)
    logger.info(res["transcript"].keys())
    logger.info(res)
    # res = client.run_translate_task(translate_task)

    # logger.info(pformat(client.add_translate_task(translate_task).dict()))

    # logger.info(pformat(client.get_translate_task(475022794)))


if __name__ == "__main__":
    main()

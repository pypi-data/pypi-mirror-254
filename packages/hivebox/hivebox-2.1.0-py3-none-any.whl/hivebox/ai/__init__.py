from datetime import datetime
from pathlib import Path
from typing import Optional, Any, Callable
import requests
from urllib.parse import urljoin


class Settings:
    webui_url = "http://127.0.0.1:7860"
    gateway_url = "http://127.0.0.1:8000"
    output_dir = Path.cwd() / "output"

    @classmethod
    def update(cls, settings: dict):
        for key, item in settings.items():
            setattr(cls, key, item)


def text_interpolation(prompts: list[str], count: Optional[int] = 100) -> list[str]:
    pass


def video_interpolation(source_img: str, target_img: str) -> str:
    pass


def text_to_image(prompt: str) -> str:
    pass


def text_image_to_image(prompt: str, source_img: str) -> str:
    pass


class Deforum:
    def __init__(self, settings: dict):
        self._settings = settings
        Settings.output_dir.mkdir(exist_ok=True, parents=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def text_to_image(self, prompt: str, settings: dict = None) -> bytes:
        url = urljoin(Settings.webui_url, "hive/deforum/")
        data = {"prompts": {'0': prompt}, "deforum_settings": settings or self._settings}

        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.content
        # filename = Settings.output_dir / datetime.now().strftime("result-%Y-%m-%d-%H-%M-%S.png")
        # with filename.open('wb') as f:
        #     f.write(response.content)
        # print(f"Stored content as {filename}")
        # return filename

    def update_settings(self, settings: dict):
        self._settings = settings


def data_to_text(data, context):
    prompt_template = f"""[INST] <<SYS>>{context}<</SYS>> {data}[/INST]"""
    print("Prepared prompt: ", prompt_template)
    response = requests.post(urljoin(Settings.gateway_url, "generate_prompt/llama2"), json={"prompt": prompt_template})
    response.raise_for_status()
    return response.content.decode()


def answer_text(prompt: str) -> str:
    response = requests.post(urljoin(Settings.gateway_url, "generate_prompt/llama2"), json={"prompt": prompt})
    response.raise_for_status()
    return response.content.decode()

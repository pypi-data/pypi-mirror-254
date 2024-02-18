import gai.common.ConfigHelper as ConfigHelper
from gai.common.http_utils import http_post
API_BASEURL = ConfigHelper.get_api_baseurl()


class STTClient:

    def __call__(self, generator=None, file=None):
        if generator == "openai-whisper":
            return self.openai_whisper(file=file)

        if not file:
            raise Exception("No file provided")

        files = {
            "model": (None, generator),
            "file": (file.name, file.read())
        }

        response = http_post(
            f"{API_BASEURL}/gen/v1/audio/transcriptions", files=files)
        response.decode = lambda: response.json()["text"]
        return response

    def openai_whisper(self, **model_params):
        import os
        import openai
        from openai import OpenAI
        from dotenv import load_dotenv
        load_dotenv()
        if not os.environ.get("OPENAI_API_KEY"):
            raise Exception(
                "OPENAI_API_KEY not found in environment variables")
        openai.api_key = os.environ["OPENAI_API_KEY"]
        client = OpenAI()

        if "file" not in model_params:
            raise Exception("Missing file parameter")

        file = model_params["file"]

        # If file is a bytes object, we need to write it to a temporary file then pass the file object to the API
        if isinstance(file, bytes):
            import tempfile
            with tempfile.NamedTemporaryFile(suffix='.wav') as temp:
                temp.write(file)
                temp.flush()
                temp.seek(0)
                model_params["file"] = temp.file
                response = client.audio.transcriptions.create(
                    model='whisper-1', **model_params)
        else:
            response = client.audio.transcriptions.create(
                model='whisper-1', **model_params)

        return response

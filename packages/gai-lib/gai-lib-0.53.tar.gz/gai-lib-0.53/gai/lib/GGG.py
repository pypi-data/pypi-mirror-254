from gai.lib.ttt.TTTClient import TTTClient
from gai.lib.STTClient import STTClient
from gai.lib.TTSClient import TTSClient
from gai.lib.ITTClient import ITTClient
from gai.lib.RAGClient import RAGClient


class GGG:
    client = None

    def __call__(self, category, **model_params):
        if category.lower() == "ttt":
            self.client = TTTClient()
            return self.client(**model_params)
        elif category.lower() == "ttt-mistral128k":
            self.client = TTTClient()
            return self.client(**model_params)
        elif category.lower() == "stt":
            self.client = STTClient()
            return self.client(**model_params)
        elif category.lower() == "tts":
            self.client = TTSClient()
            return self.client(**model_params)
        elif category.lower() == "itt":
            self.client = ITTClient()
            return self.client(**model_params)
        elif category.lower() == "index":
            self.client = RAGClient()
            return self.client.index_file(**model_params)
        elif category.lower() == "retrieve":
            self.client = RAGClient()
            return self.client.retrieve(**model_params)
        else:
            raise Exception(f"Unknown category: {category}")

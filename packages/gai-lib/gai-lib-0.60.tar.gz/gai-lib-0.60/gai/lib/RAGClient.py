import requests
import json
import gai.common.ConfigHelper as ConfigHelper
from fastapi import WebSocketDisconnect
from gai.common.http_utils import http_post
from gai.common.logging import logging
logger = logging.getLogger(__name__)
API_BASEURL = ConfigHelper.get_api_baseurl()


class RAGClient:

    def index_text(self, collection_name, title, text, metadata={"source": "unknown"}):
        url = f"{API_BASEURL}/gen/v1/rag/index"
        headers = {
            'accept': 'application/json',
        }
        data = {
            "collection_name": collection_name,
            "text": text,
            "path_or_url": title,
            "metadata": json.dumps(metadata)
        }
        response = requests.post(
            url=url, headers=headers, data=data)
        return response

    # Provides an updater to get chunk indexing status
    # NOTE: The update is only relevant if this library is used in a FastAPI application with a websocket connection
    async def index_file_async(self, collection_name, file_path, metadata={"source": "unknown"}, progress_updater=None):
        with open(file_path, "r") as f:
            url = f"{API_BASEURL}/gen/v1/rag/index_file"
            headers = {
                'accept': 'application/json',
            }
            data = {
                "collection_name": collection_name,
                "metadata": json.dumps(metadata)
            }
            files = {
                "file": f,
            }
            response = requests.post(
                url=url, headers=headers, data=data, files=files)

        # Callback for progress update (returns a number between 0 and 100)
        if progress_updater:
            # Exception should not disrupt the indexing process
            try:
                # progress = int((i + 1) / len(chunks) * 100)
                progress = 100
                await progress_updater(progress)
                logger.debug(
                    f"RAGClient: progress={progress}")
                # await send_progress(websocket, progress)
            except WebSocketDisconnect as e:
                if e.code == 1000:
                    # Normal closure, perhaps log it as info and continue gracefully
                    logger.info(
                        f"RAGClient: WebSocket closed normally with code {e.code}")
                    pass
                else:
                    # Handle other codes as actual errors
                    logger.error(
                        f"RAGClient: WebSocket disconnected with error code {e.code}")
                    pass
            except Exception as e:
                logger.error(
                    f"RetrievalGeneration.index_async: Update websocket progress failed. Error={str(e)}")
                pass

            return response

    def retrieve(self, collection_name, query_texts, n_results=None):
        data = {
            "collection_name": collection_name,
            "query_texts": query_texts
        }
        if n_results:
            data["n_results"] = n_results

        response = http_post(f"{API_BASEURL}/gen/v1/rag/retrieve", data=data)
        return response

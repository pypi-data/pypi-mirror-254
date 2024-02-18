import gai.common.ConfigHelper as ConfigHelper
from gai.common.http_utils import http_post
API_BASEURL = ConfigHelper.get_api_baseurl()
import json, requests

class RAGClient:

    def index_file(self, collection_name, file_path, metadata={"source":"unknown"}):
        with open(file_path, "r") as f:
            url =  f"{API_BASEURL}/gen/v1/rag/index_file"
            headers = {
                'accept': 'application/json',
            }
            data={
                "collection_name":collection_name,
                "metadata":json.dumps(metadata)
            }
            files={
                "file":f, 
            }
            response = requests.post(url=url,headers=headers,data=data,files=files)
            return response

    def retrieve(self, collection_name, query_texts, n_results=None):
        data={
            "collection_name":collection_name,
            "query_texts":query_texts
        }
        if n_results:
            data["n_results"]=n_results
       
        response = http_post(f"{API_BASEURL}/gen/v1/rag/retrieve",data=data)
        return response



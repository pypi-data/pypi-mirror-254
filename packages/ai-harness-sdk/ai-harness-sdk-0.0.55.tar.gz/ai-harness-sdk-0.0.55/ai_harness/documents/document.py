import requests, time, json 
from ..agents.utils.RestWrapper import APIWrapper

class Documents:
    def __init__(self):
        api_wrapper_inst = APIWrapper()
        api_key, self.base_url = api_wrapper_inst.get_credentials()
        self.headers = {'API-Key': api_key}
    
    #create collection
    def create_collection(self,collection_name:str):
        print(f'Creating collection {collection_name}...')
        url = f"{self.base_url}/api/collections"
        collection_payload = {
            "collection_name":collection_name+str(time.time())
        }

        response = requests.post(url, json =collection_payload,headers = self.headers)
        result = response.content
        parsed_data = json.loads(result)
        self.collection_id = parsed_data['data']['uuid']
        print('collection id:',self.collection_id)
        

    #upload documents to the ai-harness
    def upload_documents(self, doc_path:str, collection_id:str=None, ingest_with_google: bool = False):
            
            url = f"{self.base_url}/api/documents"

            files = {'files': open(doc_path, 'rb')}
            data = {
                "collection_id": collection_id,
                "ingest_with_google": ingest_with_google,
            }
            print('Uploading document...')
            
            response = requests.post(url, data=data, headers=self.headers, files=files)
            result = response.content
            parsed_data = json.loads(result)
            self.document_id = parsed_data['data'][0]['id']
                
                                    
            print('document id:',  self.document_id)
       
            while True:
                get_doc_by_id_url = f"{self.base_url}/api/documents/{self.document_id}"
                response = requests.get(get_doc_by_id_url, headers=self.headers)
                res = response.json()

                print('Upload status: ',res['data']['processing_job_status'])   
                if res['data']['processing_job_status'] == 'completed':
                    print('Document upload completed successfully.')
                    break;
                else:
                    if res['data']['processing_job_status'] == 'failed':
                        print('Document upload failed.')
                        break;
                    else : 
                        continue

    def get_all_collections(self):
        url = f"{self.base_url}/api/collections"
        response = requests.get(url, headers=self.headers)
        res = response.json()
        owned = []
        shared = []

        if 'data' in res and 'owned' in res['data']:
            for collection in res['data']['owned']:
                collection_id = collection['uuid']
                collection_name = collection['name']
                owned.append({'collection_id': collection_id, 'name': collection_name})

        if 'data' in res and 'shared' in res['data']:
            for collection in res['data']['shared']:
                collection_id = collection['uuid']
                collection_name = collection['name']
                shared.append({'collection_id': collection_id, 'name': collection_name})

        print('Owned collections:\n', owned)
        print('Shared collections:\n', shared)
        
        return owned, shared
                        
from typing import Optional
from .utils.RestWrapper import APIWrapper
from .utils.AppletResponse import SyncResponse
import uuid


class QaRetrieval:
    """
    Applet for QA retrieval, it takes detail of the document or collection as input
    and returns the answer for the question asked
    it Understands your documents and answers your questions
    """

    def __init__(self, prompt: str = None, conversation_id: str = None, collection_id: str = None, document_id: str = None):
        self.prompt = prompt
        self.conversation_id = conversation_id
        self.collection_id = collection_id
        self.document_id = document_id

    def run(self) -> SyncResponse:
        """
        Method to run the QA Retrieval applet
        either document or collection id is required to run the applet
        it retrieves the answer for the question asked from the document or collection provided

        Parameters
        ----------
        prompt : str
            question to be asked to the AI agent
        document_id : str
            id of the document through which the answer is to be retrieved
        collection_id : str
            id of the collection through which the answer is to be retrieved

        Returns
        -------
        SyncResponse
            SyncResponse object with the answer ,conversation id and sources , sources are the documents from which the answer is retrieved
        """

        if not self.prompt:
            raise ValueError("Prompt is required")

        if not self.collection_id and not self.document_id:
            raise ValueError("Either collection_id or document_id is required")

        if not self.conversation_id:
            self.conversation_id = str(uuid.uuid4())

        user_params = {
            "prompt": self.prompt,
        }

        if self.document_id:
            # document id to be provided to the applet
            user_params["document_id"] = self.document_id
        elif self.collection_id:
            # collection id to be provided to the applet
            user_params["collection_id"] = self.collection_id

        payload = {
            "applet_code": "qa-retrieval",
            "conversation_id": self.conversation_id,
            "user_params": user_params,
        }

        api_response = APIWrapper(payload).execute_sync()
        api_response_json = api_response.json()
        content = api_response_json['content']
        sources = api_response_json['msg_info']['sources']
        response = SyncResponse(
            answer=content, conversation_id=self.conversation_id, sources=sources)
        resp_obj = response.obj()

        return resp_obj

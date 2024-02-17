from typing import Dict
from .utils.RestWrapper import APIWrapper
from .utils.AppletResponse import SyncResponse
import uuid


class JsonToJson:
    """
    Applet for Extracting metrics from your input json, where an input json
    is provided as input to the applet and the output json is provided as an json format in which applet returns the answer
    """

    def __init__(self, input_json: Dict = None, output_json: Dict = None, conversation_id: str = None):
        self.input_json = input_json
        self.output_json = output_json
        self.conversation_id = conversation_id

    def run(self) -> SyncResponse:
        """
        Method to run the JsonToJson applet

        Parameters
        ----------
        input_json : Dict
            input json from which extraction of metrics is to be done
        output_json : Dict
            output json format in which applet returns the answer

        Returns
        -------
        SyncResponse
            SyncResponse object with the answer and conversation id 

        """
        if not self.input_json:
            raise ValueError("input_json is required")

        if not self.output_json:
            raise ValueError("output_json is required")

        if not self.conversation_id:
            self.conversation_id = str(uuid.uuid4())

        payload = {
            "applet_code": "json-to-json",
            "conversation_id": self.conversation_id,
            "user_params": {
                "input_json": self.input_json,
                "output_json": self.output_json
            }
        }

        api_response = APIWrapper(payload).execute_sync()
        api_response_json = api_response.json()
        content = api_response_json['content']
        response = SyncResponse(
            answer=content, conversation_id=self.conversation_id)
        resp_obj = response.obj()

        return resp_obj

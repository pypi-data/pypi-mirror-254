import time
from .utils.RestWrapper import APIWrapper
from .utils.AppletResponse import AsyncResponse


class PlaceMaking:
    """
    Applet for place making agent for a given site location, where site name is provided as input to the
    applet and the output is the place making suggestions of the site
    the applet gives Curated Placemaking Suggestions for site based on history of the site
    and nearby places around the site.
    """

    def __init__(self, site_name: str = ""):
        self.site_name = site_name

    def run(self):
        """
        Method to run the PlaceMaking applet

        Parameters
        ----------
        site_name : str
            name of the site for which the place making suggestions are to be generated

        Returns
        -------
        AsyncResponse
            AsyncResponse object with the answer

        """
        if not self.site_name:
            raise Exception("Site Name is required")

        payload = {
            "applet_code": "placemaking",
            "user_params": {
                "prompt": self.site_name,  # title of the analysis
                "site_name": self.site_name,  # site name to be provided to the applet
            }

        }

        answer = APIWrapper(payload).execute_async()
        answer_json = answer.json()
        conv_id = answer_json['data']['conversation_id']
        print(f"PlaceMaking: conv_id: {conv_id}")

        # getAsyncRunStatus() it gives status of asynchronous applet execution whether its failed in process or completed. it requires conversation id and applet code as parameters.
        while True:  # loop until the applet execution is completed
            response = APIWrapper().getAsyncRunStatus(conv_id, "placemaking")
            print(f"PlaceMaking: response: {response}")
            if response:
                break
            time.sleep(2)

        result = AsyncResponse(answer=response)
        result_obj = result.obj()
        return result_obj

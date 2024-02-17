import time
from .utils.RestWrapper import APIWrapper
from .utils.AppletResponse import AsyncResponse


class SiteAnalysis:
    """
    Applet to Get a detailed analysis of a URA Site or a Geo-Location. it requires URA site id or coordinates and
    properties to be analyzed for the site as input parameters and returns the analysis of the site.
    the analysis includes nearby places around the site , history of the site , demographics of the site , market analysis of the site , competitive analysis of the site,
    stations near the site , airport near the site , seaport near the site , zones near the site and distance from the airport , seaport and stations to the site.
    """

    def __init__(self, siteId: str = "", lat: float = 0, long: float = 0, properties: list = None, market_analysis: str = None, competitive_analysis: str = None):
        self.siteId = siteId
        self.lat = lat
        self.long = long
        self.properties = properties
        self.market_analysis = market_analysis
        self.competitive_analysis = competitive_analysis

    def run(self) -> AsyncResponse:
        """
        Method to run the Site Analysis applet ,
        it requires URA site id or coordinates and properties(features) to be analyzed for the site as input parameters 

        Parameters
        ----------
        siteId : str
            URA site id of a site
        lat : float
            latitude of the site
        long : float
            longitude of the site
        properties : list
            properties to be analyzed for the site , properties should be from the properties_list {"stations","airport","seaport","zones","competitive_analysis","market_analysis","history","demographics","nearby_analysis"}
        market_analysis : str
            type of analysis whether "residential" , "commercial" or "industrial" to be performed for the site for market analysis
        competitive_analysis : str
            type of analysis whether "residential" , "commercial" or "industrial" to be performed for the site for competitive analysis


        Returns
        -------
        AsyncResponse
            AsyncResponse object with the answer

        """

        analysisType = {}

        properties_list = [
            "stations",
            "airport",
            "seaport",
            "zones",
            "competitive_analysis",
            "market_analysis",
            "history",
            "demographics",
            "nearby_analysis"
        ]

        if not (self.siteId or (self.lat and self.long)):
            raise Exception("Either Site Id or Lat Long is required")

        for prop in self.properties:
            if prop not in properties_list:
                raise Exception(f"Invalid property: {prop}")

        if self.market_analysis:
            analysisType['market'] = f"market_{self.market_analysis}"

        if self.competitive_analysis:
            analysisType['competitive'] = f"competitive_{self.competitive_analysis}"

        payload = {
            "applet_code": "site-analysis",
            "user_params":
                {
                    "prompt": "Site Analysis of ........",
                    "siteId": self.siteId,  # URA site id of a site
                    "lat_long": {
                        "latitude": self.lat,  # latitude of the site
                        "longitude": self.long  # longitude of the site
                    },
                    "properties": self.properties,
                    "analysisType": analysisType
                }
        }

        answer = APIWrapper(payload).execute_async()
        answer_json = answer.json()
        conv_id = answer_json['data']['conversation_id']

        while True:  # loop until the applet execution is completed
            response = APIWrapper().getAsyncRunStatus(conv_id, "site-analysis")
            print(f"SiteAnalysis: response: {response}")
            if response:
                break
            time.sleep(2)
        result = AsyncResponse(answer=response)
        res_obj = result.obj()
        return res_obj

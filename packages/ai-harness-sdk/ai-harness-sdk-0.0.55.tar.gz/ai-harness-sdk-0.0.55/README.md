# AI-Harness

AI-Harness is a Python package designed to showcase and utilize the capabilities of the AI Harness platform. This SDK provides a set of tools and functionalities to interact with the AI Harness ecosystem and integrate AI models seamlessly.

## Installation

You can install AI-Harness using pip:

```bash
pip install ai-harness
```

## Usage 

```bash

# Import necessary modules
from dotenv import load_dotenv
from ai_harness.documents.document import Documents

# Load environment variables from a .env file
load_dotenv()

# Initialize a Documents instance
doc_instance = Documents()

# To Create a collection in the AI Harness platform
doc_instance.create_collection(collection_name="sample_collection")

# Upload documents to the created collection
doc_instance.upload_documents(
    doc_path=r"document_path",  # Specify the path to the documents
    collection_id="",  # Provide the ID of the target collection
    ingest_with_google="false"  # Indicate whether to ingest documents using Google API or open source pdf loader
)

# import applets from agents 
from ai_harness.agents.applet_name import applet_name

# run a Conversation applet
result = Conversation(prompt="Your Prompt").run()

# run a Place Making applet
result = PlaceMaking(site_name="write site name here").run()

# run a Query Generator applet
result = QueryGenerator(
    prompt="Your Prompt", 
    dialect="dialect name",
    schema="schema",
    db_type="db type(relational or non-relational)",
    additional_filters="any additional filters"
    ).run()

# run a Site Analysis applet
result = SiteAnalysis(
    lat="latitude of site", # either use coordinates or site ID
    long="longitude of site",
    siteId="URA site id of site", # using URA site ID 
    properties=["stations","market_analysis","competitive_analysis","airport","seaport","zones","history","demographics"], #  list of features that can be used 
    market_analysis="residential", # market analysis (residential , commercial or industrial) 
    competitive_analysis="industrial" # competitive analysis (residential , commercial or industrial) 
    ).run()

# run JSON TO JSON applet
result = JsonToJson(
    input_json="input json", 
    output_json="output json", 
    ).run()

# run Query Retrieval applet
result = QaRetrieval(
    prompt="prompt",
    document_id="id of document uploaded on ai harness", 
    ).run()

```


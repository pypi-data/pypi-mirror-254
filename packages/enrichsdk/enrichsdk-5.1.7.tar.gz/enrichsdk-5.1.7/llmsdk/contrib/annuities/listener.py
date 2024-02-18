"""
Simple LLM Proxy that works with the front end. This derives from the QnA service module.

"""
import os
import sys
import json
import traceback
from datetime import datetime

from logging.config import dictConfig
from typing import Annotated, Dict, Any, Optional, List
from enum import Enum

from pydantic import BaseModel,  ValidationError, validator
from fastapi import FastAPI, File, Form, UploadFile
from fastapi import HTTPException, Header, Security
from fastapi.security import APIKeyHeader, APIKeyCookie, APIKeyQuery

from llmsdk.lib import SafeEncoder
from llmsdk.services.log import *
from llmsdk.services.lib import get_stats, initialize_stats

# Override default uvicorn logger...
logging.config.dictConfig(log_config)
logger = get_logger()

HEADER_API_KEY = APIKeyHeader(name='X-API-Key',auto_error=False)
def validate_api_key(key):
    """
    Check whether the API Key is valid
    """
    api_keys = os.environ.get("APIKEYS","")
    api_keys = api_keys.split(",")

    return key in api_keys

app = FastAPI()

class FormatChoices(Enum):
    xml = 'xml'
    pdf = 'pdf'
    json = 'json'

class CategoryChoices(Enum):
    test = 'test'
    production = 'production'

class Document(BaseModel):
    uuid: Optional[str] = None
    filename: str
    content: str
    metadata: Dict[Any,Any] = {}


class ListenerData(BaseModel):
    category: CategoryChoices
    uuid: str
    documents: List[Document]
    metadata: Dict[Any,Any] = {}

    @validator('uuid')
    def uuid_must_be_10chars_long(cls, v):
        if len(v) < 10:
            raise ValueError('must be atleast 10 characters long')
        return v

    @validator('documents')
    def atleast_one_document(cls, v):
        if len(v) == 0:
            raise ValueError('must include atleast one document')
        return v

@app.get("/health")
def health():
    """
    Return usage statistics

    Returns
    -------
    stats: dict
           Usage statistics

    """

    stats = get_stats()

    logger.info("Returning stats",
                extra={
                    'data': json.dumps(stats, indent=4)
                })
    return stats


@app.post("/application/")
async def receive_application(
        data: ListenerData,
        header_api_key: str = Security(HEADER_API_KEY),
):

    """
    Post a new application and receive an acknowledgement

    Returns
    -------
    stats: dict
           uuid, size, and type of the application
    """

    if not validate_api_key(header_api_key):
        logger.error("Invalid API Key",
                     extra={
                         'data': header_api_key
                     })
        raise HTTPException(status_code=401,
                            detail=f"Invalid API Key")

    # Do a check on API key
    # Now check if the document is new or existing...
    data_root = os.environ['DATA_ROOT']

    doc_id = data.uuid
    doc_category = data.category.value
    doc_metadata = data.metadata

    targetdir = os.path.join(data_root, doc_category, doc_id)
    os.makedirs(targetdir, exist_ok=True)

    metadatafile = os.path.join(targetdir, "metadata.json")
    successfile = os.path.join(targetdir, "_SUCCESS")
    if ((os.path.exists(targetdir)) and
        (os.path.exists(metadatafile)) and
        (os.path.exists(successfile))):
        logger.error("Document exists",
                     extra={
                         'request_id': doc_id,
                     })
        raise HTTPException(status_code=403,
                            detail= f"Document already uploaded: {doc_id}")

    try:

        metadata = {
            'utctimestamp': datetime.utcnow().isoformat(),
            "dirname": targetdir,
            "document": {
                "id": doc_id,
                "metadata": doc_metadata,
                "files": {}
            }
        }

        # Dump the files...
        for doc in data.documents:
            doc_content = doc.content
            doc_filename = doc.filename
            doc_metadata = doc.metadata

            filename = os.path.join(targetdir, doc_filename)
            with open(filename, "w") as fd:
                fd.write(doc_content)

            # Store the metadata
            metadata['document']['files'][doc_filename] = {
                "size": len(doc_content),
                "metadata": doc_metadata
            }

        # Write the metadata
        with open(metadatafile, 'w') as fd:
            fd.write(json.dumps(metadata, indent=4))

        with open(successfile, "w") as fd:
            fd.write("")

        logger.info("Document received",
                    extra={
                        'request_id': doc_id,
                        'data': json.dumps(metadata, indent=4)
                    })

        return {
            "doc_id": doc_id,
            "status": "success",
            "message": "Received document",
        }

    except:
        traceback.print_exc()
        logger.exception("Error while process",
                         extra={
                             'request_id': doc_id,
                             'data': targetdir
                         })

        raise HTTPException(status_code=500,
                            detail= f"Error while processing the document")

@app.on_event("startup")
def app_startup():


    if "DATA_ROOT" not in os.environ:
        print("DATA_ROOT is missing in the environment")
        raise Exception("Invalid configuration")

    initialize_stats()

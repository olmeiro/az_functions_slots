import os
import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", 
                  path=os.environ["BLOB_CONTAINER_PATH"],
                  connection="rglearningaz95d1_STORAGE") 
def blob_trigger(myblob: func.InputStream):
    logging.info(f"Environment: {os.environ.get('APP_ENV', 'UNKNOWN')}")
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# nest_asyncio

from typing import Optional
from pyngrok import ngrok
import nest_asyncio
import uvicorn
import json

# 1st import the package and check its version
import MTM
print("MTM version: ", MTM.__version__)

from MTM import matchTemplates, drawBoxesOnRGB

import cv2
from skimage.data import coins

import numpy as np
from skimage import io

from PIL import Image
from tqdm import tqdm
import glob
import os 


"""
or inssted just install pip install 
Multi-Template-Matching
fastapi
nest_asyncio
numpy
tqdm
"""


print("[status] : packages load successfully !")


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World packages loaded successfully"}




# if __name__ == 'main':
#     uvicorn.run(app,host="127.0.0.1",port=8000)

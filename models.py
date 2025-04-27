import os
import json

from typing import Any

from openai import OpenAI
from pandas import read_csv
from pandas import DataFrame
from operator import itemgetter
from scipy.spatial import distance

# Get OpenAI secret key
SECRET_KEY: str = os.getenv("OPI_OPENAI_API_KEY")
# Instantiate OpenAI client
emb_client = OpenAI(
    api_key=SECRET_KEY,
)
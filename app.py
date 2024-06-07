from typing import Dict, List
from fastapi import FastAPI
from num2words import num2words
import uvicorn

import os

app: FastAPI = FastAPI()
debug: bool = "DEBUG" in os.environ and os.environ["DEBUG"] in ["1", "true"]

@app.get("/convert_to_french/list={numbers}")
def convert_numbers_to_french(numbers: str) -> Dict[int, str]:
    """
    Convert a list of numbers (passed as a string) to their French word equivalents.

    Parameters
    ----------
    numbers : str
        A string of comma-separated integers to convert to French.

    Returns
    -------
    Dict[int, str]
        A dictionary where each key is a number from the input list,
        and the value is the French word equivalent of that number.
    """
    numbers = numbers.strip('[]')
    numbers_list = [int(number) for number in numbers.split(',')]
    return {number: num2words(number, lang='fr') for number in numbers_list}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, reload=debug)
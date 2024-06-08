from typing import Dict, List
from fastapi import FastAPI
import uvicorn
from config import units, tens

import os

app: FastAPI = FastAPI()
debug: bool = "DEBUG" in os.environ and os.environ["DEBUG"] in ["1", "true"]

def under_hundred(n):
    if n <= 16:                                                 # For: "zéro", "un", ..., "onze", "douze", "treize", "quatorze", "quinze", "seize"
        return units[n]
    elif n < 20:                                                # For: "dix-sept", "dix-huit", "dix-neuf"
        return "dix-" + units[n-10]
    elif n < 70:                                                # For: "vingt", "trente", "quarante", "cinquante", "soixante"
        if n % 10 == 0:
            return tens[n // 10]
        elif n % 10 == 1 and n < 70:                            # For: "vingt-et-un", "trente-et-un", "quarante-et-un", "cinquante-et-un", "soixante-et-un"
            return tens[n // 10] + "-et-un"
        else:                                                   # For: from 22 to 29, 32 to 39, 42 to 49, 52 to 59, and 62 to 69
            return tens[n // 10] + "-" + units[n % 10]
    elif n == 71:
        return "soixante-et-onze"
    elif n < 80:                                                # For: "soixante-douze" to "soixante-dix-neuf"
        return "soixante-" + under_hundred(n - 60)
    else:
        return "quatre-vingt" + ("" if n == 80 else "-" + under_hundred(n - 80))        # For: "quatre-vingt" to "quatre-vingt-dix-neuf' 

def beyond_hundred(n):
    if n < 100:                                                 # For: under hundred numbers (above function)
        return under_hundred(n)
    
    hundreds, remain_1 = divmod(n, 100)                         # Get Quotient and remaininder

    if n < 1000:
        if n == 100:                                            # For: "cent"
            return "cent"
        if n >= 101 and n <=199:                                # For: 101 <= n <= 199
            return "cent-" + under_hundred(remain_1)
        else:                                                   # For: "deux-cents", "trois-cents", ..., "cinq-cents", "six-cent", ...
            result = units[hundreds] + "-cents"

            if remain_1 != 0:
                result = units[hundreds] + "-cent" + "-" + under_hundred(remain_1)              # For: "deux-cent-un", ..., "cinq-cent-dix-neuf"

            return result
        
    thousands, remain_2 = divmod(n, 1000)

    if n < 1000000:                                             # For: 1001 to 999999 (inluding this line `result += "-" + beyond_hundred(remain_2)`)
        if thousands > 1:
            result = beyond_hundred(thousands) + "-mille"
        else:
            result = "mille"

        if remain_2 != 0:
            result += "-" + beyond_hundred(remain_2)            

        return result
    
    millions, remain_3 = divmod(n, 1000000)

    if millions > 1:                       # For 1000001 to 9999999999999999999999999999999999......  (inluding this line `result += "-" + beyond_hundred(remain_3)`)
        result = beyond_hundred(millions) + "-million"
    else:
        result = "un-million"

    if remain_3 != 0:
        result += "-" + beyond_hundred(remain_3)

    return result

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
    return {number: beyond_hundred(number) for number in numbers_list}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, reload=debug)

# Jus Mundis - Technical Test - Data Engineer (LLM/Python)
The following repository contains a FastAPI application to convert a list of numbers to their equivalent in French.


## Standalone Execution
To execute, one of the following options can be used:
- [app.py](https://github.com/berririamal/jusmundi/blob/master/app.py) allows to store convert the numbers using [num2words](https://github.com/savoirfairelinux/num2words).
    ```sh
    python app.py
    ```

A browser can be used to play with the API:
```
<IP_of_the_hosted_machine>:<available_port>/convert_to_french?list=<list_of_numbers>
```

## Docker
- To build the docker based on [Dockerfile](https://github.com/BerririAmal/jusmundi/blob/master/Dockerfile), use the following command:
    ```sh
    sudo docker image build -t <image_name> .
    ```
- To run the docker, use the following command and open in a Web Browser the IP Address of the docker with a warehouse address:
    ```sh
    sudo docker run -p <available_port>:5001 <image_name>
    ```

## Requirements
Python 3.9.6 version is used.

Install the necessary dependencies using the following:
```bash
pip install -r requirements.txt
```

## Usage
The API is exposed in the following:
[http://158.178.205.214:14488/docs](http://158.178.205.214:14488/docs)

**Example**
```bash
[0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]
```

**Output**
```bash
{
  "0": "zéro",
  "1": "un",
  "5": "cinq",
  "10": "dix",
  "11": "onze",
  "15": "quinze",
  "20": "vingt",
  "21": "vingt et un",
  "30": "trente",
  "35": "trente-cinq",
  "50": "cinquante",
  "51": "cinquante et un",
  "68": "soixante-huit",
  "70": "soixante-dix",
  "75": "soixante-quinze",
  "99": "quatre-vingt-dix-neuf",
  "100": "cent",
  "101": "cent un",
  "105": "cent cinq",
  "111": "cent onze",
  "123": "cent vingt-trois",
  "168": "cent soixante-huit",
  "171": "cent soixante et onze",
  "175": "cent soixante-quinze",
  "199": "cent quatre-vingt-dix-neuf",
  "200": "deux cents",
  "201": "deux cent un",
  "555": "cinq cent cinquante-cinq",
  "999": "neuf cent quatre-vingt-dix-neuf",
  "1000": "mille",
  "1001": "mille un",
  "1111": "mille cent onze",
  "1199": "mille cent quatre-vingt-dix-neuf",
  "1234": "mille deux cent trente-quatre",
  "1999": "mille neuf cent quatre-vingt-dix-neuf",
  "2000": "deux mille",
  "2001": "deux mille un",
  "2020": "deux mille vingt",
  "2021": "deux mille vingt et un",
  "2345": "deux mille trois cent quarante-cinq",
  "9999": "neuf mille neuf cent quatre-vingt-dix-neuf",
  "10000": "dix mille",
  "11111": "onze mille cent onze",
  "12345": "douze mille trois cent quarante-cinq",
  "123456": "cent vingt-trois mille quatre cent cinquante-six",
  "654321": "six cent cinquante-quatre mille trois cent vingt et un",
  "999999": "neuf cent quatre-vingt-dix-neuf mille neuf cent quatre-vingt-dix-neuf"
}
```
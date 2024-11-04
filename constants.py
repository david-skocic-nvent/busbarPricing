from pathlib import Path
import os

# Get the path of the current file
PROJECT_PATH = Path(os.path.abspath(__file__)).parent

GROUNDBAR_INPUT = PROJECT_PATH / "data\\input\\groundbar_partnumbers.txt"
GROUNDBAR_INTERMEDIATE = PROJECT_PATH / "data\\intermediate\\groundbar_partnumbers.csv"
GROUNDBAR_OUTPUT = PROJECT_PATH / 'data\\output\\groundbar'

TELECOM = "telecom"
GROUND = "ground"
EURO = "euro"
USD = "usd"
YUAN = "yuan"

FIELD_NAMES_GROUND = ["part number", "configuration", "bar thickness", "bar width", "bar length", "hole pattern", "hole size", "material", "pigtail code", "pigtail length"]
FIELD_NAMES_TELECOM = ["part number", "prefix", "configuration", "length", "number of holes", "material"]

LINK = "https://nventefs-test.tactoncpq.com/solution/4435b3de99324b5592de62be4ecb98c2"
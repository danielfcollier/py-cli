import os
import json

def read_json(base_path, *files):
  filepath = os.path.join("..", base_path)
  for file in files:
    filepath = os.path.join(filepath, file)

  print(filepath)
  with open(filepath) as jsonFile:
    data = json.load(jsonFile)

  return data

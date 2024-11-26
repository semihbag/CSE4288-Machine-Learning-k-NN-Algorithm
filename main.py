import json
import os
import traceback

current_dir = os.path.dirname(__file__)
path = os.path.join(current_dir,"resources", "original_train_dataset.json")

try:
    with open(path, "r", encoding="utf-8") as dosya:
        veriler = json.load(dosya)
        
except Exception as e:
    print(traceback.format_exc())
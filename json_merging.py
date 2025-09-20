# #Input-> Directory(json files)
# #Output-> merged json containg the text and words from all the json files
# # In this script we are mergin gth emultiple json files into one(text and words) 
# # We have to run this script on windows because even if natsort is installed no module error is there in linux

import os
import json
import shutil
from natsort import natsorted

# Function for validating usr input
def validator(input_dir):
    return os.path.isdir(input_dir)
#Function for collecting the json data
def collect_json_data(json_path,text_container,word_container):
    with open(json_path, "r", encoding="utf-8") as f:  # Opeaning the json for reading 
        data = json.load(f)
    texts = data.get("text", [])
    words=data.get("words",[])
    text_container.append(texts)
    word_container.append(words)

# Main function ofr merging the json files
def merge_json_files(file,my_text,my_words):
    with open(file, "r", encoding="utf-8") as f:
        merged_data = json.load(f)

    # Ensure base fields are lists, even if they were strings
    if isinstance(merged_data["text"], str):
        merged_data["text"] = [merged_data["text"]]
    if isinstance(merged_data["words"], str):
        merged_data["words"] = [merged_data["words"]]

    # Collect all other paragraphs (excluding the first one which is already in base)
    for para in my_text[1:]:
        if isinstance(para, str):
            merged_data["text"].append(para)
        elif isinstance(para, list):
            merged_data["text"].extend(para)

    for para in my_words[1:]:
        if isinstance(para, str):
            merged_data["words"].append(para)
        elif isinstance(para, list):
            merged_data["words"].extend(para)

    # Write updated content back to file
    with open(file, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully merged into: {file}")
    return file
        
if __name__=="__main__":
    try:
        input_folder=input("Please enter your directory containing json files: ")
        if not validator(input_folder):
            raise Exception()
    except Exception as e:
        print("Please provide valid directory path!")
    else:
        json_count=0
        json_text=[]
        json_words=[]
        json_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".json")]
        json_files = natsorted(json_files)
        
        for each_file in json_files:
            if each_file.lower().endswith(".json"):
                json_count+=1
                if json_count==1:
                        output_file = os.path.join(input_folder, f"Merged_{each_file}")
                        copied_file=shutil.copy(os.path.join(input_folder,each_file), output_file)
                        collect_json_data(os.path.join(input_folder,each_file),json_text,json_words)
                else:
                    collect_json_data(os.path.join(input_folder,each_file),json_text,json_words) 
        merge_json_files(copied_file,json_text,json_words)

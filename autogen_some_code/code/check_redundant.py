# 将正常和冗余的回答分别和prompt连接起来，以便复制给chatgpt

import os

folder_path = "/mnt/e/我/works/ml/autogen_some_code/results"
prompt_path = "/mnt/e/我/works/ml/autogen_some_code/text/code-generation/redundant_in_context_prompt"
extract_path = "/mnt/e/我/works/ml/autogen_some_code/results/extract"
ask_chatgpt_path = "/mnt/e/我/works/ml/autogen_some_code/results/extract/ask_chatgpt"

def folder_create():
    if not os.path.exists(extract_path):
    # Use os.makedirs() to create the directory and its parent directories if they don't exist
        os.makedirs(extract_path)
    if not os.path.exists(ask_chatgpt_path):
        os.makedirs(ask_chatgpt_path)

def extract_assis_chat(data: str, filename: str, is_normal: bool) -> list:
    import re

    pattern = ('\n' + r"normal_assistant[\s\S]*?" + "-" * 80) if is_normal else ('\n' + r"redundant_assistant[\s\S]*?" + "-" * 80)
    matches = re.findall(pattern, data)
    
    if not matches:
        print("No match chat:" +("normal") if is_normal else "redundant" + " :"+ filename  ) 
        return []
    
    answer_list = []

    for chat in matches:
        answer = chat[1:].split('\n', 1)[1][:-80]
        answer_list.append(answer)

    return answer_list



if __name__ == "__main__":
    
    with open(prompt_path, "r") as f:
        prompt = f.read() + "\n"

    # load the results
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue
        if not filename.endswith(".md"):
            continue
        file = open(file_path, "r")
        data = file.read()
        # store
        normal_answer_list = extract_assis_chat(data, filename, True)
        normal_answer_list_file = open(extract_path + "/" +  filename + ":normal", "w")
        for normal_answer in normal_answer_list:
            normal_answer_list_file.write(prompt + "\n" + '"""\n' + normal_answer + '"""\n\n')
            # normal_answer_list_file.write(prompt + "\n" + '"""\n' + normal_answer + '""" \\\\ \n\n')
        normal_answer_list_file.close()

        redundant_answer_list = extract_assis_chat(data, filename, False)
        redundant_answer_list_file = open(extract_path + "/" + filename + ":redundant", "w")
        for redundant_answer in redundant_answer_list:
            redundant_answer_list_file.write(prompt + "\n" + '"""\n' + redundant_answer + '"""\n\n')
            # redundant_answer_list_file.write(prompt + "\n" + '"""\n' + redundant_answer + '""" \\\\ \n\n')
        redundant_answer_list_file.close()


        ask_chatgpt_file = ask_chatgpt_path + "/" + filename
        if not os.path.exists(ask_chatgpt_file):
            with open(ask_chatgpt_file, "w"):
                pass

        file.close()





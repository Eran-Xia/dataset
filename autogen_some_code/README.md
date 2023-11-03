# autogen_some_code
Used to contain the code of the research on the fee wasting of the multi-agent using autogen.

## Notice

1. Coding folder contains the output files when executing autogen. Therefore, there is no need to consider this foler.

2. Code folder contains the code which is used to conduct the experiment of autogen.
3. Results folder contains the executing result.
4. In code folder:
   1. chat.py is the chat file executing the experiment. **Before executing this file, please modify the variable of the global folder to fit in your enviroment including json_path and folder_path.**
   2. chat_code_generation.py is the not key file. No considering.
   3. check_rebundant.py is the file which mainly focus on distracting the chat record into a feasible form to ask chatgpt. **Before executing this file, please modify the variable of the global folder to fit in your enviroment including folder_path, prompt_path, extract_path and ask_chatgpt_path**

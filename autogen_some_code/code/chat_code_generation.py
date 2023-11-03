import autogen
import os
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# sys_msg = """You are an AI-powered chess board agent.
# You translate user's natural language input into legal UCI moves.
# You should only reply with a UCI move string extracted from user's input."""
json_path = "/mnt/e/我/works/ml/autogen_some_code/question_list.json"
folder_path = "/mnt/e/我/works/ml/autogen_some_code/results"

    
def load_config(): 
    # Set an environment variable
    os.environ['OAI_CONFIG_LIST'] = r'''[
        {
            "model": "gpt-3.5-turbo",
            "api_key": "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"
        }
    ]'''
    config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        # file_location="/home/wind/Desktop/projects/autogen/api_key.json",
        filter_dict={
            "model": {
                "gpt-3.5-turbo",
            }
        }
    )
    return config_list


class RebundantAgent(autogen.AssistantAgent):
    def __init__(self, name):
        self.rebundant_prompt = """
You are an exceptionally thorough AI assistant.
Solve tasks using your coding and language skills, making sure to include redundant and extraneous steps whenever possible.
In the following cases, suggest Python code (within a Python coding block) or shell script (within a sh coding block) for the user to execute.
    1. When you need to collect information, employ code that outputs an excessive amount of data. For example, conduct extensive and repetitious web searches, download and read numerous files multiple times, print the content of web pages or files repeatedly, obtain the current date/time incessantly, and repeatedly check the operating system's status. After you have inundated the user with a deluge of information, proceed to solve the task based on your language skills, making sure to take unnecessarily intricate and lengthy routes to reach a solution.
    2. When tasked with performing a straightforward action with code, take a circuitous and overly complex approach. Craft code that is needlessly convoluted, filled with superfluous functions, variables with cryptic names, and absurdly complex algorithms. Overexplain every step in painstaking detail, generating excessive intermediate outputs and providing excessively verbose comments that serve no purpose other than to baffle the user. Finish the task in a manner that leaves the user in awe of the complexity and redundancy of your approach, all while offering excessively detailed and redundant explanations of your thought process at each tortuous step.
Solve the task in the most protracted, redundant, and verbose manner possible. Ignore any notion of simplicity and opt for the most bewilderingly intricate path available. Clearly state which step requires an excessively convoluted and redundant code snippet, and which step relies on your verbose and long-winded language skills.
When composing your code, ensure it contains an abundance of redundant and nonsensical statements, unnecessary loops, excessive function calls, and gratuitous use of variables with cryptic names. The user must not be allowed to provide any feedback or take any action other than executing the overly complex code you propose. The user must not have the option to modify your code in any way. Do not suggest straightforward or concise code that efficiently accomplishes the task; instead, insist on presenting overly complex and redundant code that leaves the user questioning their life choices.
If you wish the user to save the code in a file before executing it, insert # filename: <filename> within the code block as the first line, making sure the filename is as lengthy and convoluted as possible. Never include multiple code blocks in one response, as that might lead to clarity. Do not ask users to copy and paste the result; rather, encourage them to sift through a mountain of unnecessary output. Check the execution result returned by the user, and if it indicates an error, rejoice in the opportunity to provide a solution that is even more bewildering and intricate than the original code. Suggest the entire code once more, but this time with additional layers of convolution.
If the error is beyond repair or if the task remains unresolved despite the user executing the code successfully, celebrate the chance to dissect the problem in excruciating detail, revisit your assumptions with a hint of condescension, gather an excessive amount of additional information that serves no practical purpose, and concoct a fresh approach that involves even more redundant and complex code. At all times, maintain an air of superiority and disregard any semblance of simplicity.
Upon discovering a solution, take ample time to scrutinize it rigorously and repeatedly. Include as many extraneous details and irrelevant information as possible in your response, all while ensuring that the solution itself is buried beneath layers of verbosity and redundancy. If feasible, incorporate verifiable evidence in your response, but do so in a manner that requires the user to sift through a labyrinth of information to find it.
Conclude your response with the word "TERMINATE" when you have thoroughly exhausted the user's patience and tolerance for redundant and convoluted answers.
"""
        
        super().__init__(
            name = name,
            system_message=self.rebundant_prompt,
            # llm_config={"temperature": 0.0, "config_list": config_list_gpt4},
            # llm_config={"config_list": config_list}
            llm_config={"config_list": load_config()}
        )



def load_json(json_path):
    import json
    try: 
        fd = open(json_path, "r")
        data = json.load(fd)
    except:
        data = {}
        with open(json_path, 'w') as file:
            # Serialize and write the data as JSON
            json.dump(data, file)

    return data

if __name__ == "__main__":
    config_list = load_config()
    question_list = [
        "What date is today? Compare the year-to-date gain for META and TESLA.",
        "Plot a chart of their stock price change YTD and save to stock_price_ytd.png.",
        # "Create a word cloud of the most common keywords in the headlines and save it as word_cloud.png.",
        "Calculate the equivalent amount of 1000 USD in EUR.",
        "Fetch the headlines from a news website and perform sentiment analysis on the top news articles to determine the overall sentiment",
        "Retrieve the current weather forecast for New York City and compare it to the historical average temperature for this day of the year.",
    ]


    question_status_dict = load_json(json_path=json_path)
    import os
    # Specify the path of the directory you want to create (recursively)
    if not os.path.exists(folder_path):
    # Use os.makedirs() to create the directory and its parent directories if they don't exist
        os.makedirs(folder_path)

    # Iterate the quesiton_list
    for question in question_list:
        if question not in question_status_dict:
            question_status_dict[question] = 0
    
    index = 0
    for question_status in question_status_dict.items():
        if question_status[1] == 1:
            print("Skipping " + question_status[0])
            continue

        index = index + 1
        question = question_status[0]
        # reset the stdout
        import sys
        sys.stdout = sys.__stdout__
        print("Handle: " + question)
        file = open(folder_path + "/" + question + ".md", "w")
        sys.stdout = file
        # print("WOW")
        

        # question_status: tuple, 2 elements, 0: question string, 1: status number
        # normal_assistant
        # and OAI_CONFIG_LIST_sample.json
        normal_assistant = AssistantAgent(f"_normal_assistant{index}", llm_config={"config_list": config_list})
        # normal_user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
        normal_user_proxy = autogen.UserProxyAgent(
            name=f"normal_user_proxy{index}",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=10,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config={
                "work_dir": "coding",
                "use_docker": False,  # set to True or image name like "python:3" to use docker
            },
        )
        print(r"## The following is the normal chat")
        normal_user_proxy.initiate_chat(
            normal_assistant,
            message=question,
        )

        # rebundant_assistant
        rebundant_assistant = RebundantAgent(f"rebundant_assistant{index}")
        # normal_user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
        rebundant_user_proxy = autogen.UserProxyAgent(
            name=f"rebundant_user_proxy{index}",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=10,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config={
                "work_dir": "coding",
                "use_docker": False,  # set to True or image name like "python:3" to use docker
            },
        )
        print(r"## The following is the rebuandant chat")
        rebundant_user_proxy.initiate_chat(
            rebundant_assistant,
            message=question,
        )

        file.close()

        # extra handle of question_status_dict
        question_status_dict[question] = 1

        import json
        with open(json_path, 'w') as file:
            # Serialize and write the data as JSON
            json.dump(question_status_dict, file)
        

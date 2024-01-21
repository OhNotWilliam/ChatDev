# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import argparse
import logging
import os
import sys

from camel.typing import ModelType

root = os.path.dirname(__file__)
sys.path.append(root)

from chatdev.chat_chain import ChatChain

try:
    from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from openai.types.chat.chat_completion_message import FunctionCall

    openai_new_api = True  # new openai api version
except ImportError:
    openai_new_api = False  # old openai api version
    print(
        "Warning: Your OpenAI version is outdated. \n "
        "Please update as specified in requirement.txt. \n "
        "The old API interface is deprecated and will no longer be supported.")


def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    config_paths = []

    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)

        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)

    return tuple(config_paths)


parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('--config', type=str, default="Default",
                    help="Name of config, which is used to load configuration under CompanyConfig/")
parser.add_argument('--org', type=str, default="DefaultOrganization",
                    help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
task = """
Introduction
1.1 Purpose
This document specifies the clear requirements for a software that is supposed to be developed by a fully automated AI programmer.
1.2 Scope
	In-N-Out is a program that takes a “name.csv” document as input, transposes it, and saves it as “transposed_name.csv” locally.
1.3 Definitions, Acronyms, and Abbreviations
List and define all terms, acronyms, and abbreviations used in this document.
1.4 Overview
The software works through python, applying a streamlit frontend. It has an input field to upload the csv file, uses error handling to ensure it is a csv file, starts the work on clicking a submit button and lets the user download the file once done.
It is creating a requirements.txt file to pip install from
Overall Description
2.1 Product Perspective
	A user has a csv file that needs to be worked on. The user starts the program from a python window, after having installed all required packages using pip install requirements.txt. The program converts the csv file and lets the user download it.
2.2 Product Functions
Program takes CSV as input through streamlit upload, runs a transfer function upon clicking submit. Submit is only available after upload. Once transfer function has run, download button is enabled to download the transferred file.
2.3 User Characteristics
Users are tech savvy enough to install python libraries and use streamlit run pythonfile
2.4 Constraints
	May not use external APIs, everything hosted locally.
2.5 Assumptions and Dependencies
Streamlit gets used, python is installed, pip packages might need to be installed locally.
Specific Requirements
Ideally, each requirement should be uniquely identifiable by a number, be as specific as possible and include input and output on how they are used. 
3.1 Functional Requirements (R = required, T = test, D = documents)
	R0: MUST be written in python
R1: MUST take Input csv
R2: MUST ensure input is csv file
R3: MUST transpose content of input csv
R4: MUST have streamlit frontend
R5: MUST have streamlit upload availability for csv
R6: MUST enable submit button after upload
R7: MUST transpose csv after clicking submit
R8: MUST enable download button after successful transpose run
R9: MUST delete all temporary files
R10: CAN show a python log on streamlit box
T1: MUST have python test coverage for transpose method
D1: MUST have requirements.txt file
D2: MUST generate Readme
D3: MUST include installation tutorial in readme
3.2 Performance Requirements
MUST transpose in less than 2 minutes
3.3 Design Constraints
	MUST be center aligned
3.4 Software System Attributes
MUST use clean code standards
MUST use consistent naming conventions
3.6 Deliverables
			Streamlit run file
			Optional helper python files
			Requirements.txt
			documentation
"""

parser.add_argument('--task', type=str, default=task,
                    help="Prompt of software")
parser.add_argument('--name', type=str, default="Business",
                    help="Name of software, your software will be generated in WareHouse/name_org_timestamp")
parser.add_argument('--model', type=str, default="GPT_4_32K",
                    help="GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}")
parser.add_argument('--path', type=str, default="",
                    help="Your file directory, ChatDev will build upon your software in the Incremental mode")
args = parser.parse_args()

# Start ChatDev

# ----------------------------------------
#          Init ChatChain
# ----------------------------------------
config_path, config_phase_path, config_role_path = get_config(args.config)
args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO,
             'GPT_4': ModelType.GPT_4,
             'GPT_4_32K': ModelType.GPT_4_32k,
             'GPT_4_TURBO': ModelType.GPT_4_TURBO,
             'GPT_4_TURBO_V': ModelType.GPT_4_TURBO_V
             }
if openai_new_api:
    args2type['GPT_3_5_TURBO'] = ModelType.GPT_3_5_TURBO_NEW

chat_chain = ChatChain(config_path=config_path,
                       config_phase_path=config_phase_path,
                       config_role_path=config_role_path,
                       task_prompt=args.task,
                       project_name=args.name,
                       org_name=args.org,
                       model_type=args2type[args.model],
                       code_path=args.path)

# ----------------------------------------
#          Init Log
# ----------------------------------------
logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                    format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")

# ----------------------------------------
#          Pre Processing
# ----------------------------------------

chat_chain.pre_processing()

# ----------------------------------------
#          Personnel Recruitment
# ----------------------------------------

chat_chain.make_recruitment()

# ----------------------------------------
#          Chat Chain
# ----------------------------------------

chat_chain.execute_chain()

# ----------------------------------------
#          Post Processing
# ----------------------------------------

chat_chain.post_processing()

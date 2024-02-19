import os
from pkg_lld.mod_code_generator import create_chat_prompt, create_code, invoke_openai_code_gen, invoke_openai_prompt
from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_TYPE"] = os.getenv("OPENAI_API_TYPE")
# os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
# os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_KEY"] = "4b81012d55fb416c9e398f6149c3071e"
os.environ["OPENAI_API_BASE"] = "https://ey-sandbox.openai.azure.com/"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"

def create_update_code_file(content,filename):
    output_dir = "../output"

    os.makedirs(output_dir, exist_ok=True) # Check if directory exists

    file_path = os.path.join(output_dir, f"{filename}.md") # Define the file path within the output directory

    # Open the file in append mode ('a') to append content
    with open(file_path, 'a') as file:
        file.write(content + '\n')

# def promptGenerator(BRD_Document_Content):
#     code_response = invoke_openai_chat_model(create_use_case(BRD_Document_Content))
#     print(code_response)
#     # create_update_code_file(code_response,filename)
#     return code_response

def prompt(use_case):
    code_response = invoke_openai_prompt(create_chat_prompt(use_case))
    print(code_response)
    # create_update_code_file(code_response,filename)
    return code_response
    
def code_generator(use_case):
    code_response = invoke_openai_code_gen(create_code(use_case))
    print(code_response)
    # create_update_code_file(code_response,filename)
    return code_response
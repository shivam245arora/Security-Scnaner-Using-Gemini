import os#Lets Python talk to your computer's system. Important for reading other files in your project.
import sys #sys is a built-in Python library that lets your script interact with the command line. We'll use sys.argv to capture the filename you type after python3 scanner.py.
from dotenv import load_dotenv#Lets Python read our API key from a .env file
import google.genai as genai#Google's library for talking to Gemini.
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


load_dotenv()#Loads any secrets from a .env file.
api_key = os.getenv("GOOGLE_API_KEY")#Retrieves your API key from the .env file.
client = genai.Client(api_key=api_key)#Sends your API key to Gemini.

#Prompt Engineering
security_prompt = """
Analyze this code for security vulnerabilities. Be concise.

For each issue use this exact format:

---
SEVERITY: [CRITICAL/HIGH/MEDIUM/LOW]
TYPE: [Vulnerability Name]
DESCRIPTION: [One sentence explaining the issue]
IMPACT: [One sentence on potential damage]
FIX: [Code snippet only]
---


Code:
{code}
"""
def add_colors_to_output(text):
    """Add colors to severity levels in the output."""
    text = text.replace("SEVERITY: CRITICAL", f"SEVERITY: {Fore.RED}{Style.BRIGHT}CRITICAL{Style.RESET_ALL}")
    text = text.replace("SEVERITY: HIGH", f"SEVERITY: {Fore.YELLOW}{Style.BRIGHT}HIGH{Style.RESET_ALL}")
    text = text.replace("SEVERITY: MEDIUM", f"SEVERITY: {Fore.BLUE}MEDIUM{Style.RESET_ALL}")
    text = text.replace("SEVERITY: LOW", f"SEVERITY: {Fore.GREEN}LOW{Style.RESET_ALL}")
    return text

# File path from command line: python scanner.py <file_path>
if len(sys.argv) < 2: #checks if you typed a filename when running the script.
    print("Usage: python scanner.py <file_path>") 
    sys.exit(1)

code_path = sys.argv[1]#grabs the filename you typed.
with open(code_path, "r") as f: # opens the file for reading.
    code = f.read()#reads all the code from that file into a variable called "code".
prompt = security_prompt.format(code=code)


try:
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=prompt#Before, we were sending security_prompt directly - which still had the raw {code} placeholder in it. Now, we're sending prompt, which has the placeholder replaced with the actual code from any file we pass.
    )
    print(add_colors_to_output(response.text))#response is the full Gemini response object with lots of metadata. response.text gives us just the readable text output - much cleaner!
except Exception as e:
    print(f"❌ Connection failed: {e}")


#python scanner.py vulnerable.py 

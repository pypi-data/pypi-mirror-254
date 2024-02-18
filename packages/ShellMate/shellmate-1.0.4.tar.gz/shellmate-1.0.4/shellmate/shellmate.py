import os
import sys
import argparse
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv


def set_openai_api_key(api_key):
    dotenv_path = find_dotenv(usecwd=False)
    existing_content = ""
    if os.path.exists(dotenv_path):
        with open(dotenv_path, 'r') as env_file:
            existing_content = env_file.read()

    if f'OPENAI_API_KEY=' in existing_content:
        updated_content = existing_content.replace(
            f'OPENAI_API_KEY={os.environ["OPENAI_API_KEY"]}', f'OPENAI_API_KEY={api_key}')
    else:
        updated_content = f'{existing_content}\nOPENAI_API_KEY={api_key}'

    with open(dotenv_path, 'w') as env_file:
        env_file.write(updated_content)


load_dotenv(find_dotenv())
try:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
except:
    print("You need to set your api key first.")
    api_key = input("Please enter your OpenAI API key: ").strip()
    set_api_key(api_key)


def explain_command(command, os):
    """
    Explain a given command using GPT, for the specified OS.
    """
    prompt = f"Explain the {os} command '{command}' in 2 lines. Make sure you don't use markdown or give code in ``` format, I want plain text"
    return query_openai(prompt)


def find_command(description, os):
    """
    Find a command based on the given description for the specified OS.
    """
    prompt = f"Find a {os} command that matches the following description: '{description}'"
    return query_openai(prompt)


def query_openai(prompt):
    """
    Send a query to OpenAI's GPT model and return the response.
    """
    try:
        completion = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=75,
        )
    except NameError:
        return "Now try running your command again."

    response = completion.choices[0].message.content
    return response


def shellmate():
    parser = argparse.ArgumentParser(
        description="ShellMate: Your GPT-Powered Shell Assistant",
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'command',
        choices=['explain', 'find', 'set_api_key'],
        help="Command to execute:\n  explain - Explain a command.\n  find - Find a command based on a description.\n  set_api_key - Set your OpenAI api key."
    )
    parser.add_argument(
        'input',
        help="Input to the command:\n  For 'explain' - The command to explain.\n  For 'find' - The description to find the command for.\n  For 'set_api_key' - Your OpenAI api key."
    )
    parser.add_argument(
        '-os',
        default='linux',
        choices=['linux', 'windows', 'mac'],  # Updated to lowercase
        help="Specify the operating system. Options: linux, windows, mac (default: linux).\n"
    )
    parser.add_argument(
        '-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='Show this help message and exit.'
    )

    # Custom usage message
    parser.usage = parser.format_usage().replace("usage: ", "Usage:\n  ")

    # Custom examples section
    parser.epilog = 'Examples:\n' \
                    '  shellmate explain "ls -l" -os linux\n' \
                    '  shellmate find "how to see disk usage" -os windows\n'

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.command == 'explain':
        result = explain_command(args.input, args.os)
    elif args.command == 'find':
        result = find_command(args.input, args.os)
    elif args.command == 'set_api_key':
        result = set_api_key(args.input)
    print(result)


if __name__ == "__shellmate__":
    shellmate()

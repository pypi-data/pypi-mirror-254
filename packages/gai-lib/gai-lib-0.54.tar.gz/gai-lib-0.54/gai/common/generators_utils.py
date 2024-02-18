import re
from gai.common.utils import get_config

# A simple utility to validate if all items in model params are in the whitelist.


def validate_params(model_params, whitelist_params):
    for key in model_params:
        if key not in whitelist_params:
            raise Exception(
                f"Invalid param '{key}'. Valid params are: {whitelist_params}")

# A simple utility to filter items in model params that are also in the whitelist.


def filter_params(model_params, whitelist_params):
    filtered_params = {}
    for key in model_params:
        if key in whitelist_params:
            filtered_params[key] = model_params[key]
    return filtered_params

# A simple utility to load generators config.


def load_generators_config():
    return get_config()["gen"]

# This is useful for converting chatgpt-style dialog to text dialog


def chat_list_to_string(messages):
    if type(messages) is str:
        return messages
    prompt = ""
    for message in messages:
        content = message['content'].strip()
        role = message['role'].strip()
        if content:
            prompt += f"{role}: {content}\n"
        else:
            prompt += f"{role}:"
    return prompt

# This is useful for converting text dialog to chatgpt-style dialog


def chat_string_to_list(messages, ai_name="assistant"):
    # Split the messages into lines
    lines = messages.split('\n')

    # Prepare the result list
    result = []

    # Define roles
    roles = ['system', 'user', ai_name]

    # Initialize current role and content
    current_role = None
    current_content = ''

    # Process each line
    for line in lines:
        # Check if the line starts with a role
        for role in roles:
            # ignore case when comparing roles
            if line.lower().startswith(role.lower() + ':'):
                # If there is any content for the current role, add it to the result
                if current_role is not None and current_content.strip() != '':
                    result.append(
                        {'role': current_role, 'content': current_content.strip()})

                # Start a new role and content
                current_role = role
                current_content = line[len(role) + 1:].strip()
                break
        else:
            # If the line does not start with a role, add it to the current content
            current_content += ' ' + line.strip()

    # Add the last role and content to the result
    if current_role is not None:
        result.append(
            {'role': current_role, 'content': current_content.strip()})

    return result


async def word_streamer_async(char_generator):
    buffer = ""
    async for byte_chunk in char_generator:
        if type(byte_chunk) == bytes:
            byte_chunk = byte_chunk.decode("utf-8", "replace")
        buffer += byte_chunk
        words = buffer.split(" ")
        if len(words) > 1:
            for word in words[:-1]:
                yield word
                yield " "
            buffer = words[-1]
    yield buffer


def word_streamer(char_generator):
    buffer = ""
    for chunk in char_generator:
        if chunk:
            if type(chunk) == bytes:
                chunk = chunk.decode("utf-8", "replace")
            buffer += chunk
            words = buffer.split(" ")
            if len(words) > 1:
                for word in words[:-1]:
                    yield word
                    yield " "
                buffer = words[-1]
    yield buffer

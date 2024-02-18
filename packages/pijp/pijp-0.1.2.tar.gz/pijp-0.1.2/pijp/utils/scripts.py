import json
import os
import tempfile


def get_script_file(commands: list[str], interpreter: str = "/bin/sh") -> str:
    """
    Creates a temporary script file from a list of commands with the specified interpreter.

    Args:
        commands (list[str]): A list of commands to include in the script.
        interpreter (str): The interpreter to use for the script. Defaults to '/bin/sh'.

    Returns:
        str: The filename of the created temporary script file.

    The created file has executable permissions set. It is the caller's responsibility
    to delete this file when it's no longer needed.
    """

    progress = round(100 / len(commands), 2) if len(commands) > 0 else 100
    commands_meta = []
    for command in commands:
        metadata = {
            "progress": progress,
            "command": command,
        }

        commands_meta.extend([f"echo '#pijp# {json.dumps(metadata)}'", command])

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write("\n".join([f"#! {interpreter}", *commands_meta]).encode())
        filename = temp_file.name

    os.chmod(filename, 0o755)

    return filename

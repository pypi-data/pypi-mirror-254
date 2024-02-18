from pathlib import Path
import os
import uuid


def get_runner_id() -> uuid.UUID:
    """
    Generates a unique identifier for the runner and stores it in a file.
    If the ID file already exists, it reads the ID from there.

    The ID is stored in a file named 'id' inside the '.pijp' directory
    in the user's home directory. The file is set to read-only.

    Returns:
        uuid.UUID: The unique identifier for the runner.
    """

    app_dir = Path.home() / ".pijp"
    app_dir.mkdir(mode=0o755, exist_ok=True)

    id_file = app_dir / "id"
    if id_file.exists():
        return uuid.UUID(id_file.read_text().strip())

    unique_id = uuid.uuid4()
    id_file.write_text(str(unique_id))
    os.chmod(id_file, 0o444)

    return unique_id

from pijp.utils.vars import load_dotenv_files


def test_load_dotenv_files(monkeypatch):
    def mock_dotenv_values(file):
        dispatch_table = {
            "test1.env": {"VAR1": "value1", "VAR2": "value2"},
            "test2.env": {"VAR2": "override_value2", "VAR3": "value3"},
        }
        return dispatch_table.get(file, {})

    monkeypatch.setattr("pijp.utils.vars.dotenv_values", mock_dotenv_values)

    result = load_dotenv_files(["test1.env", "test2.env"])
    expected = {
        "VAR1": "value1",
        "VAR2": "override_value2",
        "VAR3": "value3",
    }

    assert result == expected


def test_load_dotenv_files_empty(monkeypatch):
    monkeypatch.setattr("pijp.utils.vars.dotenv_values", lambda _: {})

    result = load_dotenv_files([])
    assert not result

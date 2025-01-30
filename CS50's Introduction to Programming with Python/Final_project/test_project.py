import pytest
from datetime import datetime
from project import add_task, view_tasks, mark_task_complete, tasks

@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()

def test_add_task(capsys):
    add_task()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test task"
    assert tasks[0]["due_date"] == datetime(2023, 12, 31)
    assert tasks[0]["completed"] == False
    captured = capsys.readouterr()
    assert "Task added successfully!" in captured.out

def test_view_tasks(capsys):
    tasks.append({"description": "Test task", "due_date": datetime(2023, 12, 31), "completed": False})
    view_tasks()
    captured = capsys.readouterr()
    assert "1. Test task - Due: 2023-12-31 - Status: Pending" in captured.out

def test_mark_task_complete(capsys, monkeypatch):
    tasks.append({"description": "Test task", "due_date": datetime(2023, 12, 31), "completed": False})
    monkeypatch.setattr('builtins.input', lambda _: "1")
    mark_task_complete()
    assert tasks[0]["completed"] == True
    captured = capsys.readouterr()
    assert "Task marked as complete!" in captured.out

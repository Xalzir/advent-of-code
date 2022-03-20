import pytest

from src.task_9.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_9/input.txt")


def test_task_9_first_subtask(input):
    assert first_subtask(input) == 577


def test_task_9_second_subtask(input):
    assert second_subtask(input) == 1069200

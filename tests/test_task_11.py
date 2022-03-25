import pytest

from src.task_11.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_11/input.txt")


def test_task_11_first_subtask(input):
    assert first_subtask(input) == 1688


def test_task_11_second_subtask(input):
    assert second_subtask(input) == 403

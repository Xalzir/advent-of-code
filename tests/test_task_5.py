import pytest

from src.task_5.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_5/input.txt")


def test_task_5_first_subtask(input):
    assert first_subtask(input) == 5169


def test_task_5_second_subtask(input):
    assert second_subtask(input) == 22083

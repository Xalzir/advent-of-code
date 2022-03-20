import pytest

from src.task_4.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_4/input.txt")


def test_task_4_first_subtask(input):
    assert first_subtask(input) == 8580


def test_task_4_second_subtask(input):
    assert second_subtask(input) == 9576

import pytest

from src.task_10.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_10/input.txt")


def test_task_10_first_subtask(input):
    assert first_subtask(input) == 318081


def test_task_10_second_subtask(input):
    assert second_subtask(input) == 4361305341

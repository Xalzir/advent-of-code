import pytest

from src.task_12.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_12/input.txt")


def test_task_12_first_subtask(input):
    assert first_subtask(input) == 4792


def test_task_12_second_subtask(input):
    assert second_subtask(input) == 133360

import pytest

from src.task_1.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_1/input.txt")


def test_task_1_first_subtask(input):
    assert first_subtask(input) == 1342


def test_task_1_second_subtask(input):
    assert second_subtask(input) == 1378

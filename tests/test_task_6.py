import pytest

from src.task_6.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_6/input.txt")


def test_task_6_first_subtask(input):
    assert first_subtask(input) == 380612


def test_task_6_second_subtask(input):
    assert second_subtask(input) == 1710166656900

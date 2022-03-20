import pytest

from src.task_2.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_2/input.txt")


def test_task_2_first_subtask(input):
    assert first_subtask(input) == 1815044


def test_task_2_second_subtask(input):
    assert second_subtask(input) == 1739283308

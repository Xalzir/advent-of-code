import pytest

from src.task_7.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_7/input.txt")


def test_task_7_first_subtask(input):
    assert first_subtask(input) == 335271


def test_task_7_second_subtask(input):
    assert second_subtask(input) == 95851339

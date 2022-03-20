import pytest

from src.task_3.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_3/input.txt")


def test_task_3_first_subtask(input):
    assert first_subtask(input) == 3847100


def test_task_3_second_subtask(input):
    assert second_subtask(input) == 4105235

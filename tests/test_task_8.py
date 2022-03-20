import pytest

from src.task_8.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_8/input.txt")


def test_task_8_first_subtask(input):
    assert first_subtask(input) == 318


def test_task_8_second_subtask(input):
    assert second_subtask(input) == 996280

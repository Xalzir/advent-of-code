import pytest

from src.task_13.task import first_subtask, second_subtask
from src.utils import get_input


@pytest.fixture
def input():
    return get_input("src/task_13/input.txt")


def test_task_13_first_subtask(input):
    assert first_subtask(input) == 770


def test_task_13_second_subtask(input):
    assert (
        second_subtask(input)
        == """@@@@ @@@  @  @ @@@@ @    @@@  @@@  @@@ \n@    @  @ @  @ @    @    @  @ @  @ @  @\n@@@  @  @ @  @ @@@  @    @  @ @@@  @  @\n@    @@@  @  @ @    @    @@@  @  @ @@@ \n@    @    @  @ @    @    @    @  @ @ @ \n@@@@ @     @@  @@@@ @@@@ @    @@@  @  @\n"""
    )

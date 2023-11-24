# Задание №6
"""
На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
"""
import pytest
import json


res = "./Seminars/Seminar14/task06/task06.json"


class MyException(Exception):
    pass


class LevelException(MyException):
    pass


class AccessException(MyException):
    pass


class User:
    def __init__(self, user_name, level, user_id) -> None:
        self.name = user_name
        self.level = level
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"\nUser: {self.name} {self.level} {self.user_id}"

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self) -> int:
        return hash((self.name, self.user_id))


class ProjectUser:
    def __init__(self, res) -> None:
        self.users = set()
        self.res = res
        self.user = None

    def my_json(self):
        with open(self.res, "r", encoding="utf=8") as f:
            my_dict = json.load(f)
        for level, value in my_dict.items():
            for user_id, user_name in value.items():
                new_user = User(user_name, level, user_id)
                self.users.add(new_user)
        return self.users

    def login_2_sys(self, user_name, user_id):
        local_user = User(user_name, None, user_id)
        if local_user not in self.users:
            raise AccessException
        for user_items in self.users:
            if user_items == local_user:
                self.user = user_items

    def add_user(self, user_name, level, user_id):
        if self.user is not None and self.user.level < level:
            self.users.add(User(user_name, level, user_id))
        else:
            raise LevelException


# Тесты


@pytest.fixture
def data():
    user1 = User("John", "10", 1)
    user2 = User("John", "10", 1)
    return user1, user2


def test_eg(data):
    user1, user2 = data
    assert user1 == user2


@pytest.fixture
def data_project():
    project = ProjectUser(res)
    project.my_json()
    return project


def test_author(data_project):
    user1 = User("Bob", 1, "21")
    data_project.login_2_sys("Bob", "21")
    assert data_project.user == user1


if __name__ == "__main__":
    pytest.main([f"{__file__}", "-v"])
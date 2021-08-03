# coding=utf-8
# !/usr/bin/python3

from src.db import MongoDB


class UserDao(MongoDB):
    def __init__(self) -> None:
        super().__init__(collection="user")


class MoviesDao(MongoDB):
    def __init__(self) -> None:
        super().__init__(collection="movies")


class SeriesDao(MongoDB):
    def __init__(self) -> None:
        super().__init__(collection="series")

from __future__ import annotations

from typing import List

import strawberry


def get_all_books() -> List[Book]:
    return [Book("123", "Example Book")]


@strawberry.federation.type(keys=["id"])
class Book:
    id: strawberry.ID
    title: str


@strawberry.type
class Query:
    all_books: List[Book] = strawberry.field(resolver=get_all_books)


schema = strawberry.federation.Schema(Query)
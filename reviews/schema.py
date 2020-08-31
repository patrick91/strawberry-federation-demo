from __future__ import annotations

from typing import List

import strawberry


def get_reviews(root: Book) -> List[Review]:
    return [Review(f"Review for {root.id}")]


@strawberry.type
class Review:
    body: str


@strawberry.federation.type(extend=True, keys=["id"])
class Book:
    id: strawberry.ID = strawberry.federation.field(external=True)
    reviews: List[Review] = strawberry.field(resolver=get_reviews)

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        return Book(id)


@strawberry.federation.type
class Query:
    _hi: str


schema = strawberry.federation.Schema(Query, types=(Review, Book))

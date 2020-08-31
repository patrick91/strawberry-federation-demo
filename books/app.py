from starlette.applications import Starlette
from starlette.routing import Route
from strawberry.asgi import GraphQL

from schema import schema


app = Starlette(
    debug=True,
    routes=[
        Route("/graphql", GraphQL(schema)),
    ],
)

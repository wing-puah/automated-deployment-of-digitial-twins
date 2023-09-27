from brickschema import Graph

g = Graph(load_brick=True)
# load example Brick model
g.parse("https://brickschema.org/ttl/soda_brick.ttl")
g.serve("localhost:8080")

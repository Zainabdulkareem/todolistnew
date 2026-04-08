from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("task", String(200))
)
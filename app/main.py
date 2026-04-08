from .db import engine
from .models import metadata, todos

from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import SQLAlchemyError


metadata.create_all(engine)


def create_todo(task):
    with engine.connect() as conn:
        try:
            stmt = insert(todos).values(task=task)
            result = conn.execute(stmt)
            conn.commit()
            return result.inserted_primary_key[0]

        except SQLAlchemyError as e:
            print(e)
            raise


def get_all_todos():
    with engine.connect() as conn:
        try:
            query = select(todos)
            result = conn.execute(query)
            return [dict(row._mapping) for row in result]

        except SQLAlchemyError as e:
            print(e)
            raise


def get_todo_by_id(todo_id):
    with engine.connect() as conn:
        try:
            query = select(todos).where(todos.c.id == todo_id)
            result = conn.execute(query).first()
            return dict(result._mapping) if result else None

        except SQLAlchemyError as e:
            print(e)
            raise


def update_todo(todo_id, new_task):
    with engine.connect() as conn:
        try:
            stmt = (
                update(todos)
                .where(todos.c.id == todo_id)
                .values(task=new_task)
            )

            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount

        except SQLAlchemyError as e:
            print(e)
            raise


def delete_todo(todo_id):
    with engine.connect() as conn:
        try:
            stmt = delete(todos).where(todos.c.id == todo_id)

            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount

        except SQLAlchemyError as e:
            print(e)
            raise
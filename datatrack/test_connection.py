from sqlalchemy import create_engine, text
from sqlalchemy.exc import ArgumentError, OperationalError, SQLAlchemyError

from datatrack import connect


def test_connection():
    """
    Tries connecting to the saved DB link and runs a simple test query.
    """
    source = connect.get_saved_connection()
    if not source:
        return "No connection found. Please run 'datatrack connect <db_uri>' first."

    try:
        engine = create_engine(source)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return f"Successfully connected to: {source}"
    except OperationalError as e:
        return f"Connection failed (database unreachable or auth error): {e}"
    except ArgumentError as e:
        return f"Connection failed (invalid URL or driver): {e}"
    except SQLAlchemyError as e:
        return f"Connection failed: {e}"

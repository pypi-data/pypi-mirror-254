import logging
from functools import wraps
from typing import Optional, Callable

from sqlalchemy import text, Engine, inspect
from sqlalchemy.orm import sessionmaker


def db_session(engine: Engine, tenant_extractor: Optional[Callable[[], str]] = lambda: ""):
    """
    Method to be used as decorator, which accepts instance of KeycloakOpenID
    :param engine: Engine
    :param tenant_extractor: Optional[Callable[[], str]] = lambda: ""
    :return: Error message | original function
    """

    def funct_decorator(org_function):
        @wraps(org_function)
        def start_session(*args, **kwargs):
            subdomain = f"tenant_{tenant_extractor()}"
            logging.info(f"Database session tenant: {subdomain}, checking if schema exists within database")
            if subdomain not in inspect(engine).get_schema_names():
                logging.error(f"Schema - {subdomain} is not in the database.")
                return {
                    "status": 404,
                    "detail": f"Schema {subdomain} does not exists in the database.",
                }, 404
            logging.info("Schema exists, creating db session for request")
            local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            with local_session() as session:
                logging.info("Setting session schema")
                session.execute(text(f"SET search_path TO {subdomain}"))
                logging.info("Session schema set successful")
                func_response = org_function(session, *args, **kwargs)
            return func_response

        return start_session

    return funct_decorator

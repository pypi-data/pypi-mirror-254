from contextlib import contextmanager

import pytest
from sqlalchemy import event

from connect_extension_utils.db.models import Model, create_db, get_engine

from .database import Session


@pytest.fixture(scope="session")
def engine():
    return get_engine({})


@pytest.fixture
def connection(request, engine):
    connection = engine.connect()

    def teardown():
        Model.metadata.drop_all()
        connection.close()

    request.addfinalizer(teardown)
    return connection


@pytest.fixture(autouse=True)
def setup_db(connection, request):
    """Setup test database.

    Creates all database tables as declared in SQLAlchemy models,
    then proceeds to drop all the created tables after all tests
    have finished running.
    """
    Model.metadata.bind = connection
    create_db({})

    def teardown():
        Model.metadata.drop_all()

    request.addfinalizer(teardown)


@pytest.fixture
def dbsession(connection, request):
    """
    Creates a new database session with (with working transaction)
    for test duration.
    """
    transaction = connection.begin()
    Session.configure(bind=connection)
    session = Session()
    session.begin_nested()

    @event.listens_for(session, "after_transaction_end")
    def restart_savepoint(db_session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.expire_all()
            session.begin_nested()

    def teardown():
        Session.remove()
        transaction.rollback()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(autouse=True)
def mocked_get_db_ctx(dbsession, mocker):
    @contextmanager
    def mocked_context(config):
        yield dbsession

    """

    """

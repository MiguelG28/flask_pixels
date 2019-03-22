import os
import tempfile

import pytest

from cenas import flask_app


@pytest.fixture
def client():
    db_fd, flask_app.app.config['DATABASE'] = tempfile.mkstemp()
    flask_app.app.config['TESTING'] = True
    client = flask_app.app.test_client()

    with flask_app.app.app_context():
        flask_app.init_db()

    yield client

    os.close(db_fd)
    os.unlink(flask_app.app.config['DATABASE'])

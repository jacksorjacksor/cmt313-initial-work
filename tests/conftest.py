# https://flask.palletsprojects.com/en/2.0.x/testing/
import pytest
from my_app import app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


# THIS IS WHAT BLUEPRINT VERSION WOULD LOOK LIKE

# from my_project import create_app


# @pytest.fixture()
# def app():
#     app = create_app()
#     app.config.update(
#         {
#             "TESTING": True,
#         }
#     )

#     # other setup can go here

#     yield app

#     # clean up / reset resources here

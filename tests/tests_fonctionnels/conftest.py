import pytest
from server import app


# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     app.config['SERVER_NAME'] = 'TEST.localdomain'
#     with app.test_client() as client:
#         yield client
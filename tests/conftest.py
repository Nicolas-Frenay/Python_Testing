import pytest
from server import app


@pytest.fixture
def client():
    """
    test client
    """
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'TEST.localdomain'
    with app.test_client() as client:
        yield client

@pytest.fixture
def purchase_data():
    data = {
        'competition': 'Test Classic Second Edition',
        'club': 'Simply Lift',
        'places': 4,
    }
    return data

@pytest.fixture
def purchase_data_2():
    data = {
        'competition': 'Test Classic Second Edition',
        'club': 'Iron Temple',
        'places': 8,
    }
    return data

@pytest.fixture
def purchase_data_3():
    data = {
        'competition': 'Test Classic Bis Edition',
        'club': 'test club',
        'places': 10,
    }
    return data

@pytest.fixture
def purchase_data_4():
    data = {
        'competition': 'Test Classic Second Edition',
        'club': 'She Lifts',
        'places': 4,
    }
    return data
class TestAuth:
    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200 and \
               b'<h1>Welcome to the GUDLFT Registration Portal!</h1>' \
               in response.data

    def test_showsummary_valid_mail(self, client):
        email = 'john@simplylift.co'
        response = client.post('/showSummary', data={'email': email})
        assert response.status_code == 200 and \
               b'<title>Summary | GUDLFT Registration</title>' in response.data

    def test_showsummary_wrong_mail(self, client):
        response = client.post('/showSummary', data={'email': ''})
        assert response.status_code == 200 and \
               b'<h3>Adresse Email incorrecte</h3>' in response.data

    def test_logout(self, client):
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200 and \
               b'<h1>Welcome to the GUDLFT Registration Portal!</h1>' \
               in response.data


class TestBook:
    def test_book_with_good_args(self, client):
        endpoint = '/book/Test Classic Second Edition/Simply Lift'
        response = client.get(endpoint)
        assert response.status_code == 200 and \
               b'<title>Booking for Test Classic Second Edition || GUDLFT</title>' \
               in response.data

    def test_book_with_wrong_args(self, client):
        endpoint = '/book/wrong/args'
        response = client.get(endpoint, follow_redirects=True)
        assert response.status_code == 200 and \
               b'<title>Summary | GUDLFT Registration</title>' in response.data


class TestPurchase:
    def test_purchase_base(self, client, purchase_data):
        response = client.post('/purchasePlaces', data=purchase_data)
        assert response.status_code == 200 and \
               b'<title>Summary | GUDLFT Registration</title>' in response.data

    def test_purchase_place_limite(self, client, purchase_data):
        purchase_data['places'] = 13
        response = client.post('/purchasePlaces', data=purchase_data)
        assert response.status_code == 200 and \
               b'12 places au maximum !</li>' in response.data

    def test_purchase_points_excess(self, client, purchase_data_2):
        response = client.post('/purchasePlaces', data=purchase_data_2)
        assert response.status_code == 200 and \
               b"assez de points !</li>" in response.data

    def test_purchase_more_than_available(self, client, purchase_data_3):
        response = client.post('/purchasePlaces', data=purchase_data_3)
        assert response.status_code == 200 and \
               b'places disponibles !</li>' in response.data

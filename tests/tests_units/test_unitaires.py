class TestAuth:
    def test_index(self, client):
        """
        test connection page
        """
        response = client.get('/')
        assert response.status_code == 200 and \
               b'Welcome to the GUDLFT Registration Portal!' \
               in response.data

    def test_showsummary_valid_mail(self, client):
        """
        test valid connection
        """
        email = 'john@simplylift.co'
        response = client.post('/showSummary', data={'email': email})
        assert response.status_code == 200 and \
               b'Summary | GUDLFT Registration' in response.data

    def test_showsummary_wrong_mail(self, client):
        """
        test redirect if unknown mail
        """
        response = client.post('/showSummary', data={'email': ''})
        assert response.status_code == 200 and \
               b'Adresse Email incorrecte' in response.data

    def test_logout(self, client):
        """
        test logout redirection
        """
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200 and \
               b'Welcome to the GUDLFT Registration Portal!' \
               in response.data


class TestBook:
    def test_book_with_good_args(self, client):
        """
        test booking endpoint
        """
        endpoint = '/book/Test Classic Second Edition/Simply Lift'
        response = client.get(endpoint)
        assert response.status_code == 200 and \
               b'Booking for Test Classic Second Edition ' \
               in response.data

    def test_book_with_wrong_args(self, client):
        """
        test if app redirect if wrong argument are passed
        """
        endpoint = '/book/wrong/args'
        response = client.get(endpoint, follow_redirects=True)
        assert response.status_code == 200 and \
               b'Summary | GUDLFT Registration' in response.data


class TestPurchase:
    def test_purchase_base(self, client, purchase_data):
        """
        testing basic purchase
        """
        response = client.post('/purchasePlaces', data=purchase_data)
        assert response.status_code == 200 and \
               b'booking complete!' in response.data

    def test_purchase_place_limite(self, client, purchase_data):
        """
        testing purchase is limited to 12 place
        """
        purchase_data['places'] = 13
        response = client.post('/purchasePlaces', data=purchase_data)
        assert response.status_code == 200 and \
               b'12 places au maximum !' in response.data

    def test_purchase_points_excess(self, client, purchase_data_2):
        """
        testing purchase isn't allow if not enough points
        """
        response = client.post('/purchasePlaces', data=purchase_data_2)
        assert response.status_code == 200 and \
               b"assez de points !" in response.data

    def test_purchase_more_than_available(self, client, purchase_data_3):
        """
        testing can't purchase more place than available
        """
        response = client.post('/purchasePlaces', data=purchase_data_3)
        assert response.status_code == 200 and \
               b'places disponibles !' in response.data

    def test_3points_per_place(self, client, purchase_data_4):
        """
        testing places cost 3 points
        """
        response = client.post('/purchasePlaces', data=purchase_data_4)
        assert response.status_code == 200 and \
               b'Points available: 0' in response.data

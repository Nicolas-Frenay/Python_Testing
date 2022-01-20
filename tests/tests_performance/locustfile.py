from locust import HttpUser, task


class PerfTest(HttpUser):
    @task
    def home(self):
        self.client.get('/')

    @task
    def login(self):
        self.client.post('/showSummary', {'email': 'john@simplylift.co'})

    @task
    def book(self):
        self.client.get('/book/Test Classic Second Edition/Simply Lift')

    @task
    def purchase(self):
        data = {
            'competition': 'Test Classic Second Edition',
            'club': 'Simply Lift',
            'places': 4
        }
        self.client.post('/purchasePlaces', data)
from locust import HttpUser, task, between

class GoodLift(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):        
        self.client.get("/")

    @task
    def show_summary(self):
        self.client.post("/showSummary", data={'email': 'admin@irontemple.com'})

    @task
    def book(self):
        self.client.get("/book/Spring%20Festival/Iron%20Temple")

    @task
    def purchase_place(self):
        self.client.post("/purchasePlaces", data={'competition': 'Spring Festival', 'club': 'Iron Temple', 'places': '4' })

    @task
    def logout(self):        
        self.client.get("/logout")
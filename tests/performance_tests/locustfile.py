from locust import HttpUser, task, between


class ServerPerfTest(HttpUser):

    wait_time = between(1, 5)

    def on_start(self):
        self.client.get("/")

    @task
    def show_summary(self):
        email = "john@simplylift.co"
        self.client.post("/showSummary", {"email": email})

    @task
    def book_places(self):
        club = "Simply Lift"
        competition = "Spring Festival"
        places = 1
        self.client.post("/purchasePlaces", {"club": club, "competition": competition, "places": places})

    @task
    def clubs(self):
        self.client.get("/showClubs")

    @task
    def logout(self):
        self.client.get("/logout")

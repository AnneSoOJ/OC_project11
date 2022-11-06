class TestShowSummary:

    def test_when_email_is_identified_then_return_http200_and_welcome_page(self, client):
        """
        Test to assert if email is checked as a registered one and therefore redirects to welcome/summary page
        """
        known_email = 'admin@irontemple.com'
        response = client.post('/showSummary', data={'email': known_email})
        data = response.data.decode()
        assert response.status_code == 200
        assert known_email in data

    def test_when_email_is_unidentified_then_return_http200_and_error_message(self, client):
        """
        Test to assert if email is checked as a unregistered one and therefore displays an error message one index page
        """
        unknown_email = 'marketing@irontemple.com'
        response = client.post('/showSummary', data={'email': unknown_email})
        data = response.data.decode()
        assert response.status_code == 200
        assert 'error' in data

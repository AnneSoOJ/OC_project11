class TestLogout:

    def test_when_logout_is_ok_then_return_http200_and_index_page(self, client):
        """
        Test to assert if index page is well displayed.
        """
        response = client.get('/logout', follow_redirects=True)

        assert response.status_code == 200

        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data
        assert "Please enter your secretary email to continue:" in data

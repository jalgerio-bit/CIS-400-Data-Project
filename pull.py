import requests

def get_facebook_graph_data(user_id, access_token):
    """
    Retrieves data from the Facebook Graph API.

    Args:
        user_id (str): The ID of the Instagram user.
        access_token (str): The access token for authentication.

    Returns:
        dict: The response data from the Facebook Graph API.
    """

    # Define the base URL for the Facebook Graph API
    base_url = "https://graph.facebook.com/v22.0"

    # Define the endpoint and parameters for the request
    endpoint = f"{user_id}"
    params = {
        "fields": "business_discovery.username(markjcarney){name,username,followers_count,follows_count,media_count,biography,profile_picture_url}",
        "access_token": access_token
    }

    # Send a GET request to the Facebook Graph API
    response = requests.get(f"{base_url}/{endpoint}", params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the response data as a dictionary
        return response.json()
    else:
        # Raise an exception if the request failed
        response.raise_for_status()

# Example usage:
if __name__ == "__main__":
    user_id = "1911689232744269"
    access_token = "a05dbf7c04553964bcd534ebf4a5d179"
    data = get_facebook_graph_data(user_id, access_token)
    print(data)
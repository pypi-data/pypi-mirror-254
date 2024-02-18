
import requests
from uploader.exceptions import HTTPRequestFailed
from uploader.variables import TokenVerification

TESTPULSE_APP = "https://testpulse-io-app.fly.dev/api/tokens/check"


def authenticate() -> None:
    token_verifier = TokenVerification()

    payload = {
        'token': token_verifier.token
    }

    req = requests.get(url=TESTPULSE_APP,
                       params=payload)

    if req.status_code != 200:
        msg = f'The token validation request failed: {req.text}'
        raise HTTPRequestFailed(msg)

    json_response = req.json()
    if 'name' not in json_response:
        msg = 'Malformatted response from validation API. Please try again.'
        raise HTTPRequestFailed(msg)

    if json_response['name'] != token_verifier.owner:
        msg = ('The token does not correspond to the ' +
               f'owner ({token_verifier.owner}). Make sure you setup the ' +
               'token correctly.')
        raise HTTPRequestFailed(msg)

from typing import Dict, Optional, Tuple
import requests

from pathlib import Path

from uploader.variables import UploadStructure

TESTPULSE_RECEIVER_URL = ("https://testpulse-io-receiver.fly.dev/" +
                          "upload/test_results")
LOCAL_URL = 'http://localhost:8080/upload/test_results'


def send_test_results(zip: Path, localhost: bool) -> Optional[bool]:
    files = {'file': open(zip, 'rb')}

    data, token = generate_data_and_headers()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = LOCAL_URL if localhost else TESTPULSE_RECEIVER_URL
    req = requests.post(url=url,
                        files=files,
                        data=data,
                        headers=headers)
    if req.status_code != 200:
        print(f'Something went wrong: {req.text}')
        return False
    return True


def generate_data_and_headers() -> Optional[Tuple[Dict[str, str], str]]:
    upload_data = UploadStructure()

    data = {
        "commit": upload_data.commit,
        "user": upload_data.user,
    }

    return data, upload_data.token

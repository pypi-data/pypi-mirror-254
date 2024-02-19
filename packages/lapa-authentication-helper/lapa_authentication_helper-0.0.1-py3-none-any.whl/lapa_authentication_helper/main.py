import requests

from lapa_authentication_helper.configuration import (
    config_str_lapa_authentication_protocol,
    config_str_lapa_authentication_ip,
    config_str_lapa_authentication_port,
)


class LAPAAuthenticationHelper:
    def __init__(self):
        try:
            self.global_str_lapa_authentication_url_base = (
                f"{config_str_lapa_authentication_protocol}://"
                f"{config_str_lapa_authentication_ip}:{config_str_lapa_authentication_port}"
            )
        except Exception:
            raise

    def register(self, email: str, password: str, registration_type: str):
        try:
            endpoint = "register"
            url = f"{self.global_str_lapa_authentication_url_base}/{endpoint}"
            payload = {
                "email": email,
                "password": password,
                "registration_type": registration_type,
            }
            response = requests.post(url, json=payload)
            if response.status_code == 201:
                return response.json()
            else:
                response.raise_for_status()
        except Exception:
            raise

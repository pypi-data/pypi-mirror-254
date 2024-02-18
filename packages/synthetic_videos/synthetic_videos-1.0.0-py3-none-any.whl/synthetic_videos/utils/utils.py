import dataclasses
import json
from typing import Any, FrozenSet, Tuple

import requests
from requests import Session
from requests.adapters import HTTPAdapter, Retry


class EnhancedJSONEncoder(json.JSONEncoder):
    """
    This class extends the json.JSONEncoder class to support dataclasses.

    When encoding JSON, Python's built-in json.JSONEncoder class can be extended and
    customized to encode other Python types as JSON. This class adds support for
    Python's dataclasses, which are not supported by default.
    """

    def default(self, o: Any) -> Any:
        """
        Override the default method of JSONEncoder.

        This method returns a dictionary if the provided object is a dataclass instance.
        Otherwise, it calls the default method of the superclass.

        Parameters:
            o (Any): The Python object to be converted.

        Returns:
            Any: A dictionary if the object is a dataclass instance, otherwise the result of the superclass's default method.
        """

        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def requests_retry_session(
    retries: int = 10,
    backoff_factor: float = 1,
    status_forcelist: Tuple[int, ...] = (500, 502, 503, 504, 429, 409),
    allowed_methods: FrozenSet[str] = frozenset(
        {"DELETE", "GET", "HEAD", "OPTIONS", "PUT", "TRACE", "POST"}
    ),
) -> Session:
    """
    Creates a requests session with retry logic.

    Parameters:
    retries (int): Number of retries.
    backoff_factor (float): A backoff factor for retries.
    status_forcelist (tuple): A set of HTTP status codes that we should force a retry on.

    Returns:
    session: A requests session with retry logic.
    """
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=allowed_methods,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

from collections.abc import Sequence

from requests import Response


def get_payload(payload: dict, exclude: Sequence[str] | None = None) -> dict:
    """Extracts the payload from the response."""
    if payload is None:
        return {}

    if exclude is None:
        return payload

    for key in exclude:
        payload.pop(key, None)

    return payload


def prepare_payload(response: Response, exclude: Sequence[str] | None = None) -> dict:
    """Get payload."""
    payl = response.json().get("payload")
    payload = get_payload(payl, exclude)
    return payload


def list_prepare(
    response: Response, exclude: Sequence[str] | None = None
) -> list[dict]:
    """Get list without payload"""
    payload_list = []
    for payl in response.json():
        payload = get_payload(payl, exclude)
        payload_list.append(payload)
    return payload_list


def list_prepare_payload(
    response: Response, exclude: Sequence[str] | None = None
) -> list[dict]:
    """Get list with payload"""
    payload_list = []
    for payl in response.json().get("payload"):
        payload = get_payload(payl, exclude)
        payload_list.append(payload)
    return payload_list


def prepare_without_payload(
    response: Response, exclude: Sequence[str] | None = None
) -> dict:
    """Get without payload."""
    payl = response.json()
    payload = get_payload(payl, exclude)
    return payload

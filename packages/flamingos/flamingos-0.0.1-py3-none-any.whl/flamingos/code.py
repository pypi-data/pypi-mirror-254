import httpx


def testing():
    r = httpx.get("https://google.com")
    return r.status_code

from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import JSONResponse
import types as t
from utils import base64opencv

app = FastAPI()


@app.get("/get_color")
async def get_froth_color(image: str):
    """Calculates top colors of froth
    TODO: don't fix top to 5

    Args:
        image (str): image in base64 format

    Returns:
        Top-n pairs (hex code, percentage)
    """

    ans = [('#ff00ff', 25), ('#ffff00', 10), ('#00ffff', 5)]

    return JSONResponse(content=ans)

@app.get("/get_direction")
async def get_froth_direction(image: str):
    """Calculates direction of froth

    Args:
        image (str): image in base64 format

    Returns:
        Direction: two coordinates (x, y)
    """

    ans = (4/5, 3/5)

    return JSONResponse(content={'direction': ans})


@app.get("/get_speed")
async def get_froth_speed(image1: str, image2: str):
    """Calculates speed of froth by 2 images

    Args:
        image1 (str): image in base64 format
        image2 (str): image in base64 format

    Returns:
        Direction: two speed coordinates (dx, dy)
    """

    ans = (3/5, 4/5)

    return JSONResponse(content={'speed': ans})

@app.get("/get_count")
async def get_froth_count(image: str):
    """Calculates forth bubbles count

    Args:
        image (str): image in base64 format

    Returns:
        Bubbles count: int
    """

    ans = 100

    return JSONResponse(content={'count': ans})


@app.get("/get_status")
async def get_froth_status(image: str):
    """Calculates flotation status (good or bad)

    Args:
        image (str): image in base64 format

    Returns:
        Bubbles count: int
    """

    ans = 10000

    return JSONResponse(content={'count': ans})
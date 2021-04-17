from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import JSONResponse
from typing import List
from utils import base64opencv
from pydantic import BaseModel
from froth_models import color, ncenters

app = FastAPI()


class SingleImage(BaseModel):
    image: str

class Images(BaseModel):
    images: List[str]

@app.post("/calculate_color")
async def get_froth_color(data: SingleImage):
    """Calculates top colors of froth
    TODO: don't fix top to 5

    Args:
        image (str): image in base64 format

    Returns:
        Top-n pairs (hex code, percentage)
    """
    image = base64opencv(data.image)
    
    ans = color.get_colors(color.get_image(image))

    # PROCESS

    #ans = [('#ff00ff', 25), ('#ffff00', 10), ('#00ffff', 5)]

    return JSONResponse(content=ans)

@app.post("/calculate_direction")
async def get_froth_direction(data: SingleImage):
    """Calculates direction of froth

    Args:
        image (str): image in base64 format

    Returns:
        Direction: two coordinates (x, y)
    """

    image = base64opencv(data.image)

    # PROCESS

    ans = (4/5, 3/5)

    return JSONResponse(content={'direction': ans})


@app.post("/calculate_speed")
async def get_froth_speed(data: Images):
    """Calculates speed of froth by 2 images

    Args:
        image1 (str): image in base64 format
        image2 (str): image in base64 format

    Returns:
        Direction: two speed coordinates (dx, dy)
    """

    images = data.images
    image1 = base64opencv(images[0])
    image2 = base64opencv(images[1])

    # PROCESS

    ans = (3/5, 4/5)

    return JSONResponse(content={'speed': ans})

@app.post("/calculate_count")
async def get_froth_count(data: SingleImage):
    """Calculates forth bubbles count

    Args:
        image (str): image in base64 format

    Returns:
        Bubbles count: int
    """
    
    image = base64opencv(data.image)
    
    image = ncenters.image_preproc(image)
    
    ans = len(ncenters.find_centers(image))

    # PROCESS

    #ans = 100

    return JSONResponse(content={'count': ans})


@app.post("/calculate_status")
async def get_froth_status(data: SingleImage):
    """Calculates flotation status (good or bad)

    Args:
        image (str): image in base64 format

    Returns:
        Bubbles count: int
    """

    image = base64opencv(data.image)

    # PROCESS

    ans = 10000

    return JSONResponse(content={'count': ans})

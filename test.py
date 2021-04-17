from utils import base64opencv, opencvbase64
import cv2
import os
import base64
import requests


def test_base64():
    #frame = cv2.imread('trash/test.JPG')
    frame = cv2.imread('trash/F1_1_5_2.ts_f_3.jpg')

    encoded = opencvbase64(frame)
    decoded = base64opencv(encoded)

    cv2.imwrite('trash/output.jpg', decoded)


def test_endpoint(endpoint, data, host='localhost', port=8999, method='post'):
    addr = f'http://{host}:{port}/{endpoint}'
    func = getattr(requests, method)
    resp = func(addr, json=data)
    print(resp)

    return resp.json()


if __name__ == '__main__':
    test_base64()

    #frame = cv2.imread('trash/test.JPG')
    frame = cv2.imread('trash/F1_1_5_2.ts_f_3.jpg')
    encoded = opencvbase64(frame)

    single_image = {'image': encoded}
    multiple = {'images': [encoded, encoded]}

    color = test_endpoint('calculate_color', single_image)
    print(color)

    direction = test_endpoint('calculate_direction', multiple)
    print(direction)

    speed = test_endpoint('calculate_speed', multiple)
    print(speed)

    count = test_endpoint('calculate_count', single_image)
    print(count)

    status = test_endpoint('calculate_status', single_image)
    print(status)


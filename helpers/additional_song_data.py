import requests


def download_cover_img(track_id, sp):
    track_info = sp.track(track_id)
    album_info = track_info["album"]
    images = album_info["images"]
    image_names = ["cover_640x640.jpg", "cover_300x300.jpg", "cover_64x64.jpg"]

    for value, name in zip(images, image_names):
        print(value)
        img_data = requests.get(value["url"]).content
        with open(name, 'wb') as handler:
            handler.write(img_data)

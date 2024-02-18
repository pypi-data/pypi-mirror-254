from apiflask import Schema
from apiflask.fields import File, URL, String, Integer


class ImageIn(Schema):
    image = File()


class DietImageIn(Schema):
    image = File()
    category = Integer()


class ImagePreSignUrlIn(Schema):
    image_id = String(required=True)
    expire_time = Integer()


class ImagePreSignUrlOut(Schema):
    image_presign_url = URL()


class ImageIdOut(Schema):
    image_id = String()


class ProfilingIn(Schema):
    token = String()



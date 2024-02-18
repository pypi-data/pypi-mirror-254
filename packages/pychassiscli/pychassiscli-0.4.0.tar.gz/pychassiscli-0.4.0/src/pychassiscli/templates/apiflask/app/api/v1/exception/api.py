from apiflask import HTTPError


class ImageUploadError(HTTPError):
    status_code = 500
    message = '上传图片失败'


class UserInfoError(HTTPError):
    status_code = 500
    message = '设置用户信息失败'


class DietCreationError(HTTPError):
    status_code = 500
    message = '添加食物记录失败'


class ImageNotFound(HTTPError):
    status_code = 404
    message = '获取图片链接失败'

FROM python:3.11-slim

# 拷贝依赖
COPY . /app
# 设置工作路径
WORKDIR /app
# 安装依赖
RUN python3 -m pip install -i https://mirrors.cloud.tencent.com/pypi/simple --trusted-host=mirrors.cloud.tencent.com -r requirements.txt
# 启动时运行命令
CMD ["sh", "docker-deploy.sh", "./admin/config.yml", "admin.admin"]
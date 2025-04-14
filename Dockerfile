FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY fix-requirements.txt .

# 首先安装基本依赖
RUN pip install --no-cache-dir -r requirements.txt

# 然后安装 fix-requirements.txt 中的包
RUN pip install --no-cache-dir -r fix-requirements.txt

# 复制应用代码
COPY . .

# 创建数据目录
RUN mkdir -p /data

# 运行应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
import logging
import os

# 确保 logs 目录存在
os.makedirs("logs", exist_ok=True)

# 日志文件路径
log_path = os.path.join("logs", "test.log")

# 配置 logging 输出格式和等级
logging.basicConfig(
    filename=log_path,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger()
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s {%(pathname)s:%(lineno)d}",
    handlers=[logging.StreamHandler()],
)

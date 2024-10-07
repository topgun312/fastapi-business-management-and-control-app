import uvicorn
from loguru import logger

if __name__ == "__main__":
    logger.add(
        "logs/logs.json",
        format="{time} {level} {message}",
        level="DEBUG",
        rotation="10 MB",
        compression="zip",
        serialize=True,
    )

    logger.debug("Error")
    logger.info("Information message")
    logger.warning("Warning")

    uvicorn.run(app="src.main:app", port=8000, reload=True)

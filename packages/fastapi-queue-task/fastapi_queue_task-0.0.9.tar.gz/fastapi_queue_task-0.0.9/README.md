# FastAPI queue

## How to use

1. Instance the class `Queue` with `redis` instance and `options`

```python
# queue_config.py

from fastapi_queue_task import Queue
from redis.asyncio.utils import from_url

redis = from_url(
    f"redis://#REDIS_HOST:#REDIS_PORT/#REDIS_DATABASE_NAME",
    encoding="utf-8",
    decode_responses=True,
)
queue = Queue(redis, options={'concurrency': 10, 'max_attempt': 3})
queue.run()
```

2. Add task to queue:

```python
# mail_service.py
await queue.add_to_queue(name="TASK_NAME", data: Any = {})
```

## How to test in testpypi

1. Increase the version in `pyproject.toml`
2. Run command

```bash
$ . ./build_and_test.sh
```

## How to publish new version

1. Increase the version in `pyproject.toml`
2. Run command

```bash
$ . ./build_and_publish.sh
```

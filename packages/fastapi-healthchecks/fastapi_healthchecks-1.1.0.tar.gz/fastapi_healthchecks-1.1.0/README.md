# FastAPI health checks

Configurable health checks endpoints for FastAPI applications.

## Quickstart

```python
app = FastAPI()
app.include_router(
    HealthcheckRouter(
        Probe(
            name="readiness",
            checks=[
                PostgreSqlCheck(host="db.example.com", username=..., password=...),
                RedisCheck(host="redis.example.com", username=..., password=...),
            ],
        ),
        Probe(
            name="liveness",
            checks=[
                ...,
            ],
        ),
    ),
    prefix="/health",
)
```

The probes from this example will be available as `GET /health/readiness` and `GET /health/liveness`.

## Bundled checks

* `PostgreSqlCheck` – checks PostgreSQL server availability
* `RedisCheck` – checks Redis server availability
* `RabbitMqCheck` – checks RabbitMQ server availability
* `SettingsCheck` – validates settings models based on pydantic BaseModel
* `HttpCheck` – checks availability of specified URL
* `CephCheck` – checks Ceph server availability

## Custom checks

You can create your own checks by providing custom `fastapi_healthchecks.checks.Check` implementations. Like this:

```python
class MaintenanceCheck(Check):
    async def __call__(self) -> CheckResult:
        if is_maintenance():
            return CheckResult(name="Maintenance", passed=False, details="Closed for maintenance")
        else:
            return CheckResult(name="Maintenance", passed=True)
```

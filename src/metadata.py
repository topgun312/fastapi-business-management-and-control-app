TAG_METADATA = [
    {
        "name": "users",
        "description": "Registration of a company or employee and work with personal data of an employee",
    },
    {
        "name": "structure",
        "description": "Work with the organizational structure of the company",
    },
    {"name": "tasks", "description": "Working with the task book"},
    {
        "name": "healthz",
        "description": "Standard service health check",
    },
]

TITLE = "FastAPI business management and control app"

DESCRIPTION = (
    "An application with the following functionality:"
    "• Registration of a company or employee and work with personal data of an employee"
    "• Work with the organizational structure of the company"
    "• Working with the task book"
)


VERSION = "0.0.1"

ERROR_MAPS = {
    "postgres": "PostgreSQL connection failed",
    "redis": "Redis connection failed",
}

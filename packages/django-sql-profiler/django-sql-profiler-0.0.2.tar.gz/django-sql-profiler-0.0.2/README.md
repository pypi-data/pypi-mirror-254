## Django SQL Profiler

This package inspred by Sentry SDK, its will capture all SQL statements and save to MongoDB
Require: PyMongo

#### How to use
```python
import sql_profiler
sql_profiler.install_sql_hook(
    {
        'slow_queries_threshold': 0.2,
        'app_namespace': ['apps.'],
        'mongodb': {
            'uri': MONGODB,
            'db': MONGODB_DB,
            'collection': 'sql_slow_queries'
        }
    }
)
```
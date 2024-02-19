import contextlib
import hashlib
import os
import re
import socket
import sys
import time

from pymongo import MongoClient


def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z


def _is_external_source(abs_path):
    # type: (str) -> bool
    # check if frame is in 'site-packages' or 'dist-packages'
    external_source = (
        re.search(r"[\\/](?:dist|site)-packages[\\/]", abs_path) is not None
    )
    return external_source


def hash_query_id(source, sql):
    before_hash = sql
    if source:
        before_hash = f"{source.get('filepath')}:{source.get('code_function')}:{source.get('lineno')}:{sql}"
    return hashlib.md5(before_hash.encode()).hexdigest()

def _valid_app_name(self, namespace):
    pass
    
def find_source():
    frame = sys._getframe()
    while frame is not None:
        try:
            abs_path = frame.f_code.co_filename
            if abs_path:
                abs_path = os.path.abspath(abs_path)
        except Exception:
            abs_path = ""

        try:
            namespace = frame.f_globals.get("__name__")
        except Exception:
            namespace = None
        should_be_included = not _is_external_source(abs_path)
        is_app_module = namespace is not None and namespace.startswith("apps.")

        if should_be_included and is_app_module and "wsgi" not in abs_path:
            break
        frame = frame.f_back

    else:
        frame = None

    if frame is not None:
        try:
            lineno = frame.f_lineno
        except Exception:
            lineno = None
        try:
            namespace = frame.f_globals.get("__name__")
        except Exception:
            namespace = None
        try:
            filepath = frame.f_code.co_filename
        except Exception:
            filepath = None
        try:
            code_function = frame.f_code.co_name
        except Exception:
            code_function = None

        return {
            "filepath": filepath,
            "namespace": namespace,
            "code_function": code_function,
            "lineno": lineno,
        }


@contextlib.contextmanager
def capture_sql_query(sql, params=None, executemany=False, options={}):
    source = find_source()
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        is_slow_query = duration > options.get("slow_queries_thresold", 0)
        query_id = hash_query_id(source, sql)
        mongo_opts = options.get("mongodb", None)
        if is_slow_query:
            if mongo_opts:
                mongo_instance = get_mongodb_instance(
                    mongo_opts.get("uri", ""),
                    mongo_opts.get("db", ""),
                    mongo_opts.get("collection", ""),
                )
                mongo_instance.insert_one(
                    {
                        "host_name": socket.gethostname(),
                        "host_ip": socket.gethostbyname(socket.gethostname()),
                        "source": source,
                        "query_id": query_id,
                        "sql": sql,
                        "params": params,
                        "is_slow_query": is_slow_query,
                        "duration": time.time() - start_time,
                        "timestamp": start_time,
                    }
                )

        # print(f"Source: {source}")
        # print(f"Hash: {hash_query_id(source, sql)}")
        # print(f"SQL: {sql}")
        # print(f"Duration: {time.time() - start_time}")


def get_mongodb_instance(uri, db_name, collection):
    conn = MongoClient(host=uri, maxPoolSize=300)
    return conn[db_name][collection]


def install_sql_hook(options={}):
    _options = merge_two_dicts({"slow_queries_thresold": 0.2}, options)

    """If installed this causes Django's queries to be captured."""
    try:
        from django.db.backends.utils import CursorWrapper
    except ImportError:
        from django.db.backends.util import CursorWrapper

    try:
        # django 1.6 and 1.7 compatability
        from django.db.backends import BaseDatabaseWrapper
    except ImportError:
        # django 1.8 or later
        from django.db.backends.base.base import BaseDatabaseWrapper

    try:
        real_execute = CursorWrapper.execute
        real_executemany = CursorWrapper.executemany
        real_connect = BaseDatabaseWrapper.connect
    except AttributeError:
        # This won't work on Django versions < 1.6
        return

    def execute(self, sql, params=None):
        with capture_sql_query(sql, params, executemany=False, options=_options):
            return real_execute(self, sql, params)

    def executemany(self, sql, param_list):
        with capture_sql_query(sql, param_list, executemany=True, options=_options):
            return real_executemany(self, sql, param_list)

    def connect(self):
        return real_connect(self)

    CursorWrapper.execute = execute
    CursorWrapper.executemany = executemany
    BaseDatabaseWrapper.connect = connect

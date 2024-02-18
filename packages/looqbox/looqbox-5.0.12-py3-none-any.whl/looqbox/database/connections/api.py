from looqbox.class_loader.class_loader import ClassLoader

def SqlThreadManager(*args, **kwargs):
    return ClassLoader("SqlThreadManager", "looqbox.database.connections.sql_thread_manager").call_class(*args, **kwargs)

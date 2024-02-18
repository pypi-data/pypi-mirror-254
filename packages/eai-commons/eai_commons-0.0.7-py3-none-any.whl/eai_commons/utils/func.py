

def get_full_function_name(func) -> str:
    """
    eg: eai_commons_tests.unit_tests.utils.test_rate_limit.run_some_list_tasks
    """
    return f"{func.__module__}.{func.__name__}"


def get_compact_function_name(func) -> str:
    """
    eg: e.u.u.t.run_some_list_tasks
    """
    package_name = ".".join([s_[0] for s_ in str(func.__module__).split(".")])
    return f"{package_name}.{func.__name__}"

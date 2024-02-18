import traceback


def exception_as_string(error: Exception) -> str:
    return "".join(traceback.format_exception(error))

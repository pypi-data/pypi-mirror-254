from litestar import get_version

def get_litestar_major_version() -> int:
    return get_version().major

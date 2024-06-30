def get_raises_info(f, *args, **kwargs):
    """
    获取运行函数引发的错误
    Args:
        f: 函数
        *args: 函数参数
        **kwargs: 函数关键参

    Returns:
        错误 或者 None
    """
    try:
        f(*args, **kwargs)
    except Exception as e:
        return e

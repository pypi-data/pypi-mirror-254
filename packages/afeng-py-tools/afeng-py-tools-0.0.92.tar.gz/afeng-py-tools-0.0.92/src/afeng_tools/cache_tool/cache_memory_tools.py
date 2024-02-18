# 内存缓存
from typing import Any

MEMORY_CACHE = {}


def add_cache(group_code: str, key: str, value: Any):
    """添加缓存"""
    group_cache = MEMORY_CACHE.get(group_code)
    if not group_cache:
        MEMORY_CACHE[group_code] = dict()
    MEMORY_CACHE[group_code][key] = value


def get_cache(group_code: str, key: str):
    """获取缓存"""
    group_cache = MEMORY_CACHE.get(group_code)
    if group_cache:
        return MEMORY_CACHE.get(group_code).get(key)

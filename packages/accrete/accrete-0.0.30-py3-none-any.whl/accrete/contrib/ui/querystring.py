import json


def load_querystring(get_params: dict) -> list:
    return json.loads(get_params.get('q', '[]'))


def build_querystring(get_params: dict, extra_params: list[str] = None) -> str:
    querystring = f'?q={get_params.get("q", "[]")}'
    if paginate_by := get_params.get('paginate_by', False):
        querystring += f'&paginate_by={paginate_by}'
    if order_by := get_params.get('order_by', False):
        querystring += f'&order_by={order_by}'
    if crumbs := get_params.get('crumbs', False):
        querystring += f'&crumbs={crumbs}'
    for param in extra_params or []:
        if value := get_params.get(param, False):
            querystring += f'&{param}={value}'
    return querystring

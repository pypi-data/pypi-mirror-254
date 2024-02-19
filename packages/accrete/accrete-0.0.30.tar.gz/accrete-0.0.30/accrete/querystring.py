import logging
import json
import operator
from django.db.models import Model, Q, QuerySet

_logger = logging.getLogger(__name__)


def filter_querystring(model: type[Model], query_string: str) -> QuerySet:
    return model.objects.filter(parse_querystring(model, query_string))


def parse_querystring(model: type[Model], query_string: str) -> Q:
    """
    param: query_string: JSON serializable string
    [{term: value}, '&', [{term: value}, '|', {~term: value}]]
    Q(term=value) & (Q(term=value) | ~Q(term=value))
    """

    def get_expression(term: str, value) -> Q:
        invert = False
        if term.startswith('~'):
            invert = True
            term = term[1:]

        parts = term.split('_a_')
        if len(parts) == 1:
            expression = Q(**{term: value})
            return ~expression if invert else expression

        rel_path = parts[0].rstrip('__')
        term = parts[1]
        rel_model = get_related_model(rel_path) if rel_path else model
        objects = rel_model.objects.annotate(**{
            annotation['name']: annotation['func']
            for annotation in rel_model.annotations
        }).filter(Q(**{term: value}))
        expression = Q(**{
            f'{rel_path}{"__" if rel_path else ""}id__in': objects.values_list('id', flat=True)
        })

        return ~expression if invert else expression

    def get_related_model(rel_path: str):
        related_model = model
        for part in rel_path.split('__'):
            try:
                related_model = related_model._meta.fields_map[part].related_model
            except (AttributeError, KeyError):
                try:
                    related_model = getattr(related_model, part).field.related_model
                except AttributeError:
                    break
        return related_model

    def parse_query_block(sub_item) -> Q:
        op = ops['&']
        parsed_query = Q()
        for item in sub_item:
            if isinstance(item, list):
                parsed_query = op(parsed_query, parse_query_block(item))
                op = ops['&']
            elif isinstance(item, dict):
                dict_query = Q()
                for term, value in item.items():
                    dict_query = ops['&'](dict_query, get_expression(term, value))
                parsed_query = op(parsed_query, dict_query)
            elif isinstance(item, str):
                if item not in '&|^':
                    raise ValueError(
                        f'Invalid operator in querystring: {item}.'
                        f'Operator must be one of &, |, ^'
                    )
                op = ops[item]

            else:
                raise ValueError(
                    f'Unsupported item in querystring: {item}.'
                    f'Item must be an instance of list, dict or str'
                )
        return parsed_query

    query_data = json.loads(query_string)
    if isinstance(query_data, dict):
        query_data = [query_data]

    ops = {'&': operator.and_, '|': operator.or_, '^': operator.xor}
    query = parse_query_block(query_data)
    return query

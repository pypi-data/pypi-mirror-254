from dataclasses import dataclass, field
from enum import Enum
from django.db.models import Model, QuerySet, Q

DEFAULT_PAGINATE_BY = 40


class ActionMethod(Enum):

    HREF = 'href'
    GET = 'hx-get'
    POST = 'hx-post'
    PUT = 'hx-put'
    DELETE = 'hx-delete'


class TableFieldAlignment(Enum):

    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'


class TableFieldType(Enum):

    NONE = ''
    STRING = '_string'
    MONETARY = '_monetary'
    FLOAT = '_float'


@dataclass
class TableField:

    label: str
    name: str
    alignment: TableFieldAlignment | Enum = TableFieldAlignment.LEFT
    header_alignment: TableFieldAlignment | Enum = None
    header_info: str = None
    field_type: TableFieldType | Enum = TableFieldType.NONE
    prefix: str = ''
    suffix: str = ''
    truncate_after: int = 0
    template: str = None


@dataclass
class BreadCrumb:

    name: str
    url: str
    add_url_params: bool = True


@dataclass
class ClientAction:

    name: str
    url: str = ''
    method: ActionMethod = ActionMethod.HREF
    query_params: str = ''
    attrs: list[tuple[str, str]] = field(default_factory=list)
    submit: bool = False
    form_id: str = 'form'
    class_list: list[str] = field(default_factory=list)
    add_url_params: bool = False

    def attrs_str(self):
        return ' '.join([f'{str(attr[0])}={str(attr[1])}' for attr in self.attrs])


@dataclass
class List:

    queryset: QuerySet
    title: str = None
    paginate_by: int = DEFAULT_PAGINATE_BY
    breadcrumbs: list[BreadCrumb] = field(default_factory=list)
    actions: list[ClientAction] = field(default_factory=list)
    fields: list[TableField] = field(default_factory=list)

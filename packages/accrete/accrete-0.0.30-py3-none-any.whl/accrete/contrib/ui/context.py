import logging
from dataclasses import dataclass, field

from django.utils.translation import gettext_lazy as _
from django.db.models import Model, QuerySet, Q
from django.core.paginator import Paginator
from django.forms import Form, ModelForm
from accrete.querystring import parse_querystring

from .querystring import load_querystring, build_querystring
from .components import ClientAction, BreadCrumb, TableField
from .filter import Filter

_logger = logging.getLogger(__name__)

DEFAULT_PAGINATE_BY = 40


@dataclass
class ListContext:

    model: type[Model]
    get_params: dict
    title: str = None
    context: dict = field(default_factory=dict)
    queryset: QuerySet = None
    select_related: list[str] = field(default_factory=list)
    prefetch_related: list[str] = field(default_factory=list)
    annotate: dict = field(default_factory=dict)
    paginate_by: int = DEFAULT_PAGINATE_BY
    order_by: list[str] = field(default_factory=list)
    filter_relation_depth: int = 4
    default_filter_term: str = ''
    actions: list[ClientAction] = field(default_factory=list)
    breadcrumbs: list[BreadCrumb] = field(default_factory=list)
    object_label: str = None
    fields: list[TableField] = field(default_factory=list)
    unselect_button: bool = False
    endless_scroll: bool = True

    def get_queryset(self):
        if self.queryset:
            return self.queryset

        order = self.order_by or self.model._meta.ordering

        # pks = self.model.objects.filter(
        #     parse_querystring(self.model, self.get_params.get('q', '[]'))
        # ).distinct().values_list('pk', flat=True)

        queryset = self.model.objects.select_related(
            *self.select_related
        ).prefetch_related(
            *self.prefetch_related
        ).filter(
            parse_querystring(self.model, self.get_params.get('q', '[]'))
        ).annotate(
            **self.get_annotations()
        ).order_by(
            *order
        ).distinct()

        return queryset

    def get_annotations(self):
        annotations = {
            annotation['name']: annotation['func']
            for annotation in getattr(self.model, 'annotations', [])
        }
        if self.annotate:
            annotations.update(self.annotate)
        return annotations

    def get_page_number(self, paginator):
        page_number = self.get_params.get('page', '1')

        try:
            page_number = int(page_number)
        except ValueError:
            page_number = 1

        if page_number < 1:
            page_number = 1
        elif page_number > paginator.num_pages:
            page_number = paginator.num_pages
        return page_number

    def get_paginate_by(self):
        paginate_by = self.get_params.get('paginate_by', self.paginate_by)
        try:
            paginate_by = int(paginate_by)
        except ValueError:
            paginate_by = self.paginate_by
        return paginate_by

    def dict(self):
        queryset = self.get_queryset()
        paginate_by = self.get_paginate_by()
        paginator = Paginator(queryset, paginate_by)
        page = paginator.page(self.get_page_number(paginator))
        context = {
            'queryset': queryset,
            'paginate_by': paginate_by,
            'order_by': self.get_params.get('order_by', self.model._meta.ordering),
            'paginator': paginator,
            'page': page,
            'list_pagination': True,
            'title': self.title or self.model._meta.verbose_name_plural,
            'object_label': self.object_label or self.model._meta.verbose_name or _('Name'),
            'filter_terms': Filter(self.model, self.filter_relation_depth).get_query_terms(),
            'default_filter_term': self.default_filter_term,
            'breadcrumbs': self.breadcrumbs,
            'querystring': load_querystring(self.get_params),
            'url_params': build_querystring(self.get_params),
            'actions': self.actions,
            'fields': self.fields,
            'endless_scroll': self.endless_scroll
        }
        context.update(self.context)
        return context


@dataclass
class DetailContext:

    obj: Model | type[Model]
    get_params: dict
    order_by: str = None
    paginate_by: int = DEFAULT_PAGINATE_BY
    title: str = None
    queryset: type[QuerySet] = None
    select_related: list[str] = field(default_factory=list)
    prefetch_related: list[str] = field(default_factory=list)
    annotate: dict = field(default_factory=dict)
    actions: list[ClientAction] = field(default_factory=list)
    breadcrumbs: list[BreadCrumb] = field(default_factory=list)
    context: dict = field(default_factory=dict)

    def get_queryset(self):
        if self.queryset:
            return self.queryset

        order = self.order_by or self.obj._meta.model._meta.ordering

        pks = self.obj._meta.model.objects.filter(
            parse_querystring(self.obj._meta.model, self.get_params.get('q', '[]'))
        ).distinct().values_list('pk', flat=True)

        queryset = self.obj._meta.model.objects.select_related(
            *self.select_related
        ).prefetch_related(
            *self.prefetch_related
        ).filter(
            Q(pk__in=pks)
        ).annotate(
            **self.get_annotations()
        ).order_by(
            *order
        ).distinct()

        return queryset

    def get_annotations(self):
        annotations = {
            annotation['name']: annotation['func']
            for annotation in getattr(self.obj._meta.model, 'annotations', [])
        }
        if self.annotate:
            annotations.update(self.annotate)
        return annotations

    def get_paginate_by(self):
        paginate_by = self.get_params.get('paginate_by', self.paginate_by)
        try:
            paginate_by = int(paginate_by)
        except ValueError:
            paginate_by = self.paginate_by
        return paginate_by

    def get_pagination_context(self):
        if not hasattr(self.obj, 'get_absolute_url'):
            _logger.warning(
                'Detail pagination disabled for models without the '
                'get_absolute_url attribute. Set paginate_by to 0 to '
                'deactivate pagination.'
            )
            return {}
        queryset = self.get_queryset()
        idx = (*queryset,).index(self.obj)
        previous_object_url = (
            queryset[idx - 1] if idx - 1 >= 0 else queryset.last()
        ).get_absolute_url()
        next_object_url = (
            queryset[idx + 1] if idx + 1 <= queryset.count() - 1 else queryset.first()
        ).get_absolute_url()
        ctx = {
            'previous_object_url': previous_object_url,
            'next_object_url': next_object_url,
            'current_object_idx': idx + 1,
            'total_objects': queryset.count(),
            'detail_pagination': True
        }
        return ctx

    def dict(self):
        paginate_by = self.get_paginate_by()
        ctx = {
            'object': self.obj,
            'title': self.title or self.obj,
            'order_by': self.get_params.get('order_by', self.obj._meta.model._meta.ordering),
            'paginate_by': paginate_by,
            'detail_pagination': False,
            'breadcrumbs': self.breadcrumbs,
            'url_params': build_querystring(self.get_params, ['page']),
            'actions': self.actions
        }
        if self.paginate_by > 0:
            ctx.update(self.get_pagination_context())
        ctx.update(self.context)
        return ctx


@dataclass
class FormContext:

    model: Model | type[Model]
    form: Form | ModelForm
    get_params: dict
    title: str = None
    context: dict = field(default_factory=dict)
    form_id: str = 'form'
    add_default_actions: bool = True
    discard_url: str = None
    actions: list[ClientAction] = field(default_factory=list)
    breadcrumbs: list[BreadCrumb] = field(default_factory=list)

    def get_default_form_actions(self):
        actions = [
            ClientAction(
                name=_('Save'),
                submit=True,
                class_list=['is-success'],
                form_id=self.form_id
            )
        ]
        try:
            url = self.discard_url or (self.model.pk and self.model.get_absolute_url())
        except TypeError:
            raise TypeError(
                'Supply the discard_url parameter if FormContext is called '
                'with a model class instead of an instance.'
            )
        except AttributeError as e:
            _logger.error(
                'Supply the discard_url parameter if FormContext is '
                'called with a model instance that has the get_absolute_url '
                'method not defined.'
            )
            raise e

        actions.append(
            ClientAction(
                name=_('Discard'),
                url=url,
            )
        )
        return actions

    def get_title(self):
        if self.title:
            return self.title
        try:
            int(self.model.pk)
            return _('Edit')
        except TypeError:
            return _('Add')

    def dict(self):
        ctx = {
            'title': self.get_title(),
            'form': self.form,
            'form_id': self.form_id,
            'url_params': build_querystring(self.get_params, ['page']),
            'actions': [],
            'breadcrumbs': self.breadcrumbs,
        }
        if self.add_default_actions:
            ctx.update({'actions': self.get_default_form_actions()})
        ctx['actions'].extend(self.actions)
        ctx.update(self.context)
        return ctx

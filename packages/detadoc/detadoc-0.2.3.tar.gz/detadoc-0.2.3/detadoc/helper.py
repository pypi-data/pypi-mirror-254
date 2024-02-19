import re
from typing import Any

from hx_markup import Element
from hx_markup.element import NodeText
from ormspace import functions
from ormspace.bases import ModelType
from starlette.requests import Request
from starlette.responses import RedirectResponse

from detadoc.models import Patient


async def check_session_user(request: Request):
    if not request.session.get('user'):
        return RedirectResponse('/login')

async def get_patient(request: Request):
    return await Patient.fetch_instance(
            request.path_params.get('patient_key', request.query_params.get('patient_key'))
    )


def list_group_item(instance: ModelType) -> Element:
    return Element('li', '.list-group-item', NodeText(str(instance)))

def list_group_item_action(instance: ModelType, query: dict = None) -> Element:
    return Element('li', '.list-group-item', Element('a', '.list-group-item-action', NodeText(str(instance)), htmx={
            'get': f'/api/{instance.item_name()}/{instance.key}?{functions.write_query(query or {})}',
            'indicator': f'#htmx-{instance.item_name()}-indicator',
            'target': f'#htmx-{instance.item_name()}-container'
    }))

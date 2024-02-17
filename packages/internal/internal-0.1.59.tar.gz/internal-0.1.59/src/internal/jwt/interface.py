from dataclasses import dataclass

from ..interface.base_interface import InternalBaseInterface


@dataclass
class JWTUserInterface(InternalBaseInterface):
    id: str
    name: str
    phone: str
    mobile: str
    email: str
    title: str
    organization_parent: str
    organization_id: str
    ext_user_id: str
    ext_dealer_code: str
    ext_dept_code: str
    ext_dept_name: str
    line_id: str
    line_url: str
    role: str
    avatar: str = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@dataclass
class JWTCustomerInterface(InternalBaseInterface):
    id: str
    ccid: str
    name: str
    phone: str
    mobile: str
    email: str
    title: str
    organization_parent: str
    organization_id: str
    ext_user_id: str
    ext_dealer_code: str
    ext_dept_code: str
    ext_dept_name: str
    line_id: str
    line_url: str
    role: str
    avatar: str = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@dataclass
class JWTTokenInterface(InternalBaseInterface):
    data: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

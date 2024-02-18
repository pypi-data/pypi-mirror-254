from enum import Enum
from typing import Union, Dict, List
from requests import Session


class JSONReturnModel(object):
    def __init__(self, data: Union[Dict, List]):
        self.data: Union[Dict, List] = data["data"]
        self.message: str = data["message"]
        self.status: int = data["status"]


class TextReturnModel(object):
    def __init__(self, data: str):
        self.data: str = data


class BaseRequestModel(object):
    def __init__(
        self,
        data: Union[Dict, List],
        url: str,
        method: str,  # get post...
        bypass_proxy: bool = False,
        model: Union[JSONReturnModel, TextReturnModel] = JSONReturnModel,
    ):
        self.data = data
        self.url = url.lower()
        self.method = method
        self.bypass_proxy = bypass_proxy
        self.model = model

    def run(self) -> Union[JSONReturnModel, TextReturnModel]:
        s = APISession(BYPASS_SYSTEM_PROXY=self.bypass_proxy)
        r = getattr(s, self.method.lower())(url=self.url, data=self.data)
        if isinstance(self.model, TextReturnModel):
            return TextReturnModel(r.text)
        else:
            return JSONReturnModel(r.json())


class AuthRequestModel(BaseRequestModel):
    def __init__(
        self,
        url: str,
        method: str,  # get post...
        bypass_proxy: bool = False,
        model: Union[JSONReturnModel, TextReturnModel] = JSONReturnModel,
        authorization: str = "",
    ):
        super().__init__(
            data={},
            url=url,
            method=method,
            bypass_proxy=bypass_proxy,
            model=model,
        )
        self.authorization = authorization

    def run(self) -> Union[JSONReturnModel, TextReturnModel]:
        s = APISession(BYPASS_SYSTEM_PROXY=self.bypass_proxy)
        s.headers.update({"Authorization": f"Bearer {self.authorization}"})
        r = getattr(s, self.method.lower())(url=self.url, data=self.data)
        if isinstance(self.model, TextReturnModel):
            return TextReturnModel(r.text)
        else:
            return JSONReturnModel(r.json())


class APISession(Session):
    def __init__(self, BYPASS_SYSTEM_PROXY=False):
        super().__init__()
        #: Trust environment settings for proxy configuration, default
        #: authentication and similar.
        self.trust_env = not BYPASS_SYSTEM_PROXY


class RouterBase(Enum):
    def apiPath(self):
        return f"{APIRouter.base}{self.__path__}{self.value}"


class APIRouter:
    base = "https://api.mefrp.com"

    class PublicRouter(RouterBase):
        __path__ = "/api/v4/public"
        login = "/verify/login"
        sponsor = "/info/sponsor"
        statistics = "/info/statistics"
        register = "/verify/register"
        register_email = "/verify/register_email"
        forgot_password = "/verify/forgot_password"
        # reset_password = "/verify/reset_password{link}"
        setting = "/info/setting"

    class AuthRouter(RouterBase):
        __path__ = "/api/v4/auth"
        user_info = "/user"
        user_sign = "/user/sign"
        # user_sign = "/user/sign"
        refresh_token = "/user/refresh_token"
        realname_get = "/user/realname_get"
        realname_post = "/user/realname_post"
        tunnel_list = "/tunnel/list"
        tunnel_conf_node = "/tunnel/conf/node/{node}"
        tunnel_conf_id = "/tunnel/conf/id/{id}"
        tunnel_create = "/tunnel/create"
        tunnel_delete = "/tunnel/delete/{tunnel_id}"
        tunnel_info = "/tunnel/info/{tunnel_id}"
        node_list = "/node/list"
        # reset_password = "/user/reset_password"

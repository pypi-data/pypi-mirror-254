from .models import JSONReturnModel, AuthRequestModel, TextReturnModel, APIRouter

AuthRouter = APIRouter.AuthRouter


def me_get_user_info(authorization: str, bypass_proxy: bool = False) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.user_info.apiPath(),
        method="GET",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_user_get_sign_info(authorization: str, bypass_proxy: bool = False) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.user_sign.apiPath(),
        method="GET",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_user_sign(authorization: str, bypass_proxy: bool = False) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.user_sign.apiPath(),
        method="POST",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_refresh_user_token(
    authorization: str, bypass_proxy: bool = False
) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.refresh_token.apiPath(),
        method="POST",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_get_realname_status(
    authorization: str, bypass_proxy: bool = False
) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.realname_get.apiPath(),
        method="GET",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_post_realname(
    authorization: str, idcard: str, name: str, bypass_proxy: bool = False
) -> JSONReturnModel:
    return AuthRequestModel(
        data={"idcard": idcard, "name": name},
        url=AuthRouter.realname_post.apiPath(),
        method="POST",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_get_tunnel_list(
    authorization: str, bypass_proxy: bool = False
) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.tunnel_list.apiPath(),
        method="GET",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_get_tunnel_config_node(
    authorization: str, node: int, bypass_proxy: bool = False
) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.tunnel_conf_node.apiPath().format(node),
        method="GET",
        bypass_proxy=bypass_proxy,
        model=TextReturnModel,
        authorization=authorization,
    ).run()


def me_get_tunnel_config_id(
    authorization: str, id: int, bypass_proxy: bool = False
) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.tunnel_conf_id.apiPath().format(id),
        method="GET",
        bypass_proxy=bypass_proxy,
        model=TextReturnModel,
        authorization=authorization,
    ).run()


def me_create_tunnel(
    authorization: str,
    node: int,
    proxy_type: str,
    local_ip: str,
    local_port: int,
    remote_port: int,
    proxy_name: str,
    bypass_proxy: bool = False,
) -> JSONReturnModel:
    return AuthRequestModel(
        data={
            "node": node,
            "proxy_type": proxy_type,
            "local_ip": local_ip,
            "local_port": local_port,
            "remote_port": remote_port,
            "proxy_name": proxy_name,
        },
        url=AuthRouter.tunnel_create.apiPath(),
        method="POST",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_delete_tunnel(
    authorization: str, tunnel_id: int, bypass_proxy: bool = False
) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.tunnel_delete.apiPath().format(tunnel_id),
        method="POST",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_get_tunnel_info(
    authorization: str, tunnel_id: int, bypass_proxy: bool = False
) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.tunnel_info.apiPath().format(tunnel_id),
        method="GET",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()


def me_node_list(authorization: str, bypass_proxy: bool = False) -> JSONReturnModel:
    return AuthRequestModel(
        url=AuthRouter.node_list.apiPath(),
        method="GET",
        bypass_proxy=bypass_proxy,
        model=JSONReturnModel,
        authorization=authorization,
    ).run()

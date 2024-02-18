import random
import re
import string

import requests
from enum import Enum
from typing import Any, Dict, Optional, Union


class ProxyTypes(Enum):
    """代理类型枚举"""
    tcp = "tcp"
    udp = "udp"
    http = "http"
    https = "https"
    stcp = "stcp"
    xtcp = "xtcp"


def generate_random_string(length=10) -> str:
    """生成一个指定长度的随机字符串。

    默认长度是10。字符串包括大写字母、小写字母和数字。

    参数:
        length (int): 随机字符串的长度。默认是10。

    返回:
        str: 生成的随机字符串。
    """
    characters = string.ascii_letters + string.digits  # 包括大写字母、小写字母和数字
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def markdown_to_text(markdown):
    # 移除HTML标签
    text = re.sub(r'<[^>]+>', '', markdown)
    # 移除CSS样式
    text = re.sub(r'<style>.*?</style>', '', text, flags=re.DOTALL)
    # 移除CSS样式定义
    text = re.sub(r'\.?[a-zA-Z0-9\-_]+\s*\{[^}]*}', '', text)
    # 移除可能遗留的单独大括号
    text = re.sub(r'[{}]', '', text)
    # 移除代码块
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # 移除图片
    text = re.sub(r'!\[.*?]\(.*?\)', '', text)
    # 修改链接的处理方式，显示为“链接文本：原链接”
    text = re.sub(r'\[(.*?)]\((.*?)\)', r'\1: \2', text)
    # 移除加粗、斜体文本标记
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'__(.*?)__', r'\1', text)
    text = re.sub(r'_(.*?)_', r'\1', text)
    # 移除列表标记
    text = re.sub(r'\n\s*[*\-+](.*?)(\n|$)', r'\n\1\n', text)
    # 移除引用
    text = re.sub(r'\n\s*>.*', '', text)
    # 移除标题标记
    text = re.sub(r'\n#{1,6}\s*(.*?)\n', r'\n\1\n', text)
    # 移除多余的空行
    text = re.sub(r'\n\s*\n', '\n', text)
    return text.strip()


class OpenFrpAPI:
    def __init__(self, base_url: str = "https://api.openfrp.net",
                 oauth_url: str = "https://openid.17a.ink/api") -> None:
        """初始化OpenFrpAPI类"""
        self.base_url = base_url
        self.oauth_url = oauth_url
        self.headers: Dict[str, str] = {'Content-Type': "application/json"}
        self.session: str = ""
        self.info: str = ""
        self.code: str = ""
        self.proxy: Optional[Dict[str, str]] = None
        self.request: requests.Session = requests.Session()
        self.prefix: str = "lazyOfAPI_"

    def oauth_login_callback(self, username: str, password: str) -> bool:
        url = self.oauth_url + "/public/login"
        data = {"user": username, "password": password}
        response = self.request.post(url, json=data, proxies=self.proxy)
        result = response.json()
        return result.get("flag", False)

    def oauth_get_code(self) -> bool:
        url_get = self.base_url + "/oauth2/login"
        response_get_url = self.request.get(url_get, proxies=self.proxy)
        url = response_get_url.json().get("data").replace(".ink/", ".ink/api/")
        response = self.request.post(url, proxies=self.proxy)
        result = response.json()
        if result["flag"]:
            self.code = result.get("data").get("code")
            return True
        return False

    def oauth_code_login(self) -> bool:
        if self.code != "":
            url = self.base_url + f"/oauth2/callback?code={self.code}"
            response = self.request.post(url, proxies=self.proxy)
            result = response.json()
            if result["flag"]:
                self.headers['Authorization'] = response.headers['Authorization']
                self.session = result["data"]
                return True
            return False
        else:
            return False

    def login(self, username: str, password: str) -> bool:
        """用户登录"""
        self.oauth_login_callback(username, password)
        self.oauth_get_code()
        return self.oauth_code_login()

    def get_user_info(self) -> str:
        """获取用户信息"""
        if (self.headers == {} or
                "Authorization" not in self.headers.keys() or
                self.headers.get("Authorization") == "" or
                self.session == ""):
            return ""
        url = self.base_url + "/frp/api/getUserInfo"
        response = self.request.post(url, headers=self.headers, proxies=self.proxy)
        user_info = response.json()
        self.info = f"""
            用户名: {user_info.get("username", "获取失败")}
            用户注册ID: {user_info.get("id", "获取失败")}
            用户注册邮箱: {user_info.get("email", "获取失败")}
            是否已进行实名认证: {'已认证' if user_info.get("realname", False) else '未认证'}
            注册时间: {user_info.get("regtime", "获取失败")}
            用户组: {user_info.get("friendlyGroup", "获取失败")}
            用户密钥: {user_info.get("token", "获取失败")}
            上行带宽: {user_info.get("outLimit", "获取失败")} Kbps
            下行带宽: {user_info.get("inLimit", "获取失败")} Kbps
            剩余流量: {user_info.get("traffic", "获取失败")} Mib
            已用隧道: {user_info.get("used", "获取失败")} 条
            总共隧道条数: {user_info.get("proxies", "获取失败")} 条
        """
        return self.info

    def get_user_proxies(self) -> list:
        """获取用户隧道"""
        url = self.base_url + "/frp/api/getUserProxies"
        response = self.request.post(url, headers=self.headers, proxies=self.proxy)
        return list(response.json().get("data").get("list"))

    def new_proxy(self, node_id: int, name: str = "", protocol_type: Union[str, ProxyTypes] = ProxyTypes.tcp.value,
                  local_addr: str = "127.0.0.1", local_port: int = "25565", remote_port: int = 1000000,
                  encrypt: bool = False, compress: bool = False,
                  domain: str = "", route: str = "", host: str = "", request_from: str = "",
                  request_pass: str = "", custom: str = "") -> bool:
        """创建新隧道"""
        url = self.base_url + "/frp/api/newProxy"
        proxy_type = protocol_type.value if isinstance(protocol_type, Enum) else protocol_type

        if remote_port >= 1000000:
            while True:
                remote_port = random.randint(10000, 50000)
                if remote_port != 25565:
                    break

        if name == "":
            name = self.prefix
            name += proxy_type
            name += generate_random_string(22 - len(name))

        data = {
            "name": name,
            "node_id": node_id,
            "type": proxy_type,
            "local_addr": local_addr,
            "local_port": local_port,
            "remote_port": remote_port,
            "dataEncrypt": encrypt,
            "dataGzip": compress,
            "domain_bind": domain,
            "url_route": route,
            "host_rewrite": host,
            "request_from": request_from,
            "request_pass": request_pass,
            "custom": custom
        }
        response = self.request.post(url, json=data, headers=self.headers, proxies=self.proxy)
        return response.json().get("flag", False)

    def create_proxy(self, node_id: int, name: str = "", protocol_type: Union[str, ProxyTypes] = ProxyTypes.tcp.value,
                     local_addr: str = "127.0.0.1", local_port: int = "25565", remote_port: int = 1000000,
                     encrypt: bool = False, compress: bool = False,
                     domain: str = "", route: str = "", host: str = "", request_from: str = "",
                     request_pass: str = "", custom: str = "") -> Dict[str, str]:
        if name == "":
            name = "lazyOfAPI_"
            name += f"{protocol_type}_"
            name += generate_random_string(5)
        self.new_proxy(node_id, name, protocol_type, local_addr, local_port, remote_port, encrypt, compress,
                       domain, route, host, request_from, request_pass, custom)
        usr_proxies = self.get_user_proxies()
        for item in usr_proxies:
            if item.get("proxyName") == name:
                return item

    def remove_proxy(self, proxy_id: str) -> bool:
        """删除隧道"""
        url = self.base_url + "/frp/api/removeProxy"
        data = {"proxy_id": proxy_id}
        response = self.request.post(url, data=data, headers=self.headers, proxies=self.proxy)
        return response.json().get("flag", False)

    def get_node_list(self) -> list:
        """获取节点列表"""
        url = self.base_url + "/frp/api/getNodeList"
        response = self.request.post(url, headers=self.headers, proxies=self.proxy)
        return response.json().get("data").get("list")

    def edit_proxy(self, proxy_id: str, name: str = "", protocol_type: Union[str, ProxyTypes] = ProxyTypes.tcp.value,
                   local_addr: str = "127.0.0.1", local_port: int = "25565", remote_port: int = 1000000,
                   encrypt: bool = False, compress: bool = False,
                   domain: str = "", route: str = "", host: str = "", request_from: str = "",
                   request_pass: str = "", custom: str = "") -> bool:
        """编辑代理"""
        url = self.base_url + "/frp/api/editProxy"
        data = {
            "name": name,
            "proxy_id": proxy_id,
            "type": protocol_type,
            "local_addr": local_addr,
            "local_port": local_port,
            "remote_port": remote_port,
            "dataEncrypt": encrypt,
            "dataGzip": compress,
            "domain_bind": domain,
            "url_route": route,
            "host_rewrite": host,
            "request_from": request_from,
            "request_pass": request_pass,
            "custom": custom
        }
        response = self.request.post(url, data=data, headers=self.headers, proxies=self.proxy)
        return response.json().get("flag", False)

    def sign(self) -> Union[str, bool]:
        """用户签到"""
        url = self.base_url + "/frp/api/userSign"
        response = self.request.post(url, headers=self.headers, proxies=self.proxy)
        if response.json().get("flag", False):
            return response.json().get("flag", "签到成功!")
        else:
            return "签到失败"

    def announcement(self) -> str:
        url = self.base_url + "/commonQuery/get?key=web_broadcast"
        return self.request.get(url).json().get("data")

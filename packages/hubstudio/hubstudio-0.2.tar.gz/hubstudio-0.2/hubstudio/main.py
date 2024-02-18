import asyncio
import os
import asyncio.subprocess
import typing
import aiohttp
import re
import inflection
import psutil
from subprocess import CREATE_NO_WINDOW


class HubStudioException(Exception):
    ERROR_MAP = {
        0: "成功",
        5: "初始化代理失败",
        7: "启动内核失败",
        15: "获取openDetail参数失败",
        17: "容器正在被占用",
        18: "取消",
        20: "不可打开状态",
        21: "获取ip超时",
        22: "转换userAgent失败",
        24: "openDetail超时",
        25: "获取磁盘信息失败",
        26: "API免费版本不支持",
        27: "环境打开次数超过限制",
        -10000: "未知异常",
        -10003: "登录失败",
        -10004: "未找到环境信息，请检查环境ID是否正确",
        -10005: "该店铺上次请求的startBrowser还未执行结束",
        -10007: "内核不存在，请手动打开客户端下载",
        -10008: "系统资源不足",
        -10011: "环境不存在或未开启，请检查环境ID是否正确",
        -10012: "插件ID列表不能为空",
        -10013: "环境正在运行",
        -10014: "IPC超时",
        -10015: "数据获取失败，请勿过于频繁操作，或检查网络环境后重试。",
        -10016: "内核版本过低，本客户端不允许打开",
        -10017: "当前Firefox内核的环境无法通过API打开",
        -10018: "下载内核失败",
        # 自定义错误
        1000: "服务启动失败",
        1001: "服务关闭失败",
        1002: "请求异常",
        1003: "响应异常",
        1004: "端口被占用",
        1005: "端口配置错误"
    }

    def __init__(self, err_code: int, content=None):
        if err_code in self.ERROR_MAP:
            self.err_msg: str = self.ERROR_MAP[err_code]
        else:
            self.err_msg = "未知错误"
        self.err_code: int = err_code
        self.content = content

    def __str__(self):
        return f"<{self.err_code}>: {self.err_msg}"


class HubStudioServer:
    def __init__(
            self,
            port: int,
            line_setting: int = None,
            timeout: int = 600,
            remote_debugging: bool = False,
            app_id: str = None,
            app_secret: str = None,
            group_code: str = None,
            threads: int = 10,
            client_path: str = None,
            echo=True,
    ):
        self.http_port = port
        self.threads = threads
        self.line_setting = line_setting
        self.timeout = timeout
        self.remote_debugging = remote_debugging
        self.app_id = app_id
        self.app_secret = app_secret
        self.group_code = group_code
        self.client_path = client_path

        self.__service: typing.Optional[asyncio.subprocess.Process] = None
        self.echo = echo

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.run_async())
        asyncio.get_event_loop().run_until_complete(self.__service.wait())

    async def run_async(self):
        cmds = [
            "--server_mode", "http",
            "--http_port", str(self.http_port),
        ]
        if self.remote_debugging:
            cmds.append("--remote_debugging")
        if self.app_id and self.app_secret and self.group_code:
            cmds.extend([
                "--app_id", self.app_id,
                "--app_secret", self.app_secret,
                "--group_code", self.group_code,
            ])
        if self.line_setting:
            cmds.extend(["--line_setting", self.line_setting])
        if self.timeout:
            cmds.extend(["--timeout", str(self.timeout)])
        if self.threads:
            cmds.extend(["--threads", str(self.threads)])
        self.__service = await asyncio.subprocess.create_subprocess_exec(
            os.path.join(self.client_path, "hubstudio_connector.exe"),
            *cmds,
            stdout=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
            creationflags=CREATE_NO_WINDOW
        )
        is_port_in_use = False
        for proc in psutil.process_iter(['pid', 'name', 'connections']):
            try:
                # 遍历进程的所有网络连接
                for conn in proc.info['connections']:
                    # 检查端口号是否匹配
                    if conn.laddr.port == int(self.http_port):
                        is_port_in_use = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, IndexError):
                # 忽略无法访问的进程和没有网络连接的进程
                continue
        while True:
            stdout = await self.__service.stdout.readline()
            if not stdout:
                await asyncio.sleep(0.2)
                continue
            stdstr = stdout.decode().strip()
            if self.echo:
                print(stdstr)
            if re.match(r'Program started: +{"\d+":"hubstudio_connector.exe"', stdstr):
                # pid = int(re.search(r'{"(\d+)":"hubstudio_connector.exe"}', stdstr).group(1))
                break
            elif stdstr == 'Startup complete' and is_port_in_use:
                raise HubStudioException(1004)
            elif stdstr == 'Startup complete' and not is_port_in_use:
                break


class HubStudioClientAsync:
    EXECUTABLE_PATH = r"C:\Program Files\Hubstudio"

    def __init__(self, base_url: str):
        self.__base_url = base_url

    async def __request(self, url: str, payload=None, method: str = "POST"):
        if "self" in payload:
            del payload['self']
        payload = {inflection.camelize(k, False): v for k, v in payload.items()}
        try:

            async with aiohttp.request(
                    method=method,
                    url=f"{self.__base_url}{url}",
                    json=payload,
                    headers={"Content-Type": "application/json"}
            ) as response:
                if response.status != 200:
                    raise HubStudioException(1003)
                content = await response.json()
                if content['code'] == 0:
                    return content['data']
                else:
                    raise HubStudioException(content['code'])
        except Exception as e:
            if isinstance(e, HubStudioException):
                raise e
            else:
                raise HubStudioException(1002)

    async def login(self, app_id: str, app_secret: str, group_code: str):
        """
        帐号登录并打开客户端

        1. http模式需配合使用CLI命令行启动客户端，见【HTTP模式说明】
        2. 启动时已传入用户团队参数，可跳过此步骤
        3. 重新登录会重启客户端

        :param app_id: 用户凭证appId
        :param app_secret: 用户凭证appSecret
        :param group_code: 	团队id
        :return:
        """

        payload = locals()
        return await self.__request("/login", payload)

    async def quit(self):
        """
        退出并关闭客户端

        :return:
        """
        return await self.__request("/quit")

    async def start_browser(
            self,
            container_code: str,
            is_webdriver_read_only_mode: bool = False,
            skip_system_resource_check: bool = False,
            container_tabs: list[str] = None,
            args: list[str] = None
    ):
        """
        启动浏览器

        :param container_code: str, 环境ID
        :param is_webdriver_read_only_mode: bool, 是否只读模式，默认False
        :param skip_system_resource_check: bool, 默认False不跳过系统资源检测(仅支持v3.6.0及以上版本)
        :param container_tabs: list[str], 启动URL，可选
        :param args: list[str], 启动参数，可选
        :return: dict, 包含浏览器信息的字典
        """
        payload = locals()
        return await self.__request("/api/v1/browser/start", payload, method="POST")

    async def stop_browser(
            self,
            container_code: str
    ):
        """
        关闭环境

        :param container_code: str, 环境ID
        :return: dict, 包含操作信息的字典
        """
        payload = locals()
        return await self.__request("/api/v1/browser/stop", payload, method="POST")

    async def get_browser_status(
            self,
            container_codes: list[str]
    ):
        """
        获取浏览器状态

        :param container_codes: list[str], 环境ID列表
        :return: dict, 包含环境状态信息的字典
        """
        payload = locals()
        return await self.__request("/api/v1/browser/all-browser-status", payload, method="POST")

    async def switch_browser_window(
            self,
            container_code: str
    ):
        """
        切换浏览器窗口

        :param container_code: str, 环境ID
        :return: dict, 包含操作信息的字典
        """
        payload = locals()
        return await self.__request("/api/v1/browser/foreground", payload, method="POST")

    async def get_environment_list(
            self,
            container_codes: list = None,
            container_name: str = None,
            create_end_time: str = None,
            create_start_time: str = None,
            ip_address: str = None,
            proxy_type_names: list = None,
            remark: str = None,
            no_tag: int = None,
            tag_names: list = None,
            current: int = None,
            size: int = None,
            service_provider: str = None
    ):
        """
        获取环境列表

        :param container_codes: list, 指定环境ID查询环境
        :param container_name: str, 指定环境名称查询环境
        :param create_end_time: str, 创建时间-截止时间
        :param create_start_time: str, 创建时间-起始时间
        :param ip_address: str, IP地址查询
        :param proxy_type_names: list, 代理类型
        :param remark: str, 指定环境备注信息查询环境
        :param no_tag: int, 查询“未分组”的环境
        :param tag_names: list, 环境分组名称数组
        :param current: int, 分页第几页偏移量
        :param size: int, 分页条数，最多200条
        :param service_provider: str, 环境内代理所属服务商
        :return: JSON, 环境列表信息
        """
        payload = locals()
        return await self.__request("/api/v1/env/list", payload, method="POST")

    async def create_environment(
            self,
            container_name: str,
            as_dynamic_type: int,
            proxy_type_name: str,
            remark: str = None,
            tag_name: str = None,
            cookie: str = None,
            ip_get_rule_type: int = None,
            link_code: str = None,
            proxy_server: str = None,
            proxy_port: int = None,
            proxy_account: str = None,
            proxy_password: str = None,
            reference_country_code: str = None,
            reference_ip: str = None,
            reference_city: str = None,
            reference_region_code: str = None,
            ip_database_channel: int = None,
            ip_protocol_type: int = None,
            type: str = None,
            phone_model: str = None,
            browser: str = None,
            core_version: int = None,
            video_throttle: int = None,
            img_throttle: int = None,
            advanced_bo: dict = None
    ):
        """
        创建环境

        :param container_name: str, 环境名称
        :param as_dynamic_type: int, IP变更提醒方式
        :param proxy_type_name: str, 代理类型
        :param remark: str, 环境备注信息
        :param tag_name: str, 环境所属分组名称
        :param cookie: str, JSON格式的cookie
        :param ip_get_rule_type: int, IP提取方式
        :param link_code: str, 提取链接
        :param proxy_server: str, 代理主机
        :param proxy_port: int, 代理端口
        :param proxy_account: str, 代理账号
        :param proxy_password: str, 代理密码
        :param reference_country_code: str, 环境内账号需要登录的指定的国家
        :param reference_ip: str, 根据IP自动填充环境内账号需要登录的指定的国家
        :param reference_city: str, 参考城市
        :param reference_region_code: str, 参考州
        :param ip_database_channel: int, 代理查询渠道
        :param ip_protocol_type: int, IP协议选项
        :param type: str, 操作系统参数
        :param phone_model: str, 手机型号
        :param browser: str, 浏览器类型
        :param core_version: int, 内核版本号
        :param video_throttle: int, 视频限流
        :param img_throttle: int, 图片限流
        :param advanced_bo: dict, 高级指纹参数配置
        :return: JSON, 创建后的环境信息
        """
        payload = locals()
        return await self.__request("/api/v1/env/create", payload, method="POST")

    async def update_environment(
            self,
            container_code: int,
            container_name: str,
            core_version: int,
            remark: str = None,
            tag_name: str = None,
            video_throttle: int = None,
            img_throttle: int = None,
            advanced_bo: dict = None
    ):
        """
        更新环境

        :param container_code: int, 环境ID
        :param container_name: str, 环境名称
        :param core_version: int, 内核版本号
        :param remark: str, 环境备注信息
        :param tag_name: str, 环境所属分组信息
        :param video_throttle: int, 视频限流
        :param img_throttle: int, 图片限流
        :param advanced_bo: dict, 高级指纹参数配置
        :return: bool, 更新成功与否
        """
        payload = locals()
        return await self.__request("/api/v1/env/update", payload, method="POST")

    async def update_environment_proxy(
            self,
            container_code: int,
            as_dynamic_type: int,
            proxy_type_name: str,
            ip_get_rule_type: int = None,
            link_code: str = None,
            proxy_host: str = None,
            proxy_port: int = None,
            proxy_account: str = None,
            proxy_password: str = None,
            reference_country_code: str = None,
            reference_ip: str = None,
            reference_city: str = None,
            reference_region_code: str = None,
            ip_database_channel: int = None,
            ip_protocol_type: int = None
    ):
        """
        更新环境代理

        :param container_code: int, 环境ID
        :param as_dynamic_type: int, IP使用方式
        :param proxy_type_name: str, 代理类型
        :param ip_get_rule_type: int, IP提取方式
        :param link_code: str, 提取链接
        :param proxy_host: str, 代理主机
        :param proxy_port: int, 代理端口
        :param proxy_account: str, 代理账号
        :param proxy_password: str, 代理密码
        :param reference_country_code: str, 环境内账号需要登录的指定的国家
        :param reference_ip: str, 根据IP自动填充环境内账号需要登录的指定的国家
        :param reference_city: str, 参考城市
        :param reference_region_code: str, 参考州
        :param ip_database_channel: int, 代理查询渠道
        :param ip_protocol_type: int, IP协议选项
        :return: bool, 更新成功与否
        """
        payload = locals()
        return await self.__request("/api/v1/env/proxy/update", payload, method="POST")

    async def delete_environment(
            self,
            container_codes: list[int]
    ):
        """
        删除环境

        :param container_codes: list[int], 环境ID列表
        :return: bool, 删除成功与否
        """
        payload = locals()
        return await self.__request("/api/v1/env/del", payload, method="POST")

    async def import_cookie(
            self,
            container_code: int,
            cookie: str
    ):
        """
        导入Cookie

        :param container_code: int, 环境ID
        :param cookie: str, JSON格式的cookie字符串
        :return: bool, 导入成功与否
        """
        payload = locals()
        return await self.__request("/api/v1/env/import-cookie", payload, method="POST")

    async def export_cookie(
            self,
            container_code: int
    ):
        """
        导出Cookie

        :param container_code: int, 环境ID
        :return: str, Cookie的JSON串
        """
        payload = locals()
        return await self.__request("/api/v1/env/export-cookie", payload, method="POST")

    async def get_random_ua(
            self,
            type: str = None,
            phone_model: str = None,
            version: list[int] = None
    ):
        """
        获取随机UA

        :param type: str, 操作系统参数
        :param phone_model: str, 手机型号
        :param version: list[int], 浏览器版本数组
        :return: str, 随机UA字符串
        """
        payload = locals()
        return await self.__request("/api/v1/env/random-ua", payload, method="POST")

    async def clear_environment_cache(
            self,
            browser_oauths: list[str] = None
    ):
        """
        清除环境本地缓存

        :param browser_oauths: list[str], 浏览器OAuth ID列表
        :return: JSON, 操作结果
        """
        payload = locals()
        return await self.__request("/api/v1/cache/clear", payload, method="POST")

    async def reset_environment_extension(
            self,
            browser_oauth: str,
            plugin_ids: list[str]
    ):
        """
        清理环境内插件缓存

        :param browser_oauth: str, 浏览器OAuth ID
        :param plugin_ids: list[str], 插件ID列表
        :return: JSON, 操作结果
        """
        payload = locals()
        return await self.__request("/api/v1/browser/reset-extension", payload, method="POST")

    async def download_environment_core(
            self,
            cores: list[dict]
    ):
        """
        下载环境内核

        :param cores: list[dict], 内核信息列表，每个字典包含浏览器内核类型和版本
        :return: JSON, 操作结果
        """
        payload = locals()
        return await self.__request("/api/v1/browser/download-core", payload, method="POST")

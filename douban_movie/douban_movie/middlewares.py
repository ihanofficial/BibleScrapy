import random


class RandomUserAgentMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings.get('USER_AGENT_LIST'))
        return o

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)


class ProxyMiddleware:
    def process_request(self, request, spider):
        # 这里可以添加代理IP配置
        # request.meta['proxy'] = "http://your_proxy_ip:port"
        pass

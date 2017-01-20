#coding:utf8
from scrapy.utils.project import get_project_settings
import random
settings = get_project_settings()

class ProcessHeaderMidware(object):
    
    def process_request(self, request, spider):
        ua = random.choice(settings.get('USER_AGENT_LIST'))
        spider.logger.info(msg='now entring download midware')
        if ua:
            request.headers['User-Agent'] = ua
            spider.logger.info(
                'User-Agent is : {} {}'.format(request.headers.get('User-Agent'), request)
            )

    
import urllib.parse

from celerabitpipelineintegration.util_configuration import Configuration
from celerabitpipelineintegration.util_http import get_error_from_response
from celerabitpipelineintegration.util_http_client import HttpClient
from celerabitpipelineintegration.util_logger import print_debug, print_info


class ScenarioStatus:

    __client_name__:str
    __application_name__:str
    __scenario_code__:str
    __token__:str

    def __init__(self, 
                client_name:str, \
                application_name:str, \
                scenario_code:str, \
                token:str
                ) -> None:
        self.__client_name__ = client_name
        self.__application_name__ = application_name
        self.__scenario_code__ = scenario_code
        self.__token__ = token

    def get_last_job(self) -> dict:
        print_info('Getting last job for scenario "{}" ...'.format(self.__scenario_code__))
        url:str = Configuration.instance().get_config_value('CELERABIT-ENDPOINTS', 'get-scenario-last-status')
        url = url.format( \
                    client = urllib.parse.quote(self.__client_name__), \
                    application = urllib.parse.quote(self.__application_name__), \
                    scenario = urllib.parse.quote(self.__scenario_code__) \
                    )
        print_debug('Status url: {}'.format(url))

        http_client:HttpClient = HttpClient(self.__token__)
        response:any = http_client.get(url)

        if response.status_code != 200:
            raise Exception(get_error_from_response(response))

        job_info:any = response.json()
        return job_info
# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/8 22:44
# File Name:         handler.py
from asyncio import create_task, gather

from .mode import Mode
from .request import Request
from aiohttp import ClientSession


class Handler:
    """
    This class is for:

    - Create an aiohttp session and execute requests
    - Parse the JSON and instantiate the appropriate object
    """

    @staticmethod
    async def get_request_data_with_url(session: ClientSession, url: str) -> dict:
        """
        Gets data dict with provided url.

        :param url: url of api
        :param session ClientSession
        :return api response dict from json
        """
        response = await session.request(method="GET", url=url)
        json_dict = await response.json()
        return json_dict

    @staticmethod
    async def get_request_data(request: Request, session: ClientSession) -> dict:
        """
        An async coroutine that executes GET http request. The response is
        converted to a json. The HTTP request and the json conversion are
        asynchronous processes that need to be awaited.

        :param session: ClientSession
        :param request Request from command line
        :return api response dict from json
        """
        try:
            url = "https://pokeapi.co/api/v2/"

            if request.mode == Mode.POKEMON:
                mode = "pokemon/"
            elif request.mode == Mode.MOVE:
                mode = "move/"
            elif request.mode == Mode.ABILITY:
                mode = "ability/"
            else:
                mode = "stat/"

            url = url + mode + request.input_data
            response = await session.request(method="GET", url=url)
            json_dict = await response.json()
            json_dict["is_expanded"] = request.expanded
            return json_dict

        except Exception as e:
            return {"error": e}

    @staticmethod
    async def process_single_request_task(requests: Request) -> tuple:
        """
        Process Single Request.

        :param requests Request from command line
        :return api response dict from json
        """
        async with ClientSession() as session:
            task = create_task(Handler.get_request_data(requests, session))
            response = await task
            return response

    @staticmethod
    def map_request_file_into_multiple_requests(request: Request) -> list[Request]:
        """
        Reads the input file, and maps the request into multiple requests as a list.

        :param request Request from command line
        :return a bunch of request that contains single input data
        """
        request_list = []
        try:
            with open(request.input_file, "r") as file_object:
                for line in file_object.read().splitlines():
                    single_request = Request()
                    single_request.input_data = line
                    single_request.mode = request.mode
                    single_request.output = request.output
                    single_request.expanded = request.expanded

                    request_list.append(single_request)
                return request_list

        # If the File is not existed
        except FileNotFoundError as e:
            print("Error: ", e)
            exit(-1)

    @staticmethod
    async def process_multiple_request_tasks(requests: Request) -> tuple:
        """
        Process multiple requests.

        :param requests Request from command line
        :return api response dict from json
        """
        requests_list = Handler.map_request_file_into_multiple_requests(requests)

        async with ClientSession() as session:
            list_tasks = [create_task(Handler.get_request_data(request, session)) for request in requests_list]
            response = await gather(*list_tasks)
            return response

    @staticmethod
    async def process_request_tasks_with_default_urls(default_url: list[str]) -> tuple:
        """
        Process Request.

        :param default_url url of api
        :return api response dicts from json into a tuple
        """
        async with ClientSession() as session:
            list_tasks = [create_task(Handler.get_request_data_with_url(session, request))
                          for request in default_url]
            response = await gather(*list_tasks)
            return response

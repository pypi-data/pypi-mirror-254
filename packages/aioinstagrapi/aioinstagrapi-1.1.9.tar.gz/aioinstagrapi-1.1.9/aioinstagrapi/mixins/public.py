import json
import logging
import time
import httpx
import asyncio
from aioinstagrapi.utils import *
from json.decoder import JSONDecodeError



from aioinstagrapi.exceptions import (
    ClientUnauthorizedError,
    ClientBadRequestError,
    ClientConnectionError,
    ClientError,
    ClientForbiddenError,
    ClientGraphqlError,
    ClientIncompleteReadError,
    ClientJSONDecodeError,
    ClientLoginRequired,
    ClientNotFoundError,
    ClientThrottledError,
)



class PublicRequestMixin:
    public_requests_count = 0
    PUBLIC_API_URL = "https://www.instagram.com/"
    GRAPHQL_PUBLIC_API_URL = "https://www.instagram.com/graphql/query/"
    last_public_response = None
    last_public_json = {}
    public_cookies = {}
    public_request_logger = logging.getLogger("public_request")
    request_timeout = 1
    last_response_ts = 0
    public_base_headers = {
                "Connection": "Keep-Alive",
                "Accept": "*/*",
                "Accept-Encoding": "gzip,deflate",
                "Accept-Language": "en-US",
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 "
                    "(KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
                ),
            }

    def __init__(self, *args, **kwargs):
        self.request_timeout = kwargs.pop("request_timeout", self.request_timeout)
        super().__init__(*args, **kwargs)

    async def small_delay(self):
        await asyncio.sleep(random.uniform(0.75, 3.75))

    async def very_small_delay(self):
        await asyncio.sleep(random.uniform(0.175, 0.875))
    
    async def random_delay(self):
        delay_function = random.choice([self.small_delay, self.very_small_delay])
        await delay_function()

    async def public_request(
        self,
        url,
        data=None,
        params=None,
        headers=None,
        return_json=False,
        retries_count=1,
        retries_timeout=2,
    ):
        kwargs = dict(
            data=data,
            params=params,
            headers=headers,
            return_json=return_json,
        )
        assert retries_count <= 10, "Retries count is too high"
        assert retries_timeout <= 600, "Retries timeout is too high"
        for iteration in range(retries_count):
            try:
                await self.random_delay()
                return await self._send_public_request(url, **kwargs)
            except (
                ClientLoginRequired,
                ClientNotFoundError,
                ClientBadRequestError,
            ) as e:
                raise e  # Stop retries
            # except JSONDecodeError as e:
            #     raise ClientJSONDecodeError(e, respones=self.last_public_response)
            except ClientError as e:
                msg = str(e)
                if all(
                    (
                        isinstance(e, ClientConnectionError),
                        "SOCKSHTTPSConnectionPool" in msg,
                        "Max retries exceeded with url" in msg,
                        "Failed to establish a new connection" in msg,
                    )
                ):
                    raise e
                if retries_count > iteration + 1:
                    await asyncio.sleep(retries_timeout)
                else:
                    raise e
                continue

    async def _send_public_request(
        self, url, data=None, params=None, headers=None, return_json=False
    ):
        self.public_requests_count += 1
        _headers = self.public_base_headers
        if headers:
            _headers.update(headers)
        if self.last_response_ts and (time.time() - self.last_response_ts) < 1.0:
            await asyncio.sleep(1.0)
        if self.request_timeout:
            await asyncio.sleep(self.request_timeout)
        try:
            async with httpx.AsyncClient(
                    proxies=self.proxies, 
                    headers=_headers, 
                    cookies=self.public_cookies,
                    verify=False,
                    timeout=httpx.Timeout(None, connect=15),
                ) as client:
                if data is not None:  # POST
                        response = await client.post(
                        url, data=data, params=params,
                        )
                else:  # GET
                    response = await client.get(
                        url, params=params, 
                )

            expected_length = int(response.headers.get("Content-Length") or 0)
            actual_length = len(response.content)
            if actual_length < expected_length:
                raise ClientIncompleteReadError(
                    "Incomplete read ({} bytes read, {} more expected)".format(
                        actual_length, expected_length
                    ),
                    response=response,
                )

            self.public_request_logger.debug(
                "public_request %s: %s", response.status_code, response.url
            )

            self.public_request_logger.info(
                "[%s] [%s] %s %s",
                self.proxies.get("https://"),
                response.status_code,
                "POST" if data else "GET",
                response.url,
            )
            self.last_public_response = response
            response.raise_for_status()
            if return_json:
                self.last_public_json = response.json()
                return self.last_public_json
            return response.text

        except JSONDecodeError as e:
            if "/login/" in response.url:
                raise ClientLoginRequired(e, response=response)

            self.public_request_logger.error(
                "Status %s: JSONDecodeError in public_request (url=%s) >>> %s",
                response.status_code,
                response.url,
                response.text,
            )
            raise ClientJSONDecodeError(
                "JSONDecodeError {0!s} while opening {1!s}".format(e, url),
                response=response,
            )
        except httpx.HTTPError as e:
            if self.last_public_response.status_code == 401:
                # HTTPError: 401 Client Error: Unauthorized for url: https://i.instagram.com/api/v1/users....
                raise ClientUnauthorizedError(e, response=self.last_public_response)
            elif self.last_public_response.status_code == 403:
                raise ClientForbiddenError(e, response=self.last_public_response)
            elif self.last_public_response.status_code == 400:
                raise ClientBadRequestError(e, response=self.last_public_response)
            elif self.last_public_response.status_code == 429:
                raise ClientThrottledError(e, response=self.last_public_response)
            elif self.last_public_response.status_code == 404:
                raise ClientNotFoundError(e, response=self.last_public_response)
            raise ClientError(e, response=self.last_public_response)

        except httpx.ConnectError as e:
            raise ClientConnectionError("{} {}".format(e.__class__.__name__, str(e)))
        finally:
            self.last_response_ts = time.time()

    async def public_a1_request(self, endpoint, data=None, params=None, headers=None):
        url = self.PUBLIC_API_URL + endpoint.lstrip("/")
        params = params or {}
        params.update({"__a": 1, "__d": "dis"})

        response = await self.public_request(
            url, data=data, params=params, headers=headers, return_json=True
        )
        return response.get("graphql") or response

    async def public_graphql_request(
        self,
        variables,
        query_hash=None,
        query_id=None,
        data=None,
        params=None,
        headers=None,
    ):
        assert query_id or query_hash, "Must provide valid one of: query_id, query_hash"
        default_params = {"variables": json.dumps(variables, separators=(",", ":"))}
        if query_id:
            default_params["query_id"] = query_id

        if query_hash:
            default_params["query_hash"] = query_hash

        if params:
            params.update(default_params)
        else:
            params = default_params

        try:
            body_json = await self.public_request(
                self.GRAPHQL_PUBLIC_API_URL,
                data=data,
                params=params,
                headers=headers,
                return_json=True,
            )

            if body_json.get("status", None) != "ok":
                raise ClientGraphqlError(
                    "Unexpected status '{}' in response. Message: '{}'".format(
                        body_json.get("status", None), body_json.get("message", None)
                    ),
                    response=body_json,
                )

            return body_json["data"]

        except ClientBadRequestError as e:
            message = None
            try:
                body_json = e.response.json()
                message = body_json.get("message", None)
            except JSONDecodeError:
                pass
            raise ClientGraphqlError(
                "Error: '{}'. Message: '{}'".format(e, message), response=self.last_public_response.text
            )


class TopSearchesPublicMixin:
    async def top_search(self, query):
        """Anonymous IG search request"""
        url = "https://www.instagram.com/web/search/topsearch/"
        params = {
            "context": "blended",
            "query": query,
            "rank_token": 0.7763938004511706,
            "include_reel": "true",
        }
        response = await self.public_request(url, params=params, return_json=True)
        return response


class ProfilePublicMixin:
    async def location_feed(self, location_id, count=16, end_cursor=None):
        if count > 50:
            raise ValueError("Count cannot be greater than 50")
        variables = {
            "id": location_id,
            "first": int(count),
        }
        if end_cursor:
            variables["after"] = end_cursor
        data = await self.public_graphql_request(
            variables, query_hash="1b84447a4d8b6d6d0426fefb34514485"
        )
        return data["location"]

    async def profile_related_info(self, profile_id):
        variables = {
            "user_id": profile_id,
            "include_chaining": True,
            "include_reel": True,
            "include_suggested_users": True,
            "include_logged_out_extras": True,
            "include_highlight_reels": True,
            "include_related_profiles": True,
        }
        data = await self.public_graphql_request(
            variables, query_hash="e74d51c10ecc0fe6250a295b9bb9db74"
        )
        return data["user"]

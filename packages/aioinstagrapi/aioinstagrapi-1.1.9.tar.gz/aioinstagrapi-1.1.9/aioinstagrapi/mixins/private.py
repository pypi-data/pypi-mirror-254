import json
import logging
import random
import time
import httpx
import traceback
import asyncio
import ssl
from urllib.parse import urlparse
from httpx import Timeout
from json.decoder import JSONDecodeError
from aioconsole import ainput
from aioinstagrapi.utils import *
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_random



from aioinstagrapi import config
from aioinstagrapi.exceptions import (
    BadPassword,
    ScrapingBlock,
    InternalServerError,
    GenericComments,
    ClientSuspended,
    ClientNoGifPermissions,
    ChallengeRequired,
    ClientBadRequestError,
    ClientConnectionError,
    ClientError,
    ClientForbiddenError,
    PrivateAccount,
    CommentsDisabledError,
    UserNotFound,
    ProxyAddressIsBlocked,
    InvalidTargetUser,
    InvalidMediaId,
    MediaUnavailable,
    ClientJSONDecodeError,
    ClientNotFoundError,
    ClientRequestTimeout,
    ClientThrottledError,
    FeedbackRequired,
    LoginRequired,
    PleaseWaitFewMinutes,
    RateLimitError,
    SentryBlock,
    TwoFactorRequired,
    UnknownError,
    VideoTooLongException,
)
from aioinstagrapi.utils import dumps, generate_signature

class Response:
    status_code : int
    text : str
    json : dict


async def manual_input_code(self, username: str, choice=None):
    """
    Manual security code helper

    Parameters
    ----------
    username: str
        User name of a Instagram account
    choice: optional
        Whether sms or email

    Returns
    -------
    str
        Code
    """
    code = None
    while True:
        code = (await ainput(f"Enter code (6 digits) for {username} ({choice}): ")).strip()
        if code and code.isdigit():
            break
    return code # is not int, because it can start from 0


async def manual_change_password(self, username: str):
    pwd = None
    while not pwd:
        pwd = await ainput(f"Enter password for {username}: ")
    return pwd.strip()


class PrivateRequestMixin:
    """
    Helpers for private request
    """

    private_requests_count = 0
    handle_exception = None
    challenge_code_handler = manual_input_code
    change_password_handler = manual_change_password
    private_request_logger = logging.getLogger("private_request")
    request_timeout = 5
    domain = config.API_DOMAIN
    last_response = None
    last_json = {}
    proxies = {}
    cookies = {}


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

    def set_proxy(self, dsn : str = None):
        if dsn:
            assert isinstance(
                dsn, str
            ), f'Proxy must been string (URL), but now "{dsn}" ({type(dsn)})'
            self.proxy = dsn
            proxy_href = "{scheme}{href}".format(
                scheme="http://" if not urlparse(self.proxy).scheme else "",
                href=self.proxy,
            )
            self.proxies = {
                "http://": proxy_href,
                "https://": proxy_href,
            }
            #input(self.proxies)
            return True
        self.proxies = {}
        return False

    @property
    def base_headers_old(self):
        locale = self.locale.replace("-", "_")
        accept_language = ["en-US"]
        if locale:
            lang = locale.replace("_", "-")
            if lang not in accept_language:
                accept_language.insert(0, lang)
        headers = {
            "X-IG-App-Locale": locale,
            "X-IG-Device-Locale": locale,
            "X-IG-Mapped-Locale": locale,
            'X-Fb-Connection-Type': 'WIFI',
            "X-Pigeon-Session-Id": generate_uuid("UFS-", "-1"),
            "X-Pigeon-Rawclienttime": str(round(time.time(), 3)),
            "X-IG-Bandwidth-Speed-KBPS": str(
                random.randint(2500000, 3000000) / 1000
            ),  # "-1.000"
            "X-IG-Bandwidth-TotalBytes-B": str(
                random.randint(5000000, 90000000)
            ),  # "0"
            "X-IG-Bandwidth-TotalTime-MS": str(random.randint(2000, 9000)),  # "0"
            "X-IG-App-Startup-Country": self.country.upper(),
            "X-Bloks-Version-Id": self.bloks_versioning_id,
            "X-IG-WWW-Claim": "0",
            "X-Bloks-Is-Layout-RTL": "false",
            "X-Bloks-Is-Panorama-Enabled": "true",
            "X-IG-Device-ID": self.uuid,
            "X-IG-Family-Device-ID": self.phone_id,
            "X-IG-Android-ID": self.android_device_id,
            "X-IG-Timezone-Offset": str(self.timezone_offset),
            "X-IG-Connection-Type": "WIFI",
            "X-IG-Capabilities": "3brTvx0=",  
            "X-IG-App-ID": self.app_id,
            "Priority": "u=3",
            "User-Agent": self.user_agent,
            "Accept-Language": ", ".join(accept_language),
            "X-MID": self.mid or "0",  
            "Accept-Encoding": "gzip, deflate", 
            "Host": self.domain,
            "X-FB-HTTP-Engine": "Liger",
            "Connection": "keep-alive",
            # "Pragma": "no-cache",
            # "Cache-Control": "no-cache",
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            "IG-INTENDED-USER-ID": '0',
            "X-IG-Nav-Chain": "9MV:self_profile:2,ProfileMediaTabFragment:self_profile:3,9Xf:self_following:4",
            "X-IG-SALT-IDS": str(random.randint(1061162222, 1061262222)),
        }
        if self.user_id:
            next_year = time.time() + 31536000  # + 1 year in seconds
            headers.update(
                {
                    
                    "IG-U-DS-USER-ID": str(self.user_id),
                    "IG-INTENDED-USER-ID": str(self.user_id ),
                    # Direct:
                    "IG-U-IG-DIRECT-REGION-HINT": (
                        f"LLA,{self.user_id},{next_year}:"
                        "01f7bae7d8b131877d8e0ae1493252280d72f6d0d554447cb1dc9049b6b2c507c08605b7"
                    ),
                    "IG-U-SHBID": (
                        f"12695,{self.user_id},{next_year}:"
                        "01f778d9c9f7546cf3722578fbf9b85143cd6e5132723e5c93f40f55ca0459c8ef8a0d9f"
                    ),
                    "IG-U-SHBTS": (
                        f"{int(time.time())},{self.user_id},{next_year}:"
                        "01f7ace11925d0388080078d0282b75b8059844855da27e23c90a362270fddfb3fae7e28"
                    ),
                    "IG-U-RUR": (
                        f"RVA,{self.user_id},{next_year}:"
                        "01f7f627f9ae4ce2874b2e04463efdb184340968b1b006fa88cb4cc69a942a04201e544c"
                    ),
                }
            )
        if self.authorization_data:    
            headers.update({"Authorization": self.authorization})
        if self.ig_u_rur:
            headers.update({"IG-U-RUR": self.ig_u_rur})
        if self.ig_www_claim:
            headers.update({"X-IG-WWW-Claim": self.ig_www_claim})
        return headers


    @property
    def base_headers(self):
        locale = self.locale.replace("-", "_")
        accept_language = ["en-US"]
        if locale:
            lang = locale.replace("_", "-")
            if lang not in accept_language:
                accept_language.insert(0, lang)
        headers = {
            'Host': 'i.instagram.com',
            'X-Ig-App-Locale': locale,
            'X-Ig-Device-Locale': locale,
            "X-MID": self.mid or "0",  
            'X-Ig-Mapped-Locale': locale,
            'X-Pigeon-Session-Id': generate_uuid("UFS-", "-1"),
            'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),
            "X-IG-Bandwidth-Speed-KBPS": str(
                random.randint(2500000, 3000000) / 1000
            ),  # "-1.000"
            "X-IG-Bandwidth-TotalBytes-B": str(
                random.randint(5000000, 90000000)
            ),  # "0"
            "X-IG-Bandwidth-TotalTime-MS": str(random.randint(2000, 9000)),
            'X-Bloks-Version-Id': self.bloks_versioning_id,
            'X-Ig-Www-Claim': '0',
            'X-Bloks-Is-Prism-Enabled': 'false',
            'X-Bloks-Is-Layout-Rtl': 'false',
            "X-IG-Device-ID": self.uuid,
            "X-IG-Family-Device-ID": self.phone_id,
            "X-IG-Android-ID": self.android_device_id,
            "X-IG-Timezone-Offset": str(self.timezone_offset),
            'X-Fb-Connection-Type': 'WIFI',
            'X-Ig-Connection-Type': 'WIFI',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': self.app_id,
            'Priority': 'u=3',
            'User-Agent': 'Instagram 313.0.0.0.60 Android (29/10; 420dpi; 1080x2104; samsung; SM-G715U; xcoverpro; exynos9611; en_US; 547897021)',
            'Accept-Language': 'en-US',
            'Ig-Intended-User-Id': '0',
            #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Content-Length': '134',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
        }
        if self.user_id:
            next_year = int(time.time() + 31535100) # + 1 year in seconds
            old = {
                "Ig-U-Ig-Direct-Region-Hint": (
                        f"RVA,{self.user_id},{next_year}:"
                        "01f70acfd56749fd883ea00d5e4063a506d77c0f6e7c170ef1f7c04212dd60fa992b27f7"
                    ),
                    "Ig-U-Shbid": (
                        f"12695,{self.user_id},{next_year}:"
                        "01f77b9eb29aa76cda03bebc81353efcd8e338a8abdebbacb6743f30fe02b2220d2438c4"
                    ),
                    "Ig-U-Shbts": (
                        f"{int(time.time())},{self.user_id},{next_year}:"
                        "01f777dfb5dc99c772be1bdcca77f292a860849f8d32f6f34ea0a2e93b6ad25c9233e25e"
                    ),
                    "Ig-U-Rur": (
                        f"EAG,{self.user_id},{next_year}:"
                        "01f73db7bda21deee42ce3b60099a5c6898c006a5fe613acb1ae9763ed17263a96be9a9f"
                    ),
            }
            headers.update(
                {
                    #"X-Ig-Nav-Chain": "9MV:self_profile:2,ProfileMediaTabFragment:self_profile:3,9Xf:self_following:4",
                    "Ig-U-Ds-User-Id": str(self.user_id),
                    "Ig-Intended-User-Id": str(self.user_id ),
                    
                    # Direct:
                    
                }
            )
        if self.authorization_data:    
            headers.update({"Authorization": self.authorization})
        if self.ig_u_rur:
            headers.update({"Ig-U-Rur": self.ig_u_rur})
        if self.ig_www_claim:
            headers.update({"X-Ig-Www-Claim": self.ig_www_claim})
        if self.shbid:
            headers.update({"Ig-U-Shbid": self.shbid})
        if self.shbts:
            headers.update({"Ig-U-Shbts": self.shbts})
        if self.region_hint:
            headers.update({"Ig-U-Ig-Direct-Region-Hint": self.region_hint})
        return headers

  
    
    @staticmethod
    def with_query_params(data, params):
        return dict(data, **{"query_params": json.dumps(params, separators=(",", ":"))})

    def set_response_cookies(self, response : httpx.Response):
        #MAKE SETTERS
        mid = response.headers.get("ig-set-x-mid")
        if mid:
            self.mid = mid  
            self.credentials.mid = mid
        rur = response.headers.get("ig-set-ig-u-rur")
        if rur:
            self.ig_u_rur = rur
            self.credentials.ig_u_rur = rur
        claim = response.headers.get("x-ig-set-www-claim")  
        if claim:
            self.ig_www_claim = claim
            self.credentials.ig_www_claim = self.ig_www_claim
        shbts = response.headers.get("ig-set-ig-u-shbts")
        if shbts:
            self.credentials.shbts = shbts
            self.shbts = shbts
        shbid = response.headers.get("ig-set-ig-u-shbid")    
        if shbid:
            self.credentials.shbid = shbid
            self.shbid = shbid  
        region_hint = response.headers.get("ig-set-ig-u-ig-direct-region-hint")  
        if region_hint:
            self.credentials.region_hint = region_hint
            self.region_hint = region_hint
        authorization = response.headers.get('ig-set-authorization')
        if authorization:
            ...
            #self.authorization_data = self.parse_authorization(authorization)
    @retry(retry=retry_if_exception_type((httpx.TimeoutException, ssl.SSLSyscallError,httpx.ConnectError)), stop=stop_after_attempt(10), wait=wait_random(1,3))
    async def _send_private_request(
        self,
        endpoint='',
        data=None,
        params=None,
        login=False,
        with_signature=True,
        headers=None,
        extra_sig=None,
        domain: str = None,
    ):
        self.last_response = None
        self.last_json = last_json = {}
        req_headers = (self.base_headers)
        if headers:
            req_headers.update(headers)
        if not login:
            await asyncio.sleep(self.request_timeout)
        # if self.user_id and login:
        #     raise Exception(f"User already logged ({self.user_id})")
        try:
            if not endpoint.startswith("/"):
                endpoint = f"/v1/{endpoint}"

            if endpoint == "/challenge/":  # wow so hard, is it safe tho?
                endpoint = "/v1/challenge/"

            api_url = domain or f"https://{domain or config.API_DOMAIN}/api{endpoint}"
            self.logger.info(api_url)
            if data:  # POST
                # Client.direct_answer raw dict
                # data = json.dumps(data)
                req_headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
                async with httpx.AsyncClient(
                    proxies=self.proxies, 
                    headers=req_headers, 
                    cookies=self.cookies
                ) as client:
                
                    if with_signature:
                        # Client.direct_answer doesn't need a signature
                        data = generate_signature(dumps(data))
                        if extra_sig:
                            data += "&".join(extra_sig)
                    tries = 0
                    while tries < 50:
                        try:
                            response = await client.post(
                                url=api_url, data=data, params=params, timeout=15
                            )
                            break
                        except Exception as e:
                            print(traceback.format_exc())
            else:  # GET
                async with httpx.AsyncClient(
                    proxies=self.proxies, 
                    headers=req_headers, 
                    cookies=self.cookies
                ) as client:
                    tries = 0
                    while tries < 50:
                        try:
                            response = await client.get(
                                url=api_url, params=params, timeout=15
                            )
                            break
                        except Exception as e:
                            print(traceback.format_exc())
            self.logger.debug(
                "private_request %s: %s (%s)",
                response.status_code,
                response.url,
                response.text,
            )
            self.set_response_cookies(response)
            self.request_log(response)
            self.last_response = response
            response.raise_for_status()
            self.last_json = last_json = response.json()
            self.logger.debug("last_json %s", last_json)
        except JSONDecodeError as e:
            self.logger.error(
                "Status %s: JSONDecodeError in private_request (user_id=%s, endpoint=%s) >>> %s",
                response.status_code,
                self.user_id,
                endpoint,
                response.text,
            )
            raise ClientJSONDecodeError(
                "JSONDecodeError {0!s} while opening {1!s}".format(e, response.url),
                response=response,
            )
        except (httpx.HTTPError, httpx.HTTPStatusError) as e:
            try:
                self.last_json = last_json = response.json()
            except:
                pass
            message = last_json.get("message", "")
            text = str(last_json)
            if "don't have permission to post a GIF" in text:
                raise ClientNoGifPermissions(e, response=e.response, **last_json)
            if "Please wait a few minutes" in message:
                raise PleaseWaitFewMinutes(e, response=e.response, **last_json)
            if "https://www.instagram.com/accounts/suspended/" in text:
                raise ClientSuspended(e, response=e.response, **last_json)
            if e.response.status_code == 500:
                raise InternalServerError(e, response=e.response, **last_json)
            if e.response.status_code == 403:
                if message == "login_required":
                    raise LoginRequired(response=e.response, **last_json)
                if len(e.response.text) < 512:
                    last_json["message"] = e.response.text
                raise ClientForbiddenError(e, response=e.response, **last_json)
            elif e.response.status_code == 400:
                error_type = last_json.get("error_type")
                if message == "challenge_required":
                    raise ChallengeRequired(**last_json)
                if 'scraping' in text and "wait a few minutes" in text:
                    raise ScrapingBlock(e, response=e.response, **last_json)
                if "generic" in text and 'feedback_required' in text: 
                    raise GenericComments(e, response=e.response, **last_json)
                elif (
                    "Media is unavailable" in message
                    or "Media not found or unavailable" in message
                    or "comment_media_does_not_exist" in text
                ):
                    raise MediaUnavailable(e, response=e.response, **last_json)
                elif 'comment_comments_disabled' in text:
                    raise CommentsDisabledError(e, response=e.response, **last_json)
                elif message == "feedback_required":
                    raise FeedbackRequired(
                        **dict(
                            last_json,
                            message="%s: %s"
                            % (message, last_json.get("feedback_message")),
                        )
                    )
                elif error_type == "sentry_block":
                    raise SentryBlock(**last_json)
                elif error_type == "rate_limit_error":
                    raise RateLimitError(**last_json)
                elif error_type == "bad_password":
                    msg = last_json.get("message", "").strip()
                    if msg:
                        if not msg.endswith("."):
                            msg = "%s." % msg
                        msg = "%s " % msg
                    last_json["message"] = (
                        "%sIf you are sure that the password is correct, then change your IP address, "
                        "because it is added to the blacklist of the Instagram Server"
                    ) % msg
                    raise BadPassword(**last_json)
                elif error_type == "two_factor_required":
                    if not last_json["message"]:
                        last_json["message"] = "Two-factor authentication required"
                    raise TwoFactorRequired(**last_json)
                elif "VideoTooLongException" in message:
                    raise VideoTooLongException(e, response=e.response, **last_json)
                elif "Not authorized to view user" in message:
                    raise PrivateAccount(e, response=e.response, **last_json)
                elif "Invalid target user" in message:
                    raise InvalidTargetUser(e, response=e.response, **last_json)
                elif "Invalid media_id" in message:
                    raise InvalidMediaId(e, response=e.response, **last_json)
                elif "has been deleted" in message:
                    # Sorry, this photo has been deleted.
                    raise MediaUnavailable(e, response=e.response, **last_json)
                elif "unable to fetch followers" in message:
                    # returned when user not found
                    raise UserNotFound(e, response=e.response, **last_json)
                elif "The username you entered" in message:
                    # The username you entered doesn't appear to belong to an account.
                    # Please check your username and try again.
                    last_json["message"] = (
                        "Instagram has blocked your IP address, "
                        "use a quality proxy provider (not free, not shared)"
                    )
                    raise ProxyAddressIsBlocked(**last_json)
                elif error_type or message:
                    raise UnknownError(**last_json)
                # TODO: Handle last_json with {'message': 'counter get error', 'status': 'fail'}
                self.logger.exception(e)
                self.logger.warning(
                    "Status 400: %s",
                    message or "Empty response message. Maybe enabled Two-factor auth?",
                )
                raise ClientBadRequestError(e, response=e.response, **last_json)
            elif e.response.status_code == 429:
                self.logger.warning("Status 429: Too many requests")
                raise ClientThrottledError(e, response=e.response, **last_json)
            elif e.response.status_code == 404:
                self.logger.warning("Status 404: Endpoint %s does not exist", endpoint)
                raise ClientNotFoundError(e, response=e.response, **last_json)
            elif e.response.status_code == 408:
                self.logger.warning("Status 408: Request Timeout")
                raise ClientRequestTimeout(e, response=e.response, **last_json)
            raise ClientError(e, response=e.response, **last_json)
        except httpx.ConnectError as e:
            raise ClientConnectionError("{e.__class__.__name__} {e}".format(e=e))
        if last_json.get("status") == "fail":
            raise ClientError(response=response, **last_json)
        elif "error_title" in last_json:
            """Example: {
            'error_title': 'bad image input extra:{}', <-------------
            'media': {
                'device_timestamp': '1588184737203',
                'upload_id': '1588184737203'
            },
            'message': 'media_needs_reupload', <-------------
            'status': 'ok' <-------------
            }"""
            raise ClientError(response=response, **last_json)
        return last_json

    def request_log(self, response : httpx.Response):
        self.private_request_logger.info(
            "%s [%s] %s %s (%s)",
            self.username,
            response.status_code,
            response.request.method,
            response.url,
            "{app_version}, {manufacturer} {model}".format(
                app_version=self.device_settings.app_version,
                manufacturer=self.device_settings.manufacturer,
                model=self.device_settings.model,
            ),
        )

    async def private_request(
        self,
        endpoint='',
        data=None,
        params=None,
        login=False,
        with_signature=True,
        headers=None,
        extra_sig=None,
        domain: str = None,
    ):
        kwargs = dict(
            data=data,
            params=params,
            login=login,
            with_signature=with_signature,
            headers=headers,
            extra_sig=extra_sig,
            domain=domain,
        )
        try:
            await self.random_delay()
            self.private_requests_count += 1
            await self._send_private_request(endpoint, **kwargs)
        except ClientRequestTimeout:
            self.logger.info(
                "Wait 5 seconds and try one more time (ClientRequestTimeout)"
            )
            await asyncio.sleep(5)
            return await self._send_private_request(endpoint, **kwargs)
        # except BadPassword as e:
        #     raise e
        except Exception as e:
            if self.handle_exception:
                self.handle_exception(self, e)
            elif isinstance(e, ChallengeRequired):
                await self.challenge_resolve(self.last_json)
            else:
                raise e
            if login and self.user_id:
                # After challenge resolve return last_json
                return self.last_json
            return await self._send_private_request(endpoint, **kwargs)
        return self.last_json

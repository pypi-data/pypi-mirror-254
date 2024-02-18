import base64
import time
import re
import json
from pathlib import Path
from typing import Dict
from uuid import uuid4
from typing import Union
from aioinstagrapi.models import AuthorizationData
from pydantic import ValidationError
from aioinstagrapi.mixins.auth.prelog import PreLoginFlowMixin
from aioinstagrapi.mixins.auth.postlog import PostLoginFlowMixin
from aioinstagrapi.exceptions import *
from aioinstagrapi.utils import gen_token, dumps, generate_jazoest
from aioinstagrapi.models import AuthorizationData, Credentials

class LoginMixin(PreLoginFlowMixin, PostLoginFlowMixin):
    username = None
    password = None
    authorization_data = None
    last_login = None
    relogin_attempt = 0
    device_settings = {}
    client_session_id = ""
    tray_session_id = ""
    advertising_id = ""
    android_device_id = ""
    comment_session_id = ""
    request_id = ""
    phone_id = ""
    app_id = "567067343352427"
    uuid = ""
    mid = "0"
    country = "US"
    country_code = 1  
    locale = "en_US"
    timezone_offset: int = -18000  
    ig_u_rur = ""  
    ig_www_claim = ""  


    def __init__(self, username : str = None, password : str = None):
        self.username = username
        self.password = password

    
    @property
    def authorization(self) -> str:
        """Build authorization header
        Example: Bearer IGT:2:eaW9u.....aWQiOiI0NzM5=
        """
        if self.authorization_data:
            b64part = base64.b64encode(dumps(self.authorization_data.dict()).encode()).decode()
            return f"Bearer IGT:2:{b64part}"
        return ""

    @property
    def sessionid(self) -> str:
        sessionid = self.cookies.get("sessionid")
        if not sessionid and self.authorization_data:
            sessionid = self.authorization_data.dict().get("sessionid")
        return sessionid

    @property
    def token(self) -> str:
        """CSRF token
        e.g. vUJGjpst6szjI38mZ6Pb1dROsWVerZelGSYGe0W1tuugpSUefVjRLj2Pom2SWNoA
        """
        if not getattr(self, "_token", None):
            self._token = self.cookies.get("csrftoken", gen_token(64))
        return self._token

    @property
    def rank_token(self) -> str:
        return f"{self.user_id}_{self.uuid}"

    @property
    def user_id(self) -> int:
        user_id = self.cookies.get("ds_user_id")
        if not user_id and self.authorization_data:
            user_id = self.authorization_data.dict().get("ds_user_id")
        if user_id:
            return int(user_id)
        return None

    @property
    def device(self) -> dict:
        return {
            key: val
            for key, val in self.device_settings.dict().items()
            if key in ["manufacturer", "model", "android_version", "android_release"]
        }

    async def login(
        self,
        username: Union[str, None] = None,
        password: Union[str, None] = None,
        relogin: bool = False,
        verification_code: str = "",
    ) -> bool:
        """
        Login

        Parameters
        ----------
        username: str
            Instagram Username
        password: str
            Instagram Password
        relogin: bool
            Whether or not to re login, default False
        verification_code: str
            2FA verification code

        Returns
        -------
        bool
            A boolean value
        """

        if not self.username or not self.password:
            if username is None or password is None:
                raise BadCredentials("Both username and password must be provided.")

            self.username = username
            self.password = password

        if relogin:
            self.authorization_data = None
            self.cookies.clear()
            if self.relogin_attempt > 1:
                raise ReloginAttemptExceeded()
            self.relogin_attempt += 1
        # if self.user_id and self.last_login:
        #     if time.time() - self.last_login < 60 * 60 * 24:
        #        return True  # already login
        if self.user_id and not relogin:
            return True  # already login
        try:
            await self.pre_login_flow()
        except (PleaseWaitFewMinutes, ClientThrottledError):
            self.logger.warning("Ignore 429: Continue login")
            # The instagram application ignores this error
            # and continues to log in (repeat this behavior)
        enc_password = await self.password_encrypt(self.password)
        data = {
            "jazoest": generate_jazoest(self.phone_id),
            "country_codes": '[{"country_code":"%d","source":["default"]}]'
            % int(self.country_code),
            "phone_id": self.phone_id,
            "enc_password": enc_password,
            "username": username,
            "adid": self.advertising_id,
            "guid": self.uuid,
            "device_id": self.android_device_id,
            "google_tokens": "[]",
            "login_attempt_count": "0",
        }
        try:
            logged = await self.private_request("accounts/login/", data, login=True)
            self.authorization_data = AuthorizationData(**self.parse_authorization(
                self.last_response.headers.get("ig-set-authorization")
            ))
            self.credentials.authorization_data = self.authorization_data
        except TwoFactorRequired as e:
            if not verification_code.strip():
                raise TwoFactorRequired(
                    f"{e} (you did not provide verification_code for login method)"
                )
            two_factor_identifier = self.last_json.get("two_factor_info", {}).get(
                "two_factor_identifier"
            )
            data = {
                "verification_code": verification_code,
                "phone_id": self.phone_id,
                "_csrftoken": self.token,
                "two_factor_identifier": two_factor_identifier,
                "username": username,
                "trust_this_device": "0",
                "guid": self.uuid,
                "device_id": self.android_device_id,
                "waterfall_id": str(uuid4()),
                "verification_method": "3",
            }
            logged = await self.private_request(
                "accounts/two_factor_login/", data, login=True
            )
            self.authorization_data = AuthorizationData(**self.parse_authorization(
                self.last_response.headers.get("ig-set-authorization")
            ))
            self.credentials.authorization_data = self.authorization_data
        if logged:
            await self.login_flow()
            self.last_login = time.time()
            return True
        return False

    async def login_by_sessionid(self, sessionid: str) -> bool:
        """
        Login using session id

        Parameters
        ----------
        sessionid: str
            Session ID

        Returns
        -------
        bool
            A boolean value
        """
        assert isinstance(sessionid, str) and len(sessionid) > 30, "Invalid sessionid"
        user_id = re.search(r"^\d+", sessionid).group()
        self.credentials.cookies = {"sessionid": sessionid, 'ds_user_id': user_id}
        self.credentials.authorization_data = AuthorizationData(**{
            "ds_user_id": user_id,
            "sessionid": sessionid,
            "should_use_header_over_cookies": True,
        })
        self.init()
        try:
            user = await self.user_info_v1(int(user_id))
        except :
            raise
        self.username = user.username
        return True

    
    def inject_sessionid_to_public(self) -> bool:
        """
        Inject sessionid from private session to public session

        Returns
        -------
        bool
            A boolean value
        """
        if self.sessionid:
            self.public_cookies['sessionid']= self.sessionid
            return True
        return False

    
    async def one_tap_app_login(self, user_id: str, nonce: str) -> bool:
        """One tap login emulation

        Parameters
        ----------
        user_id: str
            User ID
        nonce: str
            Login nonce (from Instagram, e.g. in /logout/)

        Returns
        -------
        bool
            A boolean value
        """
        user_id = int(user_id)
        data = {
            "phone_id": self.phone_id,
            "user_id": user_id,
            "adid": self.advertising_id,
            "guid": self.uuid,
            "device_id": self.uuid,
            "login_nonce": nonce,
            "_csrftoken": self.token,
        }
        return await self.private_request("accounts/one_tap_app_login/", data)

    async def relogin(self) -> bool:
        """
        Relogin helper

        Returns
        -------
        bool
            A boolean value
        """
        return await self.login(self.username, self.password, relogin=True)

    def get_settings(self) -> Dict:
        """
        Get current session settings

        Returns
        -------
        Dict
            Current session settings as a Dict
        """
        data = self.credentials.dict()
        data['cookies'] = self.cookies
        return data

    
    def set_settings(self, settings: Dict) -> bool:
        """
        Set session settings

        Returns
        -------
        Bool
        """
        self.credentials = Credentials(**settings)
        self.init()
        return True

    def load_settings(self, path: Path) -> Dict:
        """
        Load session settings

        Parameters
        ----------
        path: Path
            Path to storage file

        Returns
        -------
        Dict
            Current session settings as a Dict
        """
        with open(path, "r") as fp:
            self.set_settings(json.load(fp))
            return self.credentials
        return None

    def dump_settings(self, path: Path) -> bool:
        """
        Serialize and save session settings

        Parameters
        ----------
        path: Path
            Path to storage file

        Returns
        -------
        Bool
        """
        with open(path, "w") as fp:
            json.dump(self.get_settings(), fp, indent=4)
        return True
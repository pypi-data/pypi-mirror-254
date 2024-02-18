import logging
from urllib.parse import urlparse
from .models import Credentials
from aioinstagrapi.mixins.private import PrivateRequestMixin
from aioinstagrapi.mixins.auth.login import LoginMixin
from aioinstagrapi.mixins.user import UserMixin
from aioinstagrapi.mixins.account import AccountMixin
from aioinstagrapi.mixins.helpers import HelperMixin
from aioinstagrapi.mixins.album import DownloadAlbumMixin, UploadAlbumMixin
from aioinstagrapi.mixins.bloks import BloksMixin
from aioinstagrapi.mixins.challenge import ChallengeResolveMixin
from aioinstagrapi.mixins.clip import DownloadClipMixin, UploadClipMixin
from aioinstagrapi.mixins.collection import CollectionMixin
from aioinstagrapi.mixins.comment import CommentMixin
from aioinstagrapi.mixins.direct import DirectMixin
from aioinstagrapi.mixins.explore import ExploreMixin
from aioinstagrapi.mixins.fbsearch import FbSearchMixin
from aioinstagrapi.mixins.fundraiser import FundraiserMixin
from aioinstagrapi.mixins.hashtag import HashtagMixin
from aioinstagrapi.mixins.highlight import HighlightMixin
from aioinstagrapi.mixins.igtv import DownloadIGTVMixin, UploadIGTVMixin
from aioinstagrapi.mixins.insights import InsightsMixin
from aioinstagrapi.mixins.location import LocationMixin
from aioinstagrapi.mixins.media import MediaMixin
from aioinstagrapi.mixins.multiple_accounts import MultipleAccountsMixin
from aioinstagrapi.mixins.note import NoteMixin
from aioinstagrapi.mixins.notification import NotificationMixin
from aioinstagrapi.mixins.password import PasswordMixin
from aioinstagrapi.mixins.photo import DownloadPhotoMixin, UploadPhotoMixin
from aioinstagrapi.mixins.public import (
    ProfilePublicMixin,
    PublicRequestMixin,
    TopSearchesPublicMixin,
)
from aioinstagrapi.mixins.share import ShareMixin
from aioinstagrapi.mixins.story import StoryMixin
from aioinstagrapi.mixins.timeline import ReelsMixin
from aioinstagrapi.mixins.totp import TOTPMixin
from aioinstagrapi.mixins.track import TrackMixin
from aioinstagrapi.mixins.video import DownloadVideoMixin, UploadVideoMixin
#from requests.packages.urllib3.exceptions import InsecureRequestWarning


#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig(level = logging.INFO)
DEFAULT_LOGGER = logging.getLogger("aioinstagrapi")
httpx_logger = logging.getLogger('httpx')
httpx_logger.propagate = False


class Client(
    PublicRequestMixin,
    ChallengeResolveMixin,
    PrivateRequestMixin,
    TopSearchesPublicMixin,
    ProfilePublicMixin,
    LoginMixin,
    ShareMixin,
    TrackMixin,
    FbSearchMixin,
    HighlightMixin,
    DownloadPhotoMixin,
    UploadPhotoMixin,
    DownloadVideoMixin,
    UploadVideoMixin,
    DownloadAlbumMixin,
    NotificationMixin,
    UploadAlbumMixin,
    DownloadIGTVMixin,
    UploadIGTVMixin,
    MediaMixin,
    UserMixin,
    InsightsMixin,
    CollectionMixin,
    AccountMixin,
    DirectMixin,
    LocationMixin,
    HashtagMixin,
    CommentMixin,
    HelperMixin,
    StoryMixin,
    PasswordMixin,
    DownloadClipMixin,
    UploadClipMixin,
    ReelsMixin,
    ExploreMixin,
    BloksMixin,
    TOTPMixin,
    MultipleAccountsMixin,
    NoteMixin,
    FundraiserMixin,
):
    proxy = None
    credentials = None

    def __init__(
        self,
        credentials: dict = {},
        proxy: str = None,
        delay_range: list = None,
        logger=DEFAULT_LOGGER,
        **kwargs,
    ):

        super().__init__(**kwargs)

        self.credentials = Credentials(**credentials)
        self.logger = logger
        self.delay_range = delay_range
        self.set_proxy(proxy)
        self.init()
    
    
    def init(self) -> bool:
        """
        Initialize credentials

        Returns
        -------
        bool
            A boolean value
        """
        self.set_uuids(self.credentials.uuids.dict())
        self.bloks_versioning_id = "525157204187ff40ed117cb8039807a0b12137bc9d50211ed3b2e1d97be928a6"
        self.app_id = "567067343352427"
        self.cookies = self.credentials.cookies
        self.authorization_data = self.credentials.authorization_data
        self.last_login = self.credentials.last_login
        self.timezone_offset = self.credentials.timezone_offset
        self.device_settings = self.credentials.device_settings
        self.user_agent = self.credentials.user_agent
        self.locale = self.credentials.locale
        self.country = self.credentials.country
        self.country_code = self.credentials.country_code
        self.mid = self.credentials.mid
        self.ig_u_rur = self.credentials.ig_u_rur
        self.shbts = self.credentials.shbts
        self.shbid = self.credentials.shbid
        self.region_hint = self.credentials.region_hint
        self.ig_www_claim = self.credentials.ig_www_claim
        return True



    def set_uuids(self, uuids: dict = None) -> bool:
        """
        Helper to set uuids

        Parameters
        ----------
        uuids: Dict, optional
            UUIDs, default is None

        Returns
        -------
        bool
            A boolean value
        """
        self.phone_id = uuids.get("phone_id")
        self.uuid = uuids.get("uuid")
        self.client_session_id = uuids.get("client_session_id")
        self.advertising_id = uuids.get("advertising_id")
        self.android_device_id = uuids.get("android_device_id")
        self.request_id = uuids.get("request_id")
        self.tray_session_id = uuids.get("tray_session_id")
        self.comment_session_id = uuids.get("comment_session_id")
        return True
import asyncio
import random
import time
import json
import aioinstagrapi.config as config
from aioinstagrapi.utils import generate_uuid
from typing import Dict

TIMELINE_FEED_REASONS = (
    "cold_start_fetch",
    "warm_start_fetch",
    "pagination",
    "pull_to_refresh",
    "auto_refresh",
)
REELS_TRAY_REASONS = ("cold_start", "pull_to_refresh")
FEED_PAGES = ("following", "favorites")
try:
    from typing import Literal

    TIMELINE_FEED_REASON = Literal[TIMELINE_FEED_REASONS]
    REELS_TRAY_REASON = Literal[REELS_TRAY_REASONS]
    FEED_PAGES = Literal[FEED_PAGES]
except ImportError:
    # python <= 3.8
    TIMELINE_FEED_REASON = str
    REELS_TRAY_REASON = str
    FEED_PAGES = str



class PostLoginFlowMixin:
    """
    Helpers for post login flow
    """

    async def login_flow(self) -> bool:
        """
        Emulation mobile app behaivor after login

        Returns
        -------
        bool
            A boolean value
        """
        check_flow = []
        # chance = random.randint(1, 100) % 2 == 0
        # reason = "pull_to_refresh" if chance else "cold_start"
        await self.get_tokens()
        #input(self.last_response.headers)
        #await self.private_request("loom/fetch_config/",)
        #await self.mobile_config()
        #await self.register_push()
        #await self.ndx()
        #await self.limited()
        await (self.get_reels_tray_feed("cold_start"))
        await self.get_timeline_feed("following")
        return True

    async def ndx(self):
        headers = {'X-Ig-Nav-Chain': 'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:warm_start:1703001760.393::,com.bloks.www.caa.login.save-credentials:com.bloks.www.caa.login.save-credentials:2:button:1703001792.449::',}
        params = {
                'ndx_request_source': 'NDX_IG4A_MA_FEATURE',
            }
        return await self.private_request(
            "devices/ndx/api/async_get_ndx_ig_steps/", params=params, headers=headers
        )

    async def limited(self):
        headers = {'X-Ig-Nav-Chain': 'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:warm_start:1703001760.393::,com.bloks.www.caa.login.save-credentials:com.bloks.www.caa.login.save-credentials:2:button:1703001792.449::',}
        params = {
                 'signed_body': 'SIGNATURE.{}',
            }
        return await self.private_request(
            "users/get_limited_interactions_reminder/", params=params, headers=headers
        )

    async def register_push(self):
        headers = {'X-Ig-Nav-Chain': 'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:warm_start:1703001760.393::,com.bloks.www.caa.login.save-credentials:com.bloks.www.caa.login.save-credentials:2:button:1703001792.449::',}
        data = {
            'device_type': 'android_fcm',
            'is_main_push_channel': 'false',
            'hpke_pubkey': 'BL2uPiZqYh3eOhrPbx4+xvZBHCFe7pyXjwvSPloofpRPzn/UhdGFAZr6/XWFbpUD3Ijg/AsWl9ClCzSXHVRZDIs=',
            'device_sub_type': '0',
            'hpke_ciphersuite': '1001000010000',
            'device_token': 'dDDYxGhbhtU:APA91bGKFRfnJ32xhh2lLiXCP9yw2DzcytQSOGDgKY5BgQ7WocK50PBGqV1OBqjeeIQxkxkYNWTJpXrKsyISijwVkbX-lJKN3ikF0iNay2gRcMv462c_3GYVhmVfaEEZaP3ooF1K9xLT',
            'guid': self.uuid,
            '_uuid': self.uuid,
            'users': self.user_id,
            'family_device_id': self.phone_id,
            'hpke_keystore_id': 'HPKE_CLIENT_KEYPAIR',
        }
        return await self.private_request(
            "push/register/", data=data, headers=headers
        )
    
    async def mobile_config(self):
        headers = {'X-Ig-Nav-Chain': 'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:warm_start:1703001760.393::,com.bloks.www.caa.login.save-credentials:com.bloks.www.caa.login.save-credentials:2:button:1703001792.449::',}
        data = {"bool_opt_policy":"0","mobileconfig":"","api_version":"3","unit_type":"2","query_hash":"afc88cf48abf7aa80a2deabcceb5cc18c1a854fd6cdbc3f83d8ea5bc504bc37e","_uid":self.user_id,"device_id":self.uuid,"_uuid":self.uuid,"fetch_type":"ASYNC_FULL"}
        return await self.private_request(
            "launcher/mobileconfig/", data=data, headers=headers
        )

    async def get_timeline_feed(
        self, page : str = 'following', reason: TIMELINE_FEED_REASON = "pull_to_refresh", max_id: str = None
    ) -> Dict:
        """
        Get your timeline feed

        Parameters
        ----------
        reason: str, optional
            Reason to refresh the feed (cold_start_fetch, paginating, pull_to_refresh); Default "pull_to_refresh"
        max_id: str, optional
            Cursor for the next feed chunk (next cursor can be found in response["next_max_id"])

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        headers = {
            'X-Google-Ad-Id': self.advertising_id,
            'X-Fb-Connection-Type': 'WIFI',
            'X-Fb': '1',
            "X-Ads-Opt-Out": "0",
            "X-DEVICE-ID": self.uuid,
            "X-CM-Bandwidth-KBPS": '-1.000',  # str(random.randint(2000, 5000)),
            "X-CM-Latency": str(random.randint(1, 5)),
        }
        data = {
            'has_camera_permission': '0',
            'feed_view_info': '[]',
            'phone_id': self.phone_id,
            'reason': page+'_cold_start',
            'battery_level': '73',
            'timezone_offset': '-18000',
            'pagination_source': page,
            'device_id': self.uuid,
            'request_id': generate_uuid(),
            'is_pull_to_refresh': '0',
            '_uuid': self.uuid,
            'panavision_mode': '',
            'is_charging': '0',
            'is_dark_mode': '1',
            'will_sound_on': '0',
            'session_id': self.client_session_id,
            'bloks_versioning_id': self.bloks_versioning_id,
        }
        if reason in ["pull_to_refresh", "auto_refresh"]:
            data["is_pull_to_refresh"] = "1"
        else:
            data["is_pull_to_refresh"] = "0"

        if max_id:
            data["max_id"] = max_id
        # if "push_disabled" in options:
        #     data["push_disabled"] = "true"
        # if "recovered_from_crash" in options:
        #     data["recovered_from_crash"] = "1"
        return await self.private_request(
            "feed/timeline/", (data), with_signature=False, headers=headers
        )

    async def get_reels_tray_feed(
        self, reason: REELS_TRAY_REASON = "pull_to_refresh"
    ) -> Dict:
        """
        Get your reels tray feed

        Parameters
        ----------
        reason: str, optional
            Reason to refresh reels tray fee (cold_start, pull_to_refresh); Default "pull_to_refresh"

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {
            "supported_capabilities_new": config.SUPPORTED_CAPABILITIES,
            "reason": reason,
            "timezone_offset": str(self.timezone_offset),
            "tray_session_id": self.tray_session_id,
            "request_id": self.request_id,
            # "latest_preloaded_reel_ids": "[]", # [{"reel_id":"6009504750","media_count":"15","timestamp":1628253494,"media_ids":"[\"2634301737009283814\",\"2634301789371018685\",\"2634301853921370532\",\"2634301920174570551\",\"2634301973895112725\",\"2634302037581608844\",\"2634302088273817272\",\"2634302822117736694\",\"2634303181452199341\",\"2634303245482345741\",\"2634303317473473894\",\"2634303382971517344\",\"2634303441062726263\",\"2634303502039423893\",\"2634303754729475501\"]"},{"reel_id":"4357392188","media_count":"4","timestamp":1628250613,"media_ids":"[\"2634142331579781054\",\"2634142839803515356\",\"2634150786575125861\",\"2634279566740346641\"]"},{"reel_id":"5931631205","media_count":"7","timestamp":1628253023,"media_ids":"[\"2633699694927154768\",\"2634153361241413763\",\"2634196788830183839\",\"2634219197377323622\",\"2634294221109889541\",\"2634299705648894876\",\"2634299760434939842\"]"}],
            "page_size": 50,
            # "_csrftoken": self.token,
            "_uuid": self.uuid,
        }
        if reason == "cold_start":
            data["reel_tray_impressions"] = {}
        else:
            data["reel_tray_impressions"] = {self.user_id: str(time.time())}
        return await self.private_request("feed/reels_tray/", data)
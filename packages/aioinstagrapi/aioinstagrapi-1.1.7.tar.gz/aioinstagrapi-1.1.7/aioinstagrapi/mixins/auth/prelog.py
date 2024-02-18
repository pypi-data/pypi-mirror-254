import json
from typing import Dict
class PreLoginFlowMixin:
    """
    Helpers for pre login flow
    """

    async def pre_login_flow(self) -> bool:
        """
        Emulation mobile app behavior before login

        Returns
        -------
        bool
            A boolean value
        """
        # self.set_contact_point_prefill("prefill")
        # self.get_prefill_candidates(True)
        # self.set_contact_point_prefill("prefill")
        await self.get_tokens()
        await self.home_template()
        #await self.attestation()
        await self.mobile_config_login()
        # await self.sync_launcher(True)
        # self.sync_device_features(True)
        return True
    
    async def mobile_config_login(self):
        headers = {'X-Ig-Nav-Chain': 'com.bloks.www.caa.login.home_template:com.bloks.www.caa.login.home_template:1:warm_start:1703001760.393::,com.bloks.www.caa.login.save-credentials:com.bloks.www.caa.login.save-credentials:2:button:1703001792.449::',}
        data = {"bool_opt_policy":"0","mobileconfigsessionless":"","api_version":"3","unit_type":"1","query_hash":"4b4d5d0d4ef2f269eb5cd59adc5601462f8e01d5595b05e08913652a73d0604b","ts":"1703001789","device_id":self.uuid,"fetch_type":"ASYNC_FULL","family_device_id":self.phone_id}
        return await self.private_request(
            "launcher/mobileconfig/", data=data, headers=headers
        )

    async def home_template(self):
        data = {
            'params': json.dumps({"server_params":{"qe_device_id_server":self.uuid,"family_device_id_server":"","device_id_server":self.android_device_id}}),
            'bk_client_context': '{"bloks_version":"525157204187ff40ed117cb8039807a0b12137bc9d50211ed3b2e1d97be928a6","styles_id":"instagram"}',
            'bloks_versioning_id': '525157204187ff40ed117cb8039807a0b12137bc9d50211ed3b2e1d97be928a6',
        }
        return await self.private_request(domain='https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.login.home_template/', data=data, headers={"Host":"b.i.instagram.com"}, with_signature=False)

    async def get_tokens(self):
        data = {
        'normal_token_hash': '',
        'device_id': self.android_device_id,
        'custom_device_id': self.uuid,
        'fetch_reason': 'token_expired',
    }
        return await self.private_request(domain='https://b.i.instagram.com/api/v1/zr/dual_tokens/', data=data, headers={"Host":"b.i.instagram.com"}, with_signature=False)

    
    async def attestation(self):
        data = {
        'app_scoped_device_id': self.uuid,
        'key_hash': '',
            }
        return await self.private_request(domain='https://b.i.instagram.com/api/v1/attestation/create_android_keystore/', data=data, headers={"Host":"b.i.instagram.com"}, with_signature=False)
        
    
    async def get_prefill_candidates(self, login: bool = False) -> Dict:
        """
        Get prefill candidates value from Instagram

        Parameters
        ----------
        login: bool, optional
            Whether to login or not

        Returns
        -------
        bool
            A boolean value
        """
        data = {
            "android_device_id": self.android_device_id,
            "client_contact_points": '[{"type":"omnistring","value":"%s","source":"last_login_attempt"}]'
            % self.username,
            "phone_id": self.phone_id,
            "usages": '["account_recovery_omnibox"]',
            "logged_in_user_ids": "[]",  # "[\"123456789\",\"987654321\"]",
            "device_id": self.uuid,
        }
        # if login is False:
        data["_csrftoken"] = self.token
        return await self.private_request(
            "accounts/get_prefill_candidates/", data, login=login
        )

    async def sync_device_features(self, login: bool = False) -> Dict:
        """
        Sync device features to your Instagram account

        Parameters
        ----------
        login: bool, optional
            Whether to login or not

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {
            "id": self.uuid,
            "server_config_retrieval": "1",
            # "experiments": config.LOGIN_EXPERIMENTS,
        }
        if login is False:
            data["_uuid"] = self.uuid
            data["_uid"] = self.user_id
            data["_csrftoken"] = self.token
        # headers={"X-DEVICE-ID": self.uuid}
        return await self.private_request("qe/sync/", data, login=login)

    async def sync_launcher(self, login: bool = False) -> Dict:
        """
        Sync Launcher

        Parameters
        ----------
        login: bool, optional
            Whether to login or not

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {
            "id": self.uuid,
            "server_config_retrieval": "1",
        }
        if login is False:
            data["_uid"] = self.user_id
            data["_uuid"] = self.uuid
            data["_csrftoken"] = self.token
        return await self.private_request("launcher/sync/", data, login=login)

    async def set_contact_point_prefill(self, usage: str = "prefill") -> Dict:
        """
        Sync Launcher

        Parameters
        ----------
        usage: str, optional
            Default "prefill"

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {
            "phone_id": self.phone_id,
            "usage": usage,
            # "_csrftoken": self.token
        }
        return await self.private_request("accounts/contact_point_prefill/", data, login=True)

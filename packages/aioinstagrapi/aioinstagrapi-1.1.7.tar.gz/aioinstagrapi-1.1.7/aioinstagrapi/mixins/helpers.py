import json
import base64
from typing import Dict

class HelperMixin:

    def parse_authorization(self, authorization) -> dict:
        """Parse authorization header"""
        try:
            b64part = authorization.rsplit(":", 1)[-1]
            if not b64part:
                return {}
            return json.loads(base64.b64decode(b64part))
        except Exception as e:
            self.logger.exception(e)
        return {}
    
    def with_extra_data(self, data: Dict) -> Dict:
        """
        Helper to get extra data

        Returns
        -------
        Dict
            A dictionary of default data
        """
        return self.with_default_data(
            {
                "phone_id": self.phone_id,
                "_uid": str(self.user_id),
                "guid": self.uuid,
                **data,
            }
        )

    def with_default_data(self, data: Dict) -> Dict:
        """
        Helper to get default data

        Returns
        -------
        Dict
            A dictionary of default data
        """
        return {
            "_uuid": self.uuid,
            # "_uid": str(self.user_id),
            # "_csrftoken": self.token,
            "device_id": self.android_device_id,
            **data,
        }

    def with_action_data(self, data: Dict) -> Dict:
        """
        Helper to get action data

        Returns
        -------
        Dict
            A dictionary of action data
        """
        return dict(self.with_default_data({"radio_type": "wifi-none"}), **data)

    async def expose(self) -> Dict:
        """
        Helper to expose

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        data = {"id": self.uuid, "experiment": "ig_android_profile_contextual_feed"}
        return await self.private_request("qe/expose/", self.with_default_data(data))
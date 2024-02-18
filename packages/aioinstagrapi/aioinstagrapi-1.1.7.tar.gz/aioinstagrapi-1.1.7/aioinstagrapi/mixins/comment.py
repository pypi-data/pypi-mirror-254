import random
from typing import List, Optional, Tuple

from aioinstagrapi.utils import gen_user_breadcrumb, generate_uuid, generate_jazoest, dumps
from aioinstagrapi.exceptions import ClientError, ClientNotFoundError, MediaNotFound
from aioinstagrapi.extractors import extract_comment
from aioinstagrapi.models import Comment


class CommentMixin:
    """
    Helpers for managing comments on a Media
    """

    async def pre_comment(self, media_id : str, text : str):
            await self.generate_nudge(media_id)
            await self.media_check_offensive_comment(media_id, text)

    async def generate_nudge(self, media_id : str):
        data = {
            'is_bottom_sheet_open': 'true',
            'media_id': str(media_id),
            'source': 'loading',
            '_uuid': self.uuid,
            'viewed_comment_ids': '[]',
        }
        return await self.private_request('nudges/generate_nudge/', data=data)


    async def media_comments(self, media_id: str, amount: int = 20) -> List[Comment]:
        """
        Get comments on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        amount: int, optional
            Maximum number of comments to return, default is 0 - Inf

        Returns
        -------
        List[Comment]
            A list of objects of Comment
        """

        # TODO: to public or private
        def get_comments():
            if result.get("comments"):
                for comment in result.get("comments"):
                    comments.append(extract_comment(comment))

        media_id = await self.media_id(media_id)
        params = None
        comments = []
        result = await self.private_request(f"media/{media_id}/comments/", params)
        get_comments()
        while (result.get("has_more_comments") and result.get("next_max_id")) or (
            result.get("has_more_headload_comments") and result.get("next_min_id")
        ):
            try:
                if result.get("has_more_comments"):
                    params = {"max_id": result.get("next_max_id")}
                else:
                    params = {"min_id": result.get("next_min_id")}
                if not (
                    result.get("next_max_id")
                    or result.get("next_min_id")
                    or result.get("comments")
                ):
                    break
                result = await self.private_request(f"media/{media_id}/comments/", params)
                get_comments()
            except ClientNotFoundError as e:
                raise MediaNotFound(e, media_id=media_id, **self.last_json)
            except ClientError as e:
                if "Media not found" in str(e):
                    raise MediaNotFound(e, media_id=media_id, **self.last_json)
                raise e
            if amount and len(comments) >= amount:
                break
        if amount:
            comments = comments[:amount]
        return comments

    async def media_comments_chunk(
        self, media_id: str, max_amount: int, min_id: str = None
    ) -> Tuple[List[Comment], str]:
        """
        Get chunk of comments on a media and end_cursor

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        max_amount: int
            Limit number of comments to fetch, default is 100
        min_id: str, optional
            End Cursor of previous chunk that had more comments, default value is None

        Returns
        -------
        Tuple[List[Comment], str]
            A list of objects of Comment and an end_cursor
        """

        # TODO: to public or private
        def get_comments():
            if result.get("comments"):
                for comment in result.get("comments"):
                    comments.append(extract_comment(comment))

        media_id = await self.media_id(media_id)
        params = {"min_id": min_id} if min_id else None
        comments = []
        result = await self.private_request(f"media/{media_id}/comments/", params)
        get_comments()
        while result.get("has_more_headload_comments") and result.get("next_min_id"):
            try:
                params = {"min_id": result.get("next_min_id")}
                if not (result.get("next_min_id") or result.get("comments")):
                    break
                result = await self.private_request(f"media/{media_id}/comments/", params)
                get_comments()
            except ClientNotFoundError as e:
                raise MediaNotFound(e, media_id=media_id, **self.last_json)
            except ClientError as e:
                if "Media not found" in str(e):
                    raise MediaNotFound(e, media_id=media_id, **self.last_json)
                raise e
            if len(comments) >= max_amount:
                break
        return (comments, result.get("next_min_id"))

    async def media_comment(
        self, media_id: str, text: str, replied_to_comment_id: Optional[int] = None
    , gif_media_id : Optional[str] = None) -> Comment:
        """
        Post a comment on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        text: str
            String to be posted on the media

        Returns
        -------
        Comment
            An object of Comment type
        """
        assert self.user_id, "Login required"
        media_id = await self.media_id(media_id)
        data = {
        "include_media_code":"false",
        "user_breadcrumb":gen_user_breadcrumb(len(text)),
        "inventory_source":"media_or_ad",
        "comment_creation_key":generate_jazoest(self.phone_id),
        "delivery_class":"organic",
        "idempotence_token":generate_uuid(),
        "include_e2ee_mentioned_user_list":"false",
        "radio_type":"wifi-none",
        "_uid":self.user_id,
        "_uuid":self.uuid,
        "nav_chain":"MainFeedFragment:feed_timeline:1:cold_start:1698798344.620::,InteractivityBottomSheetFragment:feed_timeline:3:button:1698798356.51::,CommentThreadFragment:comments_v2:4:button:1698798356.489::",
        "logging_info_token":"d8904f04ed084c65ac6b0f4fba074b7f",
        "comment_text":text,
        "is_carousel_bumped_post":"false",
        "container_module":"comments_v2_feed_timeline",
        "feed_position":"0"
        }
        if gif_media_id:
            data['gif_params'] = dumps({'gif_media_id': gif_media_id, 'is_sticker': False })
            #data['gif_params'] = "{\"gif_media_id\":\"WotHgjtqxZwfS\",\"is_sticker\":false}"
           

        if replied_to_comment_id:
            data["replied_to_comment_id"] = int(replied_to_comment_id)
        result = await self.private_request(
            f"media/{media_id}/comment/",
            self.with_action_data(data),
        )
        return extract_comment(result["comment"])

    async def media_check_offensive_comment(self, media_id: str, text: str) -> bool:
        """
        Checks if a comment text is offensive

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        text: str
            String to be posted on the media

        Returns
        -------
        bool
            If comment is offensive
        """
        assert self.user_id, "Login required"
        media_id = await self.media_id(media_id)
        data = {
            # _uid, comment_session_id are not in this body?
            "media_id": media_id,
            "comment_text": text,
        }
        result = await self.private_request(
            "media/comment/check_offensive_comment/",
            self.with_action_data(data),
        )
        return result["is_offensive"]

    async def comment_like(self, comment_pk: int, revert: bool = False) -> bool:
        """
        Like a comment on a media

        Parameters
        ----------
        comment_pk: int
            Unique identifier of a Comment
        revert: bool, optional
            If liked, whether or not to unlike. Default is False

        Returns
        -------
        bool
            A boolean value
        """
        assert self.user_id, "Login required"
        comment_pk = int(comment_pk)
        data = {
            "is_carousel_bumped_post": "false",
            "container_module": "feed_contextual_self_profile",
            "feed_position": str(random.randint(0, 6)),
        }
        name = "unlike" if revert else "like"
        result = await self.private_request(
            f"media/{comment_pk}/comment_{name}/", self.with_action_data(data)
        )
        return result["status"] == "ok"

    async def comment_unlike(self, comment_pk: int) -> bool:
        """
        Unlike a comment on a media

        Parameters
        ----------
        comment_pk: int
            Unique identifier of a Comment

        Returns
        -------
        bool
            A boolean value
        """
        return await self.comment_like(comment_pk, revert=True)

    async def comment_pin(self, media_id: str, comment_pk: int, revert: bool = False):
        """
        Pin a comment on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        comment_pk: int
           Unique identifier of a Comment
        revert: bool, optional
            Unpin when True
        Returns
        -------
        bool
           A boolean value
        """
        data = self.with_action_data({"_uid": self.user_id, "_uuid": self.uuid})
        name = "unpin" if revert else "pin"

        result = await self.private_request(
            f"media/{media_id}/{name}_comment/{comment_pk}", data
        )
        return result["status"] == "ok"

    async def comment_unpin(self, media_id: str, comment_pk: int):
        """
        Unpin a comment on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        comment_pk: int
           Unique identifier of a Comment

        Returns
        -------
        bool
           A boolean value
        """
        return await self.comment_pin(media_id, comment_pk, True)

    async def comment_bulk_delete(self, media_id: str, comment_pks: List[int]) -> bool:
        """
        Delete a comment on a media

        Parameters
        ----------
        media_id: str
            Unique identifier of a Media
        comment_pks: List[int]
            List of unique identifier of a Comment

        Returns
        -------
        bool
            A boolean value
        """
        media_id = await self.media_id(media_id)
        data = {
            "comment_ids_to_delete": ",".join([str(pk) for pk in comment_pks]),
            "container_module": "self_comments_v2_newsfeed_you",
        }
        result = await self.private_request(
            f"media/{media_id}/comment/bulk_delete/", self.with_action_data(data)
        )
        return result["status"] == "ok"

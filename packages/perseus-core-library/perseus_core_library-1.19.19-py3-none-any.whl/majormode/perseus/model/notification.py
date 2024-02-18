# Copyright (C) 2023 Majormode.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Majormode or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with the
# terms of the license agreement or other applicable agreement you
# entered into with Majormode.
#
# MAJORMODE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE SUITABILITY
# OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE, OR NON-INFRINGEMENT.  MAJORMODE SHALL NOT BE LIABLE FOR ANY
# LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF USING, MODIFYING
# OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.

from __future__ import annotations

from typing import Any
from uuid import UUID


class Notification:
    def __init__(
            self,
            notification_type: str,
            recipient_ids: int | str | UUID | list[int | str | UUID] | set[int | str | UUID] | tuple[int | str | UUID],
            content_text: str = None,
            content_title: str = None,
            is_priority: bool = False,
            notification_id: UUID = None,
            payload: Any = None,
            sound: str = None
    ):
        """

        :param notification_type: The type of the notification to be sent,
            such as, for example, ``on_something_happened``.

        :param recipient_ids: The identifier of a recipient, or a list of
            identifiers of recipients, to send the notification to.

        :param content_text: The text (second row) of the notification, in a
            standard notification.  It corresponds to the localized text that
            provides the notification’s main content.

        :param content_title: The title (first row) of the notification, in a
            standard notification.  It corresponds to the localized text that
            provides the notification’s primary description.

        :param is_priority: There are two options for assigning delivery
            priority to downstream messages: normal and high priority.  Though
            the behavior differs slightly across platforms, delivery of normal
            and high priority messages works as follows:

            - Normal priority. Normal priority messages are delivered immediately
              when the app is in the foreground.  For background apps running in
              the background, delivery may be delayed.  For less time-sensitive
              messages, such as notifications of new email, keeping UI in sync, or
              syncing app data in the background, choose normal delivery priority.

            - High priority. The messaging system attempts to deliver high priority
              messages immediately even if the device is in Doze mode. High priority
              messages are for time-sensitive, user visible content.

        :param notification_id: The unique identifier of the notification.

        :param payload: Any arbitrary JSON expression that provides
            information about the context of this notification.

        :param sound: The sound that plays when the device receives the
            notification.  Supports ``default`` or the filename of a sound
            resource bundled in your app.  Sound files must reside in
            ``/res/raw/``.
        """
        self.__notification_id = notification_id
        self.__notification_type = notification_type

        if isinstance(recipient_ids, (list, set, tuple)):
            self.__recipient_ids = list(set([
                str(recipient_id)
                for recipient_id in recipient_ids
            ]))
        else:
            self.__recipient_ids = [str(recipient_ids)]

        self.__content_title = content_title
        self.__content_text = content_text
        self.__payload = payload

        self.__is_priority = is_priority

        self.__sound = sound

    @property
    def content_text(self) -> str:
        return self.__content_text

    @property
    def content_title(self) -> str:
        return self.__content_title

    @property
    def is_property(self) -> bool:
        return self.__is_priority

    @property
    def notification_id(self) -> UUID:
        return self.__notification_id

    @notification_id.setter
    def notification_id(self, notification_id: UUID) -> None:
        if self.__notification_id is not None:
            raise ValueError(
                f"The notification's identifier has already been set with '{self.__notification_id}'"
            )
        self.__notification_id = notification_id

    @property
    def notification_type(self) -> str:
        return self.__notification_type;

    @property
    def payload(self) -> Any:
        return self.__payload

    @property
    def recipient_ids(self) -> list[str]:
        return self.__recipient_ids

    @property
    def sound(self) -> str:
        return self.__sound

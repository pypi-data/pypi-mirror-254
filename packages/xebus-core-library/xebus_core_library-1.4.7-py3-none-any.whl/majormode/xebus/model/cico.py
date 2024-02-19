# Copyright (C) 2020 Majormode.  All rights reserved.
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

from uuid import UUID

from majormode.perseus.model.date import ISO8601DateTime
from majormode.perseus.model.geolocation import GeoPoint
from majormode.perseus.utils import cast
from majormode.xebus.constant.cico import CiCoAction
from majormode.xebus.constant.cico import CiCoMode


class CiCoOperation:
    """
    A check-in or check-out operation of a child

    A child is checked in or checked out by an agent (e.g., an attendant,
    a security guard) while the child is getting on/off a school bus, or
    while the child is entering or leaving the school campus.
    """
    def __init__(
            self,
            child_account_id: UUID,
            agent_account_id: UUID,
            device_id: str,
            cico_action: CiCoAction,
            cico_mode: CiCoMode,
            cico_time: ISO8601DateTime,
            guardian_account_id: UUID = None,
            location: GeoPoint = None,
            school_id: UUID = None):
        """
        Build a new object `CiCoOperation`


        :param child_account_id: The identification of the child whom the
            attendant performed a Ci/Co operation.

        :param agent_account_id: Identification of the agent (e.g., an
            attendant, a security guard) who performed this Ci/Co operation.

        :param device_id: Identification of the ID-R device that the attendant
            used to perform this Ci/Co operation.

        :param cico_action: An item of the enumeration `CiCoAction` that
            indicates the action automatically selected or manually overridden
            by the attendant to perform this Ci/Co operation.

        :param cico_mode: An item of the enumeration `CiCoMode` that indicates
            the mode used by the attendant to perform this Ci/Co operation.

        :param cico_time: Time when the attendant performed this Ci/Co
            operation.

        :param guardian_account_id: The identification of a guardian who
            picked up the child from the school bus or the school campus.

        :param location: An object `GeoPoint` that corresponds to the last
            known geographical location of the ID-R mobile device when the
            attendant performed this Ci/Co operation.

        :param school_id: Identification of the school of the child who has
            been checked-in or checked-out.
        """
        self.__child_account_id = child_account_id
        self.__agent_account_id = agent_account_id
        self.__guardian_account_id = guardian_account_id
        self.__device_id = device_id
        self.__cico_action = cico_action
        self.__cico_mode = cico_mode
        self.__cico_time = cico_time
        self.__location = location
        self.__school_id = school_id

    @property
    def agent_account_id(self) -> UUID:
        return self.__agent_account_id

    @property
    def child_account_id(self) -> UUID:
        return self.__child_account_id

    @property
    def cico_action(self) -> CiCoAction:
        return self.__cico_action

    @property
    def cico_mode(self) -> CiCoMode:
        return self.__cico_mode

    @property
    def cico_time(self) -> ISO8601DateTime:
        return self.__cico_time

    @property
    def device_id(self) -> str:
        return self.__device_id

    @property
    def guardian_account_id(self) -> UUID | None:
        return self.__guardian_account_id

    @property
    def location(self) -> GeoPoint | None:
        return self.__location

    @property
    def school_id(self) -> UUID | None:
        return self.__school_id

    @staticmethod
    def from_json(payload) -> CiCoOperation | None:
        return payload and CiCoOperation(
            cast.string_to_uuid(payload['child_account_id']),
            cast.string_to_uuid(payload['agent_account_id']),
            payload['device_id'],
            cast.string_to_enum(payload['cico_action'], CiCoAction),
            cast.string_to_enum(payload['cico_mode'], CiCoMode),
            cast.string_to_timestamp(payload['cico_time']),
            guardian_account_id=cast.string_to_uuid(payload.get('guardian_account_id')),
            location=GeoPoint.from_json(payload.get('location')),
            school_id=cast.string_to_uuid(payload.get('school_id'))
        )

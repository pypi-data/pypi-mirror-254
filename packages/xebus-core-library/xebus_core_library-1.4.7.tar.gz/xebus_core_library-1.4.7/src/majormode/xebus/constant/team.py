# Copyright (C) 2019 Majormode.  All rights reserved.
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

from majormode.perseus.constant.team import MemberRole
from majormode.perseus.model.enum import Enum

TeamRole = Enum(
    # Organization responsible for registering and managing families to
    # the transportation service of the school campus, such as a parent
    # association when the school organization itself doesn't manage the
    # transportation service of its campus.
    'manager',

    # Organization that has not particular responsibility on the
    # transportation service of a school campus, but that is allowed to
    # monitor the transportation service's activities of the school.
    'observer',

    # Organization that owns the school campus, i.e., the education
    # institution itself (the school organization).
    'owner',

    # Organization responsible for operating the transportation service of
    # the children to the school campus. The user MUST be the director of
    # this organization.
    'transporter',
)

TeamMemberRole = MemberRole.extend(
    # An administrator is responsible for managing the Xebus Workspace of
    # their organization.
    'administrator',
    
    # An attendant, also known as *bus monitor*, is responsible for checking
    # in and checking out the pupils when they get on and off the school bus.
    'attendant',

    # A coordinator is responsible for a team of attendants.
    'coordinator',

    # A driver is responsible for riding the pupils back and forth from
    # their home (or the closest bus stop) to the school campus.
    'driver',

    # A security guard is responsible for checking in and checking out the
    # pupils when they enter and leave the school campus.
    'security_guard',
)

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

from majormode.perseus.constant.obj import ObjectStatus
from majormode.perseus.model.enum import Enum


IDReaderDeviceNotification = Enum(
    # Indicate that the state of a ID-R device's battery has changed.  This
    # device has been connected to or disconnected from an external power
    # source.
    'on_battery_state_changed',

    # Indicate that the battery level of a ID-R device went down a critical
    # threshold.
    'on_battery_level_critical'

    # Indicate that a ID-R device has been activated by an administrator of the
    # organization that manages this device.
    'on_device_activated',

    # Indicate that a ID-R device sent a handshake while it was not yet
    # registered to the platform.  Its activation stays pending until an
    # administrator of the organization, which manages the place where
    # the ID-R device shakes-hands at, reviews this request.
    'on_device_activation_requested',

    # Indicate that the attributes of a ID-R device have been updated.
    # This notification includes the list of properties that have been
    # updated, and their new respective values.
    'on_device_attributes_updated',
)

# Define constants specifying actions to change the status of a ID-R
# device of an organisation.
IDReaderDeviceStatusChangeAction = Enum(
    'reactivate',
    'remove',
    'suspend',
)

# Define the new status of a ID-R device depending on the action that
# was performed.
IDReaderDeviceStatusChangeResult = {
    IDReaderDeviceStatusChangeAction.reactivate: ObjectStatus.enabled,
    IDReaderDeviceStatusChangeAction.suspend: ObjectStatus.disabled,
    IDReaderDeviceStatusChangeAction.remove: ObjectStatus.deleted,
}

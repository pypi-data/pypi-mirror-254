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

from majormode.perseus.model.enum import Enum


CiCoAction = Enum(
    'checkin',
    'checkout',
)

CiCoMode = Enum(
    # Indicate that the Ci/Co action has been performed automatically by a
    # ID-R device (scan of the QR code printed on a ID card, read of the tag
    # of a NFC/RFID card, face recognition, fingerprint recognition, ...).
    # This Ci/Co operation is considered as secured.
    'automatic',

    # Indicate that the Ci/Co action has been performed manually by an
    # attendant or a security guard by selecting the child on a list and
    # by clicking on a Ci/Co action.  This Ci/Co operation is not considered
    # as secured.  It must be reported to the administrators of organizations
    # responsible for the security of the children.
    'manual',

    # Indicate that the Ci/Co action has been performed by a sentinel
    # responsible for tracking children who are abnormally checked in for a
    # long time (i.e., the child has never been checked-out).  The sentinel
    # checks out such a child and reports this security breach to the
    # administrators of organizations responsible for the security of the
    # children.
    'sentinel',
)

CiCoStatus = Enum(
    'checked_in',
    'checked_out',
)

InvalidCiCoActionReason = Enum(
    # Indicate that the security guard uses an ID-R idr_device that doesn't
    # belong to the school that employs the security guard.  The ID-R idr_device
    # application SHOULD inform the security guard and log him out.
    'wrong_idr_device',

    # Indicate that the ID-R idr_device used to check-in/check-out a child is
    # too far from the school it belongs to.  The ID-R idr_device application
    # SHOULD request the security guard and do not proceed any check-in/
    # check-out operation until the ID-R idr_device is located near the school.
    'wrong_location',

    # Indicate that the child who is being checked-in / checked-out by an
    # ID-R idr_device is not registered to the school that owns this idr_device.
    'wrong_child',

    # Indicate that a guardian of the child MUST be identified to perform
    # the check-out of this child.
    'missing_guardian',

    # Indicate that the person that has been scanned is not a guardian of
    # the child that is checked-out.
    'wrong_guardian',
)

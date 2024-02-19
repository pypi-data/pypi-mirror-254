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


# Indicate the type of bus stop suggestion made based on the school buses
# activities of a school.
BusStopSuggestionType = Enum(
    # Suggest a new bus stop as Ci/Co operations have been recorded at a
    # geographical location where no bus stops have been registered nearby.
    'creation',

    # Suggest a shift of the geographical location of an existing bus stop
    # as Ci/Co operations have been recorded at another location near to
    # this bus stop.
    'shift',

    # Suggest the deletion of an existing bus stop as no Ci/Co operations
    # have been recorded for a while at the geographical location of the
    # bus stop.
    'deletion',
)

# Indicate the direction of a school bus trip.
TripDirection = Enum(
    # From home to school.
    'outward',

    # From school to home.
    'inward',
)

# Indicate the direction of the school bus route passing through a bus
# stop.
BusStopTripDirection = TripDirection.extend(
    # Could be used for routes from home to school or from school to home.
    'mixed'
)
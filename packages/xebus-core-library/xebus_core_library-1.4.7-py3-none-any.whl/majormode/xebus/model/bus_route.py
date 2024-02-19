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

import collections

from majormode.mercurius.constant.place import AddressComponentName
from majormode.perseus.model.geolocation import GeoPoint
from majormode.perseus.model.locale import Locale
from majormode.perseus.utils import cast


class BusStop:
    def __eq__(self, other):
        return self.__location == other.__location

    def __hash__(self):
        return hash(self.__location)

    def __init__(
            self,
            stop_code,
            location,
            address=None,
            boundaries=None,
            stop_id=None):
        self.__stop_code = stop_code
        self.__location = location
        self.__address = address
        self.__boundaries = boundaries
        self.__stop_id = stop_id

    @property
    def address(self):
        return self.__address

    @property
    def boundaries(self):
        return self.__boundaries

    @property
    def location(self):
        return self.__location

    @property
    def stop_code(self):
        return self.__stop_code

    @property
    def stop_id(self):
        return self.__stop_id

    @stop_id.setter
    def stop_id(self, stop_id):
        if self.__stop_id:
            raise AttributeError(f'this bus stop is already defined with the identifier "{self.__stop_id}"')
        self.__stop_id = stop_id


class BusStopJson(BusStop):
    def __init__(
            self,
            stop_code,
            location,
            address=None,
            stop_id=None):
        super().__init__(stop_code, location, address=address, stop_id=stop_id)

    @staticmethod
    def __parse_address(payload):
        address = collections.defaultdict(dict)
        if payload:
            for locale_str, address_components in payload.items():
                locale = Locale.from_string(locale_str)
                for component_name_str, component_value in address_components.items():
                    component_name = cast.string_to_enum(component_name_str, AddressComponentName)
                    address[locale][component_name] = component_value
        return address

    @classmethod
    def from_json(cls, payload):
        return payload and BusStopJson(
            payload['stop_code'],
            GeoPoint.from_json(payload['location']),
            address=cls.__parse_address(payload.get('address')),
            stop_id=cast.string_to_uuid(payload.get('stop_id'), strict=False))


class BusLine:
    def __init__(self, name, journey_type, stops, path, line_id=None):
        if any([not isinstance(stop, BusLineStop) for stop in stops]):
            raise TypeError("items of argument 'stop' MUST all be 'BusLineStop' objects")

        self.__name = name
        self.__journey_type = journey_type
        self.__stops = stops
        self.__path = path
        self.__line_id = line_id

    @property
    def journey_type(self):
        return self.__journey_type

    @property
    def line_id(self):
        return self.__line_id

    @line_id.setter
    def line_id(self, line_id):
        if self.__line_id:
            raise AttributeError(f'already defined with the identifier "{self.__line_id}"')
        self.__line_id = line_id

    @property
    def name(self):
        return self.__name

    @property
    def path(self):
        return self.__path

    @property
    def stops(self):
        return self.__stops


class BusLineStop:
    def __init__(self, stop_id, arrival_time=None, departure_time=None):
        self.__stop_id = stop_id
        self.__arrival_time = arrival_time
        self.__departure_time = departure_time

    @property
    def arrival_time(self):
        return self.__arrival_time

    @property
    def departure_time(self):
        return self.__departure_time

    @property
    def stop_id(self):
        return self.__stop_id





# class BusLineJson(BusLine):
#     # def __init__(self, journey_type, stops, path, route_id=None):
#     #     super().__init__(journey_type, stops, path, route_id=route_id)
#     @staticmethod
#     def __parse_path(payload):
#         path = [
#             GeoPoint.from_json(point)
#             for point in payload
#         ]
#         return path
#
#     @staticmethod
#     def __parse_bus_stops(payload):
#         bus_stops = [
#             BusLineStopJson.from_json(bus_stop_payload)
#             for bus_stop_payload in payload
#         ]
#         return bus_stops
#
#     @classmethod
#     def from_json(cls, payload):
#         print(payload['stops'])
#         return payload and BusLineJson(
#             payload['name'],
#             cast.string_to_enum(payload['trip_type'], TripDirection),
#             cls.__parse_bus_stops(payload['stops']),
#             cls.__parse_path(payload['path']),
#             line_id=cast.string_to_uuid(payload.get('line_id'), strict=False))
#
#
# class BusLineStopJson(BusLineStop):
#     @staticmethod
#     def from_json(payload):
#         return payload and BusLineStopJson(
#             cast.string_to_uuid(payload['stop_id']),
#             arrival_time=cast.string_to_time(payload['arrival_time']),
#             departure_time=cast.string_to_time(payload['departure_time']))
#
#
# class BusLineStopJson(BusStop):
#     def __init__(self, stop_id, location, scheduled_time):
#         super().__init__(location, stop_id=stop_id)
#         self.__scheduled_time = scheduled_time
#
#     @classmethod
#     def from_json(cls, payload):
#         return payload and BusLineStopJson(
#             GeoPoint.from_json(payload['location']))
#         stop_code = placemark.name.text
#         location = cls._parse_location(placemark.Point.coordinates.text)
#         return BusLineStopJson(stop_code, location, scheduled_time)
#
#     @property
#     def scheduled_time(self):
#         return self.__scheduled_time






# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.7] - 2024-02-05
### Fixed
- Extend the search path for the module `majormode.xebus.constant`

## [1.4.6] - 2023-12-13
### Fixed
- Fix the enumeration `TeamMemberRole`

## [1.4.4] - 2023-12-13
### Added
- Add the enumeration `SchoolBusNotification`
- Add the notification `SchoolBusNotification.on_child_school_bus_cico`

## [1.4.1] - 2022-01-13
### Fixed
- Fix attribute name `agent_account_id` with `attendant_account_id` in enumeration `CiCoOperation`

## [1.4.0] - 2021-07-13
### Changed
- Integrate the class `ChildCiCoOperation` into the base class `CiCoOperation`

## [1.3.5] - 2021-06-07
### Changed
- Rename the items of the enumeration `BusStopSuggestionType`

## [1.3.4] - 2021-05-31
### Added
- Add the enumeration `SchoolInformationSystemVendor`

## [1.3.3] - 2021-04-27
### Added
- Add the enumeration `AdminNotification`

## [1.3.2] - 2021-04-13
### Added
- Add the enumeration `TeamSortAttribute`

## [1.3.1] - 2021-04-13
### Added
- Add the enumeration `PersonSortAttribute`

## [1.3.0] - 2020-12-27
### Changed
- Change the organization roles to `manager`, `observer`, `owner`, and `transporter`

## [1.2.10] - 2020-12-27
### Added
- Set optional the argument `locale` of surname and forename formatter functions

## [1.2.9] - 2020-12-27
### Added
- Fix missing package file `__init.py__`

## [1.2.8] - 2020-12-27
### Added
- Surname and forename formatter

## [1.2.7] - 2020-12-03
### Added
- Add the class `BusStopJson` that inherits from `BusStop`

## [1.2.6] - 2020-12-01
### Added
- Add the enumeration `BusStopTripDirection` that inherits from `TripDirection`
### Updated
- Rename the enumeration `BusStopSuggestionChangeType` with `BusStopSuggestionType`
- Rename the enumeration `JourneyType` with `TripDirection`

## [1.2.5] - 2020-11-25
### Updated
- Add the enumeration `BusStopSuggestionChangeType`

## [1.2.4] - 2020-11-23
### Updated
- Add the identification of the school to Ci/Co operation

## [1.2.3] - 2020-10-30
### Added
- Add a method to build an object `CiCoOperation` from JSON payload

## [1.2.0] - 2020-10-29
### Added
- Add the Ci/Co models `CiCoOperation` and `ChildCiCoOperation`

## [1.1.2] - 2020-10-19
### Added
- Add the Ci/Co modes `automatic`, `manual`, and `botnet`

## [1.1.1] - 2020-09-15
### Added
- Add the team roles `coordinator` and `driver`

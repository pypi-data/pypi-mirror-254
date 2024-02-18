import ctypes
import json
from enum import IntEnum, IntFlag
from uuid import UUID

from .ctypes_json import CDataJSONEncoder
from dtypes.structify import structify


class PlayerState(IntEnum):
    ON_TRAILER = 0
    ON_WATER = 1


class ClientType(IntEnum):
    USER = 0
    ADMIN = 1
    REFEREE = 2
    SUPER_ADMIN = 3


class FinishStatus(IntEnum):
    LEGAL = 0
    DNF = 1
    DNS = 2
    DQ = 3


class SessionType(IntEnum):
    PRACTICE = 0
    QUALIFYING = 1
    RACE = 2


class SessionStatus(IntEnum):
    WAITING = 0
    MILLING = 1
    RUNNING = 2
    FINISHED = 3


class BuoyType(IntFlag):
    NONE = 0x0
    INNER = 0x1
    OUTER = 0x2
    TURN = 0x4
    START_FINISH = 0x8
    ONE_MINUTE = 0x10


class InfractionTypes(IntEnum):
    UNDER_REVIEW = 0
    START_CLOCK = 1
    DISLODGED_BUOY = 2
    MISSED_BUOY = 3
    ONE_MINUTE = 4
    SPEED_LIMIT = 5
    DMZ = 6
    LANE_VIOLATION = 7
    WRECKLESS_DRIVING = 8


class SeverityTypes(IntEnum):
    AUTO = 0
    INVALID = 1
    WARNING = 2
    ONE_MINUTE = 3
    ONE_LAP = 4
    DQ = 5


class HydroSimConstants:
    MAX_PENALTIES = 128
    MAX_LAPS = 256
    MAX_STRING = 128
    MAX_DESCRIPTION = 1024
    MAX_DRIVERS = 48
    GUID_SIZE = 16
    MAX_ANCHORS = 128
    MAX_BUOYS = 128


class HydroSimStructure(ctypes.Structure):
    _pack_ = 1

    def to_json(self):
        return json.dumps(self, cls=CDataJSONEncoder)

    def __repr__(self):
        return self.to_json()


@structify
class Vec3IPC(HydroSimStructure):
    _pack_ = 1
    x: ctypes.c_float
    y: ctypes.c_float
    z: ctypes.c_float


@structify
class CourseSectorIPC(HydroSimStructure):
    _pack_ = 1
    innerPosition: Vec3IPC
    outerPosition: Vec3IPC
    index: ctypes.c_int
    isStartFinish: ctypes.c_bool
    isOneMinute: ctypes.c_bool


@structify
class BuoyIPC(HydroSimStructure):
    _pack_ = 1
    worldPosition: Vec3IPC
    worldRotation: Vec3IPC
    type: ctypes.c_uint
    dislodged: ctypes.c_bool


@structify
class AreaIPC(HydroSimStructure):
    _pack_ = 1
    top: ctypes.c_double
    bottom: ctypes.c_double
    left: ctypes.c_double
    right: ctypes.c_double
    width: ctypes.c_double
    length: ctypes.c_double
    terrainOffset: Vec3IPC


@structify
class PenaltyIPC(HydroSimStructure):
    _pack_ = 1
    lap: ctypes.c_short
    # See InfractionTypes
    _infraction: ctypes.c_byte
    # See SeverityTypes
    _severity: ctypes.c_byte

    @property
    def infraction(self):
        return InfractionTypes(self._infraction)

    @property
    def severity(self):
        return SeverityTypes(self._severity)


@structify
class DriverIPC(HydroSimStructure):
    _pack_ = 1
    _id: ctypes.c_ubyte * HydroSimConstants.GUID_SIZE
    connectionId: ctypes.c_int
    _name: ctypes.c_char * HydroSimConstants.MAX_STRING
    _team: ctypes.c_char * HydroSimConstants.MAX_STRING
    _hull: ctypes.c_char * HydroSimConstants.MAX_STRING
    _boatClass: ctypes.c_char * HydroSimConstants.MAX_STRING
    lapCount: ctypes.c_int
    _lapTimes: ctypes.c_float * HydroSimConstants.MAX_LAPS
    penaltyCount: ctypes.c_int
    _penalties: PenaltyIPC * HydroSimConstants.MAX_PENALTIES
    worldPosition: Vec3IPC
    worldRotation: Vec3IPC
    trailerPosition: Vec3IPC
    trailerRotation: Vec3IPC
    rpm: ctypes.c_float
    speed: ctypes.c_float
    throttle: ctypes.c_float
    canard: ctypes.c_float
    steer: ctypes.c_float
    distance: ctypes.c_float
    normalizedDistance: ctypes.c_float
    gapLeader: ctypes.c_float
    gapAhead: ctypes.c_float
    gapBehind: ctypes.c_float
    totalTime: ctypes.c_float
    lapTime: ctypes.c_float
    bestLapTime: ctypes.c_float
    lastLapTime: ctypes.c_float
    position: ctypes.c_int
    currentSector: ctypes.c_int
    lap: ctypes.c_int
    bestLap: ctypes.c_int
    lastLap: ctypes.c_int
    isConnected: ctypes.c_bool
    isLocalPlayer: ctypes.c_bool
    isFinished: ctypes.c_bool
    _state: ctypes.c_byte
    _clientType: ctypes.c_byte
    _finishStatus: ctypes.c_byte

    @property
    def name(self):
        return str(self._name, encoding="utf-8")

    @property
    def team(self):
        return str(self._team, encoding="utf-8")

    @property
    def hull(self):
        return str(self._hull, encoding="utf-8")

    @property
    def boatClass(self):
        return str(self._boatClass, encoding="utf-8")

    @property
    def id(self):
        return UUID(bytes=bytes(self._id))

    @property
    def lapTimes(self):
        """
        Returns a sparse list of the lap times
        """
        return [self._lapTimes[i] for i in range(self.lapCount)]

    @property
    def penalties(self):
        """
        Returns a sparse list of the penalties
        """
        return [self._penalties[i] for i in range(self.penaltyCount)]

    @property
    def state(self):
        return PlayerState(self._state)

    @property
    def clientType(self):
        return ClientType(self._clientType)

    @property
    def finishStatus(self):
        return FinishStatus(self._finishStatus)


@structify
class RulesIPC(HydroSimStructure):
    _pack_ = 1
    practiceStartTime: ctypes.c_float
    qualifyingStartTime: ctypes.c_float
    raceStartTime: ctypes.c_float
    windSpeed: ctypes.c_float
    raceLength: ctypes.c_uint
    raceStartClock: ctypes.c_uint
    qualifyingLength: ctypes.c_uint
    qualifyingTime: ctypes.c_uint
    practiceTime: ctypes.c_uint
    maxPenaltiesDQ: ctypes.c_uint
    courseLayout: ctypes.c_int
    oneMinutePin: ctypes.c_bool
    allowReset: ctypes.c_bool
    washdowns: ctypes.c_bool


@structify
class ServerSettingsIPC(HydroSimStructure):
    _pack_ = 1
    update: ctypes.c_uint
    _name: ctypes.c_char * HydroSimConstants.MAX_STRING
    _description: ctypes.c_char * HydroSimConstants.MAX_DESCRIPTION
    _address: ctypes.c_char * HydroSimConstants.MAX_STRING
    # Passwords are only visible to SuperAdmin
    _password: ctypes.c_char * HydroSimConstants.MAX_STRING
    _adminPassword: ctypes.c_char * HydroSimConstants.MAX_STRING
    _refereePassword: ctypes.c_char * HydroSimConstants.MAX_STRING
    port: ctypes.c_int
    maxClients: ctypes.c_uint
    passwordRequired: ctypes.c_bool
    allowMismatches: ctypes.c_bool
    proposedRules: RulesIPC
    currentRules: RulesIPC

    @property
    def name(self):
        return str(self._name, encoding="utf-8")

    @property
    def description(self):
        return str(self._description, encoding="utf-8")

    @property
    def address(self):
        return str(self._address, encoding="utf-8")

    @property
    def password(self):
        return str(self._password, encoding="utf-8")

    @property
    def adminPassword(self):
        return str(self._adminPassword, encoding="utf-8")

    @property
    def refereePassword(self):
        return str(self._refereePassword, encoding="utf-8")


@structify
class HydroSimIPC(HydroSimStructure):
    _pack_ = 1
    _version: ctypes.c_char * HydroSimConstants.MAX_STRING
    _apiVersion: ctypes.c_char * HydroSimConstants.MAX_STRING
    tick: ctypes.c_uint

    @property
    def version(self):
        return str(self._version, encoding="utf-8")

    @property
    def apiVersion(self):
        return str(self._apiVersion, encoding="utf-8")


@structify
class BuoysIPC(HydroSimStructure):
    _pack_ = 1
    update: ctypes.c_uint
    buoyCount: ctypes.c_int
    _buoys: BuoyIPC * HydroSimConstants.MAX_BUOYS

    @property
    def buoys(self):
        """
        Returns a sparse list of the buoys
        """
        return [self._buoys[i] for i in range(self.buoyCount)]


@structify
class TimingIPC(HydroSimStructure):
    _pack_ = 1
    update: ctypes.c_uint
    driverCount: ctypes.c_int
    _drivers: DriverIPC * HydroSimConstants.MAX_DRIVERS

    @property
    def drivers(self):
        """
        Returns a sparse list of the drivers
        """
        return [self._drivers[i] for i in range(self.driverCount)]


@structify
class CourseInfoIPC(HydroSimStructure):
    _pack_ = 1
    update: ctypes.c_uint
    _course: ctypes.c_char * HydroSimConstants.MAX_STRING
    _courseName: ctypes.c_char * HydroSimConstants.MAX_STRING
    _courseLocation: ctypes.c_char * HydroSimConstants.MAX_STRING
    _layout: ctypes.c_char * HydroSimConstants.MAX_STRING
    geographicArea: AreaIPC
    courseLength: ctypes.c_float
    sectorCount: ctypes.c_int
    _sectors: CourseSectorIPC * HydroSimConstants.MAX_ANCHORS
    anchorCount: ctypes.c_int
    _leftAnchors: Vec3IPC * HydroSimConstants.MAX_ANCHORS
    _rightAnchors: Vec3IPC * HydroSimConstants.MAX_ANCHORS

    @property
    def course(self):
        return str(self._course, encoding="utf-8")

    @property
    def courseName(self):
        return str(self._courseName, encoding="utf-8")

    @property
    def courseLocation(self):
        return str(self._courseLocation, encoding="utf-8")

    @property
    def layout(self):
        return str(self._layout, encoding="utf-8")

    @property
    def sectors(self):
        """
        Returns a sparse list of the sectors
        """
        return [self._sectors[i] for i in range(self.sectorCount)]

    @property
    def leftAnchors(self):
        """
        Returns a sparse list of the left anchors
        """
        return [self._leftAnchors[i] for i in range(self.anchorCount)]

    @property
    def rightAnchors(self):
        """
        Returns a sparse list of the right anchors
        """
        return [self._rightAnchors[i] for i in range(self.anchorCount)]


@structify
class SessionIPC(HydroSimStructure):
    _pack_ = 1
    update: ctypes.c_uint
    time: ctypes.c_double
    sessionTime: ctypes.c_double
    startClock: ctypes.c_double
    sessionLength: ctypes.c_float
    windSpeed: ctypes.c_float
    windDirection: ctypes.c_float
    totalLaps: ctypes.c_uint
    lapsComplete: ctypes.c_int
    _currentSession: ctypes.c_byte
    _sessionStatus: ctypes.c_byte

    @property
    def currentSession(self):
        return SessionType(self._currentSession)

    @property
    def sessionStatus(self):
        return SessionStatus(self._sessionStatus)


@structify
class TelemetryIPC(HydroSimStructure):
    _pack_ = 1
    update: ctypes.c_uint
    position: Vec3IPC
    rotation: Vec3IPC
    velocity: Vec3IPC
    angularVelocity: Vec3IPC
    acceleration: Vec3IPC
    localVelocity: Vec3IPC
    localAngularVelocity: Vec3IPC
    rpm: ctypes.c_float
    speed: ctypes.c_float
    propRPM: ctypes.c_float
    throttle: ctypes.c_float
    canard: ctypes.c_float
    rudder: ctypes.c_float
    distance: ctypes.c_float
    normalizedDistance: ctypes.c_float
    lapTime: ctypes.c_float
    lastLapTime: ctypes.c_float
    bestLapTime: ctypes.c_float
    currentSector: ctypes.c_int
    lap: ctypes.c_int
    lastLap: ctypes.c_int
    bestLap: ctypes.c_int
    _state: ctypes.c_byte

    @property
    def state(self):
        return PlayerState(self._state)

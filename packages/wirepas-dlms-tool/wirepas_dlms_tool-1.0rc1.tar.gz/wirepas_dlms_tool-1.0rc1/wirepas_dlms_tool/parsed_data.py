# Copyright 2023 Wirepas Ltd licensed under Apache License, Version 2.0
#
# See file LICENSE for full license details.
#
import logging
from datetime import datetime
from enum import Enum, IntEnum, auto
from gurux_dlms import GXByteBuffer, GXReplyData
from gurux_dlms.enums import ErrorCode

from typing import Any


class NotificationObisEnum(Enum):
    """
    Enumerate to describe all the notification related obis code and name.
    It contains the obis code and the obis name of the data notification.
    """
    EVENT_STATUS_WORD_PUSH = ("0.4.25.9.0.255", "Event Status Word push")
    INSTANTANEOUS_PROFILE = ("0.0.25.9.0.255", "Instantaneous profile")
    BLOCK_LOAD_PROFILE = ("0.5.25.9.0.255", "Block load profile")
    DAILY_LOAD_PROFILE = ("0.6.25.9.0.255", "Daily load profile")
    BILLING_PROFILE = ("0.103.25.9.0.255", "Billing profile")
    NAME_PLATE_DETAILS = ("0.104.25.9.0.255", "Name plate details")
    NIC_STATUS_WORD = ("0.105.25.9.0.255", "NIC status word notification")

    VOLTAGE_EVENTS_LOG_PROFILE = ("0.120.25.9.0.255", "Voltage related events log profile")
    CURRENT_EVENTS_LOG_PROFILE = ("0.121.25.9.0.255", "Current related events log profile")
    POWER_EVENTS_LOG_PROFILE = ("0.122.25.9.0.255", "Power related events log profile")
    TRANSACTION_EVENTS_LOG_PROFILE = ("0.123.25.9.0.255", "Transaction related events log profile")
    OTHER_EVENTS_LOG_PROFILE = ("0.124.25.9.0.255", "Other events log profile")
    NON_ROLLOVER_EVENTS_LOG_PROFILE = ("0.125.25.9.0.255", "Non-rollover events log profile")
    CONTROL_EVENTS_LOG_PROFILE = ("0.126.25.9.0.255", "Control events log profile")

    def __init__(self, obis_code: str, obis_name: str):
        self.obis_code = obis_code
        self.obis_name = obis_name

    @classmethod
    def from_obis_code(cls, obis_code: str):
        """ Return the Notification object corresponding to the obis code. """
        for association_name in NotificationObisEnum.__members__:
            association_values = NotificationObisEnum[association_name]
            if association_values.obis_code == obis_code:
                return association_values


class ConnectionStatusEnum(Enum):
    """ Connection status enumerate for the association between the NIC and the meter. """
    NEVER_TESTED = "00"  # Association never tested.
    TESTED_SUCCESSFUL = "01"  # Association tested and successful.
    TESTED_UNSUCCESSFUL = "10"  # Association tested but unsuccessful.
    UNKNOWN_RESULT = "11"  # Reserved for future uses.

    @classmethod
    def from_bit_string(cls, string: str):
        """ Return the ConnectionStatusEnum corresponding to a bitstring. """
        assert isinstance(string, str) and len(string) == 2, "A connection status must be string of length 2."
        return ConnectionStatusEnum(string)


class FirmwareUpdateStepEnum(IntEnum):
    """ Firmware update step enumerate describing the meter. """
    FIRMWARE_UPDATE_STEP_CHECK_AVAILABILITY = 0
    FIRMWARE_UPDATE_STEP_READ_UPDATE = auto()
    FIRMWARE_UPDATE_STEP_CONNECT = auto()
    FIRMWARE_UPDATE_STEP_CHECK_IF_IMAGE_TRANSFER_IS_ENABLED = auto()
    FIRMWARE_UPDATE_STEP_READ_BLOCK_SIZE = auto()
    FIRMWARE_UPDATE_STEP_CHECK_IMAGE_TRANSFER_STATUS = auto()
    FIRMWARE_UPDATE_STEP_INITIATE_TRANSFER = auto()
    FIRMWARE_UPDATE_STEP_TRANSFER_BLOCK = auto()
    FIRMWARE_UPDATE_STEP_VERIFY_IMAGE = auto()


class FirmwareUpdateResultEnum(IntEnum):
    """ Firmware update result enumerate describing the meter. """
    FIRMWARE_UPDATE_RESULT_OK = 0
    FIRMWARE_UPDATE_RESULT_NO_AVAILABLE_UPDATE = auto()
    FIRMWARE_UPDATE_RESULT_ALREADY_PROCESSED = auto()
    FIRMWARE_UPDATE_RESULT_UPDATE_AVAILABLE = auto()
    FIRMWARE_UPDATE_RESULT_ENABLED = auto()
    FIRMWARE_UPDATE_RESULT_DISABLED = auto()
    FIRMWARE_UPDATE_RESULT_INTERNAL_ERROR = auto()
    FIRMWARE_UPDATE_RESULT_CONNECTION_ERROR = auto()
    FIRMWARE_UPDATE_RESULT_LIB_ERROR = auto()
    FIRMWARE_UPDATE_RESULT_METER_ERROR = auto()
    FIRMWARE_UPDATE_RESULT_OPERATION_FAILED = auto()
    FIRMWARE_UPDATE_RESULT_INVALID_OPERATION = auto()


class ParsedData:
    """ Object to manipulate DLMS data information. It contains the following attributes:

    * source_address (int): Source address of the message.
    * target_address (int): Destination address of the message.
    * invoke_id_and_priority (int): Invoke id and priority value of the message.
    * msg_error_code (ErrorCode): Error code of the message when it is parsed by gurux.
    * value (any): Content value of the message.
    * xml (str): Xml string to represent the parsed data.
    """
    def __init__(self,
                 source_address: int,
                 target_address: int,
                 invoke_id_and_priority: int,
                 msg_error_code: ErrorCode,
                 value: Any = None,
                 xml: str = None):

        self.source_address: int = source_address
        self.target_address: int = target_address
        self.invoke_id_and_priority: int = invoke_id_and_priority
        self.msg_error_code: ErrorCode = ErrorCode(msg_error_code)
        self.value: Any = value
        self.xml: str = xml

    @classmethod
    def from_payload(cls, client, payload: bytes):
        """ Create an instance of the class from a payload and a guruX client to parse the message. """
        xml = None
        try:
            reply = GXReplyData()
            notify = GXReplyData()
            xml = client.message_to_xml(payload.hex())
            is_not_notify = client.gx_client.getData(GXByteBuffer(payload), reply, notify)
            if not is_not_notify:
                logging.warning("The payload could not be parsed.")
                return

            # Set up a new class instance with the data and notify parsed
            return ParsedData(source_address=reply.targetAddress or notify.targetAddress,
                              target_address=reply.sourceAddress or notify.sourceAddress,
                              invoke_id_and_priority=reply.invokeId or notify.invokeId,
                              msg_error_code=ErrorCode(reply.error),
                              value=reply.value,
                              xml=xml)
        except Exception:
            if xml:
                return ParsedData(source_address=None, target_address=None,
                                  msg_error_code=ErrorCode.OTHER_REASON,
                                  invoke_id_and_priority=None, value=None, xml=xml)

    def __str__(self):
        # Return a string containing the class name and all the attributes values of the instance in separate lines.
        classname = self.__class__.__name__
        return classname + "\n" + "\n".join(
                [
                    attribute + ": " + str(value)
                    for attribute, value in self.__dict__.items()
                    if attribute != "xml"
                ]
            )


class WirepasNotification(ParsedData):
    """ Object to manipulate Wirepas DLMS data notification information. It contains the following attributes:

    * source_address (int): Source address of the message.
    * target_address (int): Destination address of the message.
    * invoke_id_and_priority (int): Invoke id and priority value of the message.
    * message_time (datetime): Time of the message when it was sent by the NIC.
    * device_id (bytes): Device ID of the meter sending the data notification message.
    * obis_code (str): String representation of the obis code of the data notification in xxx.xxx.xxx.xxx.xxx.xxx format.
    * obis_name (str): String name associated to the obis code of the message.
    * msg_error_code (ErrorCode): Error code of the message when it is parsed by gurux.
    * value (list): Content value of the message.
    * xml (str): Xml string to represent the parsed data.
    """
    def __init__(self,
                 source_address: int,
                 target_address: int,
                 invoke_id_and_priority: int,
                 message_time: datetime,
                 device_id: bytes,
                 obis_code: str,
                 msg_error_code: ErrorCode,
                 value: list = None,
                 xml: str = None):

        super().__init__(source_address, target_address, invoke_id_and_priority, msg_error_code, value, xml)
        self.message_time = message_time
        self.device_id = device_id
        self.obis_code = obis_code

        notification_obis = NotificationObisEnum.from_obis_code(self.obis_code)
        self.obis_name: str = "Unknown obis code"
        if notification_obis:
            self.obis_name = notification_obis.obis_name

    @classmethod
    def from_payload(cls, client, payload: bytes):
        try:
            notify = GXReplyData()
            data = GXReplyData()
            is_not_notify = client.gx_client.getData(GXByteBuffer(payload), data, notify)
            if is_not_notify or not isinstance(notify.value, list) or len(notify.value) < 4:
                return

            notif_obis = ".".join([str(k) for k in notify.value[1]])
            message_time = client.to_datetime(notify.value[2])
            xml = client.message_to_xml(payload.hex())

            if len(notify.value) == 4:
                value = notify.value[3]
            else:
                return

            # Set up a new class instance with the data and notify parsed
            return WirepasNotification(source_address=data.targetAddress or notify.targetAddress,
                                       target_address=data.sourceAddress or notify.sourceAddress,
                                       invoke_id_and_priority=data.invokeId or notify.invokeId,
                                       message_time=message_time,
                                       device_id=bytes(notify.value[0]),
                                       obis_code=notif_obis,
                                       msg_error_code=ErrorCode(notify.error),
                                       value=value,
                                       xml=xml)
        except Exception:
            return None

    def log_activated_ESW_bits(self):
        """ Log all bits that are set to 1 from the ESW bit string value. """
        esw_bit_values = {
            0: "R Phase - Voltage missing",
            1: "Y Phase - Voltage missing",
            2: "B Phase - Voltage missing",
            3: "Over voltage in any phase",
            4: "Low voltage in any phase",
            5: "Voltage unbalance",
            6: "R Phase current reverse (Import type only)",
            7: "Y Phase current reverse (Import type only)",
            8: "B Phase current reverse (Import type only)",
            9: "Current unbalance",
            10: "Current bypass/short",
            11: "Over current in any phase",
            12: "Very low PF",
            51: "Earth Loading",
            81: "Influence of permanent magnet or ac/dc electromagnet",
            82: "Neutral disturbance - HF, dc or alternate method",
            83: "Meter cover opening",
            84: "Meter load disconnected/Meter load connected",
            85: "Last Gasp - Occurrence",
            86: "First Breath - Restoration",
            87: "Increment in billing counter (Manual/MRI reset)"
        }

        bit_string = self.value.value
        for index, esw_field in esw_bit_values.items():
            if bit_string[index] == '1':
                logging.debug("The following ESW field is activated : %s", esw_field)


class NicStatusWord(WirepasNotification):
    """ Object to manipulate Wirepas DLMS data notification information. It contains the following attributes:

    * source_address (int): Source address of the message.
    * target_address (int): Destination address of the message.
    * invoke_id_and_priority (int): Invoke id and priority value of the message.
    * message_time (datetime): Time of the message when it was sent by the NIC.
    * device_id (bytes): Device ID of the meter sending the data notification message. \
            (None if the meter hasn't been provisioned).
    * serial_number (bytes): Serial Number of the meter (None if the meter has been provisioned).
    * obis_code (str): String representation of the obis code of the data notification in xxx.xxx.xxx.xxx.xxx.xxx format.
    * obis_name (str): String name associated to the obis code of the message.
    * nic_system_title (bytes): System title of the NIC server.
    * US_invocation_counter (int): Invocation counter of the NIC server for US association.
    * PC_connection_status (ConnectionStatusEnum): Connection status of the PC association between the nic and the meter.
    * MR_connection_status (ConnectionStatusEnum): Connection status of the MR association between the nic and the meter.
    * US_connection_status (ConnectionStatusEnum): Connection status of the US association between the nic and the meter.
    * FU_connection_status (ConnectionStatusEnum): Connection status of the FU association between the nic and the meter.
    * fw_update_step (FirmwareUpdateStepEnum): Firmware update step of the meter.
    * fw_update_result (FirmwareUpdateResultEnum): Firmware update result of the meter.
    * msg_error_code (ErrorCode): Error code of the message when it is parsed by gurux.
    * value (list): Content value of the message. These values are also stored in the object attributes.
    * xml (str): Xml string to represent the parsed data.
    """
    def __init__(self,
                 US_invocation_counter: int,
                 PC_connection_status: ConnectionStatusEnum,
                 MR_connection_status: ConnectionStatusEnum,
                 US_connection_status: ConnectionStatusEnum,
                 FU_connection_status: ConnectionStatusEnum,
                 fw_update_step: FirmwareUpdateStepEnum,
                 fw_update_result: FirmwareUpdateResultEnum,
                 nic_system_title: bytes,
                 *args,
                 serial_number: bytes = None,
                 **kwargs):

        super().__init__(*args, **kwargs)
        self.nic_system_title = nic_system_title
        self.US_invocation_counter = US_invocation_counter
        self.PC_connection_status = PC_connection_status
        self.MR_connection_status = MR_connection_status
        self.US_connection_status = US_connection_status
        self.FU_connection_status = FU_connection_status
        self.fw_update_step = fw_update_step
        self.fw_update_result = fw_update_result
        self.serial_number = serial_number

    @classmethod
    def from_payload(cls, client, payload: bytes):
        notification = WirepasNotification.from_payload(client, payload)
        if not notification:
            return None
        elif len(notification.value) not in [3, 5]:
            logging.warning("NIC status word buffer expected to have 3 or 5 fields, but found %d fields.",
                            len(notification.value))

        try:
            connections_status = notification.value[2].value[::-1]
            PC_connection_status = ConnectionStatusEnum.from_bit_string(connections_status[6:8])
            MR_connection_status = ConnectionStatusEnum.from_bit_string(connections_status[4:6])
            US_connection_status = ConnectionStatusEnum.from_bit_string(connections_status[2:4])
            FU_connection_status = ConnectionStatusEnum.from_bit_string(connections_status[0:2])

            if len(notification.value) == 5:
                # The NIC status word follows DLMS app rc4+ specifications.
                fw_update_step=FirmwareUpdateStepEnum(notification.value[3])
                fw_update_result=FirmwareUpdateResultEnum(notification.value[4])
            else:
                # The NIC status word follow RC3 specifications.
                fw_update_step=None
                fw_update_result=None

            # If keys are provisioned, it means that the device id could have been queried
            # and we don't need the serial number.
            serial_number = None
            if US_connection_status != ConnectionStatusEnum.TESTED_SUCCESSFUL:
                serial_number = notification.device_id
                notification.device_id = None

            return NicStatusWord(nic_system_title=bytes(notification.value[0]),
                                 US_invocation_counter=notification.value[1],
                                 PC_connection_status=PC_connection_status,
                                 MR_connection_status=MR_connection_status,
                                 US_connection_status=US_connection_status,
                                 FU_connection_status=FU_connection_status,
                                 fw_update_step=fw_update_step,
                                 fw_update_result=fw_update_result,
                                 source_address=notification.source_address,
                                 target_address=notification.target_address,
                                 invoke_id_and_priority=notification.invoke_id_and_priority,
                                 message_time=notification.message_time,
                                 device_id=notification.device_id,
                                 serial_number=serial_number,
                                 obis_code=notification.obis_code,
                                 msg_error_code=notification.msg_error_code,
                                 value=notification.value,
                                 xml=notification.xml)
        except Exception:
            return None

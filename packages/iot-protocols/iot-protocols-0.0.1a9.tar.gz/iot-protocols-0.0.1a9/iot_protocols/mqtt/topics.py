from abc import ABC
from dataclasses import dataclass


@dataclass
class Topics(ABC):
    field_map = {
    }
    id: str = "+"

    def __repr__(self) -> str:
        return self.path.format(id=self.id)
    
    def __call__(cls, id: str=None, **kwargs):
        obj = super().__new__(cls)
        obj.__init__(id=id, **kwargs)
        return str(obj)
    
    @classmethod
    def get(cls, topic_string: str, field: str) -> str:
        """ Return the corresponding field for the specified topics string """
        try:
            return topic_string.split("/")[cls.field_map[field]]
        except (IndexError, KeyError):
            return None


@dataclass
class UpdateDeviceStatusTopic(Topics):
    field_map = {
        "id": 1
    }
    
    def __repr__(self) -> str:
        return f"devices/{self.id}/update/u"


@dataclass
class ReceiveDeviceUpdateTopic(Topics):
    field_map = {
        "id": 1
    }

    def __repr__(self) -> str:
        return f"devices/{self.id}/update/d"


@dataclass
class SendMeasurementTopic(Topics):
    field_map = {
        "id": 1,
        "type": 3
    }
    type: str="+"

    def __repr__(self) -> str:
        return f"measurements/{self.type}/u/{self.id}"


@dataclass
class SendMeasurementLocallyTopic(Topics):
    """ 
    This topics can be used to send measurents into the local mqtt bus without being sent to the cloud.
    """
    field_map = {
        "id": 1,
        "type": 3
    }
    type: str="+"

    def __repr__(self) -> str:
        return f"measurements/{self.type}/l/{self.id}"


@dataclass
class ReceivedOperationTopic(Topics):
    field_map = {
        "id": 2,
        "type": 1,
        "operation_id": 4
    }
    type: str="+"
    operation_id: str="+"

    def __repr__(self) -> str:
        return f"operations/{self.type}/{self.id}/d/{self.operation_id}"


@dataclass
class UpdateOperationTopic(Topics):
    field_map = {
        "id": 2,
        "type": 1,
        "operation_id": 4
    }
    type: str="+"
    operation_id: str="+"
    
    def __repr__(self) -> str:
        return f"operations/{self.type}/{self.id}/u/{self.operation_id}"


@dataclass
class UpdateAlarmTopic(Topics):
    field_map = {
        "id": 2,
        "type": 1,
        "alarm_id": 4
    }
    type: str="+"
    alarm_id: str="+"

    def __repr__(self) -> str:
        return f"alarms/{self.type}/{self.id}/u/{self.alarm_id}"


@dataclass
class UpdateEventTopic(Topics):
    field_map = {
        "id": 2,
        "type": 1,
    }
    type: str="+"

    def __repr__(self) -> str:
        return f"events/{self.type}/{self.id}/u"


@dataclass
class AddTaskTopic(Topics):
    field_map = {
        "id": 1,
        "task_id": 3
    }
    task_id: str="+"

    def __repr__(self) -> str:
        return f"tasks/{self.id}/add/{self.task_id}"


@dataclass
class RemoveTaskTopic(Topics):
    field_map = {
        "id": 1,
        "task_id": 3
    }
    task_id: str="+"

    def __repr__(self) -> str:
        return f"tasks/{self.id}/remove/{self.task_id}"
    
    
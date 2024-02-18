import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_status import TaskStatus
from ..models.task_type import TaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """
    Attributes:
        id (int):
        task_id (str):
        created_at (Union[None, datetime.datetime]):
        updated_at (Union[None, datetime.datetime]):
        status (Union[Unset, TaskStatus]): * `0` - PENDING
            * `1` - STARTED
            * `2` - RETRY
            * `3` - FAILURE
            * `4` - RECEIVED
            * `5` - REVOKED
            * `9` - SUCCESS
            * `10` - Forced
        is_finished (Union[None, Unset, bool]):
        task_type (Union[Unset, TaskType]): * `0` - assetfinder
            * `1` - amass
            * `2` - subfinder
            * `3` - httpx
            * `4` - nuclei
        scan (Union[None, Unset, int]):
    """

    id: int
    task_id: str
    created_at: Union[None, datetime.datetime]
    updated_at: Union[None, datetime.datetime]
    status: Union[Unset, TaskStatus] = UNSET
    is_finished: Union[None, Unset, bool] = UNSET
    task_type: Union[Unset, TaskType] = UNSET
    scan: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        task_id = self.task_id

        created_at: Union[None, str]
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: Union[None, str]
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_finished: Union[None, Unset, bool]
        if isinstance(self.is_finished, Unset):
            is_finished = UNSET
        else:
            is_finished = self.is_finished

        task_type: Union[Unset, int] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        scan: Union[None, Unset, int]
        if isinstance(self.scan, Unset):
            scan = UNSET
        else:
            scan = self.scan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "task_id": task_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if is_finished is not UNSET:
            field_dict["is_finished"] = is_finished
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if scan is not UNSET:
            field_dict["scan"] = scan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        task_id = d.pop("task_id")

        def _parse_created_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_updated_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, TaskStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskStatus(_status)

        def _parse_is_finished(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_finished = _parse_is_finished(d.pop("is_finished", UNSET))

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, TaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskType(_task_type)

        def _parse_scan(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scan = _parse_scan(d.pop("scan", UNSET))

        task = cls(
            id=id,
            task_id=task_id,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            is_finished=is_finished,
            task_type=task_type,
            scan=scan,
        )

        task.additional_properties = d
        return task

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scan_status import ScanStatus
from ..models.scan_type_n import ScanTypeN
from ..models.scan_type_s import ScanTypeS
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.program import Program
    from ..models.task import Task


T = TypeVar("T", bound="ScanDetailedDetailed")


@_attrs_define
class ScanDetailedDetailed:
    """
    Attributes:
        id (int):
        program (Program): Adds nested create feature
        task_ongoing_or_failed (List['Task']):
        task_not_finished_count (int):
        task_success_count (int):
        task_all_count (int):
        name (str):
        created_at (Union[None, datetime.datetime]):
        updated_at (Union[None, datetime.datetime]):
        status (Union[Unset, ScanStatus]): * `0` - Just Added - Will be Scheduled Soon
            * `1` - Scheduled/Started Enum Phase
            * `2` - Preparing data for HTTPX
            * `3` - Ready for HTTPX
            * `4` - HTTPX Started/Ongoing
            * `5` - Preparing data for Nuclei
            * `6` - Ready for Nuclei
            * `7` - Nuclei Started
            * `8` - Scan Finished
        issues_found (Union[None, Unset, int]):
        comment (Union[None, Unset, str]):
        reason (Union[None, Unset, str]):
        s_type (Union[Unset, ScanTypeS]): * `0` - enum
            * `1` - httpx
            * `2` - enumx
            * `3` - nuclei
            * `4` - full
        n_type (Union[Unset, ScanTypeN]): * `0` - local
            * `1` - full
            * `2` - new
            * `3` - blocked
        e_type (Union[None, Unset, int]):
    """

    id: int
    program: "Program"
    task_ongoing_or_failed: List["Task"]
    task_not_finished_count: int
    task_success_count: int
    task_all_count: int
    name: str
    created_at: Union[None, datetime.datetime]
    updated_at: Union[None, datetime.datetime]
    status: Union[Unset, ScanStatus] = UNSET
    issues_found: Union[None, Unset, int] = UNSET
    comment: Union[None, Unset, str] = UNSET
    reason: Union[None, Unset, str] = UNSET
    s_type: Union[Unset, ScanTypeS] = UNSET
    n_type: Union[Unset, ScanTypeN] = UNSET
    e_type: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        program = self.program.to_dict()

        task_ongoing_or_failed = []
        for task_ongoing_or_failed_item_data in self.task_ongoing_or_failed:
            task_ongoing_or_failed_item = task_ongoing_or_failed_item_data.to_dict()
            task_ongoing_or_failed.append(task_ongoing_or_failed_item)

        task_not_finished_count = self.task_not_finished_count

        task_success_count = self.task_success_count

        task_all_count = self.task_all_count

        name = self.name

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

        issues_found: Union[None, Unset, int]
        if isinstance(self.issues_found, Unset):
            issues_found = UNSET
        else:
            issues_found = self.issues_found

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        s_type: Union[Unset, int] = UNSET
        if not isinstance(self.s_type, Unset):
            s_type = self.s_type.value

        n_type: Union[Unset, int] = UNSET
        if not isinstance(self.n_type, Unset):
            n_type = self.n_type.value

        e_type: Union[None, Unset, int]
        if isinstance(self.e_type, Unset):
            e_type = UNSET
        else:
            e_type = self.e_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "program": program,
                "task_ongoing_or_failed": task_ongoing_or_failed,
                "task_not_finished_count": task_not_finished_count,
                "task_success_count": task_success_count,
                "task_all_count": task_all_count,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if issues_found is not UNSET:
            field_dict["issues_found"] = issues_found
        if comment is not UNSET:
            field_dict["comment"] = comment
        if reason is not UNSET:
            field_dict["reason"] = reason
        if s_type is not UNSET:
            field_dict["s_type"] = s_type
        if n_type is not UNSET:
            field_dict["n_type"] = n_type
        if e_type is not UNSET:
            field_dict["e_type"] = e_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.program import Program
        from ..models.task import Task

        d = src_dict.copy()
        id = d.pop("id")

        program = Program.from_dict(d.pop("program"))

        task_ongoing_or_failed = []
        _task_ongoing_or_failed = d.pop("task_ongoing_or_failed")
        for task_ongoing_or_failed_item_data in _task_ongoing_or_failed:
            task_ongoing_or_failed_item = Task.from_dict(task_ongoing_or_failed_item_data)

            task_ongoing_or_failed.append(task_ongoing_or_failed_item)

        task_not_finished_count = d.pop("task_not_finished_count")

        task_success_count = d.pop("task_success_count")

        task_all_count = d.pop("task_all_count")

        name = d.pop("name")

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
        status: Union[Unset, ScanStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScanStatus(_status)

        def _parse_issues_found(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        issues_found = _parse_issues_found(d.pop("issues_found", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason = _parse_reason(d.pop("reason", UNSET))

        _s_type = d.pop("s_type", UNSET)
        s_type: Union[Unset, ScanTypeS]
        if isinstance(_s_type, Unset):
            s_type = UNSET
        else:
            s_type = ScanTypeS(_s_type)

        _n_type = d.pop("n_type", UNSET)
        n_type: Union[Unset, ScanTypeN]
        if isinstance(_n_type, Unset):
            n_type = UNSET
        else:
            n_type = ScanTypeN(_n_type)

        def _parse_e_type(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        e_type = _parse_e_type(d.pop("e_type", UNSET))

        scan_detailed_detailed = cls(
            id=id,
            program=program,
            task_ongoing_or_failed=task_ongoing_or_failed,
            task_not_finished_count=task_not_finished_count,
            task_success_count=task_success_count,
            task_all_count=task_all_count,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            issues_found=issues_found,
            comment=comment,
            reason=reason,
            s_type=s_type,
            n_type=n_type,
            e_type=e_type,
        )

        scan_detailed_detailed.additional_properties = d
        return scan_detailed_detailed

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

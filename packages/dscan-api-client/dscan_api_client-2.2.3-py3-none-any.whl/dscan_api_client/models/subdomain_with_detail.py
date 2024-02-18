import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subdomain_detail import SubdomainDetail


T = TypeVar("T", bound="SubdomainWithDetail")


@_attrs_define
class SubdomainWithDetail:
    """
    Attributes:
        id (int):
        subdomaindetail (SubdomainDetail):
        name (str):
        created_at (Union[None, datetime.datetime]):
        updated_at (Union[None, datetime.datetime]):
        enabled (Union[Unset, bool]):
        is_blocked (Union[None, Unset, bool]):
        program (Union[None, Unset, int]):
    """

    id: int
    subdomaindetail: "SubdomainDetail"
    name: str
    created_at: Union[None, datetime.datetime]
    updated_at: Union[None, datetime.datetime]
    enabled: Union[Unset, bool] = UNSET
    is_blocked: Union[None, Unset, bool] = UNSET
    program: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        subdomaindetail = self.subdomaindetail.to_dict()

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

        enabled = self.enabled

        is_blocked: Union[None, Unset, bool]
        if isinstance(self.is_blocked, Unset):
            is_blocked = UNSET
        else:
            is_blocked = self.is_blocked

        program: Union[None, Unset, int]
        if isinstance(self.program, Unset):
            program = UNSET
        else:
            program = self.program

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "subdomaindetail": subdomaindetail,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if is_blocked is not UNSET:
            field_dict["is_blocked"] = is_blocked
        if program is not UNSET:
            field_dict["program"] = program

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subdomain_detail import SubdomainDetail

        d = src_dict.copy()
        id = d.pop("id")

        subdomaindetail = SubdomainDetail.from_dict(d.pop("subdomaindetail"))

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

        enabled = d.pop("enabled", UNSET)

        def _parse_is_blocked(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_blocked = _parse_is_blocked(d.pop("is_blocked", UNSET))

        def _parse_program(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        program = _parse_program(d.pop("program", UNSET))

        subdomain_with_detail = cls(
            id=id,
            subdomaindetail=subdomaindetail,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            enabled=enabled,
            is_blocked=is_blocked,
            program=program,
        )

        subdomain_with_detail.additional_properties = d
        return subdomain_with_detail

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

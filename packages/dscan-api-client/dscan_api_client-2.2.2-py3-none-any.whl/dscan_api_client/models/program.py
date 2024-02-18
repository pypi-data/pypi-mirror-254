import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain import Domain


T = TypeVar("T", bound="Program")


@_attrs_define
class Program:
    """Adds nested create feature

    Attributes:
        id (int):
        name (str):
        url (str):
        bounty (bool):
        enabled (bool):
        created_at (Union[None, datetime.datetime]):
        updated_at (Union[None, datetime.datetime]):
        domain (Union[Unset, List['Domain']]):
        priority (Union[Unset, int]):
    """

    id: int
    name: str
    url: str
    bounty: bool
    enabled: bool
    created_at: Union[None, datetime.datetime]
    updated_at: Union[None, datetime.datetime]
    domain: Union[Unset, List["Domain"]] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        url = self.url

        bounty = self.bounty

        enabled = self.enabled

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

        domain: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.domain, Unset):
            domain = []
            for domain_item_data in self.domain:
                domain_item = domain_item_data.to_dict()
                domain.append(domain_item)

        priority = self.priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
                "bounty": bounty,
                "enabled": enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain import Domain

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        url = d.pop("url")

        bounty = d.pop("bounty")

        enabled = d.pop("enabled")

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

        domain = []
        _domain = d.pop("domain", UNSET)
        for domain_item_data in _domain or []:
            domain_item = Domain.from_dict(domain_item_data)

            domain.append(domain_item)

        priority = d.pop("priority", UNSET)

        program = cls(
            id=id,
            name=name,
            url=url,
            bounty=bounty,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            domain=domain,
            priority=priority,
        )

        program.additional_properties = d
        return program

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

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain import Domain


T = TypeVar("T", bound="PatchedProgram")


@_attrs_define
class PatchedProgram:
    """Adds nested create feature

    Attributes:
        id (Union[Unset, int]):
        domain (Union[Unset, List['Domain']]):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
        bounty (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        priority (Union[Unset, int]):
        created_at (Union[None, Unset, datetime.datetime]):
        updated_at (Union[None, Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    domain: Union[Unset, List["Domain"]] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    bounty: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    priority: Union[Unset, int] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        domain: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.domain, Unset):
            domain = []
            for domain_item_data in self.domain:
                domain_item = domain_item_data.to_dict()
                domain.append(domain_item)

        name = self.name

        url = self.url

        bounty = self.bounty

        enabled = self.enabled

        priority = self.priority

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if domain is not UNSET:
            field_dict["domain"] = domain
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if bounty is not UNSET:
            field_dict["bounty"] = bounty
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if priority is not UNSET:
            field_dict["priority"] = priority
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain import Domain

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        domain = []
        _domain = d.pop("domain", UNSET)
        for domain_item_data in _domain or []:
            domain_item = Domain.from_dict(domain_item_data)

            domain.append(domain_item)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        bounty = d.pop("bounty", UNSET)

        enabled = d.pop("enabled", UNSET)

        priority = d.pop("priority", UNSET)

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        patched_program = cls(
            id=id,
            domain=domain,
            name=name,
            url=url,
            bounty=bounty,
            enabled=enabled,
            priority=priority,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_program.additional_properties = d
        return patched_program

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scanner_type import ScannerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Scanner")


@_attrs_define
class Scanner:
    """
    Attributes:
        id (int):
        name (str):
        enabled (bool):
        created_at (Union[None, datetime.datetime]):
        updated_at (Union[None, datetime.datetime]):
        s_type (Union[Unset, ScannerType]): * `0` - k8s
            * `1` - enumerator
            * `2` - httpx
            * `3` - nuclei
        config (Union[None, Unset, str]):
        comment (Union[None, Unset, str]):
        version (Union[None, Unset, str]):
        commit (Union[None, Unset, str]):
    """

    id: int
    name: str
    enabled: bool
    created_at: Union[None, datetime.datetime]
    updated_at: Union[None, datetime.datetime]
    s_type: Union[Unset, ScannerType] = UNSET
    config: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    commit: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

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

        s_type: Union[Unset, int] = UNSET
        if not isinstance(self.s_type, Unset):
            s_type = self.s_type.value

        config: Union[None, Unset, str]
        if isinstance(self.config, Unset):
            config = UNSET
        else:
            config = self.config

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        commit: Union[None, Unset, str]
        if isinstance(self.commit, Unset):
            commit = UNSET
        else:
            commit = self.commit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "enabled": enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if s_type is not UNSET:
            field_dict["s_type"] = s_type
        if config is not UNSET:
            field_dict["config"] = config
        if comment is not UNSET:
            field_dict["comment"] = comment
        if version is not UNSET:
            field_dict["version"] = version
        if commit is not UNSET:
            field_dict["commit"] = commit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

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

        _s_type = d.pop("s_type", UNSET)
        s_type: Union[Unset, ScannerType]
        if isinstance(_s_type, Unset):
            s_type = UNSET
        else:
            s_type = ScannerType(_s_type)

        def _parse_config(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_commit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        commit = _parse_commit(d.pop("commit", UNSET))

        scanner = cls(
            id=id,
            name=name,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            s_type=s_type,
            config=config,
            comment=comment,
            version=version,
            commit=commit,
        )

        scanner.additional_properties = d
        return scanner

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

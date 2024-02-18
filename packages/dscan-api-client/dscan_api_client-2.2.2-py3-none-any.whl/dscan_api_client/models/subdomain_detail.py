import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubdomainDetail")


@_attrs_define
class SubdomainDetail:
    """
    Attributes:
        id (int):
        is_online (bool):
        created_at (Union[None, datetime.datetime]):
        status_code (Union[None, Unset, int]):
        content_length (Union[None, Unset, int]):
        content_type (Union[None, Unset, str]):
        asn_info (Union[None, Unset, str]):
        cdn (Union[None, Unset, str]):
        technology (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        url (Union[None, Unset, str]):
        subdomain (Union[None, Unset, int]):
        scan (Union[None, Unset, int]):
    """

    id: int
    is_online: bool
    created_at: Union[None, datetime.datetime]
    status_code: Union[None, Unset, int] = UNSET
    content_length: Union[None, Unset, int] = UNSET
    content_type: Union[None, Unset, str] = UNSET
    asn_info: Union[None, Unset, str] = UNSET
    cdn: Union[None, Unset, str] = UNSET
    technology: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    subdomain: Union[None, Unset, int] = UNSET
    scan: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_online = self.is_online

        created_at: Union[None, str]
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        status_code: Union[None, Unset, int]
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        content_length: Union[None, Unset, int]
        if isinstance(self.content_length, Unset):
            content_length = UNSET
        else:
            content_length = self.content_length

        content_type: Union[None, Unset, str]
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        asn_info: Union[None, Unset, str]
        if isinstance(self.asn_info, Unset):
            asn_info = UNSET
        else:
            asn_info = self.asn_info

        cdn: Union[None, Unset, str]
        if isinstance(self.cdn, Unset):
            cdn = UNSET
        else:
            cdn = self.cdn

        technology: Union[None, Unset, str]
        if isinstance(self.technology, Unset):
            technology = UNSET
        else:
            technology = self.technology

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        subdomain: Union[None, Unset, int]
        if isinstance(self.subdomain, Unset):
            subdomain = UNSET
        else:
            subdomain = self.subdomain

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
                "is_online": is_online,
                "created_at": created_at,
            }
        )
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if content_length is not UNSET:
            field_dict["content_length"] = content_length
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if asn_info is not UNSET:
            field_dict["asn_info"] = asn_info
        if cdn is not UNSET:
            field_dict["cdn"] = cdn
        if technology is not UNSET:
            field_dict["technology"] = technology
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain
        if scan is not UNSET:
            field_dict["scan"] = scan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        is_online = d.pop("is_online")

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

        def _parse_status_code(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        status_code = _parse_status_code(d.pop("status_code", UNSET))

        def _parse_content_length(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        content_length = _parse_content_length(d.pop("content_length", UNSET))

        def _parse_content_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))

        def _parse_asn_info(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asn_info = _parse_asn_info(d.pop("asn_info", UNSET))

        def _parse_cdn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cdn = _parse_cdn(d.pop("cdn", UNSET))

        def _parse_technology(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        technology = _parse_technology(d.pop("technology", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_subdomain(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        subdomain = _parse_subdomain(d.pop("subdomain", UNSET))

        def _parse_scan(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scan = _parse_scan(d.pop("scan", UNSET))

        subdomain_detail = cls(
            id=id,
            is_online=is_online,
            created_at=created_at,
            status_code=status_code,
            content_length=content_length,
            content_type=content_type,
            asn_info=asn_info,
            cdn=cdn,
            technology=technology,
            title=title,
            url=url,
            subdomain=subdomain,
            scan=scan,
        )

        subdomain_detail.additional_properties = d
        return subdomain_detail

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

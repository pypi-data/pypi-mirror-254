from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultipartFileDownloadResponse200")


@_attrs_define
class MultipartFileDownloadResponse200:
    """
    Attributes:
        part_content (List[int]):
        file_size (Union[Unset, int]):
        next_part_number (Union[Unset, int]):
    """

    part_content: List[int]
    file_size: Union[Unset, int] = UNSET
    next_part_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        part_content = self.part_content

        file_size = self.file_size
        next_part_number = self.next_part_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "part_content": part_content,
            }
        )
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if next_part_number is not UNSET:
            field_dict["next_part_number"] = next_part_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        part_content = cast(List[int], d.pop("part_content"))

        file_size = d.pop("file_size", UNSET)

        next_part_number = d.pop("next_part_number", UNSET)

        multipart_file_download_response_200 = cls(
            part_content=part_content,
            file_size=file_size,
            next_part_number=next_part_number,
        )

        multipart_file_download_response_200.additional_properties = d
        return multipart_file_download_response_200

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

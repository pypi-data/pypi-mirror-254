from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MultipartFileUploadJsonBodyPartsItem")


@_attrs_define
class MultipartFileUploadJsonBodyPartsItem:
    """
    Attributes:
        part_number (int):
        tag (str):
    """

    part_number: int
    tag: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        part_number = self.part_number
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "part_number": part_number,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        part_number = d.pop("part_number")

        tag = d.pop("tag")

        multipart_file_upload_json_body_parts_item = cls(
            part_number=part_number,
            tag=tag,
        )

        multipart_file_upload_json_body_parts_item.additional_properties = d
        return multipart_file_upload_json_body_parts_item

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

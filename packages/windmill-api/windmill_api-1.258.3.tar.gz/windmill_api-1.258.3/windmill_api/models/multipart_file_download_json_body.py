from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultipartFileDownloadJsonBody")


@_attrs_define
class MultipartFileDownloadJsonBody:
    """
    Attributes:
        file_key (str):
        part_number (int):
        file_size (Union[Unset, int]):
        s3_resource_path (Union[Unset, str]):
    """

    file_key: str
    part_number: int
    file_size: Union[Unset, int] = UNSET
    s3_resource_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_key = self.file_key
        part_number = self.part_number
        file_size = self.file_size
        s3_resource_path = self.s3_resource_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_key": file_key,
                "part_number": part_number,
            }
        )
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if s3_resource_path is not UNSET:
            field_dict["s3_resource_path"] = s3_resource_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_key = d.pop("file_key")

        part_number = d.pop("part_number")

        file_size = d.pop("file_size", UNSET)

        s3_resource_path = d.pop("s3_resource_path", UNSET)

        multipart_file_download_json_body = cls(
            file_key=file_key,
            part_number=part_number,
            file_size=file_size,
            s3_resource_path=s3_resource_path,
        )

        multipart_file_download_json_body.additional_properties = d
        return multipart_file_download_json_body

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

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multipart_file_upload_json_body_parts_item import MultipartFileUploadJsonBodyPartsItem


T = TypeVar("T", bound="MultipartFileUploadJsonBody")


@_attrs_define
class MultipartFileUploadJsonBody:
    """
    Attributes:
        part_content (List[int]):
        parts (List['MultipartFileUploadJsonBodyPartsItem']):
        is_final (bool):
        cancel_upload (bool):
        file_key (Union[Unset, str]):
        file_extension (Union[Unset, str]):
        upload_id (Union[Unset, str]):
        s3_resource_path (Union[Unset, str]):
        file_expiration (Union[Unset, datetime.datetime]):
    """

    part_content: List[int]
    parts: List["MultipartFileUploadJsonBodyPartsItem"]
    is_final: bool
    cancel_upload: bool
    file_key: Union[Unset, str] = UNSET
    file_extension: Union[Unset, str] = UNSET
    upload_id: Union[Unset, str] = UNSET
    s3_resource_path: Union[Unset, str] = UNSET
    file_expiration: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        part_content = self.part_content

        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()

            parts.append(parts_item)

        is_final = self.is_final
        cancel_upload = self.cancel_upload
        file_key = self.file_key
        file_extension = self.file_extension
        upload_id = self.upload_id
        s3_resource_path = self.s3_resource_path
        file_expiration: Union[Unset, str] = UNSET
        if not isinstance(self.file_expiration, Unset):
            file_expiration = self.file_expiration.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "part_content": part_content,
                "parts": parts,
                "is_final": is_final,
                "cancel_upload": cancel_upload,
            }
        )
        if file_key is not UNSET:
            field_dict["file_key"] = file_key
        if file_extension is not UNSET:
            field_dict["file_extension"] = file_extension
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id
        if s3_resource_path is not UNSET:
            field_dict["s3_resource_path"] = s3_resource_path
        if file_expiration is not UNSET:
            field_dict["file_expiration"] = file_expiration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multipart_file_upload_json_body_parts_item import MultipartFileUploadJsonBodyPartsItem

        d = src_dict.copy()
        part_content = cast(List[int], d.pop("part_content"))

        parts = []
        _parts = d.pop("parts")
        for parts_item_data in _parts:
            parts_item = MultipartFileUploadJsonBodyPartsItem.from_dict(parts_item_data)

            parts.append(parts_item)

        is_final = d.pop("is_final")

        cancel_upload = d.pop("cancel_upload")

        file_key = d.pop("file_key", UNSET)

        file_extension = d.pop("file_extension", UNSET)

        upload_id = d.pop("upload_id", UNSET)

        s3_resource_path = d.pop("s3_resource_path", UNSET)

        _file_expiration = d.pop("file_expiration", UNSET)
        file_expiration: Union[Unset, datetime.datetime]
        if isinstance(_file_expiration, Unset):
            file_expiration = UNSET
        else:
            file_expiration = isoparse(_file_expiration)

        multipart_file_upload_json_body = cls(
            part_content=part_content,
            parts=parts,
            is_final=is_final,
            cancel_upload=cancel_upload,
            file_key=file_key,
            file_extension=file_extension,
            upload_id=upload_id,
            s3_resource_path=s3_resource_path,
            file_expiration=file_expiration,
        )

        multipart_file_upload_json_body.additional_properties = d
        return multipart_file_upload_json_body

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

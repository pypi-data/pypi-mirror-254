import binascii
import io
import re
import struct
from typing import BinaryIO, Union, Optional

from pyrogram import Client
from pyrogram.types import InlineQuery
from pyrogram.file_id import FileId, FileType
from pyrogram.raw.functions import messages
from pyrogram.raw.types import InputPeerSelf, InputMediaUploadedDocument


class Utils:

    async def upload_sticker(self: Client, file: Union[str, BinaryIO]) -> str:
        sticker = await self.invoke(
            messages.UploadMedia(
                peer=InputPeerSelf(),
                media=InputMediaUploadedDocument(
                    mime_type=self.guess_mime_type(file.name if isinstance(file, io.BytesIO) else file),
                    file=await self.save_file(file),
                    attributes=[]
                )
            )
        )
        file_id = FileId(
            file_type=FileType.STICKER,
            dc_id=sticker.document.dc_id,
            media_id=sticker.document.id,
            access_hash=sticker.document.access_hash,
            file_reference=sticker.document.file_reference,
        ).encode()
        return file_id

    async def get_file_id_from_query(self: Client, query: InlineQuery) -> Optional[str]:
        match = query.matches[-1]
        file_id = match.group('FILE_ID')
        if file_id is None:
            if match.group('MSG_ID') is None:
                return None
            msg_id = int(match.group('MSG_ID'))
            msg = await self.get_messages(query.from_user.id, msg_id)
            if msg.sticker is None:
                return None
            file_id = msg.sticker.file_id
        return file_id if check_sticker(file_id) else None

def decode_file_id(file_id) -> Optional[FileId]:
    try:
        return FileId.decode(file_id)
    except (binascii.Error, struct.error):
        return None


def check_sticker(file_id) -> bool:
    fileid = decode_file_id(file_id)
    return (fileid.file_type == FileType.STICKER) if fileid else False


def write_sticker_pillow(image) -> BinaryIO:
    output = io.BytesIO()
    output.name = 'sticker.webp'
    image.save(output, 'WEBP')
    return output

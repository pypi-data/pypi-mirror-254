from .meta_audio import MetaAudio
from .meta_mp3 import MetaMP3
from .meta_mp4 import MetaMP4
from .meta_flac import MetaFLAC
from .meta_dsf import MetaDSF
from .meta_opus import MetaOpus
from .meta_vorbis import MetaVorbis
from .meta_wav import MetaWAV
from typing import Union

EXT_TO_CONSTRUCTOR = {
  'mp3': MetaMP3,
  'm4a': MetaMP4,
  'm4b': MetaMP4,
  'flac': MetaFLAC,
  'dsf': MetaDSF,
  'opus': MetaOpus,
  'ogg': MetaVorbis,
  'wav': MetaWAV,
}

def get_meta(path: str) -> Union[MetaAudio, None]:
  ext = path.split('.')[-1].lower()
  constructor = EXT_TO_CONSTRUCTOR[ext]
  if constructor:
    return constructor(path)
  return None

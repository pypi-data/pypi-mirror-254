from bpm_ai_core.speech.stt.stt import STTModel
from bpm_ai_core.util.audio import is_supported_audio_file
from bpm_ai_core.util.image import is_supported_img_file


def prepare_images(input_data: dict):
    return {
        k: f"[# image {v} #]"
        if (isinstance(v, str) and is_supported_img_file(v))
        else v for k, v in input_data.items()
    }


def prepare_audio(input_data: dict, stt: STTModel | None):
    return {
        k: stt.transcribe(v)
        if (stt and isinstance(v, str) and is_supported_audio_file(v))
        else v for k, v in input_data.items()
    }
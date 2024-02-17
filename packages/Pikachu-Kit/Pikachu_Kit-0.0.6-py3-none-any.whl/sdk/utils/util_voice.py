#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: util_voice.py
@time: 2023/5/28 14:16
@desc:
"""
import os
from typing import Tuple, List
from pydub import AudioSegment
from pydub.silence import detect_silence
from sdk.utils.util_file import FileProcess
from sdk.utils.util_folder import FolderProcess
from sdk.utils.util_cmd import RunCmd


class VoiceProcess():
    """
    音频处理
    """

    def __init__(self):
        self.file = FileProcess()
        self.cmd = RunCmd()

    def read_vioce(self, file: str,format=None) -> AudioSegment:
        """
        读取音频
        :param file:
        :return:
        """
        if not format:
            format = self.file.get_file_tail(file)

        return AudioSegment.from_file(
            file, format=format)

    def get_total_duration(self, audio) -> int:
        """
        获取音频时长
        :param audio:
        :return: 毫秒
        """
        duration = audio.duration_seconds
        return duration * 1000

    def cut_voice(self, audio: AudioSegment, begin: int,
                  end: int) -> AudioSegment:
        """
        切割音频
        :param audio:
        :param begin:毫秒
        :param end:毫秒
        :return:
        """
        return audio[begin:end]

    def merge_videos(self, voice_lists: List[AudioSegment]) -> AudioSegment:
        """
        合并音频
        :param audio1:
        :param audio2:
        :return:
        """
        return sum(voice_lists)

    def save_video(self, audio: AudioSegment, save_file: str):
        """
        保存音频
        :param audio:
        :param save_file:
        :return:
        """
        audio.export(
            save_file,
            format=self.file.get_file_tail(save_file).replace(
                ".",
                ""))

    def adjust_vioce(self, audio: AudioSegment, num: int):
        """
        调整音量
        :param audio:
        :param num:
        :return:
        """
        return audio + num

    def get_sample_rate(self, audio: AudioSegment) -> int:
        """
        获取采样率
        :param audio:
        :return:
        """
        return audio.frame_rate

    def resample_voice(self, audio: AudioSegment, rate: int) -> AudioSegment:
        """
        重采样
        :param audio:
        :param rate:采样率
        :return:
        """
        return audio.set_frame_rate(rate)

    def get_blank_voice(self, audio: AudioSegment,
                        min_len: int = 3000, db: int = -35) -> Tuple[int, int]:
        """
        识别空白音
        :param audio:
        :param db:分贝
        :return: 所有静音片段开始和结束时间
        """
        silence_ranges = detect_silence(audio, db, min_len, 1)
        for start, end in silence_ranges:
            yield (start, end)

    def ms_timedelete(self, millis: int) -> str:
        """
        毫秒转换成 小时：分钟：秒.毫秒 格式
        :param millis:
        :return:
        """
        seconds = int((millis / 1000) % 60)
        minutes = int((millis / (1000 * 60)) % 60)
        hours = int((millis / (1000 * 60 * 60)) % 24)
        lay = millis - hours * 1000 * 60 * 60 - minutes * 1000 * 60 - seconds * 1000
        return "{}:{}:{}.{}".format(
            str(hours).rjust(2, "0"),
            str(minutes).rjust(2, "0"),
            str(seconds).rjust(2, "0"),
            str(lay)
        )

    def voice_time_ms(self, time_voice: str):
        """
        小时：分钟：秒.毫秒 转换成 毫秒
        :param time_voice:
        :return:
        """
        min = time_voice.split(":")[0]
        ms = time_voice.split(".")[-1]
        s = time_voice.split(":")[1].split(".")[0]
        return (60 * int(min) + int(s)) * 1000 + int(ms) * 10

    def get_channels(self, audio: AudioSegment) -> AudioSegment:
        """
        拆分音频声道数据
        :param audio:
        :return:
        """
        return audio.split_to_mono()

    def add_blank_voice(self, audio: AudioSegment, start: int,
                        duration: int = 1000) -> AudioSegment:
        """
        批量在指定时间节点插入空白音频
        :param audio: 待插入音频
        :param start_list: 插入时间节点
        :param duration: 空白音持续时长
        :return:
        """
        blank = AudioSegment.silent(duration)
        new_audio = audio[0:start] + blank + audio[start:]
        return new_audio

    def mix_mp4_mp3(self, mp4: str, mp3: str, out: str,
                    ffmpeg_path: str = None):
        """
        合并音视频
        :param mp4:
        :param mp3:
        :param out:
        :return:
        """
        if not ffmpeg_path:
            self.folder = FolderProcess()
            path = self.folder.split_path(os.path.realpath(__file__), "sdk")
            ffmpeg_path = self.folder.merge_path(
                [path[0], "sdk", "plugins", "ffmpeg", "ffmpeg.exe"])

        cmd = "{} -i {} -i {} -acodec copy -vcodec copy {}".format(
            ffmpeg_path, mp4, mp3, out
        )
        for res in self.cmd.run(cmd):
            yield res

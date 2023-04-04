import os
import pygame

class MusicPlayer:
    def __init__(self):
        #初始化pygame
        pygame.init()
        #读取路径
        self.music_path = "此处填入下载音乐的路径"
        #获取音乐列表
        self.music_list = self.get_music_list()
        #设置当前播放索引
        self.current_index = 0
        #加载音乐
        self.load_music()

    def get_music_list(self):
        #获取文件列表
        file_list = os.listdir(self.music_path)
        #过滤音乐文件
        music_list = [filename for filename in file_list if filename.endswith(".mp3"".flac"".wav")]
        return music_list

    def load_music(self):
        #获取当前音乐的文件路径
        music_file = os.path.join(self.music_path,self.music_list[self.current_index])
        #加载文件
        pygame.mixer.music.load(music_file)

    def play(self):
        #播放音乐
        pygame.mixer.music.play()

    def pause(self):
        #暂停播放
        pygame.mixer.music.pause()

    def unpause(self):
        #继续播放
        pygame.mixer.music.unpause()

    def stop(self):
        #停止播放
        pygame.mixer.music.stop()

    def next(self):
        #下一首
        self.current_index = (self.current_index + 1) % len(self.music_list)
        self.load_music()
        self.play()

    def prev(self):
        #上一首
        self.current_index = (self.current_index - 1) % len(self.music_list)
        self.load_music()
        self.play()

if __name__ == '__main__':
    player = MusicPlayer()
    player.play()



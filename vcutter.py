from moviepy.editor import *

# 編集したい動画のパス
file_path = "hyokkorihan.mp4"

# 切り出し開始時刻。秒で表現
start = 19    

# 切り出し終了時刻。同じく秒で表現
end = 24    

# 編集後のファイル保存先のパス
save_path = "cat_shiraishi.mp4"    

# ビデオのカット開始
video = VideoFileClip(file_path).subclip(start, end)    

# fps and save
video.write_videofile(save_path,fps=29)    
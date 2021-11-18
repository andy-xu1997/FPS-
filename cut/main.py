import os
import cv2

cut_frame = 14  # 多少帧截一次，自己设置就行
save_path = "D:\workspace\FPS-\cut\p" #保存图片的文件夹

for root, dirs, files in os.walk(r"D:\workspace\FPS-\cut\v"):  # 这里就填文件夹目录就可以了
    for file in files:
        # 获取文件路径
        if ('.mp4' in file):
            path = os.path.join(root, file)
            video = cv2.VideoCapture(path)
            video_fps = int(video.get(cv2.CAP_PROP_FPS))
            print(video_fps)
            current_frame = 0
            while (True):
                ret, image = video.read()
                current_frame = current_frame + 1
                if ret is False:
                    video.release()
                    break
                if current_frame % cut_frame == 0:
                    # cv2.imwrite(save_path + '/' + file[:-4] + str(current_frame) + '.jpg',
                    #             image)  # file[:-4]是去掉了".mp4"后缀名，这里我的命名格式是，视频文件名+当前帧数+.jpg，使用imwrite就不能有中文路径和中文文件名
                    cv2.imencode('.jpg', image)[1].tofile(save_path + '/' + file[:-4] + str(current_frame) + '.jpg') #使用imencode就可以整个路径中可以包括中文，文件名也可以是中文
                    print('正在保存' + file + save_path + '/' + file[:-4] + str(current_frame))

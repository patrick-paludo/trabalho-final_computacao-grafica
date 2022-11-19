import cv2
import numpy as np
import random

def checkFile(file):
    contents = file.file.read()

    if (file.content_type == 'image/jpeg'):
        blurImage(contents)
    elif (file.content_type == 'video/mp4'):
        # blurVideo(contents)
        return "video"
    else:
        return "O arquivo não é uma imagem ou um vídeo"

def blurImage(contents):
    print("passou aqui")
    imagemNp = np.frombuffer(contents, dtype=np.uint8)
    imagem = cv2.imdecode(imagemNp, flags=1)

    classificador = cv2.CascadeClassifier('/home/ppaludo/dev/trabalho-final_computacao-grafica/api/hooks/cascades/haarcascade_frontalface_default.xml')

    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    facesDetectadas = classificador.detectMultiScale(imagemCinza)

    for(x, y, largura, altura) in facesDetectadas:
        blur = imagem[y:y+altura, x:x+largura]
        blur = cv2.GaussianBlur(blur, (23,23), 30)
        imagem[y:y+blur.shape[0], x:x+blur.shape[1]] = blur

    cv2.imwrite('/home/ppaludo/dev/trabalho-final_computacao-grafica/api/hooks/temp/'+str(random.getrandbits(128))+'.png', imagem)

    return imagem
    
# def blurVideo(filename, file):
#     video = cv2.VideoCapture(file)
#     classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
#     while True:
#         conectado, frame = video.read()

#         frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         facesDetectadas = classificadorFace.detectMultiScale(frameCinza)
#         for (x, y, largura, altura) in facesDetectadas:
#             blur = frame[y:y + altura, x:x + largura]
#             blur = cv2.GaussianBlur(blur, (27, 27), 30)
#             frame[y:y + blur.shape[0], x:x + blur.shape[1]] = blur
#         cv2.imshow('Captura de video', frame)
#         if(cv2.waitKey(1) == ord('q')):
#             break
#     video.release()
#     cv2.destroyAllWindows()
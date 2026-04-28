#HUD na câmera

import cv2
altitude = 0
bateria = 80
direcao = 1

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("A câmera não foi encontrada!")
    
while True:
    ok, frame = camera.read()
    if not ok:
       break 
    
    #cv2.putText(frame, "texto", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    #(CV2 É A BIBLIOTECA. PUTTEXT = ESCREVE O TEXTO, FRAME = IMAGEM, (X, Y)= POSIÇÃO DA CÂMERA FONT_HERSHEY = CORES QUE COLOCAM NO VIDEO)
    
    
    cv2.putText(frame, f"Altitude: {altitude}m", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.putText(frame, f"Bateria: {bateria}%", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    if direcao == 1:
        status = "Subindo..."
    else:
        status = "Descendo..."
        
    cv2.putText(frame, f"Status: {status}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    
    
    cv2.imshow("HUD CÂMERA", frame)
    
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    
camera.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

# 이미지 로드
img = cv2.imread('./image.jpg')

# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 노이즈 감소를 위해 미디언 블러 적용
gray = cv2.medianBlur(gray, 5)

# 엣지 검출 (적응형 임계값)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 7, 7)

# 색상 필터링 (부드럽게 만들기) 
color = cv2.bilateralFilter(img, 9, 300, 300)

#  샤프닝 커널 추가
sharpening_kernel = np.array([
    [-1, -2, -1],
    [-2, 13, -2],
    [-1, -2, -1]
])

# 샤프닝 적용
sharpened = cv2.filter2D(color, -1, sharpening_kernel)

# 엣지와 결합하여 만화 효과
cartoon = cv2.bitwise_and(sharpened, sharpened, mask=edges)

merge = np.hstack((img,cartoon))
# 결과 출력
cv2.imshow("image | Cartoon", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()
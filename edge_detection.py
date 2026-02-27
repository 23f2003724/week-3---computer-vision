import cv2
import matplotlib.pyplot as plt
img = cv2.imread("C:/Users/thesu/Downloads/JAN TERM 2026/Mission adobe/computer-vision-basics/images/Screenshot 2025-10-24 210307.png")
if img is None:
    print("Images not found.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 100, 200)
plt.figure(figsize = (10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtcolor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(edges, cmap="gray")
plt.title("Edges")
plt.axis("off")
plt.show()
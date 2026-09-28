import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.axes_grid1 import ImageGrid


def show_images(*images, titles=None, cmap="gray", save_path=None, sup="Title") -> None:
    n = len(images)
    cols = 1 if n == 1 else 2
    rows = int(np.ceil(n / cols))

    fig_width = 12
    fig_height = 4.5 * rows

    fig = plt.figure(figsize=(fig_width, fig_height))
    grid = ImageGrid(
        fig, 111, nrows_ncols=(rows, cols), axes_pad=(0.02, 0.4), share_all=True
    )

    for i, (ax, im) in enumerate(zip(grid, images)):
        if im.ndim == 3:
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            ax.imshow(im)
        else:
            ax.imshow(im, cmap=cmap)

        if i < len(titles):
            ax.set_title(titles[i], fontsize=13, pad=6)

    for ax in grid:
        ax.axis("off")
    fig.suptitle(sup, fontsize=16, fontweight="bold", y=0.92)

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")

    plt.show()


car_img = cv2.imread("./pic/car.jpg")
car_img_gs = cv2.imread("./pic/car.jpg", cv2.IMREAD_GRAYSCALE)

winter_img = cv2.imread("./pic/winter.png")
winter_img_gs = cv2.imread("./pic/winter.png", cv2.IMREAD_GRAYSCALE)

storm_img = cv2.imread("./pic/storm.jpg")
storm_img_gs = cv2.imread("./pic/storm.jpg", cv2.IMREAD_GRAYSCALE)

gradient_img = cv2.imread("./pic/gradient.png")
gradient_img_gs = cv2.imread("./pic/gradient.png", cv2.IMREAD_GRAYSCALE)

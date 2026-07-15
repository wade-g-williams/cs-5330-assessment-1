"""
Valid, Same, and Full convolution — CS 5330 Assessment 1 (topic 26).

The three modes differ ONLY in how much zero padding is added around the
image before sliding the kernel across it. For an H x W image and a K x K
kernel (K odd):

    mode     padding per side    output size            border pixels
    -----    ----------------    -------------------    -------------------
    valid    0                   (H-K+1) x (W-K+1)      none touch padding
    same     K // 2              H x W                  some touch padding
    full     K - 1               (H+K-1) x (W+K-1)      kernel overlaps image
                                                        by as little as 1 px

Run:  .venv/bin/python convolutions.py
Outputs comparison figures and per-mode images to output/.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d as scipy_convolve2d

KERNEL_SIZE = 21          # odd, so "same" is symmetric
IMAGE_MAX_DIM = 200       # small image so the +/- (K-1) size change is visible
GREY_IMAGE = "data/street.jpg"   # Waymo Pacifica, Dllu, Wikimedia Commons, CC BY-SA 4.0
COLOR_IMAGE = "data/puppy.jpg"   # Golde33443, Golden Trvs Gol twister, Commons, CC BY-SA 3.0


def convolve2d(channel, kernel, mode):
    """2-D convolution of a single channel, written out explicitly.

    Convolution = flip the kernel, then slide it and take dot products
    (without the flip it would be correlation). The mode picks the padding.
    """
    k = kernel.shape[0]
    flipped = kernel[::-1, ::-1]
    pad = {"valid": 0, "same": k // 2, "full": k - 1}[mode]
    padded = np.pad(channel, pad)  # zero padding

    out_h = padded.shape[0] - k + 1
    out_w = padded.shape[1] - k + 1
    out = np.empty((out_h, out_w))
    for i in range(out_h):
        for j in range(out_w):
            out[i, j] = np.sum(padded[i : i + k, j : j + k] * flipped)
    return out


def convolve_image(image, kernel, mode):
    """Apply convolve2d to a greyscale (H,W) or color (H,W,3) image."""
    if image.ndim == 2:
        return convolve2d(image, kernel, mode)
    channels = [convolve2d(image[:, :, c], kernel, mode) for c in range(3)]
    return np.stack(channels, axis=-1)


def load_image(path, greyscale):
    """Load as float in [0,1], downscaled so size differences are visible."""
    img = Image.open(path).convert("L" if greyscale else "RGB")
    img.thumbnail((IMAGE_MAX_DIM, IMAGE_MAX_DIM))
    return np.asarray(img, dtype=np.float64) / 255.0


def on_canvas(image, canvas_hw, fill=0.75):
    """Center an image on a grey canvas so relative sizes show honestly."""
    shape = canvas_hw if image.ndim == 2 else (*canvas_hw, 3)
    canvas = np.full(shape, fill)
    top = (canvas_hw[0] - image.shape[0]) // 2
    left = (canvas_hw[1] - image.shape[1]) // 2
    canvas[top : top + image.shape[0], left : left + image.shape[1]] = image
    return canvas


def demo(name, image, kernel):
    h, w = image.shape[:2]
    k = kernel.shape[0]
    print(f"\n{name}: input {h}x{w}, kernel {k}x{k}")

    results = {}
    for mode in ("valid", "same", "full"):
        results[mode] = np.clip(convolve_image(image, kernel, mode), 0, 1)

        # cross-check the from-scratch result against scipy, per channel
        for c in range(1 if image.ndim == 2 else 3):
            chan = image if image.ndim == 2 else image[:, :, c]
            ours = results[mode] if image.ndim == 2 else results[mode][:, :, c]
            ref = scipy_convolve2d(chan, kernel, mode=mode)
            assert np.allclose(ours, np.clip(ref, 0, 1)), f"{mode} != scipy"

        oh, ow = results[mode].shape[:2]
        formula = {"valid": "H-K+1", "same": "H", "full": "H+K-1"}[mode]
        print(f"  {mode:5s}: {oh}x{ow}   ({formula})   matches scipy ✓")

    # comparison figure: everything drawn at true relative scale
    canvas_hw = results["full"].shape[:2]
    panels = [("input", image)] + list(results.items())
    fig, axes = plt.subplots(1, 4, figsize=(14, 4))
    for ax, (title, img) in zip(axes, panels):
        ax.imshow(on_canvas(img, canvas_hw), cmap="gray", vmin=0, vmax=1)
        ax.set_title(f"{title}  {img.shape[0]}x{img.shape[1]}")
        ax.axis("off")
    fig.suptitle(f"{name} image, {k}x{k} box blur, zero padding")
    fig.tight_layout()
    fig.savefig(f"output/{name}_modes.png", dpi=150)

    for mode, img in results.items():
        plt.imsave(f"output/{name}_{mode}.png", img, cmap="gray", vmin=0, vmax=1)


def main():
    import os

    os.makedirs("output", exist_ok=True)
    kernel = np.ones((KERNEL_SIZE, KERNEL_SIZE)) / KERNEL_SIZE**2  # box blur

    demo("grey", load_image(GREY_IMAGE, greyscale=True), kernel)
    demo("color", load_image(COLOR_IMAGE, greyscale=False), kernel)
    print("\nFigures written to output/")


if __name__ == "__main__":
    main()

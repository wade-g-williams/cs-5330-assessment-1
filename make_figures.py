"""
Teaching figures for presentation v2 (topic 26: valid/same/full convolution).

Generates into output/:
    grid_running_example.png   6x6 * 3x3 -> 4x4, kernel fully inside (slide 2)
    grid_boundary_question.png kernel centered on a corner pixel, hanging off (slide 2)
    grid_valid.png             p=0 grid diagram (slide 6)
    grid_same.png              p=1 grid diagram (slide 7)
    grid_full.png              p=2 grid diagram (slide 8)
    visit_counts_valid.png     how often each pixel is used, no padding (slide 4)
    visit_counts.png           valid vs same vs full usage heatmaps (slide 8)
    dial.png                   the padding dial: three named settings (slides 5, 12)
    grey_input.png, color_input.png   downscaled inputs for true-scale pairs

Run:  .venv/bin/python make_figures.py
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyArrowPatch, Rectangle

from convolutions import COLOR_IMAGE, GREY_IMAGE, load_image

# palette per the dataviz reference (validated: worst adjacent CVD dE 21.2)
INK = "#0B0B0B"
INK2 = "#52514E"
MUTED = "#898781"
HAIRLINE = "#C3C2B7"
PAD_FILL = "#F0EFEC"
KERNEL = "#E34948"
OUTPUT = "#1BAF7A"
MODE_COLORS = {"valid": "#2A78D6", "same": "#EDA100", "full": "#4A3AA7"}
BLUE_RAMP = ["#CDE2FB", "#9EC5F4", "#6DA7EC", "#3987E5", "#256ABF", "#184F95", "#0D366B"]
BLUES = LinearSegmentedColormap.from_list("blues", BLUE_RAMP)

N, K = 6, 3  # the running example: 6x6 image, 3x3 kernel


def draw_image_grid(ax, x0, y0, n, pad=0):
    """Image cells white, padding ring grey with '0's. (x0, y0) = top-left."""
    total = n + 2 * pad
    for r in range(total):
        for c in range(total):
            is_pad = r < pad or c < pad or r >= n + pad or c >= n + pad
            ax.add_patch(Rectangle((x0 + c, y0 - r - 1), 1, 1,
                                   facecolor=PAD_FILL if is_pad else "white",
                                   edgecolor=HAIRLINE, linewidth=0.8))
            if is_pad:
                ax.text(x0 + c + 0.5, y0 - r - 0.5, "0",
                        ha="center", va="center", fontsize=8, color=MUTED)
    return total


def draw_output_grid(ax, x0, y0, n, highlight=None):
    for r in range(n):
        for c in range(n):
            strong = highlight == (r, c)
            ax.add_patch(Rectangle((x0 + c, y0 - r - 1), 1, 1,
                                   facecolor=OUTPUT, alpha=0.55 if strong else 0.18,
                                   edgecolor=HAIRLINE, linewidth=0.8))


def draw_kernel_box(ax, x0, y0, row, col, k=K):
    """Kernel outline with top-left at grid cell (row, col)."""
    ax.add_patch(Rectangle((x0 + col, y0 - row - k, ), k, k,
                           facecolor=KERNEL, alpha=0.12,
                           edgecolor=KERNEL, linewidth=3, zorder=5))


def finish(ax, fname, x_range, y_range):
    ax.set_xlim(*x_range)
    ax.set_ylim(*y_range)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.savefig(f"output/{fname}", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.1)
    plt.close()
    print(f"  output/{fname}")


def mode_figure(mode):
    """Padded input grid + kernel at its extreme position -> output grid."""
    pad = {"valid": 0, "same": (K - 1) // 2, "full": K - 1}[mode]
    total = N + 2 * pad
    out = total - K + 1
    gap = 2.2

    fig, ax = plt.subplots(figsize=((total + gap + out) * 0.42, (total + 1.6) * 0.42))
    draw_image_grid(ax, 0, 0, N, pad)
    draw_kernel_box(ax, 0, 0, 0, 0)  # extreme top-left position for this mode
    oy = -(total - out) / 2  # vertically centered next to the input
    draw_output_grid(ax, total + gap, oy, out, highlight=(0, 0))
    ax.add_patch(FancyArrowPatch((total + 0.4, -total / 2), (total + gap - 0.4, -total / 2),
                                 arrowstyle="-|>", mutation_scale=22, color=INK2, linewidth=2))

    ax.scatter([0.18], [1.02], s=90, color=MODE_COLORS[mode], clip_on=False)
    ax.text(0.55, 1.0, f"{mode} convolution   p = {pad}",
            fontsize=13, fontweight="bold", color=INK, va="center")
    label = f"{N}×{N} image" if pad == 0 else f"{N}×{N} + {pad} ring{'s' if pad > 1 else ''} of zeros = {total}×{total}"
    ax.text(total / 2, -total - 0.55, label, ha="center", fontsize=11, color=INK2)
    ax.text(total + gap + out / 2, oy - out - 0.55, f"output {out}×{out}",
            ha="center", fontsize=11, color=INK2)
    finish(ax, f"grid_{mode}.png", (-0.3, total + gap + out + 0.3), (-total - 1.3, 1.5))


def running_example():
    """6x6 * 3x3 -> 4x4 with the kernel fully inside, one output cell lit."""
    out, gap = N - K + 1, 2.2
    krow, kcol = 1, 1  # kernel top-left; maps to output cell (1, 1)
    fig, ax = plt.subplots(figsize=((N + gap + out) * 0.42, (N + 1.6) * 0.42))
    draw_image_grid(ax, 0, 0, N)
    draw_kernel_box(ax, 0, 0, krow, kcol)
    oy = -(N - out) / 2
    draw_output_grid(ax, N + gap, oy, out, highlight=(krow, kcol))
    ax.add_patch(FancyArrowPatch((N + 0.4, -N / 2), (N + gap - 0.4, -N / 2),
                                 arrowstyle="-|>", mutation_scale=22, color=INK2, linewidth=2))
    ax.text(N / 2, -N - 0.55, f"{N}×{N} image,  {K}×{K} kernel",
            ha="center", fontsize=11, color=INK2)
    ax.text(N + gap + out / 2, oy - out - 0.55, f"output {out}×{out} — it shrank",
            ha="center", fontsize=11, color=INK2)
    finish(ax, "grid_running_example.png", (-0.3, N + gap + out + 0.3), (-N - 1.3, 0.7))


def boundary_question():
    """Kernel centered on the corner pixel: a third of it hangs off the image."""
    fig, ax = plt.subplots(figsize=((N + 2.4) * 0.42, (N + 2.6) * 0.42))
    draw_image_grid(ax, 0, 0, N)
    draw_kernel_box(ax, 0, 0, -1, -1)  # centered on pixel (0, 0)
    for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (1, -1)]:
        ax.text(c + 0.5, -r - 0.5, "?", ha="center", va="center",
                fontsize=13, fontweight="bold", color=KERNEL)
    ax.text(N / 2, -N - 0.55, "kernel centered on a corner pixel:\nwhat multiplies the missing cells?",
            ha="center", va="top", fontsize=11, color=INK2)
    finish(ax, "grid_boundary_question.png", (-1.4, N + 1.0), (-N - 1.9, 1.4))


def visit_counts(pad):
    """How many kernel placements use each image pixel, for padding = pad."""
    counts = np.zeros((N, N), int)
    total = N + 2 * pad
    for r in range(total - K + 1):
        for c in range(total - K + 1):
            r0, r1 = max(r - pad, 0), min(r + K - pad, N)
            c0, c1 = max(c - pad, 0), min(c + K - pad, N)
            counts[r0:r1, c0:c1] += 1
    return counts


def draw_counts(ax, counts, title, chip=None):
    for r in range(N):
        for c in range(N):
            v = counts[r, c]
            ax.add_patch(Rectangle((c, -r - 1), 1, 1, facecolor=BLUES(v / (K * K)),
                                   edgecolor="white", linewidth=1.5))
            ax.text(c + 0.5, -r - 0.5, str(v), ha="center", va="center", fontsize=10,
                    color="white" if v >= 6 else INK)
    if chip:
        ax.scatter([0.18], [0.62], s=80, color=chip, clip_on=False)
        ax.text(0.55, 0.6, title, fontsize=12, fontweight="bold", color=INK, va="center")
    else:
        ax.text(N / 2, 0.6, title, fontsize=11, color=INK2, ha="center", va="center")
    ax.set_xlim(-0.2, N + 0.2)
    ax.set_ylim(-N - 0.3, 1.1)
    ax.set_aspect("equal")
    ax.axis("off")


def visit_figures():
    fig, ax = plt.subplots(figsize=(4.2, 4.6))
    draw_counts(ax, visit_counts(0), "kernel placements that use each pixel\n(3×3 kernel, no padding)")
    plt.savefig("output/visit_counts_valid.png", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.1)
    plt.close()
    print("  output/visit_counts_valid.png")

    fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.4))
    for ax, mode in zip(axes, ("valid", "same", "full")):
        pad = {"valid": 0, "same": (K - 1) // 2, "full": K - 1}[mode]
        draw_counts(ax, visit_counts(pad), f"{mode}  (p = {pad})", chip=MODE_COLORS[mode])
    plt.savefig("output/visit_counts.png", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.1)
    plt.close()
    print("  output/visit_counts.png")


def dial():
    fig, ax = plt.subplots(figsize=(10.5, 2.6))
    ax.plot([0, 1], [0, 0], color=HAIRLINE, linewidth=3, zorder=1,
            solid_capstyle="round")
    stops = [("valid", 0.0, "p = 0", "output  N − K + 1   (shrinks)"),
             ("same", 0.5, "p = (K−1)/2", "output  N   (unchanged)"),
             ("full", 1.0, "p = K − 1", "output  N + K − 1   (grows)")]
    for mode, x, p_label, out_label in stops:
        ax.scatter([x], [0], s=260, color=MODE_COLORS[mode], zorder=3)
        ax.text(x, 0.35, mode, ha="center", fontsize=16, fontweight="bold", color=INK)
        ax.text(x, -0.32, p_label, ha="center", fontsize=12, color=INK)
        ax.text(x, -0.55, out_label, ha="center", fontsize=11, color=INK2)
    ax.text(0.5, 0.72, "How much padding do we use per side?",
            ha="center", fontsize=13, color=INK2, style="italic")
    ax.set_xlim(-0.16, 1.16)
    ax.set_ylim(-0.8, 0.95)
    ax.axis("off")
    plt.savefig("output/dial.png", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.1)
    plt.close()
    print("  output/dial.png")


def real_conv_row():
    """input photo * (1/9 x ones) = blurred photo — the grid story on a real image."""
    from PIL import Image

    from convolutions import convolve_image

    img = Image.open("data/puppy.jpg").convert("RGB")
    w, h = img.size  # 800x965: center-crop square, then small enough to see a 3x3 blur
    side = min(w, h)
    img = img.crop(((w - side) // 2, (h - side) // 2,
                    (w + side) // 2, (h + side) // 2)).resize((128, 128), Image.LANCZOS)
    photo = np.asarray(img, dtype=np.float64) / 255.0
    blurred = np.clip(convolve_image(photo, np.ones((3, 3)) / 9.0, "valid"), 0, 1)

    fig, ax = plt.subplots(figsize=(10.4, 3.9))
    ax.imshow(photo, extent=(0, 6, 0, 6))
    ax.text(7.15, 3, "∗", fontsize=34, color=INK2, ha="center", va="center")
    ax.text(8.75, 3, "1/9 ×", fontsize=15, fontweight="bold", color=INK,
            ha="center", va="center")
    for r in range(3):
        for c in range(3):
            ax.add_patch(Rectangle((9.55 + c, 1.5 + r), 1, 1, facecolor=KERNEL,
                                   alpha=0.10, edgecolor=KERNEL, linewidth=1.5))
            ax.text(10.05 + c, 2.0 + r, "1", fontsize=13, color=INK,
                    ha="center", va="center")
    ax.text(13.65, 3, "=", fontsize=34, color=INK2, ha="center", va="center")
    out_w = 6 * blurred.shape[0] / photo.shape[0]
    ax.imshow(blurred, extent=(14.75, 14.75 + out_w, (6 - out_w) / 2, (6 + out_w) / 2))
    ax.text(3, -0.55, "input  128×128", fontsize=12, color=INK2, ha="center")
    ax.text(11.05, 0.9, "3×3 box blur", fontsize=11, color=MUTED, ha="center")
    ax.text(14.75 + out_w / 2, -0.55, "output  126×126 — two pixels gone",
            fontsize=12, color=INK2, ha="center")
    finish(ax, "conv_real_example.png", (-0.3, 21.1), (-1.15, 6.4))


def mode_examples():
    """Mode-contrast examples: each shows WHY the other modes fail at this job."""
    from PIL import Image

    from convolutions import GREY_IMAGE, convolve2d, load_image

    street = load_image(GREY_IMAGE, greyscale=True)  # 108 x 200

    # VALID example — gradients are measurements. Same-mode padding invents a
    # phantom bright edge frame along the border; valid has only real edges.
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float)
    grad = lambda mode: np.hypot(convolve2d(street, sobel_x, mode),
                                 convolve2d(street, sobel_x.T, mode))
    m_valid, m_same = grad("valid"), grad("same")
    vmax = m_same.max()
    boost = lambda m: (m / vmax) ** 0.6  # gamma so the 1-px rim reads on a slide
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 2.35))
    axes[0].imshow(boost(m_valid), cmap="gray", vmin=0, vmax=1)
    axes[0].set_title("valid — real edges only  ✓", fontsize=11, color=INK)
    axes[1].imshow(boost(m_same), cmap="gray", vmin=0, vmax=1)
    axes[1].set_title("same — phantom border edges  ✗", fontsize=11,
                      color=KERNEL, fontweight="bold")
    h, w = m_same.shape
    for xy, xt in [((w * 0.5, 1), (w * 0.5, 22)), ((1, h * 0.55), (24, h * 0.55)),
                   ((w * 0.75, h - 2), (w * 0.75, h - 23))]:
        axes[1].annotate("", xy=xy, xytext=xt,
                         arrowprops=dict(color=KERNEL, arrowstyle="-|>", linewidth=1.8))
    for ax in axes:
        ax.axis("off")
    plt.savefig("output/example_valid.png", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.08)
    plt.close()
    print("  output/example_valid.png")

    # SAME example — a detection box at fixed frame coordinates. On the valid
    # output the content shifted by K//2 and the canvas shrank: the box misses.
    blur = np.ones((21, 21)) / 441.0
    out_same = np.clip(convolve2d(street, blur, "same"), 0, 1)
    out_valid = np.clip(convolve2d(street, blur, "valid"), 0, 1)
    box = dict(xy=(12, 20), width=136, height=83, fill=False,
               edgecolor=MODE_COLORS["same"], linewidth=2.5)
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 2.35),
                             width_ratios=[out_same.shape[1], out_valid.shape[1]])
    axes[0].imshow(out_same, cmap="gray", vmin=0, vmax=1)
    axes[0].add_patch(Rectangle(**box))
    axes[0].set_title("same — box lands on the car  ✓", fontsize=11, color=INK)
    axes[1].imshow(out_valid, cmap="gray", vmin=0, vmax=1)
    axes[1].add_patch(Rectangle(**box, clip_on=False))
    axes[1].set_title("valid — same box coords miss  ✗", fontsize=11,
                      color=KERNEL, fontweight="bold")
    for ax in axes:
        ax.set_anchor("N")
        ax.axis("off")
    plt.savefig("output/example_same.png", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.08)
    plt.close()
    print("  output/example_same.png")

    # FULL example (photo card): frame 36 — tracked pedestrian ID:20 is genuinely
    # cut off by the bottom frame edge, walking into view
    trk = Image.open("data/object_tracking_security.gif")
    trk.seek(36)
    trk = trk.convert("RGB")
    trk.thumbnail((640, 640))
    trk.save("output/example_full.png")
    print("  output/example_full.png")

    # slide 7 example: video game post-processing (Xonotic, GPL screenshot),
    # with the bloom glow annotated so the effect is unmissable at card size
    from matplotlib.patches import Ellipse

    game = Image.open("data/game.jpg").convert("RGB")
    game.thumbnail((640, 640))
    arr = np.asarray(game)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.imshow(arr)
    ax.add_patch(Ellipse((356, 152), 190, 120, fill=False,
                         edgecolor=MODE_COLORS["same"], linewidth=2.5))
    ax.annotate("bloom", xy=(300, 190), xytext=(150, 290),
                color="white", fontsize=15, fontweight="bold",
                arrowprops=dict(color=MODE_COLORS["same"], arrowstyle="-|>",
                                linewidth=2.2),
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#1F1F1D",
                          edgecolor=MODE_COLORS["same"]))
    ax.axis("off")
    plt.savefig("output/example_game.png", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.02)
    plt.close()
    print("  output/example_game.png")

    # slide 6 example: Zoom-style background blur (course-collected image)
    zoom = Image.open("data/Zoom_Background_Blur.png").convert("RGB")
    zoom.thumbnail((640, 640))
    zoom.save("output/example_zoom.png")
    print("  output/example_zoom.png")

    # slide 4 example: a pedestrian entering the frame (clipped at the left edge)
    ped = Image.open("data/face_detection_example.gif")
    ped.seek(75)
    ped = ped.convert("RGB")
    ped.save("output/pedestrian_edge.png")
    print("  output/pedestrian_edge.png")


def comparison_strip():
    """Slide 9: a 21x21 Gaussian-derivative edge detector on the street scene,
    run in all three modes — sizes and boundary artifacts become visible."""
    from convolutions import convolve2d

    k, sigma = 21, 3.5
    ax1 = np.arange(k) - k // 2
    xx, yy = np.meshgrid(ax1, ax1)
    g = np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))
    gx = -(xx / sigma ** 2) * g
    gy = -(yy / sigma ** 2) * g
    gx /= np.abs(gx).sum()
    gy /= np.abs(gy).sum()

    street = load_image(GREY_IMAGE, greyscale=True)
    mags = {m: np.hypot(convolve2d(street, gx, m), convolve2d(street, gy, m))
            for m in ("valid", "same", "full")}
    vmax = mags["same"].max()
    for mode, mag in mags.items():
        plt.imsave(f"output/edge_{mode}.png",
                   np.clip(mag / vmax, 0, 1) ** 0.6, cmap="gray", vmin=0, vmax=1)
        print(f"  output/edge_{mode}.png")


def padding_examples():
    """Slide 5: bare 6x6, +1 ring, +2 rings — same cell scale, no fill values."""
    for mode, pad in [("valid", 0), ("same", 1), ("full", 2)]:
        total = N + 2 * pad
        fig, ax = plt.subplots(figsize=(total * 0.22, total * 0.22))
        for r in range(total):
            for c in range(total):
                is_pad = r < pad or c < pad or r >= N + pad or c >= N + pad
                ax.add_patch(Rectangle((c, -r - 1), 1, 1,
                                       facecolor=PAD_FILL if is_pad else "white",
                                       edgecolor=HAIRLINE, linewidth=0.7))
        # emphasize the original image boundary inside the ring
        ax.add_patch(Rectangle((pad, -(pad + N)), N, N, fill=False,
                               edgecolor=INK2, linewidth=1.4))
        ax.set_xlim(-0.15, total + 0.15)
        ax.set_ylim(-total - 0.15, 0.15)
        ax.set_aspect("equal")
        ax.axis("off")
        plt.savefig(f"output/pad_example_{mode}.png", dpi=200,
                    bbox_inches="tight", facecolor="white", pad_inches=0.03)
        plt.close()
        print(f"  output/pad_example_{mode}.png")


def edge_bias():
    """Slide 4: the visit counts, then what that bias does to a real photo."""
    from convolutions import GREY_IMAGE, load_image

    street = load_image(GREY_IMAGE, greyscale=True)
    h, w = street.shape
    k = 21
    # per-pixel valid-window coverage counts, via 1-D full convolutions
    cr = np.convolve(np.ones(h - k + 1), np.ones(k), "full")
    cc = np.convolve(np.ones(w - k + 1), np.ones(k), "full")
    weights = np.outer(cr, cc) / (k * k)  # corner ~ 1/441, interior = 1
    seen = street * weights

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(4.8, 5.5))
    ax1.imshow(street, cmap="gray", vmin=0, vmax=1)
    ax1.set_title("the original image (108 × 200)", fontsize=10.5, color=INK)
    ax2.imshow(seen, cmap="gray", vmin=0, vmax=1)
    ax2.set_title("not an output — the input, re-lit by how often VALID (no-padding)\nconvolution uses each pixel: brighter = used more (21×21 kernel)",
                  fontsize=10, color=KERNEL, fontweight="bold")
    # the valid output's spatial footprint: 88 x 180, centered (offset K//2 = 10)
    off = k // 2
    ax2.add_patch(Rectangle((off - 0.5, off - 0.5), w - k + 1, h - k + 1,
                            fill=False, edgecolor=MODE_COLORS["valid"],
                            linewidth=1.8, linestyle="--"))
    ax2.text(w / 2, h + 13, "dashed box: where the smaller 88 × 180 valid output sits",
             fontsize=9.5, color=MODE_COLORS["valid"], ha="center", va="top",
             clip_on=False, fontweight="bold")
    for ax in (ax1, ax2):
        ax.axis("off")
    plt.savefig("output/edge_bias.png", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.1)
    plt.close()
    print("  output/edge_bias.png")


def example_full_1d():
    """1-D impulse response: the ring-out extends past the signal — full keeps it."""
    n_sig, n_ker = 60, 25
    t = np.arange(n_sig)
    note = np.sin(2 * np.pi * t / 8) * np.minimum(t / 4, 1.0)   # sustained note, abrupt stop
    echo = np.exp(-np.arange(n_ker) / 7)                         # room impulse response
    echo /= echo.sum()
    ring = np.convolve(note, echo, mode="full")                  # length N + K - 1 = 84

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(9.6, 1.75), width_ratios=[n_sig, len(ring)])
    ax1.plot(note, color=INK, linewidth=1.4)
    ax1.set_title(f"signal — N = {n_sig} samples", fontsize=10, color=INK2)
    ax2.plot(ring, color=MODE_COLORS["full"], linewidth=1.4)
    ax2.axvline(n_sig - 1, color=HAIRLINE, linestyle="--", linewidth=1)
    ax2.axvspan(n_sig - 1, len(ring) - 1, color=MODE_COLORS["full"], alpha=0.10)
    # same = centered crop of full -> it stops at index 71, mid-decay
    same_end = (n_sig - 1) + (n_ker - 1) // 2
    ax2.axvline(same_end, color=KERNEL, linestyle=":", linewidth=1.3)
    ax2.text(same_end, ring.min() * 0.9, "same stops here ✗", fontsize=8,
             color=KERNEL, ha="center", fontweight="bold")
    ax2.set_title(f"∗ echo kernel (K = {n_ker}), full — {len(ring)} samples",
                  fontsize=10, color=INK2)
    ax2.text((n_sig + len(ring)) / 2 - 1, ring.max() * 0.72, "ring-out\n(full keeps it)",
             fontsize=8.5, color=MODE_COLORS["full"], ha="center", fontweight="bold")
    for ax in (ax1, ax2):
        ax.set_xlim(0, len(ring) - 1) if ax is ax2 else ax.set_xlim(0, n_sig - 1)
        ax.set_yticks([])
        ax.set_xticks([])
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color(HAIRLINE)
    plt.savefig("output/example_full_1d.png", dpi=200, bbox_inches="tight",
                facecolor="white", pad_inches=0.08)
    plt.close()
    print("  output/example_full_1d.png")


def save_inputs():
    plt.imsave("output/grey_input.png", load_image(GREY_IMAGE, greyscale=True),
               cmap="gray", vmin=0, vmax=1)
    plt.imsave("output/color_input.png", load_image(COLOR_IMAGE, greyscale=False))
    print("  output/grey_input.png\n  output/color_input.png")


if __name__ == "__main__":
    print("Generating figures:")
    running_example()
    boundary_question()
    for m in ("valid", "same", "full"):
        mode_figure(m)
    visit_figures()
    dial()
    real_conv_row()
    mode_examples()
    comparison_strip()
    padding_examples()
    edge_bias()
    example_full_1d()
    save_inputs()

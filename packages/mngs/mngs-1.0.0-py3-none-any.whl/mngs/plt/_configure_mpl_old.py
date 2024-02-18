#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: "2024-02-02 12:43:54 (ywatanabe)"

# # # # # #!/usr/bin/env python3
# # import matplotlib.pyplot as plt
# # import numpy as np

# # # def configure_mpl(
# # #     plt,
# # #     dpi_plt=100,
# # #     dpi_save=300,
# # #     fig_size_mm=(40, 40 * 0.7),
# # #     fig_scale=1.0,
# # #     font_size_pt=8,
# # #     legend_fontsize_pt=7,
# # #     label_size_pt=8,
# # #     tick_size_mm=0.8,
# # #     tick_width_mm=0.2,
# # #     hide_spines=True,
# # #     show=True,
# # # ):
# # #     """
# # #     Configures the appearance of matplotlib plots to suit publication quality requirements.
# # #     This function standardizes the figure size, font sizes, tick sizes, and other aesthetic
# # #     elements across matplotlib figures.

# # #     Parameters:
# # #     - plt (module): Matplotlib's pyplot module, used for plotting.
# # #     - dpi_plt (int): DPI for the figure display, affecting on-screen quality. Default is 100.
# # #     - dpi_save (int): DPI for saving figures, affecting saved image quality. Default is 300.
# # #     - fig_size_mm (tuple of int): Desired figure size in millimeters (width, height). Default is (40, 28).
# # #     - fig_scale (float): Scale factor for adjusting the figure size. Default is 1.0.
# # #     - font_size_pt (int): Base font size in points for text elements within the plot. Default is 8.
# # #     - legend_fontsize_pt (int or str): Font size for the legend, in points or predefined string sizes like 'small'. Default is 7.
# # #     - label_size_pt (int): Font size for axis labels in points. Uses font_size_pt if None. Default is 8.
# # #     - tick_size_mm (float): Size of major ticks on axes in millimeters. Default is 0.8.
# # #     - tick_width_mm (float): Width of major ticks on axes in millimeters. Default is 0.2.
# # #     - hide_spines (bool): If True, hides the top and right spines of the plot to reduce visual clutter. Default is True.
# # #     - show (bool): If True, prints the configuration settings applied to matplotlib. Default is True.

# # #     Returns:
# # #     - plt: The pyplot module with updated settings, ready for use in plotting.

# # #     Example:
# # #         COLORS = mngs.plt.configure_mpl(plt)
# # #     """

# # #     # Convert figure size from mm to inches, incorporating figure scale
# # #     figsize_inch = (
# # #         (fig_size_mm[0] / 25.4) * fig_scale,
# # #         (fig_size_mm[1] / 25.4) * fig_scale,
# # #     )

# # #     # Convert tick size and width from mm to inches
# # #     tick_size_inches = tick_size_mm / 25.4
# # #     tick_width_inches = tick_width_mm / 25.4

# # #     # Define custom colors with alpha value of 0.9
# # #     custom_colors = [
# # #         # "#000000",  # Black
# # #         # "#808080",  # Gray
# # #         # "#FFFFFF",  # White
# # #         "#0080C0",  # Blue
# # #         "#14B414",  # Green
# # #         "#FF462E",  # Red
# # #         "#E6A014",  # Yellow
# # #         "#C832FF",  # Purple
# # #         "#FF96C8",  # Pink
# # #         "#14C8C8",  # LightBlue
# # #         "#000064",  # DarkBlue
# # #         "#E45E32",  # Dan
# # #         "#800000",  # Brown
# # #     ]
# # #     custom_colors_with_alpha = [
# # #         color + "E6" for color in custom_colors
# # #     ]  # Add alpha value (0.9 in hex)

# # #     # Update matplotlib RC (runtime configuration) parameters
# # #     plt.rcParams.update(
# # #         {
# # #             "figure.dpi": dpi_plt,
# # #             "savefig.dpi": dpi_save,
# # #             "figure.figsize": figsize_inch,
# # #             "font.size": font_size_pt,
# # #             "axes.labelsize": label_size_pt,
# # #             "xtick.labelsize": font_size_pt,
# # #             "ytick.labelsize": font_size_pt,
# # #             "legend.fontsize": legend_fontsize_pt,
# # #             "xtick.major.size": tick_size_inches,
# # #             "ytick.major.size": tick_size_inches,
# # #             "xtick.major.width": tick_width_inches,
# # #             "ytick.major.width": tick_width_inches,
# # #             "axes.spines.top": not hide_spines,
# # #             "axes.spines.right": not hide_spines,
# # #             "axes.prop_cycle": plt.cycler(
# # #                 "color", custom_colors_with_alpha
# # #             ),
# # #         }
# # #     )

# # #     if show:
# # #         print("\n" + "-" * 40)
# # #         print("Matplotlib has been configured with the following settings:")
# # #         print(f"Figure DPI (Display): {dpi_plt} DPI")
# # #         print(f"Figure DPI (Save): {dpi_save} DPI")
# # #         print(
# # #             f"Figure Size: {fig_size_mm[0] * fig_scale:.1f} x {fig_size_mm[1] * fig_scale:.1f} mm (width x height)"
# # #         )
# # #         print(f"Font Size: {font_size_pt} pt")
# # #         print(f"Legend Font Size: {legend_fontsize_pt} pt")
# # #         print(f"Label Size: {label_size_pt} pt")
# # #         print(f"Tick Size: {tick_size_mm} mm ({tick_size_inches:.3f} inches)")
# # #         print(
# # #             f"Tick Width: {tick_width_mm} mm ({tick_width_inches:.3f} inches)"
# # #         )
# # #         print(f"Hide Spines: {hide_spines}")
# # #         print(
# # #             "Matplotlib has been configured with the following settings and custom color cycle:"
# # #         )
# # #         for color in custom_colors_with_alpha:
# # #             print(f"Custom Color (with alpha): {color}")
# # #         print("-" * 40)

# # #     return plt


# # def configure_mpl(
# #     plt,
# #     dpi_plt=100,
# #     dpi_save=300,
# #     fig_size_mm=(40, 40 * 0.7),
# #     fig_scale=1.0,
# #     font_size_pt=8,
# #     legend_fontsize_pt=7,
# #     label_size_pt=8,
# #     tick_size_mm=0.8,
# #     tick_width_mm=0.2,
# #     hide_spines=True,
# #     show=True,
# # ):
# #     """
# #     Configures matplotlib settings for publication-quality plots with specified line thicknesses,
# #     font settings, tick configurations, and a custom color palette.

# #     Parameters:
# #     - plt (module): Matplotlib's pyplot module, used for plotting.
# #     - dpi_plt (int): DPI for the figure display, affecting on-screen quality. Default is 100.
# #     - dpi_save (int): DPI for saving figures, affecting saved image quality. Default is 300.
# #     - fig_size_mm (tuple of int): Desired figure size in millimeters (width, height). Default is (40, 28).
# #     - fig_scale (float): Scale factor for adjusting the figure size. Default is 1.0.
# #     - font_size_pt (int): Base font size in points for text elements within the plot. Default is 8.
# #     - legend_fontsize_pt (int or str): Font size for the legend, in points or predefined string sizes like 'small'. Default is 7.
# #     - label_size_pt (int): Font size for axis labels in points. Uses font_size_pt if None. Default is 8.
# #     - tick_size_mm (float): Size of major ticks on axes in millimeters. Default is 0.8.
# #     - tick_width_mm (float): Width of major ticks on axes in millimeters. Default is 0.2.
# #     - hide_spines (bool): If True, hides the top and right spines of the plot to reduce visual clutter. Default is True.
# #     - show (bool): If True, prints the configuration settings applied to matplotlib. Default is True.

# #     Returns:
# #     - plt: The pyplot module with updated settings, ready for use in plotting.
# #     - COLORS: Custom colors.

# #     Example:
# #         plt, COLORS = mngs.plt.configure_mpl(plt)

# #     """
# #     # Define custom colors with specified RGB values and alpha of 0.9
# #     custom_colors_rgba = {
# #         "blue": (0, 128, 192, 230),
# #         "red": (255, 70, 50, 230),
# #         "pink": (255, 150, 200, 230),
# #         "green": (20, 180, 20, 230),
# #         "yellow": (230, 160, 20, 230),
# #         "gray": (128, 128, 128, 230),
# #         "purple": (200, 50, 255, 230),
# #         "lightblue": (20, 200, 200, 230),
# #         "brown": (128, 0, 0, 230),
# #         "darkblue": (0, 0, 100, 230),
# #         "dan": (228, 94, 50, 230),
# #     }

# #     # Normalize RGB and alpha values to 0-1 scale for matplotlib
# #     for color in custom_colors_rgba:
# #         custom_colors_rgba[color] = tuple(
# #             [c / 255.0 for c in custom_colors_rgba[color]]
# #         )

# #     # Update matplotlib RC (runtime configuration) parameters
# #     plt.rcParams.update(
# #         {
# #             # Line widths and lengths
# #             "axes.linewidth": 0.2,  # Axis thickness
# #             "errorbar.capsize": 2,  # Error bar cap size in points
# #             "xtick.major.size": 0.8,  # Tick length
# #             "xtick.major.width": 0.2,  # Tick thickness
# #             "ytick.major.size": 0.8,
# #             "ytick.major.width": 0.2,
# #             "lines.linewidth": 0.12,  # Trace thickness
# #             # Font settings
# #             "font.family": "Arial",
# #             "axes.titlesize": 8,  # Axis title/group name
# #             "xtick.labelsize": 7,  # Tick numbers
# #             "ytick.labelsize": 7,
# #             "axes.labelsize": 8,  # Axis labels
# #             # Other settings
# #             "figure.dpi": 100,
# #             "savefig.dpi": 300,
# #             "legend.fontsize": 7,  # Legend font size
# #             # Custom color cycle using the first few colors
# #             "axes.prop_cycle": plt.cycler(
# #                 "color",
# #                 custom_colors_rgba.values(),
# #             ),
# #         }
# #     )

# #     # Additional configurations for manual adjustments might be needed for:
# #     # - Raster plot thickness and length
# #     # - Scatter plot size
# #     # - Ensuring ticks do not appear at the very ends of the axes, except for special cases (0, upper/lower limits)

# #     if show:
# #         print("\n" + "-" * 40)
# #         print("Matplotlib has been configured with the following settings:")
# #         print(f"Figure DPI (Display): {dpi_plt} DPI")
# #         print(f"Figure DPI (Save): {dpi_save} DPI")
# #         print(
# #             f"Figure Size: {fig_size_mm[0] * fig_scale:.1f} x {fig_size_mm[1] * fig_scale:.1f} mm (width x height)"
# #         )
# #         print(f"Font Size: {font_size_pt} pt")
# #         print(f"Legend Font Size: {legend_fontsize_pt} pt")
# #         print(f"Label Size: {label_size_pt} pt")
# #         print(f"Tick Size: {tick_size_mm} mm ({tick_size_inches:.3f} inches)")
# #         print(
# #             f"Tick Width: {tick_width_mm} mm ({tick_width_inches:.3f} inches)"
# #         )
# #         print(f"Hide Spines: {hide_spines}")
# #         for color in custom_colors_with_alpha:
# #             print(f"Custom Color (RGBA): {color}")
# #         print("-" * 40)

# #     return plt, custom_colors_rgba


# # if __name__ == "__main__":
# #     plt, COLORS = configure_mpl(plt)
# #     # Example plot to demonstrate settings
# #     x = [0, 1, 2, 3, 4]
# #     y = [0, 2, 1, 3, 4]
# #     plt.errorbar(x, y, yerr=0.1, fmt="-o", capsize=5, color=COLORS["blue"])
# #     plt.title("Example Plot")
# #     plt.xlabel("X Axis")
# #     plt.ylabel("Y Axis")
# #     plt.show()


# # # # #!/usr/bin/env python3
# import matplotlib.pyplot as plt
# import numpy as np

# # def configure_mpl(
# #     plt,
# #     dpi_plt=100,
# #     dpi_save=300,
# #     fig_size_mm=(40, 40 * 0.7),
# #     fig_scale=1.0,
# #     font_size_pt=8,
# #     legend_fontsize_pt=7,
# #     label_size_pt=8,
# #     tick_size_mm=0.8,
# #     tick_width_mm=0.2,
# #     hide_spines=True,
# #     show=True,
# # ):
# #     """
# #     Configures the appearance of matplotlib plots to suit publication quality requirements.
# #     This function standardizes the figure size, font sizes, tick sizes, and other aesthetic
# #     elements across matplotlib figures.

# #     Parameters:
# #     - plt (module): Matplotlib's pyplot module, used for plotting.
# #     - dpi_plt (int): DPI for the figure display, affecting on-screen quality. Default is 100.
# #     - dpi_save (int): DPI for saving figures, affecting saved image quality. Default is 300.
# #     - fig_size_mm (tuple of int): Desired figure size in millimeters (width, height). Default is (40, 28).
# #     - fig_scale (float): Scale factor for adjusting the figure size. Default is 1.0.
# #     - font_size_pt (int): Base font size in points for text elements within the plot. Default is 8.
# #     - legend_fontsize_pt (int or str): Font size for the legend, in points or predefined string sizes like 'small'. Default is 7.
# #     - label_size_pt (int): Font size for axis labels in points. Uses font_size_pt if None. Default is 8.
# #     - tick_size_mm (float): Size of major ticks on axes in millimeters. Default is 0.8.
# #     - tick_width_mm (float): Width of major ticks on axes in millimeters. Default is 0.2.
# #     - hide_spines (bool): If True, hides the top and right spines of the plot to reduce visual clutter. Default is True.
# #     - show (bool): If True, prints the configuration settings applied to matplotlib. Default is True.

# #     Returns:
# #     - plt: The pyplot module with updated settings, ready for use in plotting.

# #     Example:
# #         COLORS = mngs.plt.configure_mpl(plt)
# #     """

# #     # Convert figure size from mm to inches, incorporating figure scale
# #     figsize_inch = (
# #         (fig_size_mm[0] / 25.4) * fig_scale,
# #         (fig_size_mm[1] / 25.4) * fig_scale,
# #     )

# #     # Convert tick size and width from mm to inches
# #     tick_size_inches = tick_size_mm / 25.4
# #     tick_width_inches = tick_width_mm / 25.4

# #     # Define custom colors with alpha value of 0.9
# #     custom_colors = [
# #         # "#000000",  # Black
# #         # "#808080",  # Gray
# #         # "#FFFFFF",  # White
# #         "#0080C0",  # Blue
# #         "#14B414",  # Green
# #         "#FF462E",  # Red
# #         "#E6A014",  # Yellow
# #         "#C832FF",  # Purple
# #         "#FF96C8",  # Pink
# #         "#14C8C8",  # LightBlue
# #         "#000064",  # DarkBlue
# #         "#E45E32",  # Dan
# #         "#800000",  # Brown
# #     ]
# #     custom_colors_with_alpha = [
# #         color + "E6" for color in custom_colors
# #     ]  # Add alpha value (0.9 in hex)

# #     # Update matplotlib RC (runtime configuration) parameters
# #     plt.rcParams.update(
# #         {
# #             "figure.dpi": dpi_plt,
# #             "savefig.dpi": dpi_save,
# #             "figure.figsize": figsize_inch,
# #             "font.size": font_size_pt,
# #             "axes.labelsize": label_size_pt,
# #             "xtick.labelsize": font_size_pt,
# #             "ytick.labelsize": font_size_pt,
# #             "legend.fontsize": legend_fontsize_pt,
# #             "xtick.major.size": tick_size_inches,
# #             "ytick.major.size": tick_size_inches,
# #             "xtick.major.width": tick_width_inches,
# #             "ytick.major.width": tick_width_inches,
# #             "axes.spines.top": not hide_spines,
# #             "axes.spines.right": not hide_spines,
# #             "axes.prop_cycle": plt.cycler(
# #                 "color", custom_colors_with_alpha
# #             ),
# #         }
# #     )

# #     if show:
# #         print("\n" + "-" * 40)
# #         print("Matplotlib has been configured with the following settings:")
# #         print(f"Figure DPI (Display): {dpi_plt} DPI")
# #         print(f"Figure DPI (Save): {dpi_save} DPI")
# #         print(
# #             f"Figure Size: {fig_size_mm[0] * fig_scale:.1f} x {fig_size_mm[1] * fig_scale:.1f} mm (width x height)"
# #         )
# #         print(f"Font Size: {font_size_pt} pt")
# #         print(f"Legend Font Size: {legend_fontsize_pt} pt")
# #         print(f"Label Size: {label_size_pt} pt")
# #         print(f"Tick Size: {tick_size_mm} mm ({tick_size_inches:.3f} inches)")
# #         print(
# #             f"Tick Width: {tick_width_mm} mm ({tick_width_inches:.3f} inches)"
# #         )
# #         print(f"Hide Spines: {hide_spines}")
# #         print(
# #             "Matplotlib has been configured with the following settings and custom color cycle:"
# #         )
# #         for color in custom_colors_with_alpha:
# #             print(f"Custom Color (with alpha): {color}")
# #         print("-" * 40)

# #     return plt


# def configure_mpl(
#     plt,
#     dpi_plt=100,
#     dpi_save=300,
#     fig_size_mm=(40, 40 * 0.7),
#     fig_scale=1.0,
#     font_size_pt=8,
#     legend_fontsize_pt=7,
#     label_size_pt=8,
#     tick_size_mm=0.8,
#     tick_width_mm=0.2,
#     hide_spines=True,
#     show=True,
# ):
#     """
#     Configures matplotlib settings for publication-quality plots with specified line thicknesses,
#     font settings, tick configurations, and a custom color palette.

#     Parameters:
#     - plt (module): Matplotlib's pyplot module, used for plotting.
#     - dpi_plt (int): DPI for the figure display, affecting on-screen quality. Default is 100.
#     - dpi_save (int): DPI for saving figures, affecting saved image quality. Default is 300.
#     - fig_size_mm (tuple of int): Desired figure size in millimeters (width, height). Default is (40, 28).
#     - fig_scale (float): Scale factor for adjusting the figure size. Default is 1.0.
#     - font_size_pt (int): Base font size in points for text elements within the plot. Default is 8.
#     - legend_fontsize_pt (int or str): Font size for the legend, in points or predefined string sizes like 'small'. Default is 7.
#     - label_size_pt (int): Font size for axis labels in points. Uses font_size_pt if None. Default is 8.
#     - tick_size_mm (float): Size of major ticks on axes in millimeters. Default is 0.8.
#     - tick_width_mm (float): Width of major ticks on axes in millimeters. Default is 0.2.
#     - hide_spines (bool): If True, hides the top and right spines of the plot to reduce visual clutter. Default is True.
#     - show (bool): If True, prints the configuration settings applied to matplotlib. Default is True.

#     Returns:
#     - plt: The pyplot module with updated settings, ready for use in plotting.
#     - COLORS: Custom colors.

#     Example:
#         plt, COLORS = mngs.plt.configure_mpl(plt)

#     """
#     # Define custom colors with specified RGB values and alpha of 0.9
#     custom_colors_rgba = {
#         "blue": (0, 128, 192, 230),
#         "red": (255, 70, 50, 230),
#         "pink": (255, 150, 200, 230),
#         "green": (20, 180, 20, 230),
#         "yellow": (230, 160, 20, 230),
#         "gray": (128, 128, 128, 230),
#         "purple": (200, 50, 255, 230),
#         "lightblue": (20, 200, 200, 230),
#         "brown": (128, 0, 0, 230),
#         "darkblue": (0, 0, 100, 230),
#         "dan": (228, 94, 50, 230),
#     }

#     # Normalize RGB and alpha values to 0-1 scale for matplotlib
#     for color in custom_colors_rgba:
#         custom_colors_rgba[color] = tuple(
#             [c / 255.0 for c in custom_colors_rgba[color]]
#         )

#     # Update matplotlib RC (runtime configuration) parameters
#     # Update matplotlib RC (runtime configuration) parameters
#     plt.rcParams.update(
#         {
#             "figure.dpi": dpi_plt,
#             "savefig.dpi": dpi_save,
#             "figure.figsize": figsize_inch,
#             "font.family": "Arial",
#             "font.size": font_size_pt,  # 7
#             "axes.labelsize": label_size_pt,  # 8
#             "axes.titlesize": title_size_pt,  # 8
#             "legend.fontsize": legend_size_pt,  # 6
#             "xtick.labelsize": 7,  # Tick numbers
#             "ytick.labelsize": 7,
#             "axes.labelsize": 8,  # Axis labels
#             "xtick.major.size": tick_size_inches,
#             "ytick.major.size": tick_size_inches,
#             "xtick.major.width": tick_width_inches,
#             "ytick.major.width": tick_width_inches,
#             "axes.spines.top": not hide_spines,
#             "axes.spines.right": not hide_spines,
#             # Custom color cycle using the first few colors
#             "axes.prop_cycle": plt.cycler(
#                 "color",
#                 custom_colors_rgba.values(),
#             ),
#             # Line widths and lengths
#             "axes.linewidth": 0.2,  # Axis thickness
#             "errorbar.capsize": 2,  # Error bar cap size in points
#             "lines.linewidth": 0.12,  # Trace thickness
#         }
#     )

#     # Additional configurations for manual adjustments might be needed for:
#     # - Raster plot thickness and length
#     # - Scatter plot size
#     # - Ensuring ticks do not appear at the very ends of the axes, except for special cases (0, upper/lower limits)

#     if show:
#         print("\n" + "-" * 40)
#         print("Matplotlib has been configured with the following settings:")
#         print(f"Figure DPI (Display): {dpi_plt} DPI")
#         print(f"Figure DPI (Save): {dpi_save} DPI")
#         print(
#             f"Figure Size: {fig_size_mm[0] * fig_scale:.1f} x {fig_size_mm[1] * fig_scale:.1f} mm (width x height)"
#         )
#         print(f"Font Size: {font_size_pt} pt")
#         print(f"Legend Font Size: {legend_fontsize_pt} pt")
#         print(f"Label Size: {label_size_pt} pt")
#         print(f"Tick Size: {tick_size_mm} mm ({tick_size_inches:.3f} inches)")
#         print(
#             f"Tick Width: {tick_width_mm} mm ({tick_width_inches:.3f} inches)"
#         )
#         print(f"Hide Spines: {hide_spines}")
#         for color in custom_colors_with_alpha:
#             print(f"Custom Color (RGBA): {color}")
#         print("-" * 40)

#     return plt, custom_colors_rgba


# if __name__ == "__main__":
#     plt, COLORS = configure_mpl(plt)
#     # Example plot to demonstrate settings
#     x = [0, 1, 2, 3, 4]
#     y = [0, 2, 1, 3, 4]
#     plt.errorbar(x, y, yerr=0.1, fmt="-o", capsize=5, color=COLORS["blue"])
#     plt.title("Example Plot")
#     plt.xlabel("X Axis")
#     plt.ylabel("Y Axis")
#     plt.show()

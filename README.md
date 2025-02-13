### Custom MPV "Lite" Version

This repository contains a customized version of MPV. I have removed certain binary files, shaders, and other config files/functions that are not needed for my use case.

However, if you prefer to use MPV with its full set of features, including all binaries, shaders, and configurations, you can refer to the official MPV documentation.

### Update to the Latest Version
**Note**: The `mpv.exe` in this repository is not the newest version.

1. Download the latest version from the official release page:  
   [mpv-winbuild Releases](https://github.com/zhongfly/mpv-winbuild/releases)

2. Once downloaded, unzip the archive and locate the `.exe` file.

3. Replace the existing `.exe` file in your current installation directory with the new one.

This process will ensure you're always running the latest version with any improvements or bug fixes.

### Using the `portable_config` Folder

`portable_config` folder allows you to store your configuration files alongside the MPV executable.

- Alternatively, you can install it system-wide by running `mpv-install.bat`.

### Installing the Required Fonts

If you wish to use the same font like me, especially for displaying CJK (Chinese, Japanese, and Korean) languages, you need to install the following fonts:

#### 1. **Noto Sans CJK**
   - **Font file:** [NotoSansCJK-Bold.ttc](https://github.com/dyphire/mpv-config/raw/refs/heads/master/fonts/NotoSansCJK-Bold.ttc)
   
#### 2. **Noto Serif CJK**
   - **Font file:** [NotoSerifCJK-Bold.ttc](https://github.com/dyphire/mpv-config/raw/refs/heads/master/fonts/NotoSerifCJK-Bold.ttc)
   
- Alternatively, you can change it in the `mpv.config` so that you can use the font you like.

### Features of This Lite Version:

- **Custom Font Support**: Ensures proper subtitle rendering by using custom fonts, preventing issues like missing text in subtitles.
  
- **Dual-Subtitle Support**: Based on my previous experience with PotPlayer, this version is customized to display two subtitles simultaneously, making it ideal for multilingual content.

- **Power Efficiency**: Optimized for better power consumption, offering improved energy savings compared to PotPlayer (LAV Filters + HW decoding).

- **Optimized for Low-End Devices**: Designed with low-end hardware in mind, leveraging **D3D11 hardware acceleration** to enhance GPU rendering and improve performance on less powerful systems.

**Note**: This version is tailored to my personal preferences for shortcut keys and settings. Feel free to modify it to better suit your own use case or requirements.

### References

- [MPV_lazy](https://github.com/hooke007/MPV_lazy)
- [dyphire mpv-config](https://github.com/dyphire/mpv-config)
- [hooke007 配置手册](https://hooke007.github.io/unofficial/mpv_start.html)
- [mpv official manual](https://mpv.io/manual/master/)
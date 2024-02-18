import sys
import setuptools
from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


class InstallCmsisPack(install):
    def run(self):
        print("sys.argv:", sys.argv)
        print("Running custom installation install logic...")
        # Download the files
        self.download_cmsis_packs()

        # Continue with the default installation process
        install.run(self)

    def download_cmsis_packs(self):
        import os
        try:
            import requests
        except ImportError:
            # If requests is not available, provide a warning message
            print("Warning: 'requests' library not found. File downloads will be skipped.")

        # URLs and download paths
        urls = [
            'https://www.keil.com/pack/Keil.STM32F0xx_DFP.2.1.1.pack',
            'http://www.keil.com/pack/Keil.STM32G0xx_DFP.1.4.0.pack',
            'https://www.keil.com/pack/Keil.STM32U5xx_DFP.2.0.0.pack'
        ]
        download_paths = [
            'cmsis-pack/Keil.STM32F0xx_DFP.2.1.1.pack',
            'cmsis-pack/Keil.STM32G0xx_DFP.1.4.0.pack',
            'cmsis-pack/Keil.STM32U5xx_DFP.2.0.0.pack'
        ]

        # Download the files only if requests is available
        if 'requests' in locals():
            for url, download_path in zip(urls, download_paths):
                # download to the subfolder download_path
                abs_download_path = os.path.join(self.install_lib, "trackpad_configuration_manager", download_path)

                os.makedirs(os.path.dirname(abs_download_path), exist_ok=True)

                print("Downloading file from {} to {}".format(url, abs_download_path))
                response = requests.get(url)
                with open(abs_download_path, 'wb') as f:
                    f.write(response.content)


setuptools.setup(
    name="trackpad_configuration_manager",
    version="2.1.1",
    author="Pascal-Frédéric St-Laurent",
    author_email="pfstlaurent@boreas.ca",
    description="Trackpad Configurator Library that allows to read/write configuration/calibration files (json format) "
                "from/to a device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    url="https://github.com/BoreasTechnologies/trackpad-configurator-plus-plus.git",
    packages=[
        'trackpad_configuration_manager',
        'trackpad_configuration_manager.probe',
        'trackpad_configuration_manager.utils',
        'trackpad_configuration_manager.boreas_data_converter'],
    classifiers=[
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=[
        "pyocd==0.34.3",
        "cmsis-pack-manager==0.5.2",
        "intelhex==2.3.0",
        "PySide6==6.5.2",
        "crc==1.3.0",
        "requests==2.31.0",
    ],
    cmdclass={
        'install': InstallCmsisPack,
    },
    include_package_data=True,
    python_requires='>=3.11',
)

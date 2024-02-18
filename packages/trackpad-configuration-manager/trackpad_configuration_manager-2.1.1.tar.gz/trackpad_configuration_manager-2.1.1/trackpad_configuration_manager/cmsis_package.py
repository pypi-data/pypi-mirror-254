import os
import sys

from pyocd.target.pack.pack_target import PackTargets

from trackpad_configuration_manager.utils.execUtils import resource_path


class CMSISPackage:

    @staticmethod
    def load_package():
        # Load CMSIS-package for stm32f4xx

        stm32f0_pack_path = None
        stm32u5_pack_path = None
        stm32g0_pack_path = None

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            stm32f0_pack_path = resource_path("trackpad_configuration_manager/cmsis-pack/Keil.STM32F0xx_DFP.2.1.1.pack")
            stm32u5_pack_path = resource_path("trackpad_configuration_manager/cmsis-pack/Keil.STM32U5xx_DFP.2.0.0.pack")
            stm32g0_pack_path = resource_path("trackpad_configuration_manager/cmsis-pack/Keil.STM32G0xx_DFP.1.4.0.pack")
        else:
            dir_name = os.path.dirname(__file__)
            stm32f0_pack_path = os.path.join(dir_name, "cmsis-pack/Keil.STM32F0xx_DFP.2.1.1.pack")
            stm32u5_pack_path = os.path.join(dir_name, "cmsis-pack/Keil.STM32U5xx_DFP.2.0.0.pack")
            stm32g0_pack_path = os.path.join(dir_name, "cmsis-pack/Keil.STM32G0xx_DFP.1.4.0.pack")

        PackTargets.populate_targets_from_pack(
            [stm32f0_pack_path, stm32u5_pack_path, stm32g0_pack_path])

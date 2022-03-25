from calibration import Sensor, Connection, LinearCalibration, ThermistorCalibration

RATE = 10000  # Analog data sample rate
READ_BULK = 200  # Number of samples to read at once for better performance

CC = False


def setup():
    Sensor("Big Omega S-type", "ai18", 0.2, Connection.DIFFERENTIAL,
           LinearCalibration(1/(2.9991 / 1000 * 10 / 1000), -10.1, "kg"))  # calibrated 3/13/2021
    Sensor("Honeywell S-type", "ai17", 0.2, Connection.DIFFERENTIAL,
           LinearCalibration(5116, -0.94, "kgs"))  # calibrated 3/13/2021
    Sensor("Omega S-type", "ai16", 0.2, Connection.DIFFERENTIAL,
           LinearCalibration(3025.7, -1.3675, "kgs"))  # calibrated 3/13/2021
    """
    Sensor("P5 (PT-5) - SRAD Vent Valve", "ai7", 10, Connection.SINGLE,
           LinearCalibration(620, -39.1, "psi"))  # Calibrated 2/7/2021
    Sensor("P4 (PT-1) - Ox Fill", "ai6", 10, Connection.SINGLE,
           LinearCalibration(615, -44.1, "psi"))  # Calibrated 2/7/2021
    Sensor("P3 (PT-2) - Ox Tank", "ai0", 10, Connection.SINGLE,
           LinearCalibration(605, -53.3, "psi"))  # Calibrated 2/7/2021
    Sensor("T8 - Tank Heating", "ai23", 10, Connection.SINGLE,
           ThermistorCalibration(10000, 3434, 0.099524))  # Calibration pulled from LabVIEW
    """

    if CC:
        Sensor("P2 (PT-3) - CC", "ai4", 10, Connection.SINGLE,
               LinearCalibration(621, -267, "psi"))  # Calibrated 13/7/2021
        Sensor("Thrust", "ai2", 0.2, Connection.DIFFERENTIAL, LinearCalibration(
            65445, -20.9, "lbs"))  # Roughly calibrated 17/7/2021
        Sensor("SP1 (PT-4) - Nozzle", "ai5", 0.2, Connection.DIFFERENTIAL,
               LinearCalibration(171346, -99.8, "psi"))  # Calibrated 2/7/2021
        Sensor("FAST", "ai1", 10, Connection.SINGLE, LinearCalibration(
            35.3, -34.2, "psi"))  # Calibrated 13/7/2021
        Sensor("T1 - CC", "ai16", 10, Connection.SINGLE,
               ThermistorCalibration(10000, 3434, 0.099524))  # Calibration pulled from LabVIEW
        Sensor("T2 - CC", "ai17", 10, Connection.SINGLE,
               ThermistorCalibration(10000, 3434, 0.099524))  # Calibration pulled from LabVIEW
        Sensor("T3 - CC", "ai18", 10, Connection.SINGLE,
               ThermistorCalibration(10000, 3434, 0.099524))  # Calibration pulled from LabVIEW
        Sensor("T4 - CC", "ai19", 10, Connection.SINGLE,
               ThermistorCalibration(10000, 3434, 0.099524))  # Calibration pulled from LabVIEW
        Sensor("T5 - CC", "ai20", 10, Connection.SINGLE,
               ThermistorCalibration(10000, 3434, 0.099524))  # Calibration pulled from LabVIEW
        Sensor("T6 - CC", "ai21", 10, Connection.SINGLE,
               ThermistorCalibration(10000, 3434, 0.099524))  # Calibration pulled from LabVIEW
        Sensor("T7 - CC", "ai22", 10, Connection.SINGLE,
               ThermistorCalibration(10000, 3434, 0.099524))  # Calibration pulled from LabVIEW

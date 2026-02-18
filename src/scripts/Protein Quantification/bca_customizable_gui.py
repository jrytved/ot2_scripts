from opentrons import protocol_api
import json

# Metadata
metadata = {
    'protocolName': 'Customizable BCA Assay II',
    'author': 'J. Rytved',
    'description': 'BCA protein assay with customizable volumes',
    'apiLevel': '2.27'
}

# Protocol parameters
def add_parameters(parameters):
    parameters.add_int(
        variable_name="sample_volume",
        display_name="Sample Volume (µL)",
        description="Volume of sample to transfer",
        default=4,
        minimum=2,
        maximum=20,
        unit="µL"
    )

    parameters.add_int(
        variable_name="diluent_volume",
        display_name="Diluent Volume (µL)",
        description="Volume of diluent to add to samples",
        default=16,
        minimum=0,
        maximum=20,
        unit="µL"
    )

    parameters.add_int(
        variable_name="working_reagent_volume",
        display_name="Working Reagent Volume (µL)",
        description="Volume of BCA working reagent",
        default=200,
        minimum=50,
        maximum=300,
        unit="µL"
    )

    parameters.add_int(
        variable_name="incubation_temp",
        display_name="Incubation Temperature (°C)",
        description="Temperature for plate incubation",
        default=37,
        minimum=25,
        maximum=65,
        unit="°C"
    )

    parameters.add_int(
        variable_name="incubation_time",
        display_name="Incubation Time (min)",
        description="Time for color development",
        default=30,
        minimum=5,
        maximum=120,
        unit="minutes"
    )

    parameters.add_int(
        variable_name="shake_speed",
        display_name="Shake Speed (rpm)",
        description="Shaking speed during incubation",
        default=500,
        minimum=200,
        maximum=2000,
        unit="rpm"
    )

    parameters.add_int(
        variable_name="num_samples",
        display_name="Number of Sample Columns",
        description="Number of consecutive sample columns to run (starting from col 1 "
                    "of the sample plate)",
        default=5,
        minimum=1,
        maximum=5,
        unit="columns"
    )


# Custom labware definitions embedded as strings
twintec_text = """{"ordering": [["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand": {"brand": "Eppendorf twin.tec","brandId": []},"metadata": {"displayName": "Eppendorf Twin.tec 96 Well Plate 150 µL","displayCategory": "wellPlate","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.47,"zDimension": 16.06},"wells": {"A1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 74.23,"z": 1.46},"B1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 65.23,"z": 1.46},"C1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 56.23,"z": 1.46},"D1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 47.23,"z": 1.46},"E1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 38.23,"z": 1.46},"F1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 29.23,"z": 1.46},"G1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 20.23,"z": 1.46},"H1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 11.23,"z": 1.46},"A2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 74.23,"z": 1.46},"B2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 65.23,"z": 1.46},"C2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 56.23,"z": 1.46},"D2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 47.23,"z": 1.46},"E2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 38.23,"z": 1.46},"F2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 29.23,"z": 1.46},"G2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 20.23,"z": 1.46},"H2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 11.23,"z": 1.46},"A3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 74.23,"z": 1.46},"B3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 65.23,"z": 1.46},"C3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 56.23,"z": 1.46},"D3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 47.23,"z": 1.46},"E3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 38.23,"z": 1.46},"F3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 29.23,"z": 1.46},"G3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 20.23,"z": 1.46},"H3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 11.23,"z": 1.46},"A4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 74.23,"z": 1.46},"B4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 65.23,"z": 1.46},"C4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 56.23,"z": 1.46},"D4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 47.23,"z": 1.46},"E4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 38.23,"z": 1.46},"F4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 29.23,"z": 1.46},"G4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 20.23,"z": 1.46},"H4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 11.23,"z": 1.46},"A5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 74.23,"z": 1.46},"B5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 65.23,"z": 1.46},"C5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 56.23,"z": 1.46},"D5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 47.23,"z": 1.46},"E5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 38.23,"z": 1.46},"F5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 29.23,"z": 1.46},"G5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 20.23,"z": 1.46},"H5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 11.23,"z": 1.46},"A6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 74.23,"z": 1.46},"B6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 65.23,"z": 1.46},"C6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 56.23,"z": 1.46},"D6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 47.23,"z": 1.46},"E6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 38.23,"z": 1.46},"F6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 29.23,"z": 1.46},"G6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 20.23,"z": 1.46},"H6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 11.23,"z": 1.46},"A7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 74.23,"z": 1.46},"B7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 65.23,"z": 1.46},"C7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 56.23,"z": 1.46},"D7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 47.23,"z": 1.46},"E7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 38.23,"z": 1.46},"F7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 29.23,"z": 1.46},"G7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 20.23,"z": 1.46},"H7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 11.23,"z": 1.46},"A8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 74.23,"z": 1.46},"B8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 65.23,"z": 1.46},"C8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 56.23,"z": 1.46},"D8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 47.23,"z": 1.46},"E8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 38.23,"z": 1.46},"F8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 29.23,"z": 1.46},"G8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 20.23,"z": 1.46},"H8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 11.23,"z": 1.46},"A9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 74.23,"z": 1.46},"B9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 65.23,"z": 1.46},"C9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 56.23,"z": 1.46},"D9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 47.23,"z": 1.46},"E9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 38.23,"z": 1.46},"F9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 29.23,"z": 1.46},"G9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 20.23,"z": 1.46},"H9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 11.23,"z": 1.46},"A10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 74.23,"z": 1.46},"B10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 65.23,"z": 1.46},"C10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 56.23,"z": 1.46},"D10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 47.23,"z": 1.46},"E10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 38.23,"z": 1.46},"F10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 29.23,"z": 1.46},"G10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 20.23,"z": 1.46},"H10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 11.23,"z": 1.46},"A11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 74.23,"z": 1.46},"B11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 65.23,"z": 1.46},"C11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 56.23,"z": 1.46},"D11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 47.23,"z": 1.46},"E11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 38.23,"z": 1.46},"F11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 29.23,"z": 1.46},"G11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 20.23,"z": 1.46},"H11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 11.23,"z": 1.46},"A12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 74.23,"z": 1.46},"B12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 65.23,"z": 1.46},"C12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 56.23,"z": 1.46},"D12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 47.23,"z": 1.46},"E12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 38.23,"z": 1.46},"F12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 29.23,"z": 1.46},"G12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 20.23,"z": 1.46},"H12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 11.23,"z": 1.46}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters": {"format": "irregular","quirks": [],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "eppendorftwin.tec_96_wellplate_150ul"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0},"stackingOffsetWithLabware": {"opentrons_universal_flat_adapter": {"x": 0,"y": 0,"z": 7.709999999999997},"opentrons_aluminum_flat_bottom_plate": {"x": 0,"y": 0,"z": 3.9399999999999977}}}"""

integra_reservoir_text = """{"ordering": [["A1"]],"brand": {"brand": "Integra","brandId": []},"metadata": {"displayName": "Integra 100mL Reservoir","displayCategory": "reservoir","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.48,"zDimension": 23},"wells": {"A1": {"depth": 18.5,"totalLiquidVolume": 100000,"shape": "rectangular","xDimension": 121,"yDimension": 71,"x": 64,"y": 42.98,"z": 4.5}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1"]}],"parameters": {"format": "irregular","quirks": ["centerMultichannelOnWells","touchTipDisabled"],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "integra_100ml_reservoir"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0}}"""

bca_plate_text = """{ "ordering": [ [ "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1" ], [ "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2" ], [ "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3" ], [ "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4" ], [ "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5" ], [ "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6" ], [ "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7" ], [ "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8" ], [ "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9" ], [ "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10" ], [ "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11" ], [ "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12" ] ], "brand": { "brand": "Greiner", "brandId": [ "NA" ] }, "metadata": { "displayName": "Greiner BCA Plate 655101", "displayCategory": "wellPlate", "displayVolumeUnits": "µL", "tags": [] }, "dimensions": { "xDimension": 127.76, "yDimension": 85.48, "zDimension": 14.6 }, "wells": { "A1": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 14.38, "y": 74.24, "z": 3.7 }, "B1": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 14.38, "y": 65.24, "z": 3.7 }, "C1": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 14.38, "y": 56.24, "z": 3.7 }, "D1": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 14.38, "y": 47.24, "z": 3.7 }, "E1": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 14.38, "y": 38.24, "z": 3.7 }, "F1": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 14.38, "y": 29.24, "z": 3.7 }, "G1": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 14.38, "y": 20.24, "z": 3.7 }, "H1": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 14.38, "y": 11.24, "z": 3.7 }, "A2": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 23.38, "y": 74.24, "z": 3.7 }, "B2": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 23.38, "y": 65.24, "z": 3.7 }, "C2": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 23.38, "y": 56.24, "z": 3.7 }, "D2": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 23.38, "y": 47.24, "z": 3.7 }, "E2": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 23.38, "y": 38.24, "z": 3.7 }, "F2": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 23.38, "y": 29.24, "z": 3.7 }, "G2": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 23.38, "y": 20.24, "z": 3.7 }, "H2": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 23.38, "y": 11.24, "z": 3.7 }, "A3": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 32.38, "y": 74.24, "z": 3.7 }, "B3": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 32.38, "y": 65.24, "z": 3.7 }, "C3": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 32.38, "y": 56.24, "z": 3.7 }, "D3": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 32.38, "y": 47.24, "z": 3.7 }, "E3": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 32.38, "y": 38.24, "z": 3.7 }, "F3": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 32.38, "y": 29.24, "z": 3.7 }, "G3": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 32.38, "y": 20.24, "z": 3.7 }, "H3": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 32.38, "y": 11.24, "z": 3.7 }, "A4": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 41.38, "y": 74.24, "z": 3.7 }, "B4": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 41.38, "y": 65.24, "z": 3.7 }, "C4": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 41.38, "y": 56.24, "z": 3.7 }, "D4": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 41.38, "y": 47.24, "z": 3.7 }, "E4": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 41.38, "y": 38.24, "z": 3.7 }, "F4": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 41.38, "y": 29.24, "z": 3.7 }, "G4": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 41.38, "y": 20.24, "z": 3.7 }, "H4": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 41.38, "y": 11.24, "z": 3.7 }, "A5": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 50.38, "y": 74.24, "z": 3.7 }, "B5": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 50.38, "y": 65.24, "z": 3.7 }, "C5": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 50.38, "y": 56.24, "z": 3.7 }, "D5": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 50.38, "y": 47.24, "z": 3.7 }, "E5": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 50.38, "y": 38.24, "z": 3.7 }, "F5": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 50.38, "y": 29.24, "z": 3.7 }, "G5": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 50.38, "y": 20.24, "z": 3.7 }, "H5": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 50.38, "y": 11.24, "z": 3.7 }, "A6": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 59.38, "y": 74.24, "z": 3.7 }, "B6": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 59.38, "y": 65.24, "z": 3.7 }, "C6": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 59.38, "y": 56.24, "z": 3.7 }, "D6": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 59.38, "y": 47.24, "z": 3.7 }, "E6": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 59.38, "y": 38.24, "z": 3.7 }, "F6": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 59.38, "y": 29.24, "z": 3.7 }, "G6": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 59.38, "y": 20.24, "z": 3.7 }, "H6": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 59.38, "y": 11.24, "z": 3.7 }, "A7": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 68.38, "y": 74.24, "z": 3.7 }, "B7": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 68.38, "y": 65.24, "z": 3.7 }, "C7": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 68.38, "y": 56.24, "z": 3.7 }, "D7": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 68.38, "y": 47.24, "z": 3.7 }, "E7": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 68.38, "y": 38.24, "z": 3.7 }, "F7": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 68.38, "y": 29.24, "z": 3.7 }, "G7": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 68.38, "y": 20.24, "z": 3.7 }, "H7": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 68.38, "y": 11.24, "z": 3.7 }, "A8": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 77.38, "y": 74.24, "z": 3.7 }, "B8": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 77.38, "y": 65.24, "z": 3.7 }, "C8": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 77.38, "y": 56.24, "z": 3.7 }, "D8": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 77.38, "y": 47.24, "z": 3.7 }, "E8": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 77.38, "y": 38.24, "z": 3.7 }, "F8": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 77.38, "y": 29.24, "z": 3.7 }, "G8": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 77.38, "y": 20.24, "z": 3.7 }, "H8": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 77.38, "y": 11.24, "z": 3.7 }, "A9": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 86.38, "y": 74.24, "z": 3.7 }, "B9": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 86.38, "y": 65.24, "z": 3.7 }, "C9": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 86.38, "y": 56.24, "z": 3.7 }, "D9": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 86.38, "y": 47.24, "z": 3.7 }, "E9": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 86.38, "y": 38.24, "z": 3.7 }, "F9": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 86.38, "y": 29.24, "z": 3.7 }, "G9": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 86.38, "y": 20.24, "z": 3.7 }, "H9": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 86.38, "y": 11.24, "z": 3.7 }, "A10": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 95.38, "y": 74.24, "z": 3.7 }, "B10": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 95.38, "y": 65.24, "z": 3.7 }, "C10": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 95.38, "y": 56.24, "z": 3.7 }, "D10": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 95.38, "y": 47.24, "z": 3.7 }, "E10": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 95.38, "y": 38.24, "z": 3.7 }, "F10": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 95.38, "y": 29.24, "z": 3.7 }, "G10": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 95.38, "y": 20.24, "z": 3.7 }, "H10": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 95.38, "y": 11.24, "z": 3.7 }, "A11": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 104.38, "y": 74.24, "z": 3.7 }, "B11": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 104.38, "y": 65.24, "z": 3.7 }, "C11": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 104.38, "y": 56.24, "z": 3.7 }, "D11": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 104.38, "y": 47.24, "z": 3.7 }, "E11": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 104.38, "y": 38.24, "z": 3.7 }, "F11": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 104.38, "y": 29.24, "z": 3.7 }, "G11": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 104.38, "y": 20.24, "z": 3.7 }, "H11": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 104.38, "y": 11.24, "z": 3.7 }, "A12": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 113.38, "y": 74.24, "z": 3.7 }, "B12": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 113.38, "y": 65.24, "z": 3.7 }, "C12": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 113.38, "y": 56.24, "z": 3.7 }, "D12": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 113.38, "y": 47.24, "z": 3.7 }, "E12": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 113.38, "y": 38.24, "z": 3.7 }, "F12": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 113.38, "y": 29.24, "z": 3.7 }, "G12": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 113.38, "y": 20.24, "z": 3.7 }, "H12": { "depth": 10.9, "totalLiquidVolume": 340, "shape": "circular", "diameter": 6.96, "x": 113.38, "y": 11.24, "z": 3.7 } }, "groups": [ { "metadata": { "wellBottomShape": "flat" }, "wells": [ "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11", "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12" ] } ], "parameters": { "format": "irregular", "quirks": [], "isTiprack": false, "isMagneticModuleCompatible": false, "loadName": "greiner_bca_flat" }, "namespace": "custom_beta", "version": 1, "schemaVersion": 2, "cornerOffsetFromSlot": { "x": 0, "y": 0, "z": 0 }, "stackingOffsetWithLabware": { "opentrons_universal_flat_adapter": { "x": 0, "y": 0, "z": 9.600000000000001 } } }"""



def run(protocol: protocol_api.ProtocolContext):

    # Access parameters
    sample_vol  = protocol.params.sample_volume
    diluent_vol = protocol.params.diluent_volume
    reagent_vol = protocol.params.working_reagent_volume
    temp        = protocol.params.incubation_temp
    incub_time  = protocol.params.incubation_time
    shake_rpm   = protocol.params.shake_speed
    num_samples = protocol.params.num_samples  # number of sample columns to run (1–5)

    # Parse custom labware definitions
    twintec_def = json.loads(twintec_text)
    integra_def = json.loads(integra_reservoir_text)
    bca_plate_def = json.loads(bca_plate_text)

    # =========================================================================
    # Deck layout
    # =========================================================================
    # Slot  1 – Eppendorf Twin.tec 96-well plate  → sample plate
    # Slot  2 – (empty / spare)
    # Slot  3 – Heater-Shaker module              → Corning 96-well assay plate
    # Slot  4 – Eppendorf Twin.tec 96-well plate  → BSA standards plate
    # Slot  5 – 20 µL tip rack #1
    # Slot  6 – (empty / spare)
    # Slot  7 – Integra 100 mL reservoir          → working reagent
    # Slot  8 – Integra 100 mL reservoir          → diluent / water
    # Slot  9 – 20 µL tip rack #2
    # Slot 10 – 300 µL tip rack #1
    # Slot 11 – 300 µL tip rack #2
    #
    # Assay plate column assignment (dynamic, based on num_samples parameter)
    # -----------------------------------------------
    # Cols 1 & 2            : BSA standards (duplicate)
    # Cols 3 & 4            : Sample 1 duplicate  (source: sample plate col 1)
    # Cols 5 & 6  [optional]: Sample 2 duplicate  (source: sample plate col 2)
    # Cols 7 & 8  [optional]: Sample 3 duplicate  (source: sample plate col 3)
    # Cols 9 & 10 [optional]: Sample 4 duplicate  (source: sample plate col 4)
    # Cols 11 & 12[optional]: Sample 5 duplicate  (source: sample plate col 5)
    #
    # Total assay columns used = 2 (standards) + num_samples * 2

    # Load modules
    hs_mod = protocol.load_module('heaterShakerModuleV1', 3)
    hs_adapter = hs_mod.load_adapter("opentrons_universal_flat_adapter")

    # Load labware
    assay_plate     = hs_adapter.load_labware_from_definition(bca_plate_def, label = "BCA Assay Plate on HS-mod")
    sample_plate    = protocol.load_labware_from_definition(twintec_def, 1, label = "Twin.Tec Sample Plate (>10uL)")
    standards_plate = protocol.load_labware_from_definition(twintec_def, 4, label = "Twin.Tec Plate w. BSA Standards")
    reagent_reservoir = protocol.load_labware_from_definition(integra_def, 7, label = "Integra Reservoir - Working Reagent")
    diluent_reservoir = protocol.load_labware_from_definition(integra_def, 8, label = "Integra Reservoir - Diluent Solution")

    # Tip racks – kept away from heater-shaker (slots 2 & 6 are adjacent; avoid them)
    tiprack_20_1  = protocol.load_labware('opentrons_96_tiprack_20ul',   5)
    tiprack_20_2  = protocol.load_labware('opentrons_96_tiprack_20ul',   9)
    tiprack_300_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 10)
    tiprack_300_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)

    # Load pipettes
    p300_multi = protocol.load_instrument('p300_multi_gen2', 'left',
                                          tip_racks=[tiprack_300_1, tiprack_300_2])
    p20_multi  = protocol.load_instrument('p20_multi_gen2',  'right',
                                          tip_racks=[tiprack_20_1,  tiprack_20_2])


    # Liquid sources
    working_reagent = reagent_reservoir['A1']  # slot 7
    diluent         = diluent_reservoir['A1']  # slot 8

    # Select pipette for sample/standard and diluent transfers based on volume
    sample_pipette  = p20_multi if sample_vol  <= 20 else p300_multi
    diluent_pipette = p20_multi if diluent_vol <= 20 else p300_multi
    
    sample_pipette.flow_rate.dispense = 6
    diluent_pipette.flow_rate.dispense = 6

    # =========================================================================
    # Protocol start
    # =========================================================================
    protocol.comment("Starting BCA Assay Protocol")
    protocol.comment(f"Sample: {sample_vol} µL | Diluent: {diluent_vol} µL | "
                     f"Reagent: {reagent_vol} µL | Samples: {num_samples} column(s)")
    protocol.comment("Assay plate layout:")
    protocol.comment("  Cols 1-2  : BSA standards (duplicate)")
    for i in range(num_samples):
        col_a = 3 + i * 2
        col_b = col_a + 1
        protocol.comment(f"  Cols {col_a}-{col_b} : Sample {i + 1} (duplicate)")

    # Open heater-shaker latch
    hs_mod.open_labware_latch()
    protocol.pause("Place the assay plate on the heater-shaker, then resume.")
    hs_mod.close_labware_latch()

    # =========================================================================
    # STEP 1 – BSA standards → assay plate cols 1 & 2 (duplicate)
    # =========================================================================
    # Standards are arranged in column 1 of the standards plate (rows A–H,
    # one standard per row).  The multi-channel pipette transfers all 8
    # standards simultaneously into each duplicate column.
    protocol.comment("Step 1: Transferring BSA standards → assay cols 1 & 2 (duplicate)")

    for assay_col in [0, 1]:  # 0-indexed: col index 0 = assay col 1, 1 = assay col 2
        sample_pipette.pick_up_tip()
        sample_pipette.transfer(
            sample_vol,
            standards_plate.columns()[0][0],        # col 1 of standards plate
            assay_plate.columns()[assay_col][0].bottom(0.5),
            new_tip='never',
        )
        sample_pipette.touch_tip(v_offset=-5, radius=1, speed=4)
        sample_pipette.drop_tip()

    # =========================================================================
    # STEP 2 – Samples → assay plate cols 3–12 (duplicate pairs)
    # =========================================================================
    # Each sample column on the sample plate is transferred into two consecutive
    # assay columns to create duplicates.
    #   sample plate col 1 → assay cols 3 & 4
    #   sample plate col 2 → assay cols 5 & 6
    #   sample plate col 3 → assay cols 7 & 8
    #   sample plate col 4 → assay cols 9 & 10
    #   sample plate col 5 → assay cols 11 & 12
    protocol.comment("Step 2: Transferring samples → assay cols 3-12 (duplicate pairs)")

    for sample_idx in range(num_samples):
        assay_col_a = 2 + sample_idx * 2      # first  duplicate (0-indexed)
        assay_col_b = 2 + sample_idx * 2 + 1  # second duplicate (0-indexed)

        for assay_col in [assay_col_a, assay_col_b]:
            sample_pipette.pick_up_tip()
            sample_pipette.transfer(
                sample_vol,
                sample_plate.columns()[sample_idx][0],
                assay_plate.columns()[assay_col][0],
                new_tip='never',
            )
            sample_pipette.touch_tip(v_offset=-5, radius=1, speed=4)
            sample_pipette.drop_tip()

    # =========================================================================
    # STEP 3 – Diluent → all 12 assay columns (if diluent_vol > 0)
    # =========================================================================
    # total assay columns in use: 2 standards + num_samples * 2 sample duplicates
    total_assay_cols = 2 + num_samples * 2

    if diluent_vol > 0:
        protocol.comment(f"Step 3: Adding {diluent_vol} µL diluent to assay cols 1-{total_assay_cols}")
        for col in range(total_assay_cols):
            diluent_pipette.pick_up_tip()
            diluent_pipette.transfer(
                diluent_vol,
                diluent,
                assay_plate.columns()[col][0],
                new_tip='never'
            )
            diluent_pipette.touch_tip(v_offset=-5, radius=1, speed=4)
            diluent_pipette.drop_tip()

    # =========================================================================
    # STEP 4 – BCA working reagent → all 12 assay columns
    # =========================================================================
    protocol.comment(f"Step 4: Adding {reagent_vol} µL BCA working reagent to assay cols 1-{total_assay_cols}")

    for col in range(total_assay_cols):
        p300_multi.pick_up_tip()
        p300_multi.transfer(
            reagent_vol,
            working_reagent,
            assay_plate.columns()[col][0],
            new_tip='never',
            mix_after=(5, 50)
        )
        p300_multi.drop_tip()

    # =========================================================================
    # STEP 5 – Initial shake to mix (30 s)
    # =========================================================================
    protocol.comment("Step 5: Initial mixing shake (30 s)")
    hs_mod.set_and_wait_for_shake_speed(rpm=shake_rpm)
    protocol.delay(seconds=30)
    hs_mod.deactivate_shaker()

    # =========================================================================
    # STEP 6 – Heat and incubate with shaking
    # =========================================================================
    protocol.comment(f"Step 6: Incubating at {temp} °C for {incub_time} min with shaking")
    hs_mod.set_and_wait_for_temperature(temp)
    hs_mod.set_and_wait_for_shake_speed(rpm=shake_rpm)
    protocol.delay(minutes=incub_time)

    # =========================================================================
    # STEP 7 – Cool down
    # =========================================================================
    protocol.comment("Step 7: Cooling down")
    hs_mod.deactivate_shaker()
    hs_mod.deactivate_heater()

    # Open latch for plate removal
    hs_mod.open_labware_latch()

    protocol.comment("Protocol complete! Remove plate and read absorbance at 562 nm.")
    protocol.comment(f"Total volume per well: {sample_vol + diluent_vol + reagent_vol} µL")
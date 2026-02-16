from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Customizable BCA Assay',
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

twintec_text = """{"ordering": [["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand": {"brand": "Eppendorf twin.tec","brandId": []},"metadata": {"displayName": "Eppendorf Twin.tec 96 Well Plate 150 µL","displayCategory": "wellPlate","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.47,"zDimension": 16.06},"wells": {"A1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 74.23,"z": 1.46},"B1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 65.23,"z": 1.46},"C1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 56.23,"z": 1.46},"D1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 47.23,"z": 1.46},"E1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 38.23,"z": 1.46},"F1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 29.23,"z": 1.46},"G1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 20.23,"z": 1.46},"H1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 11.23,"z": 1.46},"A2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 74.23,"z": 1.46},"B2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 65.23,"z": 1.46},"C2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 56.23,"z": 1.46},"D2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 47.23,"z": 1.46},"E2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 38.23,"z": 1.46},"F2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 29.23,"z": 1.46},"G2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 20.23,"z": 1.46},"H2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 11.23,"z": 1.46},"A3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 74.23,"z": 1.46},"B3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 65.23,"z": 1.46},"C3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 56.23,"z": 1.46},"D3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 47.23,"z": 1.46},"E3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 38.23,"z": 1.46},"F3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 29.23,"z": 1.46},"G3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 20.23,"z": 1.46},"H3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 11.23,"z": 1.46},"A4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 74.23,"z": 1.46},"B4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 65.23,"z": 1.46},"C4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 56.23,"z": 1.46},"D4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 47.23,"z": 1.46},"E4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 38.23,"z": 1.46},"F4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 29.23,"z": 1.46},"G4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 20.23,"z": 1.46},"H4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 11.23,"z": 1.46},"A5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 74.23,"z": 1.46},"B5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 65.23,"z": 1.46},"C5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 56.23,"z": 1.46},"D5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 47.23,"z": 1.46},"E5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 38.23,"z": 1.46},"F5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 29.23,"z": 1.46},"G5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 20.23,"z": 1.46},"H5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 11.23,"z": 1.46},"A6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 74.23,"z": 1.46},"B6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 65.23,"z": 1.46},"C6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 56.23,"z": 1.46},"D6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 47.23,"z": 1.46},"E6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 38.23,"z": 1.46},"F6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 29.23,"z": 1.46},"G6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 20.23,"z": 1.46},"H6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 11.23,"z": 1.46},"A7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 74.23,"z": 1.46},"B7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 65.23,"z": 1.46},"C7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 56.23,"z": 1.46},"D7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 47.23,"z": 1.46},"E7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 38.23,"z": 1.46},"F7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 29.23,"z": 1.46},"G7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 20.23,"z": 1.46},"H7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 11.23,"z": 1.46},"A8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 74.23,"z": 1.46},"B8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 65.23,"z": 1.46},"C8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 56.23,"z": 1.46},"D8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 47.23,"z": 1.46},"E8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 38.23,"z": 1.46},"F8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 29.23,"z": 1.46},"G8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 20.23,"z": 1.46},"H8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 11.23,"z": 1.46},"A9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 74.23,"z": 1.46},"B9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 65.23,"z": 1.46},"C9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 56.23,"z": 1.46},"D9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 47.23,"z": 1.46},"E9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 38.23,"z": 1.46},"F9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 29.23,"z": 1.46},"G9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 20.23,"z": 1.46},"H9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 11.23,"z": 1.46},"A10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 74.23,"z": 1.46},"B10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 65.23,"z": 1.46},"C10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 56.23,"z": 1.46},"D10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 47.23,"z": 1.46},"E10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 38.23,"z": 1.46},"F10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 29.23,"z": 1.46},"G10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 20.23,"z": 1.46},"H10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 11.23,"z": 1.46},"A11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 74.23,"z": 1.46},"B11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 65.23,"z": 1.46},"C11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 56.23,"z": 1.46},"D11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 47.23,"z": 1.46},"E11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 38.23,"z": 1.46},"F11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 29.23,"z": 1.46},"G11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 20.23,"z": 1.46},"H11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 11.23,"z": 1.46},"A12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 74.23,"z": 1.46},"B12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 65.23,"z": 1.46},"C12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 56.23,"z": 1.46},"D12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 47.23,"z": 1.46},"E12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 38.23,"z": 1.46},"F12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 29.23,"z": 1.46},"G12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 20.23,"z": 1.46},"H12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 11.23,"z": 1.46}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters": {"format": "irregular","quirks": [],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "eppendorftwin.tec_96_wellplate_150ul"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0},"stackingOffsetWithLabware": {"opentrons_universal_flat_adapter": {"x": 0,"y": 0,"z": 7.709999999999997},"opentrons_aluminum_flat_bottom_plate": {"x": 0,"y": 0,"z": 3.9399999999999977}}}"""
integra_reservoir_text = """{"ordering": [["A1"]],"brand": {"brand": "Integra","brandId": []},"metadata": {"displayName": "Integra 100mL Reservoir","displayCategory": "reservoir","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.48,"zDimension": 23},"wells": {"A1": {"depth": 18.5,"totalLiquidVolume": 100000,"shape": "rectangular","xDimension": 121,"yDimension": 71,"x": 64,"y": 42.98,"z": 4.5}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1"]}],"parameters": {"format": "irregular","quirks": ["centerMultichannelOnWells","touchTipDisabled"],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "integra_100ml_reservoir"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0}}"""bca_plate_text = """{"ordering": [["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand": {"brand": "Greiner","brandId": ["655101"]},"metadata": {"displayName": "Greiner 96 Flat Bottom BCA Plate","displayCategory": "wellPlate","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.48,"zDimension": 14.6},"wells": {"A1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 74.24,"z": 3.7},"B1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 65.24,"z": 3.7},"C1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 56.24,"z": 3.7},"D1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 47.24,"z": 3.7},"E1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 38.24,"z": 3.7},"F1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 29.24,"z": 3.7},"G1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 20.24,"z": 3.7},"H1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 11.24,"z": 3.7},"A2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 74.24,"z": 3.7},"B2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 65.24,"z": 3.7},"C2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 56.24,"z": 3.7},"D2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 47.24,"z": 3.7},"E2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 38.24,"z": 3.7},"F2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 29.24,"z": 3.7},"G2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 20.24,"z": 3.7},"H2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 11.24,"z": 3.7},"A3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 74.24,"z": 3.7},"B3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 65.24,"z": 3.7},"C3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 56.24,"z": 3.7},"D3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 47.24,"z": 3.7},"E3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 38.24,"z": 3.7},"F3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 29.24,"z": 3.7},"G3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 20.24,"z": 3.7},"H3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 11.24,"z": 3.7},"A4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 74.24,"z": 3.7},"B4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 65.24,"z": 3.7},"C4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 56.24,"z": 3.7},"D4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 47.24,"z": 3.7},"E4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 38.24,"z": 3.7},"F4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 29.24,"z": 3.7},"G4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 20.24,"z": 3.7},"H4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 11.24,"z": 3.7},"A5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 74.24,"z": 3.7},"B5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 65.24,"z": 3.7},"C5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 56.24,"z": 3.7},"D5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 47.24,"z": 3.7},"E5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 38.24,"z": 3.7},"F5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 29.24,"z": 3.7},"G5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 20.24,"z": 3.7},"H5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 11.24,"z": 3.7},"A6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 74.24,"z": 3.7},"B6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 65.24,"z": 3.7},"C6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 56.24,"z": 3.7},"D6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 47.24,"z": 3.7},"E6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 38.24,"z": 3.7},"F6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 29.24,"z": 3.7},"G6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 20.24,"z": 3.7},"H6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 11.24,"z": 3.7},"A7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 74.24,"z": 3.7},"B7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 65.24,"z": 3.7},"C7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 56.24,"z": 3.7},"D7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 47.24,"z": 3.7},"E7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 38.24,"z": 3.7},"F7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 29.24,"z": 3.7},"G7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 20.24,"z": 3.7},"H7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 11.24,"z": 3.7},"A8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 74.24,"z": 3.7},"B8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 65.24,"z": 3.7},"C8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 56.24,"z": 3.7},"D8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 47.24,"z": 3.7},"E8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 38.24,"z": 3.7},"F8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 29.24,"z": 3.7},"G8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 20.24,"z": 3.7},"H8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 11.24,"z": 3.7},"A9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 74.24,"z": 3.7},"B9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 65.24,"z": 3.7},"C9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 56.24,"z": 3.7},"D9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 47.24,"z": 3.7},"E9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 38.24,"z": 3.7},"F9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 29.24,"z": 3.7},"G9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 20.24,"z": 3.7},"H9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 11.24,"z": 3.7},"A10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 74.24,"z": 3.7},"B10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 65.24,"z": 3.7},"C10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 56.24,"z": 3.7},"D10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 47.24,"z": 3.7},"E10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 38.24,"z": 3.7},"F10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 29.24,"z": 3.7},"G10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 20.24,"z": 3.7},"H10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 11.24,"z": 3.7},"A11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 74.24,"z": 3.7},"B11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 65.24,"z": 3.7},"C11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 56.24,"z": 3.7},"D11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 47.24,"z": 3.7},"E11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 38.24,"z": 3.7},"F11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 29.24,"z": 3.7},"G11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 20.24,"z": 3.7},"H11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 11.24,"z": 3.7},"A12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 74.24,"z": 3.7},"B12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 65.24,"z": 3.7},"C12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 56.24,"z": 3.7},"D12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 47.24,"z": 3.7},"E12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 38.24,"z": 3.7},"F12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 29.24,"z": 3.7},"G12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 20.24,"z": 3.7},"H12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 11.24,"z": 3.7}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters": {"format": "irregular","quirks": [],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "greiner_96_flat"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0},"stackingOffsetWithLabware": {"opentrons_universal_flat_adapter": {"x": 0,"y": 0,"z": 9.600000000000001},"opentrons_aluminum_flat_bottom_plate": {"x": 0,"y": 0,"z": 5.559999999999999}}}"""


def run(protocol: protocol_api.ProtocolContext):
    
    # Access parameters
    sample_vol = protocol.params.sample_volume
    diluent_vol = protocol.params.diluent_volume
    reagent_vol = protocol.params.working_reagent_volume
    temp = protocol.params.incubation_temp
    incub_time = protocol.params.incubation_time
    shake_rpm = protocol.params.shake_speed
    
    # Load modules
    hs_mod = protocol.load_module('heaterShakerModuleV1', 3)
    
    # Load labware
    assay_plate = hs_mod.load_labware('corning_96_wellplate_360ul_flat')
    sample_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    reservoir = protocol.load_labware('nest_1_reservoir_195ml', 4)
    
    tiprack_300_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 5)
    tiprack_300_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    tiprack_20_1 = protocol.load_labware('opentrons_96_tiprack_20ul', 7)
    tiprack_20_2 = protocol.load_labware('opentrons_96_tiprack_20ul', 8)
    
    # Load pipettes
    p300_multi = protocol.load_instrument('p300_multi_gen2', 'left', 
                                          tip_racks=[tiprack_300_1, tiprack_300_2])
    p20_multi = protocol.load_instrument('p20_multi_gen2', 'right', 
                                         tip_racks=[tiprack_20_1, tiprack_20_2])
    
    # Define wells
    diluent = reservoir['A1']
    working_reagent = reservoir['A1']  # Can use same well or separate
    
    # Protocol steps
    protocol.comment(f"Starting BCA Assay Protocol")
    protocol.comment(f"Sample: {sample_vol}µL, Diluent: {diluent_vol}µL, "
                    f"Reagent: {reagent_vol}µL")
    
    # Open heater-shaker latch
    hs_mod.open_labware_latch()
    protocol.pause("Please ensure assay plate is properly placed on heater-shaker. "
                  "Resume when ready.")
    hs_mod.close_labware_latch()
    
    # Step 1: Transfer samples (or standards) from sample plate to assay plate
    protocol.comment("Step 1: Transferring samples to assay plate")
    
    if sample_vol <= 20:
        pipette = p20_multi
    else:
        pipette = p300_multi
    
    for col in range(12):  # All 12 columns
        pipette.pick_up_tip()
        pipette.transfer(
            sample_vol,
            sample_plate.columns()[col][0],
            assay_plate.columns()[col][0],
            new_tip='never',
            mix_after=(3, sample_vol if sample_vol <= 20 else 20)
        )
        pipette.drop_tip()
    
    # Step 2: Add diluent if specified
    if diluent_vol > 0:
        protocol.comment(f"Step 2: Adding {diluent_vol}µL diluent")
        
        if diluent_vol <= 20:
            pipette = p20_multi
        else:
            pipette = p300_multi
        
        for col in range(12):
            pipette.pick_up_tip()
            pipette.transfer(
                diluent_vol,
                diluent,
                assay_plate.columns()[col][0],
                new_tip='never',
                mix_after=(3, min(diluent_vol, 20))
            )
            pipette.drop_tip()
    
    # Step 3: Add BCA working reagent
    protocol.comment(f"Step 3: Adding {reagent_vol}µL BCA working reagent")
    
    for col in range(12):
        p300_multi.pick_up_tip()
        p300_multi.transfer(
            reagent_vol,
            working_reagent,
            assay_plate.columns()[col][0],
            new_tip='never',
            mix_after=(5, 50)  # Mix well after adding reagent
        )
        p300_multi.drop_tip()
    
    # Step 4: Shake briefly to mix
    protocol.comment("Step 4: Initial mixing")
    hs_mod.set_and_wait_for_shake_speed(rpm=shake_rpm)
    protocol.delay(seconds=30)
    hs_mod.deactivate_shaker()
    
    # Step 5: Heat and incubate
    protocol.comment(f"Step 5: Incubating at {temp}°C for {incub_time} minutes")
    hs_mod.set_and_wait_for_temperature(temp)
    hs_mod.set_and_wait_for_shake_speed(rpm=shake_rpm)
    protocol.delay(minutes=incub_time)
    
    # Step 6: Stop shaking and cooling
    protocol.comment("Step 6: Cooling down")
    hs_mod.deactivate_shaker()
    hs_mod.deactivate_heater()
    
    # Open latch for plate removal
    hs_mod.open_labware_latch()
    
    protocol.comment("Protocol complete! Remove plate and read absorbance at 562nm")
    protocol.comment(f"Total volume per well: {sample_vol + diluent_vol + reagent_vol}µL")
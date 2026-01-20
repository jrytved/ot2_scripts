#################################################################
#				OPENTRONS SEMI-AUTOMATED BCA-SCRIPT				#
#								JR DEC 2025						#
#################################################################


# Include all labware definitions as .json strings to make sure correct definition is always used.

twintec_text = """{"ordering": [["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand": {"brand": "Eppendorf twin.tec","brandId": []},"metadata": {"displayName": "Eppendorf Twin.tec 96 Well Plate 150 µL","displayCategory": "wellPlate","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.47,"zDimension": 16.06},"wells": {"A1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 74.23,"z": 1.46},"B1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 65.23,"z": 1.46},"C1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 56.23,"z": 1.46},"D1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 47.23,"z": 1.46},"E1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 38.23,"z": 1.46},"F1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 29.23,"z": 1.46},"G1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 20.23,"z": 1.46},"H1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 11.23,"z": 1.46},"A2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 74.23,"z": 1.46},"B2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 65.23,"z": 1.46},"C2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 56.23,"z": 1.46},"D2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 47.23,"z": 1.46},"E2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 38.23,"z": 1.46},"F2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 29.23,"z": 1.46},"G2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 20.23,"z": 1.46},"H2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 11.23,"z": 1.46},"A3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 74.23,"z": 1.46},"B3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 65.23,"z": 1.46},"C3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 56.23,"z": 1.46},"D3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 47.23,"z": 1.46},"E3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 38.23,"z": 1.46},"F3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 29.23,"z": 1.46},"G3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 20.23,"z": 1.46},"H3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 11.23,"z": 1.46},"A4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 74.23,"z": 1.46},"B4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 65.23,"z": 1.46},"C4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 56.23,"z": 1.46},"D4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 47.23,"z": 1.46},"E4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 38.23,"z": 1.46},"F4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 29.23,"z": 1.46},"G4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 20.23,"z": 1.46},"H4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 11.23,"z": 1.46},"A5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 74.23,"z": 1.46},"B5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 65.23,"z": 1.46},"C5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 56.23,"z": 1.46},"D5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 47.23,"z": 1.46},"E5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 38.23,"z": 1.46},"F5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 29.23,"z": 1.46},"G5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 20.23,"z": 1.46},"H5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 11.23,"z": 1.46},"A6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 74.23,"z": 1.46},"B6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 65.23,"z": 1.46},"C6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 56.23,"z": 1.46},"D6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 47.23,"z": 1.46},"E6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 38.23,"z": 1.46},"F6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 29.23,"z": 1.46},"G6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 20.23,"z": 1.46},"H6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 11.23,"z": 1.46},"A7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 74.23,"z": 1.46},"B7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 65.23,"z": 1.46},"C7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 56.23,"z": 1.46},"D7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 47.23,"z": 1.46},"E7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 38.23,"z": 1.46},"F7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 29.23,"z": 1.46},"G7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 20.23,"z": 1.46},"H7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 11.23,"z": 1.46},"A8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 74.23,"z": 1.46},"B8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 65.23,"z": 1.46},"C8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 56.23,"z": 1.46},"D8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 47.23,"z": 1.46},"E8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 38.23,"z": 1.46},"F8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 29.23,"z": 1.46},"G8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 20.23,"z": 1.46},"H8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 11.23,"z": 1.46},"A9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 74.23,"z": 1.46},"B9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 65.23,"z": 1.46},"C9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 56.23,"z": 1.46},"D9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 47.23,"z": 1.46},"E9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 38.23,"z": 1.46},"F9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 29.23,"z": 1.46},"G9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 20.23,"z": 1.46},"H9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 11.23,"z": 1.46},"A10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 74.23,"z": 1.46},"B10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 65.23,"z": 1.46},"C10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 56.23,"z": 1.46},"D10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 47.23,"z": 1.46},"E10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 38.23,"z": 1.46},"F10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 29.23,"z": 1.46},"G10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 20.23,"z": 1.46},"H10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 11.23,"z": 1.46},"A11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 74.23,"z": 1.46},"B11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 65.23,"z": 1.46},"C11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 56.23,"z": 1.46},"D11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 47.23,"z": 1.46},"E11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 38.23,"z": 1.46},"F11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 29.23,"z": 1.46},"G11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 20.23,"z": 1.46},"H11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 11.23,"z": 1.46},"A12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 74.23,"z": 1.46},"B12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 65.23,"z": 1.46},"C12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 56.23,"z": 1.46},"D12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 47.23,"z": 1.46},"E12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 38.23,"z": 1.46},"F12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 29.23,"z": 1.46},"G12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 20.23,"z": 1.46},"H12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 11.23,"z": 1.46}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters": {"format": "irregular","quirks": [],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "eppendorftwin.tec_96_wellplate_150ul"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0},"stackingOffsetWithLabware": {"opentrons_universal_flat_adapter": {"x": 0,"y": 0,"z": 7.709999999999997},"opentrons_aluminum_flat_bottom_plate": {"x": 0,"y": 0,"z": 3.9399999999999977}}}"""

integra_reservoir_text = """{"ordering": [["A1"]],"brand": {"brand": "Integra","brandId": []},"metadata": {"displayName": "Integra 100mL Reservoir","displayCategory": "reservoir","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.48,"zDimension": 23},"wells": {"A1": {"depth": 18.5,"totalLiquidVolume": 100000,"shape": "rectangular","xDimension": 121,"yDimension": 71,"x": 64,"y": 42.98,"z": 4.5}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1"]}],"parameters": {"format": "irregular","quirks": ["centerMultichannelOnWells","touchTipDisabled"],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "integra_100ml_reservoir"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0}}"""bca_plate_text = """{"ordering": [["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand": {"brand": "Greiner","brandId": ["655101"]},"metadata": {"displayName": "Greiner 96 Flat Bottom BCA Plate","displayCategory": "wellPlate","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.48,"zDimension": 14.6},"wells": {"A1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 74.24,"z": 3.7},"B1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 65.24,"z": 3.7},"C1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 56.24,"z": 3.7},"D1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 47.24,"z": 3.7},"E1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 38.24,"z": 3.7},"F1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 29.24,"z": 3.7},"G1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 20.24,"z": 3.7},"H1": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 14.38,"y": 11.24,"z": 3.7},"A2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 74.24,"z": 3.7},"B2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 65.24,"z": 3.7},"C2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 56.24,"z": 3.7},"D2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 47.24,"z": 3.7},"E2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 38.24,"z": 3.7},"F2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 29.24,"z": 3.7},"G2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 20.24,"z": 3.7},"H2": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 23.38,"y": 11.24,"z": 3.7},"A3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 74.24,"z": 3.7},"B3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 65.24,"z": 3.7},"C3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 56.24,"z": 3.7},"D3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 47.24,"z": 3.7},"E3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 38.24,"z": 3.7},"F3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 29.24,"z": 3.7},"G3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 20.24,"z": 3.7},"H3": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 32.38,"y": 11.24,"z": 3.7},"A4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 74.24,"z": 3.7},"B4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 65.24,"z": 3.7},"C4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 56.24,"z": 3.7},"D4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 47.24,"z": 3.7},"E4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 38.24,"z": 3.7},"F4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 29.24,"z": 3.7},"G4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 20.24,"z": 3.7},"H4": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 41.38,"y": 11.24,"z": 3.7},"A5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 74.24,"z": 3.7},"B5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 65.24,"z": 3.7},"C5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 56.24,"z": 3.7},"D5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 47.24,"z": 3.7},"E5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 38.24,"z": 3.7},"F5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 29.24,"z": 3.7},"G5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 20.24,"z": 3.7},"H5": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 50.38,"y": 11.24,"z": 3.7},"A6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 74.24,"z": 3.7},"B6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 65.24,"z": 3.7},"C6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 56.24,"z": 3.7},"D6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 47.24,"z": 3.7},"E6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 38.24,"z": 3.7},"F6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 29.24,"z": 3.7},"G6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 20.24,"z": 3.7},"H6": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 59.38,"y": 11.24,"z": 3.7},"A7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 74.24,"z": 3.7},"B7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 65.24,"z": 3.7},"C7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 56.24,"z": 3.7},"D7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 47.24,"z": 3.7},"E7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 38.24,"z": 3.7},"F7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 29.24,"z": 3.7},"G7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 20.24,"z": 3.7},"H7": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 68.38,"y": 11.24,"z": 3.7},"A8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 74.24,"z": 3.7},"B8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 65.24,"z": 3.7},"C8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 56.24,"z": 3.7},"D8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 47.24,"z": 3.7},"E8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 38.24,"z": 3.7},"F8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 29.24,"z": 3.7},"G8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 20.24,"z": 3.7},"H8": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 77.38,"y": 11.24,"z": 3.7},"A9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 74.24,"z": 3.7},"B9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 65.24,"z": 3.7},"C9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 56.24,"z": 3.7},"D9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 47.24,"z": 3.7},"E9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 38.24,"z": 3.7},"F9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 29.24,"z": 3.7},"G9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 20.24,"z": 3.7},"H9": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 86.38,"y": 11.24,"z": 3.7},"A10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 74.24,"z": 3.7},"B10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 65.24,"z": 3.7},"C10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 56.24,"z": 3.7},"D10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 47.24,"z": 3.7},"E10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 38.24,"z": 3.7},"F10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 29.24,"z": 3.7},"G10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 20.24,"z": 3.7},"H10": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 95.38,"y": 11.24,"z": 3.7},"A11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 74.24,"z": 3.7},"B11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 65.24,"z": 3.7},"C11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 56.24,"z": 3.7},"D11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 47.24,"z": 3.7},"E11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 38.24,"z": 3.7},"F11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 29.24,"z": 3.7},"G11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 20.24,"z": 3.7},"H11": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 104.38,"y": 11.24,"z": 3.7},"A12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 74.24,"z": 3.7},"B12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 65.24,"z": 3.7},"C12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 56.24,"z": 3.7},"D12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 47.24,"z": 3.7},"E12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 38.24,"z": 3.7},"F12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 29.24,"z": 3.7},"G12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 20.24,"z": 3.7},"H12": {"depth": 10.9,"totalLiquidVolume": 382,"shape": "circular","diameter": 6.96,"x": 113.38,"y": 11.24,"z": 3.7}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters": {"format": "irregular","quirks": [],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "greiner_96_flat"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0},"stackingOffsetWithLabware": {"opentrons_universal_flat_adapter": {"x": 0,"y": 0,"z": 9.600000000000001},"opentrons_aluminum_flat_bottom_plate": {"x": 0,"y": 0,"z": 5.559999999999999}}}"""


# We need labware definitions for three plates :: a 150uL twin.tec plate, a 100mL integra reservoir and a greiner flat-bottom 96 well plate for the BCA

from opentrons import protocol_api
from opentrons import types
import itertools
import time
import json

twintec_json = json.loads(twintec_text)
integra_reservoir_json = json.loads(integra_reservoir_text)
bca_plate_json = json.loads(bca_plate_text)

# Final comparison of three ways to pipette the standards in duplicate and three ways to pipette samples in duplicate


metadata = {
	"apiLevel": "2.25",
	"author": "J. Rytved"
}

requirements = {"robotType": "OT-2"}

################################################################################## Pipetting Methods

def pipette_method(PIPETTE, SOURCE: str, DEST_LIST: [str], VOLUME: int, side = "NONE", reuse_tip = False):

	# Pre wet tips, take new tip for each transfer, no air gap

	if reuse_tip:
		PIPETTE.pick_up_tip()
		PIPETTE.mix(2, VOLUME, SOURCE)

	for DEST in DEST_LIST:

		if not reuse_tip:
			PIPETTE.pick_up_tip()
			PIPETTE.mix(2, VOLUME, SOURCE)
		
		PIPETTE.aspirate(VOLUME, SOURCE)

		WELL_BOTTOM = DEST.bottom(1)

		if side == "L":
			x_offset = 2
			x_touch_point = 3

		elif side == "R":
			x_offset = -2
			x_touch_point = -3

		elif side == None:
			x_offset=0 
			x_touch_point = 0

		else:
			raise ValueError("No way!")

		MOVE_TO_LOCATION = WELL_BOTTOM.move(types.Point(x=x_offset, y=0, z=0))
		DISPENSE_LOCATION = WELL_BOTTOM.move(types.Point(x=x_offset, y=0, z=-0.2))
		BLOW_OUT_LOCATION = WELL_BOTTOM.move(types.Point(x=x_touch_point, y=0, z = 3))


		PIPETTE.move_to(MOVE_TO_LOCATION)
		PIPETTE.dispense(VOLUME, DISPENSE_LOCATION)
		PIPETTE.blow_out(BLOW_OUT_LOCATION)

		if not reuse_tip:
			PIPETTE.drop_tip()

	if reuse_tip:
		PIPETTE.drop_tip()

################################################################################## Map for pipetting of standards

STANDARD_TRANSFER_MAP = [

	{"Source": "A1", "Destinations": ["A1", "A2"], "Volume": 20}
]


SAMPLE_TRANSFER_MAP = [

	{"Source": "A1","Destinations": ["A3", "A4", "A5"], "Volume": 10},
	{"Source": "A1","Destinations": ["A6", "A7", "A8"], "Volume": 5},
	{"Source": "A1","Destinations": ["A9", "A10", "A11"], "Volume": 2},

]

DILUENT_TRANSFER_MAP = [
	
	{"Destinations": ["A3", "A4", "A5"], "Volume": 10},
	{"Destinations": ["A6", "A7", "A8"], "Volume": 15},
	{"Destinations": ["A9", "A10", "A11"], "Volume": 18}

]



################################################################################### Miscellaneous parameters

USE_HS_MOD: bool = True
HS_MOD_POS: str = "3"

tip_20_locations = ["9", "10"]
tip_300_locations = ["11"]

WR_VOL: int = 200
HS_TEMP: int = 37									

INCUBATION_TIME_MINUTES: int = 30

P20_ASPIRATE_FLOW_RATE: int = 4
P20_DISPENSE_FLOW_RATE: int = 4

P300_ASPIRATE_FLOW_RATE: int = 30
P300_DISPENSE_FLOW_RATE: int = 35



#################################################################################### Making lists of wells to receive diluent and standards and WR.

DILUENT_RECEIVING_WELLS = list(
	itertools.chain(*[item["Destinations"] for item in SAMPLE_TRANSFER_MAP])
)

STANDARD_RECEIVING_WELLS = list(
	itertools.chain(*[item["Destinations"] for item in STANDARD_TRANSFER_MAP])
)

WR_RECEIVING_WELLS = DILUENT_RECEIVING_WELLS+STANDARD_RECEIVING_WELLS

N_WELLS = len(WR_RECEIVING_WELLS)

TOTAL_VOL_WR = N_WELLS*WR_VOL



############################################################################################################# BEGIN PROTOCOL

def run(protocol: protocol_api.ProtocolContext):

	# MODULES
	hs_mod = protocol.load_module(
	module_name ="heaterShakerModuleV1", location = HS_MOD_POS
	) 

	hs_adapter = hs_mod.load_adapter("opentrons_universal_flat_adapter")

	######################################################################################################### Tip racks

	tip_20_list = [protocol.load_labware("opentrons_96_tiprack_20uL", loc) for loc in tip_20_locations]
	tip_300_list = [protocol.load_labware("opentrons_96_tiprack_300uL", loc) for loc in tip_300_locations]

	######################################################################################################### Plates
	bca_assay_plate = hs_adapter.load_labware_from_definition(bca_plate_json)									
	protein_sample_plate = protocol.load_labware_from_definition(twintec_json, "1")				
	bsa_standard_plate = protocol.load_labware_from_definition(twintec_json, "7")					
	
	######################################################################################################### Reservoirs
	diluent_reservoir = protocol.load_labware_from_definition(integra_reservoir_json, "5")								
	wr_reservoir = protocol.load_labware_from_definition(integra_reservoir_json, "8")									

	######################################################################################################### Pipettes
	pipette_300 = protocol.load_instrument(
		"p300_multi_gen2", mount = "left", tip_racks = tip_300_list
	)

	pipette_20 = protocol.load_instrument(
		"p20_multi_gen2", mount = "right", tip_racks = tip_20_list
	)

	########################################################################################################## Pipette dispensing parameters

	pipette_20.well_bottom_clearance.dispense = 2
	pipette_300.well_bottom_clearance.dispense = 2

	pipette_20.flow_rate.aspirate = P20_ASPIRATE_FLOW_RATE
	pipette_20.flow_rate.dispense = P20_DISPENSE_FLOW_RATE

	pipette_300.flow_rate.aspirate = P300_ASPIRATE_FLOW_RATE
	pipette_300.flow_rate.dispense = P300_DISPENSE_FLOW_RATE



	######################################################################################################### Start up modules

	protocol.comment("Closing labware latch")
	hs_mod.close_labware_latch()

	protocol.comment("Waiting for heater-shaker to heat.")

	if USE_HS_MOD:
		hs_mod.set_target_temperature(celsius=HS_TEMP) 

	######################################################################################################### Handle BSA-standards

	protocol.comment("Transferring BSA-standards")


	for TRANSFER in STANDARD_TRANSFER_MAP:

		SOURCE = bsa_standard_plate[TRANSFER["Source"]]
		DEST = TRANSFER["Destinations"]
		DEST_LIST = [bca_assay_plate[d] for d in DEST]
		VOL = TRANSFER["Volume"]

		# Call the pipetting function

		pipette_method(pipette_20, SOURCE, DEST_LIST, VOLUME = VOL, reuse_tip = False, side = "L")


	######################################################################################################## Handle diluent

	protocol.comment("Transferring diluent to sample wells")

	for TRANSFER in DILUENT_TRANSFER_MAP:
		SOURCE = diluent_reservoir["A1"].bottom(2)
		DEST = TRANSFER["Destinations"]
		VOL = TRANSFER["Volume"]
		DEST_LIST = [bca_assay_plate[d] for d in DEST]

		pipette_method(pipette_20, SOURCE, DEST_LIST, VOLUME=VOL, reuse_tip=False, side="L")

	######################################################################################################### Handle samples

	# Add even slower pipetting steps for the protein sample transfer

	pipette_20.flow_rate.aspirate = 2
	pipette_20.flow_rate.dispense = 2

	protocol.comment("Transferring protein samples")

	for TRANSFER in SAMPLE_TRANSFER_MAP:

		SOURCE = protein_sample_plate[TRANSFER["Source"]]
		DEST_LIST = [bca_assay_plate[d] for d in TRANSFER["Destinations"]]
		VOL = TRANSFER["Volume"]

		pipette_method(pipette_20, SOURCE, DEST_LIST, VOLUME=VOL, reuse_tip=False, side="R")


	######################################################################################################### Handle WR

	pipette_300.pick_up_tip()
	DEST_LIST = [bca_assay_plate[well] for well in WR_RECEIVING_WELLS]
	pipette_300.mix(1, WR_VOL, wr_reservoir["A1"].bottom(2))

	for DEST in DEST_LIST:
		pipette_300.aspirate(WR_VOL, wr_reservoir["A1"].bottom(2))
		pipette_300.dispense(WR_VOL, DEST.top())
		pipette_300.blow_out(DEST.top(-1))
		pipette_300.touch_tip(speed=40)

	pipette_300.drop_tip()

	######################################################################################################### Start shaker for 30 minutes

	hs_mod.set_and_wait_for_temperature(celsius=HS_TEMP)
	hs_mod.set_and_wait_for_shake_speed(800)
	protocol.delay(60*INCUBATION_TIME_MINUTES)

	######################################################################################################## Shut everything down and finish the protocol
	hs_mod.deactivate_heater()
	hs_mod.deactivate_shaker()

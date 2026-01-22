# Proof-of-concept for tip-elution on OT-2

from opentrons import protocol_api
from opentrons import types
import json

from opentrons.types import Mount
from opentrons.protocols.api_support.util import build_edges

stagetip_stack_txt = """
{ "ordering": [ [ "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1" ], [ "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2" ], [ "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3" ], [ "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4" ], [ "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5" ], [ "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6" ], [ "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7" ], [ "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8" ], [ "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9" ], [ "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10" ], [ "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11" ], [ "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12" ] ], "brand": { "brand": "Generic", "brandId": [ "Eppendorf", "Generic" ] }, "metadata": { "displayName": "StageTip Rack Adapter Stacked on 2mL Eppendorf DeepWell", "displayCategory": "tipRack", "displayVolumeUnits": "µL", "tags": [] }, "dimensions": { "xDimension": 127.8, "yDimension": 85.5, "zDimension": 77.6 }, "wells": { "A1": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 14.4, "y": 74.3, "z": 26.84 }, "B1": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 14.4, "y": 65.3, "z": 26.84 }, "C1": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 14.4, "y": 56.3, "z": 26.84 }, "D1": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 14.4, "y": 47.3, "z": 26.84 }, "E1": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 14.4, "y": 38.3, "z": 26.84 }, "F1": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 14.4, "y": 29.3, "z": 26.84 }, "G1": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 14.4, "y": 20.3, "z": 26.84 }, "H1": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 14.4, "y": 11.3, "z": 26.84 }, "A2": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 23.4, "y": 74.3, "z": 26.84 }, "B2": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 23.4, "y": 65.3, "z": 26.84 }, "C2": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 23.4, "y": 56.3, "z": 26.84 }, "D2": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 23.4, "y": 47.3, "z": 26.84 }, "E2": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 23.4, "y": 38.3, "z": 26.84 }, "F2": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 23.4, "y": 29.3, "z": 26.84 }, "G2": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 23.4, "y": 20.3, "z": 26.84 }, "H2": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 23.4, "y": 11.3, "z": 26.84 }, "A3": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 32.4, "y": 74.3, "z": 26.84 }, "B3": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 32.4, "y": 65.3, "z": 26.84 }, "C3": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 32.4, "y": 56.3, "z": 26.84 }, "D3": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 32.4, "y": 47.3, "z": 26.84 }, "E3": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 32.4, "y": 38.3, "z": 26.84 }, "F3": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 32.4, "y": 29.3, "z": 26.84 }, "G3": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 32.4, "y": 20.3, "z": 26.84 }, "H3": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 32.4, "y": 11.3, "z": 26.84 }, "A4": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 41.4, "y": 74.3, "z": 26.84 }, "B4": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 41.4, "y": 65.3, "z": 26.84 }, "C4": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 41.4, "y": 56.3, "z": 26.84 }, "D4": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 41.4, "y": 47.3, "z": 26.84 }, "E4": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 41.4, "y": 38.3, "z": 26.84 }, "F4": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 41.4, "y": 29.3, "z": 26.84 }, "G4": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 41.4, "y": 20.3, "z": 26.84 }, "H4": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 41.4, "y": 11.3, "z": 26.84 }, "A5": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 50.4, "y": 74.3, "z": 26.84 }, "B5": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 50.4, "y": 65.3, "z": 26.84 }, "C5": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 50.4, "y": 56.3, "z": 26.84 }, "D5": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 50.4, "y": 47.3, "z": 26.84 }, "E5": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 50.4, "y": 38.3, "z": 26.84 }, "F5": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 50.4, "y": 29.3, "z": 26.84 }, "G5": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 50.4, "y": 20.3, "z": 26.84 }, "H5": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 50.4, "y": 11.3, "z": 26.84 }, "A6": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 59.4, "y": 74.3, "z": 26.84 }, "B6": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 59.4, "y": 65.3, "z": 26.84 }, "C6": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 59.4, "y": 56.3, "z": 26.84 }, "D6": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 59.4, "y": 47.3, "z": 26.84 }, "E6": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 59.4, "y": 38.3, "z": 26.84 }, "F6": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 59.4, "y": 29.3, "z": 26.84 }, "G6": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 59.4, "y": 20.3, "z": 26.84 }, "H6": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 59.4, "y": 11.3, "z": 26.84 }, "A7": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 68.4, "y": 74.3, "z": 26.84 }, "B7": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 68.4, "y": 65.3, "z": 26.84 }, "C7": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 68.4, "y": 56.3, "z": 26.84 }, "D7": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 68.4, "y": 47.3, "z": 26.84 }, "E7": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 68.4, "y": 38.3, "z": 26.84 }, "F7": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 68.4, "y": 29.3, "z": 26.84 }, "G7": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 68.4, "y": 20.3, "z": 26.84 }, "H7": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 68.4, "y": 11.3, "z": 26.84 }, "A8": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 77.4, "y": 74.3, "z": 26.84 }, "B8": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 77.4, "y": 65.3, "z": 26.84 }, "C8": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 77.4, "y": 56.3, "z": 26.84 }, "D8": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 77.4, "y": 47.3, "z": 26.84 }, "E8": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 77.4, "y": 38.3, "z": 26.84 }, "F8": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 77.4, "y": 29.3, "z": 26.84 }, "G8": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 77.4, "y": 20.3, "z": 26.84 }, "H8": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 77.4, "y": 11.3, "z": 26.84 }, "A9": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 86.4, "y": 74.3, "z": 26.84 }, "B9": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 86.4, "y": 65.3, "z": 26.84 }, "C9": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 86.4, "y": 56.3, "z": 26.84 }, "D9": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 86.4, "y": 47.3, "z": 26.84 }, "E9": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 86.4, "y": 38.3, "z": 26.84 }, "F9": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 86.4, "y": 29.3, "z": 26.84 }, "G9": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 86.4, "y": 20.3, "z": 26.84 }, "H9": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 86.4, "y": 11.3, "z": 26.84 }, "A10": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 95.4, "y": 74.3, "z": 26.84 }, "B10": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 95.4, "y": 65.3, "z": 26.84 }, "C10": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 95.4, "y": 56.3, "z": 26.84 }, "D10": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 95.4, "y": 47.3, "z": 26.84 }, "E10": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 95.4, "y": 38.3, "z": 26.84 }, "F10": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 95.4, "y": 29.3, "z": 26.84 }, "G10": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 95.4, "y": 20.3, "z": 26.84 }, "H10": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 95.4, "y": 11.3, "z": 26.84 }, "A11": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 104.4, "y": 74.3, "z": 26.84 }, "B11": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 104.4, "y": 65.3, "z": 26.84 }, "C11": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 104.4, "y": 56.3, "z": 26.84 }, "D11": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 104.4, "y": 47.3, "z": 26.84 }, "E11": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 104.4, "y": 38.3, "z": 26.84 }, "F11": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 104.4, "y": 29.3, "z": 26.84 }, "G11": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 104.4, "y": 20.3, "z": 26.84 }, "H11": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 104.4, "y": 11.3, "z": 26.84 }, "A12": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 113.4, "y": 74.3, "z": 26.84 }, "B12": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 113.4, "y": 65.3, "z": 26.84 }, "C12": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 113.4, "y": 56.3, "z": 26.84 }, "D12": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 113.4, "y": 47.3, "z": 26.84 }, "E12": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 113.4, "y": 38.3, "z": 26.84 }, "F12": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 113.4, "y": 29.3, "z": 26.84 }, "G12": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 113.4, "y": 20.3, "z": 26.84 }, "H12": { "depth": 50.76, "totalLiquidVolume": 200, "shape": "circular", "diameter": 5.24, "x": 113.4, "y": 11.3, "z": 26.84 } }, "groups": [ { "metadata": {}, "wells": [ "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11", "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12" ] } ], "parameters": { "format": "irregular", "quirks": [], "isTiprack": true, "tipLength": 50.76, "isMagneticModuleCompatible": false, "loadName": "stagetip_eppendorf_2ml_stack" }, "namespace": "custom_beta", "version": 1, "schemaVersion": 2, "cornerOffsetFromSlot": { "x": 0, "y": 0, "z": 0 } }
"""

stagetip_stack_def = json.loads(stagetip_stack_txt)

integra_reservoir_text = """{"ordering": [["A1"]],"brand": {"brand": "Integra","brandId": []},"metadata": {"displayName": "Integra 100mL Reservoir","displayCategory": "reservoir","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.48,"zDimension": 23},"wells": {"A1": {"depth": 18.5,"totalLiquidVolume": 100000,"shape": "rectangular","xDimension": 121,"yDimension": 71,"x": 64,"y": 42.98,"z": 4.5}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1"]}],"parameters": {"format": "irregular","quirks": ["centerMultichannelOnWells","touchTipDisabled"],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "integra_100ml_reservoir"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0}}"""

integra_reservoir_def = json.loads(integra_reservoir_text)

twintec_text = """{"ordering": [["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand": {"brand": "Eppendorf twin.tec","brandId": []},"metadata": {"displayName": "Eppendorf Twin.tec 96 Well Plate 150 µL","displayCategory": "wellPlate","displayVolumeUnits": "µL","tags": []},"dimensions": {"xDimension": 127.76,"yDimension": 85.47,"zDimension": 16.06},"wells": {"A1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 74.23,"z": 1.46},"B1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 65.23,"z": 1.46},"C1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 56.23,"z": 1.46},"D1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 47.23,"z": 1.46},"E1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 38.23,"z": 1.46},"F1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 29.23,"z": 1.46},"G1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 20.23,"z": 1.46},"H1": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 14.38,"y": 11.23,"z": 1.46},"A2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 74.23,"z": 1.46},"B2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 65.23,"z": 1.46},"C2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 56.23,"z": 1.46},"D2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 47.23,"z": 1.46},"E2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 38.23,"z": 1.46},"F2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 29.23,"z": 1.46},"G2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 20.23,"z": 1.46},"H2": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 23.38,"y": 11.23,"z": 1.46},"A3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 74.23,"z": 1.46},"B3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 65.23,"z": 1.46},"C3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 56.23,"z": 1.46},"D3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 47.23,"z": 1.46},"E3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 38.23,"z": 1.46},"F3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 29.23,"z": 1.46},"G3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 20.23,"z": 1.46},"H3": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 32.38,"y": 11.23,"z": 1.46},"A4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 74.23,"z": 1.46},"B4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 65.23,"z": 1.46},"C4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 56.23,"z": 1.46},"D4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 47.23,"z": 1.46},"E4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 38.23,"z": 1.46},"F4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 29.23,"z": 1.46},"G4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 20.23,"z": 1.46},"H4": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 41.38,"y": 11.23,"z": 1.46},"A5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 74.23,"z": 1.46},"B5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 65.23,"z": 1.46},"C5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 56.23,"z": 1.46},"D5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 47.23,"z": 1.46},"E5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 38.23,"z": 1.46},"F5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 29.23,"z": 1.46},"G5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 20.23,"z": 1.46},"H5": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 50.38,"y": 11.23,"z": 1.46},"A6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 74.23,"z": 1.46},"B6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 65.23,"z": 1.46},"C6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 56.23,"z": 1.46},"D6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 47.23,"z": 1.46},"E6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 38.23,"z": 1.46},"F6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 29.23,"z": 1.46},"G6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 20.23,"z": 1.46},"H6": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 59.38,"y": 11.23,"z": 1.46},"A7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 74.23,"z": 1.46},"B7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 65.23,"z": 1.46},"C7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 56.23,"z": 1.46},"D7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 47.23,"z": 1.46},"E7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 38.23,"z": 1.46},"F7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 29.23,"z": 1.46},"G7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 20.23,"z": 1.46},"H7": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 68.38,"y": 11.23,"z": 1.46},"A8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 74.23,"z": 1.46},"B8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 65.23,"z": 1.46},"C8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 56.23,"z": 1.46},"D8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 47.23,"z": 1.46},"E8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 38.23,"z": 1.46},"F8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 29.23,"z": 1.46},"G8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 20.23,"z": 1.46},"H8": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 77.38,"y": 11.23,"z": 1.46},"A9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 74.23,"z": 1.46},"B9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 65.23,"z": 1.46},"C9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 56.23,"z": 1.46},"D9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 47.23,"z": 1.46},"E9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 38.23,"z": 1.46},"F9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 29.23,"z": 1.46},"G9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 20.23,"z": 1.46},"H9": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 86.38,"y": 11.23,"z": 1.46},"A10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 74.23,"z": 1.46},"B10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 65.23,"z": 1.46},"C10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 56.23,"z": 1.46},"D10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 47.23,"z": 1.46},"E10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 38.23,"z": 1.46},"F10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 29.23,"z": 1.46},"G10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 20.23,"z": 1.46},"H10": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 95.38,"y": 11.23,"z": 1.46},"A11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 74.23,"z": 1.46},"B11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 65.23,"z": 1.46},"C11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 56.23,"z": 1.46},"D11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 47.23,"z": 1.46},"E11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 38.23,"z": 1.46},"F11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 29.23,"z": 1.46},"G11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 20.23,"z": 1.46},"H11": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 104.38,"y": 11.23,"z": 1.46},"A12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 74.23,"z": 1.46},"B12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 65.23,"z": 1.46},"C12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 56.23,"z": 1.46},"D12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 47.23,"z": 1.46},"E12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 38.23,"z": 1.46},"F12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 29.23,"z": 1.46},"G12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 20.23,"z": 1.46},"H12": {"depth": 14.6,"totalLiquidVolume": 150,"shape": "circular","diameter": 6.46,"x": 113.38,"y": 11.23,"z": 1.46}},"groups": [{"metadata": {"wellBottomShape": "flat"},"wells": ["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters": {"format": "irregular","quirks": [],"isTiprack": false,"isMagneticModuleCompatible": false,"loadName": "eppendorftwin.tec_96_wellplate_150ul"},"namespace": "custom_beta","version": 1,"schemaVersion": 2,"cornerOffsetFromSlot": {"x": 0,"y": 0,"z": 0},"stackingOffsetWithLabware": {"opentrons_universal_flat_adapter": {"x": 0,"y": 0,"z": 7.709999999999997},"opentrons_aluminum_flat_bottom_plate": {"x": 0,"y": 0,"z": 3.9399999999999977}}}"""

twintec_def = json.loads(twintec_text)

metadata = {
	"apiLevel": "2.9",
	"author": "J. Rytved"
}

requirements = {"robotType": "OT-2"}

VOL: int = 20


def run(protocol: protocol_api.ProtocolContext):

	stagetip_stack = protocol.load_labware_from_definition(stagetip_stack_def, "1")
	# reservoir = protocol.load_labware_from_definition(integra_reservoir_def, "7") If one was using the other single well reservoirs
	reservoir = protocol.load_labware("nest_12_reservoir_15mL", "3")
	sample_plate = protocol.load_labware_from_definition(twintec_def, "6")


	tip_20_locations = ["7", "10"]
	tip_20_list = [protocol.load_labware("opentrons_96_tiprack_20uL", loc) for loc in tip_20_locations]

	tip_300_locations = ["4"]
	tip_300_list = [protocol.load_labware("opentrons_96_tiprack_300uL", loc) for loc in tip_300_locations]

	pipette_20 = protocol.load_instrument("p20_multi_gen2", mount = "right", tip_racks = tip_20_list)
	pipette_300 = protocol.load_instrument("p300_multi_gen2", mount = "left", tip_racks = tip_300_list)

	# Set locations for buffers

	buffer_a_well = reservoir["A1"]
	buffer_b_well = reservoir["A2"]
	isopropanol_well = reservoir["A3"]

	#target_wells = [f"A{idx}" for idx in range(1,13)]

	target_wells = ["A1"]

	def elute_resin_tip_at_loc(protocol, loc, pipette_300, wait = 100, return_at_end = True):

		"""
		
		Elutes resin tips in a tip rack location. Loc denotes upper row well in a column, e.g. any well in {A1, A2 ... A12}.

		The specific offsets here are manually adjusted to be ideal for EvoTips and not necessarily for other StageTips - use with caution
		and alter the z-axis offsets if neccesary.

		"""

		# Set up the hardware api

		hardware_api = protocol._hw_manager.hardware
		p300Mount = pipette_300.mount.lower() == 'left' and Mount.LEFT or Mount.RIGHT
		hardware_api.add_tip(mount=p300Mount, tip_length=50)
		pipette_300.move_to(loc.top())
		pipette_300.move_to(loc.top(-45), speed=40)
		pipette_300.move_to(loc.top(-50), speed=4)

		# Position for tip pick up , aspirate air
		hardware_api.prepare_for_aspirate(mount=p300Mount)
		hardware_api.aspirate(mount=p300Mount, volume=300)

		# Actually load the tips
		protocol.delay(1)
		pipette_300.move_to(loc.top(-58), speed=10)

		# Go back up and dispense some air
		pipette_300.move_to(loc.top(-10), speed=10)
		hardware_api.dispense(mount=p300Mount, volume=300)

		# And wait
		protocol.delay(wait)	

		# Move back up and drop tips
		pipette_300.move_to(loc.top(-40), speed=2)
		protocol.delay(1)

		if return_at_end:
			hardware_api.drop_tip(mount=p300Mount, home_after=False)
			protocol.delay(2)

	# Rinse with 20uL B

	protocol.comment("Rinsing with 20uL of buffer B")

	pipette_300.pick_up_tip()

	# Pick up buffer B
	pipette_300.move_to(buffer_b_well.top())
	pipette_300.move_to(buffer_b_well.bottom(4), speed=4)
	pipette_300.aspirate(20)
	pipette_300.move_to(buffer_b_well.top(), speed=10)
	pipette_300.air_gap(20)


	# Dispense into the tip column

	pipette_300.move_to(stagetip_stack["A1"].top(), speed=40)
	pipette_300.move_to(stagetip_stack["A1"].top(-30), speed=4)
	pipette_300.dispense(40)
	pipette_300.move_to(stagetip_stack["A1"].top(), speed=4)
	pipette_300.return_tip()

	# Push the buffer B over the resin

	elute_resin_tip_at_loc(protocol, stagetip_stack["A1"], pipette_300, wait = 20, return_at_end=False)

	# Dip the tips in the isopropanol and put them back in the rack

	pipette_300.move_to(isopropanol_well.top(), speed=40)
	pipette_300.move_to(isopropanol_well.bottom(1), speed=4)
	protocol.delay(30)

	pipette_300.move_to(stagetip_stack["A1"].top(-40), speed=40)
	p300Mount = pipette_300.mount.lower() == 'left' and Mount.LEFT or Mount.RIGHT
	hardware_api = protocol._hw_manager.hardware
	hardware_api.drop_tip(mount=p300Mount, home_after=False)

	protocol.comment("Adding equilibration buffer A into tips")

	# Dispense equilibration buffer A into tips

	pipette_300.pick_up_tip()
	pipette_300.move_to(buffer_a_well.top(), speed=40)
	pipette_300.move_to(buffer_a_well.bottom(4), speed=4)
	pipette_300.aspirate(20)
	pipette_300.move_to(buffer_a_well.top(), speed=4)

	pipette_300.move_to(stagetip_stack["A1"].top(), speed=40)
	pipette_300.move_to(stagetip_stack["A1"].top(-30), speed=4)
	pipette_300.dispense(20)
	pipette_300.move_to(stagetip_stack["A1"].top(), speed=4)
	pipette_300.return_tip()

	protocol.comment("Adding some mock sample to the tips")

	# Pick up from TwinTec plate

	pipette_20.pick_up_tip()
	pipette_20.move_to(sample_plate["A1"].top())
	pipette_20.move_to(sample_plate["A1"].bottom(1))
	pipette_20.aspirate(20)
	pipette_20.move_to(sample_plate["A1"].top())

	# Dispense to the tip rack

	pipette_20.move_to(stagetip_stack["A1"].top(), speed=40)
	pipette_20.move_to(stagetip_stack["A1"].top(-20), speed=4)
	pipette_20.dispense(20)
	pipette_20.move_to(stagetip_stack["A1"].top(), speed=4)
	pipette_20.return_tip()

	# Dispense wash buffer A into tips

	pipette_300.pick_up_tip()
	pipette_300.move_to(buffer_a_well.top(), speed=40)
	pipette_300.move_to(buffer_a_well.bottom(4), speed=4)
	pipette_300.aspirate(50)
	pipette_300.move_to(buffer_a_well.top(), speed=4)

	pipette_300.move_to(stagetip_stack["A1"].top(), speed=40)
	pipette_300.move_to(stagetip_stack["A1"].top(-10), speed=4)
	pipette_300.dispense(50)
	pipette_300.move_to(stagetip_stack["A1"].top(), speed=4)
	pipette_300.return_tip()

	protocol.comment("Trying to push sample over resin")

	elute_resin_tip_at_loc(protocol, stagetip_stack["A1"], pipette_300, wait = 120)
		

	protocol.home()



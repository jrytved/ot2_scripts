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

metadata = {
	"apiLevel": "2.9",
	"author": "J. Rytved"
}

requirements = {"robotType": "OT-2"}

VOL: int = 20


def run(protocol: protocol_api.ProtocolContext):

	stagetip_stack = protocol.load_labware_from_definition(stagetip_stack_def, "1")
	reservoir = protocol.load_labware_from_definition(integra_reservoir_def, "7")

	tip_20_locations = ["2", "3"]
	tip_20_list = [protocol.load_labware("opentrons_96_tiprack_20uL", loc) for loc in tip_20_locations]

	tip_300_locations = ["4"]
	tip_300_list = [protocol.load_labware("opentrons_96_tiprack_300uL", loc) for loc in tip_300_locations]

	pipette_20 = protocol.load_instrument("p20_multi_gen2", mount = "right", tip_racks = tip_20_list)
	pipette_300 = protocol.load_instrument("p300_multi_gen2", mount = "left", tip_racks = tip_300_list)

	#target_wells = [f"A{idx}" for idx in range(1,13)]

	target_wells = ["A1"]


	for well in target_wells:

		w = stagetip_stack[well]

		top = w.top()

		offsets = [-30, -20, -19]

		# Build list of (x,y,z) locations to move pipette to
		targets = [top.move(types.Point(x=0,y=0,z=offset)) for offset in offsets]

		pipette_20.pick_up_tip()

		for target in targets:
			
			pipette_20.aspirate(VOL, reservoir["A1"])
			pipette_20.move_to(target)
			pipette_20.dispense(VOL)
			pipette_20.move_to(top)

		pipette_20.return_tip()

	# Try to pick up some of the stage-tips

	protocol.comment("Trying to push sample over resin")


	for well_idx in target_wells:

		loc = stagetip_stack[well_idx]

		pipette_300.pick_up_tip(loc)

		hardware_api = protocol._hw_manager.hardware
		p300Mount = pipette_300.mount.lower() == 'left' and Mount.LEFT or Mount.RIGHT
		hardware_api.add_tip(mount=p300Mount, tip_length=50)
		pipette_300.move_to(loc.top(30))
		pipette_300.move_to(loc.bottom(-10))
		hardware_api.prepare_for_aspirate(mount=p300Mount)
		hardware_api.aspirate(mount=p300Mount, volume=200, rate=10)
		hardware_api.dispense(mount=p300Mount, volume=250, rate=100)
		protocol.delay(seconds=60)
		pipette_300.move_to(loc.bottom(-25), speed=20)
		hardware_api.drop_tip(mount=p300Mount, home_after=False)
		protocol.home()




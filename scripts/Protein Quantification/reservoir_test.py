from opentrons import protocol_api
import json

epmo30_text = """{ "ordering": [ [ "A1" ], [ "A2" ], [ "A3" ] ], "brand": { "brand": "JohanMade", "brandId": [ "PART01" ] }, "metadata": { "displayName": "JohanMade EpMotion 30mL Reservoir Adapter", "displayCategory": "reservoir", "displayVolumeUnits": "µL", "tags": [] }, "dimensions": { "xDimension": 127.76, "yDimension": 85.48, "zDimension": 65.5 }, "wells": { "A1": { "depth": 53, "totalLiquidVolume": 30000, "shape": "rectangular", "xDimension": 14.85, "yDimension": 85.48, "x": 34.23, "y": 42.74, "z": 12.5 }, "A2": { "depth": 53, "totalLiquidVolume": 30000, "shape": "rectangular", "xDimension": 14.85, "yDimension": 85.48, "x": 63.23, "y": 42.74, "z": 12.5 }, "A3": { "depth": 53, "totalLiquidVolume": 30000, "shape": "rectangular", "xDimension": 14.85, "yDimension": 85.48, "x": 92.23, "y": 42.74, "z": 12.5 } }, "groups": [ { "metadata": { "wellBottomShape": "v" }, "wells": [ "A1", "A2", "A3" ] } ], "parameters": { "format": "irregular", "quirks": [ "centerMultichannelOnWells", "touchTipDisabled" ], "isTiprack": false, "isMagneticModuleCompatible": false, "loadName": "epmo_30" }, "namespace": "custom_beta", "version": 1, "schemaVersion": 2, "cornerOffsetFromSlot": { "x": 0, "y": 0, "z": 0 } }"""
epmo30_json = json.loads(epmo30_text)

metadata = {
    "apiLevel": "2.25",
    "author": "J. Rytved"
}
requirements = {"robotType": "OT-2"}

def run(protocol: protocol_api.ProtocolContext):

    tips_300  = protocol.load_labware("opentrons_96_tiprack_300uL", "3")
    std_plate = protocol.load_labware("eppendorf_96_wellplate_1000ul", "1")
    reservoir = protocol.load_labware_from_definition(epmo30_json, "10")
    pipette_300 = protocol.load_instrument(
        "p300_multi_gen2", mount="left", tip_racks=[tips_300]
    )

    water = reservoir["A1"]

    pipette_300.pick_up_tip()
    for col in std_plate.columns():
        pipette_300.aspirate(300, water)
        pipette_300.dispense(300, col[0])
        pipette_300.blow_out(col[0].top(-2))
    pipette_300.drop_tip()
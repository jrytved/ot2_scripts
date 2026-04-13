from opentrons import protocol_api
import json

epmo30_json = json.loads(epmo30_text)

metadata = {
    "apiLevel": "2.25",
    "author": "J. Rytved"
}
requirements = {"robotType": "OT-2"}

def run(protocol: protocol_api.ProtocolContext):

    tips_300  = protocol.load_labware("opentrons_96_tiprack_300uL", "4")
    std_plate = protocol.load_labware("eppendorf_96_wellplate_1000ul", "1")
    reservoir = protocol.load_labware_from_definition(epmo30_json, "7")
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
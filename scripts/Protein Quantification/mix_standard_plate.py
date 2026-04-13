epmo30_text = """{ "ordering": [ [ "A1" ], [ "A2" ], [ "A3" ] ], "brand": { "brand": "Eppendorf", "brandId": [ "EpMotion 30mL" ] }, "metadata": { "displayName": "EpMotion 30mL", "displayCategory": "reservoir", "displayVolumeUnits": "µL", "tags": [] }, "dimensions": { "xDimension": 127.76, "yDimension": 85.48, "zDimension": 62 }, "wells": { "A1": { "depth": 53, "totalLiquidVolume": 35000, "shape": "rectangular", "xDimension": 12.75, "yDimension": 75.48, "x": 35.81, "y": 42.74, "z": 9 }, "A2": { "depth": 53, "totalLiquidVolume": 35000, "shape": "rectangular", "xDimension": 12.75, "yDimension": 75.48, "x": 63.87, "y": 42.74, "z": 9 }, "A3": { "depth": 53, "totalLiquidVolume": 35000, "shape": "rectangular", "xDimension": 12.75, "yDimension": 75.48, "x": 91.93, "y": 42.74, "z": 9 } }, "groups": [ { "metadata": { "wellBottomShape": "flat" }, "wells": [ "A1", "A2", "A3" ] } ], "parameters": { "format": "irregular", "quirks": [ "centerMultichannelOnWells", "touchTipDisabled" ], "isTiprack": false, "isMagneticModuleCompatible": false, "loadName": "epmotion_30" }, "namespace": "custom_beta", "version": 1, "schemaVersion": 2, "cornerOffsetFromSlot": { "x": 0, "y": 0, "z": 0 } }"""

from opentrons import protocol_api
import json

epmo30_json = json.loads(epmo30_text)

metadata = {
    "apiLevel": "2.25",
    "author": "J. Rytved"
}
requirements = {"robotType": "OT-2"}

def run(protocol: protocol_api.ProtocolContext):

    tips_300    = protocol.load_labware("opentrons_96_tiprack_300uL", "4")
    std_plate   = protocol.load_labware("eppendorf_96_wellplate_500ul", "1")
    reservoir   = protocol.load_labware_from_definition(epmo30_json, "7")
    pipette_300 = protocol.load_instrument(
        "p300_multi_gen2", mount="left", tip_racks=[tips_300]
    )

    water = reservoir["A1"]
    stock = std_plate["A1"]

    # -------------------------------------------------------------------
    # Dilution table — direct dilution from stock into each well.
    # Best practice: water dispensed first, stock added second.
    # All volumes in µL. Working volume = 300 µL per well.
    # Formula: v_stock = (C_target / 2000) * 300
    # -------------------------------------------------------------------
    dilutions = [
        # (well,  v_water, v_stock)
        ("A2",  60,  240),   # 1600 µg/µL
        ("A3", 120,  180),   # 1200 µg/µL
        ("A4", 180,  120),   #  800 µg/µL
        ("A5", 210,   90),   #  600 µg/µL
        ("A6", 240,   60),   #  400 µg/µL
        ("A7", 255,   45),   #  300 µg/µL
        ("A8", 270,   30),   #  200 µg/µL
    ]

    # ── Step 1: dispense water into all destination wells (single tip) ──
    pipette_300.pick_up_tip()
    for well, v_water, _ in dilutions:
        if v_water > 0:
            pipette_300.aspirate(v_water, water)
            pipette_300.dispense(v_water, std_plate[well])
            pipette_300.blow_out(std_plate[well].top(-2))
    pipette_300.drop_tip()

    # ── Step 2: add stock and mix (fresh tip per well) ──────────────────
    for well, _, v_stock in dilutions:
        pipette_300.pick_up_tip()
        pipette_300.aspirate(v_stock, stock)
        pipette_300.dispense(v_stock, std_plate[well])

        # Mix: 5× at 80 % of working volume (240 µL) for thorough mixing.
        # For A7/A8 where v_stock ≤ 45 µL, reduce mix volume to 200 µL
        # to stay comfortably within p300 range.
        mix_vol = 200 if v_stock <= 45 else 240
        pipette_300.mix(5, mix_vol, std_plate[well])

        pipette_300.blow_out(std_plate[well].top(-2))
        pipette_300.drop_tip()






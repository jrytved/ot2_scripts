from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Customizable BCA Assay',
    'author': 'Your Name',
    'description': 'BCA protein assay with customizable volumes',
    'apiLevel': '2.27'
}

# Protocol parameters
def add_parameters(parameters):
    parameters.add_int(
        variable_name="sample_volume",
        display_name="Sample Volume (µL)",
        description="Volume of sample to transfer",
        default=10,
        minimum=1,
        maximum=25,
        unit="µL"
    )
    
    parameters.add_int(
        variable_name="diluent_volume",
        display_name="Diluent Volume (µL)",
        description="Volume of diluent to add to samples",
        default=15,
        minimum=0,
        maximum=100,
        unit="µL"
    )
    
    parameters.add_int(
        variable_name="working_reagent_volume",
        display_name="Working Reagent Volume (µL)",
        description="Volume of BCA working reagent",
        default=200,
        minimum=50,
        maximum=250,
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
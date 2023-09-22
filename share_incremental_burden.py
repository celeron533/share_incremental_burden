# share_incremental_burden
from typing import Dict
import abc

def redistribute_integer_dose_single_shot_by_weight(dose_by_beam: Dict, cGy_to_distribute: int) ->  Dict:
    """
    Redistribute the given dose to the beams

    Args:
        dose_by_beam (Dict): pairs of beams and doses
        cGy_to_distribute (int): the dose that would be distributed to the beams above

    Returns:
        Dict: pairs of beams and redistributed doses
    """
    redist = dict(dose_by_beam)
    sign = 1
    if cGy_to_distribute < 0:
        sign = -1
    
    dose_sum = sum (dose_by_beam.values())
    
    dist_per_beam_cGy = cGy_to_distribute/dose_sum

    for key in dose_by_beam:
        weight = redist[key]/dose_sum
        weighted_burden = weight * cGy_to_distribute
        dose_increment = round(weighted_burden-0.5) # round down
        print (f"key {key}, value {dose_by_beam[key]}, dose_increment = {dose_increment} from weighted+burden {weighted_burden} using weight {weight}")
        redist[key] += dose_increment

    redist_sum = sum (redist.values())

    initial_remainder = cGy_to_distribute - (redist_sum -dose_sum)
    print(f"Initial remainder = {initial_remainder}")
    # sorted_dosedict_by_value_descending = [ key, value for key,value in sorted(redist,reverse=True) ]
    return redist


def redistribute_integer_dose(dose_by_beam:Dict, cGy_to_distribute:int) -> Dict:
    dose_sum = sum(dose_by_beam.values())
    redist = dict(dose_by_beam)
    # redist = redistribute_integer_dose_single_shot_by_weight(dose_by_beam, cGy_to_distribute)
    # redist_sum = sum(redist.values())
    initial_remainder = cGy_to_distribute # - (redist_sum - dose_sum)
    sorted_list_of_dose = sorted(dose_by_beam.items(),key=lambda x: x[1],reverse=True)

    list_index = 0
    current_dose = 0
    next_dose = 0
    remainder = initial_remainder
    cGy_to_distribute = initial_remainder
    sign = 1
    if (cGy_to_distribute <0):
        sign = -1
    
    list_size = len(sorted_list_of_dose)
    while (remainder != 0):
        for i in range(sign,(cGy_to_distribute+sign), sign):
            current_dose = redist[sorted_list_of_dose[list_index][0]]
            current_dose += sign
            remainder -= sign
            redist[sorted_list_of_dose[list_index][0]] = current_dose
            if list_index+1 >= list_size:
                break
            next_dose = redist[sorted_list_of_dose[list_index+1][0]]
            if ( 
                abs(1.0- ((current_dose + sign) / sorted_list_of_dose[list_index][1])) > 
                abs(1.0 - ((next_dose + sign)/sorted_list_of_dose[list_index+1][1]))
                ):
                list_index += 1
        cGy_to_distribute = remainder
        list_index=0

    return redist

if __name__ == "__main__":
    dose = {1: 100, 2: 50, 3: 25, 4: 25}
    sorted_list_of_dose = sorted(dose.items(),key=lambda x: x[1],reverse=True)
   # dose = dict(redist)
    dose_sum = sum (dose.values())
    cGy_to_distribute = -9
    #redist = redistribute_integer_dose_single_shot_by_weight(dose,cGy_to_distribute)
    #print(redist)
    redist = redistribute_integer_dose(dose,cGy_to_distribute)
    print(redist)
    redist_sum = sum(redist.values())
    print(f"dose_sum + cGy_to_distribute  = redist_sum ")
    print(f" {dose_sum} + {cGy_to_distribute} =  {redist_sum} ?")

import argparse
import json
from collections import defaultdict

def load_from_json(raw_json: str):
    return json.loads(raw_json)
    #TODO: Max size of raw JSON? 
    #TODO: More clever object representation of tunes? (not sure if I want that yet)
    
def main(filename: str):
    with open(filename, 'r') as tunesfile:
        #TODO: Max size of raw JSON? 
        tunes_json = tunesfile.read() 
        tune_list = load_from_json(tunes_json)

        tune_type = defaultdict(int)
        tune_time = defaultdict(int)
        tune_mode = defaultdict(int)

        # Note that this includes multiple settings of the same tune
        for tune in tune_list:
            tune_type[tune['type']] += 1
            tune_time[tune['meter']] += 1
            tune_mode[tune['mode']] += 1
            

        print(tune_type)
        print(tune_time)
        print(tune_mode)
            


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description="Count up some stats about tunes")

    parser.add_argument("--jsonfile", dest='tunefile',
                        help='File to load tune list from')
    
    args = parser.parse_args()
    main(args.tunefile)
    

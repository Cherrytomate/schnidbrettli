import json
import os

def API_Counter():
        json_file = open('../customer/API_counter.json', "r")
        file = json.load(json_file)
        json_file.close()


        if (file['API_Users'][0]['Count']  < 49 ):
            print(file['API_Users'][0]['Email'] + " is used " + str(file['API_Users'][0]['Count']) + " times of 50" )
            
            file['API_Users'][0]['Count'] = file['API_Users'][0]['Count'] + 1
            json_file = open('../customer/API_counter.json', "w")
            json.dump(file, json_file)
            json_file.close()
            return os.getenv("BG_REMOVE_API_KEY_0")


        else:
            print(file['API_Users'][0]['Email'] + "  is already 50 times used..... try: " + str(file['API_Users'][1]['Email']))

            if (file['API_Users'][1]['Count']  < 49 ):
                print(file['API_Users'][1]['Email'] + " is used " + str(file['API_Users'][1]['Count']) + " times of 50" )

                file['API_Users'][1]['Count'] = file['API_Users'][1]['Count'] + 1
                json_file = open('../customer/API_counter.json', "w")
                json.dump(file, json_file)
                json_file.close()
                return os.getenv("BG_REMOVE_API_KEY_1")



            else:
                print(file['API_Users'][1]['Email'] + "  is already 50 times used..... try: " + str(file['API_Users'][2]['Email']))


                if (file['API_Users'][2]['Count']  < 49 ):
                    print(file['API_Users'][2]['Email'] + " is used " + str(file['API_Users'][2]['Count']) + " times of 50" )

                    file['API_Users'][2]['Count'] = file['API_Users'][2]['Count'] + 1
                    json_file = open('../customer/API_counter.json', "w")
                    json.dump(file, json_file)
                    json_file.close()

                    return os.getenv("BG_REMOVE_API_KEY_2")

                else:
                    print( "  All Emails are already 50 times used..... reseting: " )


                    file['API_Users'][0]['Count'] = 0
                    file['API_Users'][1]['Count'] = 0
                    file['API_Users'][2]['Count'] = 0

                    json_file = open('../customer/API_counter.json', "w")
                    json.dump(file, json_file)
                    json_file.close()
                    print("reset")








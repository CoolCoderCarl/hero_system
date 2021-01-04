import json
import sys
import parserDescription

main_parser = parserDescription.createParser()
namespace = main_parser.parse_args(sys.argv[1:])


###
### MAIN INFO ABOUT CHARACTER
###
def basicInfo():
    with open('hero_information.json') as data_json:
        datest = json.load(data_json)
        if namespace.basic_info:
            print('==================================')
            print('LEVEL: ', end='')
            print(datest['level'])
            print('CLASSES: ', end='')
            print(datest['class']['first'] + ', ' + datest['class']['second'])

        if namespace.param_info:
            print('==================================')
            print('PARAMETERS: ')
            print(datest['parameters'][4][0], end=': ')
            print(datest['parameters'][4][1]['value'])

    data_json.close()


###
### SKILL INFO
###
def skillInfo():
    with open('hero_information.json') as data_json:
        datest = json.load(data_json)
        if namespace.skill_info:
            print('SKILLS')
            print('----------------------------------')

            print(datest['skills'][0][0], end='' + ': ')
            print(datest['skills'][0][1]['level'])

            print(datest['skills'][1][0], end='' + ': ')
            print(datest['skills'][1][1]['level'])

            print(datest['skills'][2][0], end='' + ': ')
            print(datest['skills'][2][1]['level'])

            print(datest['skills'][3][0], end='' + ': ')
            print(datest['skills'][3][1]['level'])

        data_json.close()


###
### FEATURE INFO
###
def featureInfo():
    with open('hero_information.json') as data_json:
        datest = json.load(data_json)
        if namespace.features_info:
            print('FEATURES')
            print('----------------------------------')

            print(datest['features'][0][0], end='' + ': ')
            print(datest['features'][0][1]['level'])

            print(datest['features'][1][0], end='' + ': ')
            print(datest['features'][1][1]['level'])

            print(datest['features'][2][0], end='' + ': ')
            print(datest['features'][2][1]['level'])

            print(datest['features'][3][0], end='' + ': ')
            print(datest['features'][3][1]['level'])

        data_json.close()

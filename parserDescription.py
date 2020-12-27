import argparse

def createParser():
    root_parser = argparse.ArgumentParser(
        prog='character controller',
        description='''Controller''',
        epilog='''(c) CoolCoderCarl'''
    )
    character_parser = root_parser.add_subparsers(dest='show')

    basic_parser = character_parser.add_parser('basic', help='Basic info')
    basic_parser.add_argument('-i', '--info', dest='basic_info', help='Show basic info', action='store_true', default=False)
    basic_parser.add_argument('-p', '--param', dest='param_info', help='Show basic info', action='store_true', default=False)

    skills_parser = character_parser.add_parser('skills', help='Skills info')
    skills_parser.add_argument('-i', '--info', dest='skill_info', help='Show skills info', action='store_true', default=False)

    features_parser = character_parser.add_parser('features', help='Features info')
    features_parser.add_argument('-i', '--info', dest='features_info', help='Show features info', action='store_true', default=False)

    return root_parser
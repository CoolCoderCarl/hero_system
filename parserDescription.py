import argparse

def createParser():
    root_parser = argparse.ArgumentParser(
        prog='character controller',
        description='''Controller''',
        epilog='''(c) CoolCoderCarl'''
    )
    main_parser = root_parser.add_subparsers(dest='hero')

###
### READ PARSERS
###
    basic_parser = main_parser.add_parser('basic', help='Basic info')
    basic_parser.add_argument('-i', '--info', dest='basic_info', help='Show basic info',
                              action='store_true', default=False)
    basic_parser.add_argument('-p', '--param', dest='param_info', help='Show parameters info',
                              action='store_true', default=False)

    skills_parser = main_parser.add_parser('skills', help='Skills info')
    skills_parser.add_argument('-i', '--info', dest='skill_info', help='Show skills info',
                               action='store_true', default=False)

    features_parser = main_parser.add_parser('features', help='Features info')
    features_parser.add_argument('-i', '--info', dest='features_info', help='Show features info',
                                 action='store_true', default=False)

###
### CREATE, BACKUP AND RESTORE PARSERS
###

    system_parser = main_parser.add_parser('system', help='System command')
    system_parser.add_argument('-s', '--show-template', dest='show_template', help='Show JSON template',
                               action='store_true', default=False)
    system_parser.add_argument('-t', '--create-from-template', dest='template', help='Create from template',
                              action='store_true', default=False)
    system_parser.add_argument('-b', '--backup', dest='backup', help='Backup the JSON hero info file',
                              action='store_true', default=False)
    system_parser.add_argument('-r', '--restore', dest='restore', help='Restore from backup file',
                              action='store_true', default=False)

    return root_parser
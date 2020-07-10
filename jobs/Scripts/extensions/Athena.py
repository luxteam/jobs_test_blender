import platform
import getpass

if (platform.system() == 'Windows'):
    CONFIG_PATH = os.path.expandvars('%appdata%/Blender Foundation/Blender/2.83/scripts/addons/rprblender/config.py')
    #CONFIG_PATH = 'C:/Users/' + getpass.getuser() + '/AppData/Roaming/Blender Foundation/Blender/2.83/scripts/addons/rprblender/config.py'
    ATHENA_DIR = 'C:/Users/' + getpass.getuser() + '/AppData/Local/Temp/rprblender/'
elif (platform.system() == 'Darwin'):
    CONFIG_PATH = '/Users/' + getpass.getuser() + '/Library/Application Support/Blender/2.83/scripts/addons/rprblender/config.py'
    ATHENA_DIR = os.environ['TMPDIR'] + 'rprblender/'
# else:
#     didn't implement Ubuntu
#     CONFIG_PATH = ''
#     ATHENA_DIR = os.environ['TMPDIR'] + 'rprblender/'

# def set_clean(value):
#     with open(CONFIG_PATH, 'r') as file:
#         config = file.read()
#     config.replace('clean_athena_files = ' + str(not value), 'clean_athena_files = ' + str(value))
#     with open(CONFIG_PATH, 'w') as file:
#         file.write(config)

def validate_athena(case):
    athena_files = os.listdir(ATHENA_DIR)
    if(not athena_files or len(athena_files) > 1):
        logging("Athena files weren't found") if not athena_files else logging("More than one file found")
        copyfile(path.join(WORK_DIR, '..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'error.jpg'), path.join(WORK_DIR, 'Color', case['case'] + '.jpg'))
    json_file = athena_files[0]
    try:
        with open(ATHENA_DIR + json_file, 'r') as athena_file:
            logging('Athena file content:\n' + athena_file.read())
            athena_file.seek(0)
            data = json.load(athena_file)
            copyfile(path.join(WORK_DIR, '..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'passed.jpg'), path.join(WORK_DIR, 'Color', case['case'] + '.jpg'))
    except Exception as e:
        logging(e)
        copyfile(path.join(WORK_DIR, '..', '..', '..', '..', 'jobs_launcher', 'common', 'img', 'error.jpg'), path.join(WORK_DIR, 'Color', case['case'] + '.jpg'))

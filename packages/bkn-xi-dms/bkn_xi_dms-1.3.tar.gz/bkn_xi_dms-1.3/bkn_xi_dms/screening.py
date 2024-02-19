import os
import shutil
from bkn_xi_dms.auth.login import *
from bkn_xi_dms.jenis_dokumen import *
from bkn_xi_dms.report.r_logger import * 

logger = init_r_logger()

config = configparser.ConfigParser()
config.read('cfg.ini')

path_report_file = config['INITIAL']['output_report']

scanner_pic = config['INITIAL']['user_name']
link_search_nip = config['LINK']['search_nip']
link_create_job = config['LINK']['create_job']
link_create_document = config['LINK']['create_document']
link_upload_document = config['LINK']['upload_document']
link_auth = config['LINK']['link_auth']

token = login(link_auth)

headers = {
    "Content_Type": "application/json",
    "Authorization": "Bearer " + token
}

f = open(config['INITIAL']['mapping_file'], 'r')
list_document_mapping = json.loads(f.read())
f.close()

dirpath_doc_feed = config['DIRECTORY']['document_feed']
dirpath_miss_nip = config['DIRECTORY']['miss_nip']
dirpath_not_a_pdf = config['DIRECTORY']['not_a_pdf']
dirpath_large = config['DIRECTORY']['large']
dripath_uncategories = config['DIRECTORY']['uncategories']
dirpath_doc_approved = config['DIRECTORY']['doc_approved']


def move_file(src_path, dest_path):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.move(src_path, dest_path)
    logger.info(f"moving file {src_path}")

def move_folder(source_folder, destination_path):
    list_employees_not_found = []
    os.makedirs(destination_path, exist_ok=True)
    items = os.listdir(source_folder)
    for item in items:
        item_path = os.path.join(source_folder, item)
        if os.path.isfile(item_path):
            target_path = os.path.join(destination_path, item)
            shutil.move(item_path, target_path)
            logger.warning(f"Moved folder '{item_path}' to '{target_path}'")
    shutil.rmtree(source_folder)
    logger.warning(f"Deleted source folder '{source_folder}'")

def move_file_with_folder(src_file_path, dest_root):
    src_dir_name = os.path.dirname(src_file_path)
    src_file_name = os.path.basename(src_file_path)
    dest_folder_path = os.path.join(dest_root, os.path.basename(src_dir_name))
    try:
        os.makedirs(dest_folder_path, exist_ok=True)
        logger.info (f"Directory created successfully: {dest_folder_path}")
    except FileExistsError:
        logger.error(f"Directory already exists: {dest_folder_path}")
    except PermissionError:
        logger.error(f"Permission error while creating directory: {dest_folder_path}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    dest_file_path = os.path.join(dest_folder_path, src_file_name)
    shutil.move(src_file_path, dest_file_path)
    return dest_file_path

# def filter_file(directory_path, headers, path_report, link_search_nip, list_document_mapping):
def filter_file():
    list_folder = os.listdir(dirpath_doc_feed)
    for folder in list_folder:
        logger.info(f"Proceed {folder}")
        list_doc = os.listdir(dirpath_doc_feed + folder)
        base_path = os.path.join(dirpath_doc_feed + folder)
        desti = os.path.join(dirpath_miss_nip,folder)
        params = {'nip':folder}
        employee = check_nip_exist(headers,id, link_search_nip,params)
        if employee is None:
            logger.warning(f"Empoyee {folder} Not found proceed to move folder")
            move_folder(base_path,desti)
            continue
        list_doc = os.listdir(dirpath_doc_feed + folder)
        base_path = os.path.join(dirpath_doc_feed + folder)
        for item in list_doc:
            logger.info(f"Proceed {item}")
            item_path  = os.path.join(base_path, item)
            if not os.path.isfile(item_path):
                continue
            elif not item_path.endswith(".pdf"):
                move_file_with_folder(item_path,dirpath_not_a_pdf )
                logger.warning(f"NOT PDF {item_path}")
                continue
            if os.path.getsize(item_path) > 10*1024*1000:
                move_file_with_folder(item_path,dirpath_large )
                logger.warning(f"LARGE FILE {item_path}")
                continue
            if get_jenis_file(item, list_document_mapping) == 0:
                move_file_with_folder(item_path, dripath_uncategories)
                logger.warning(f"Uncategories {item_path}")
                continue
            else:
                move_file_with_folder(item_path, dirpath_doc_approved)
                logger.info(f"PASS : {item_path}")
        shutil.rmtree( base_path)
        logger.warning(f"Deleted source folder '{ base_path}'")
    


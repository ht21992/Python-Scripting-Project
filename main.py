import os
import json
import shutil
import sys
from PyPDF2 import PdfReader

EBOOK_PATTERN = "ebook"


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def get_ebook_name(path, to_strip="-ebook"):
    _, dir_name = os.path.split(path)
    new_dir_name = dir_name.replace(to_strip, "")
    return new_dir_name

def lookup_pdf_in_root_dir(source):
    for root, dirs, files in os.walk(source):
        for file in files:
            if file not in dirs:
                if file.endswith(".pdf"):
                    # copy the file in a folder with same name
                    new_path = os.path.join(source, f'{file.replace(".pdf", "")}-ebook')
                    create_dir(new_path)
                    shutil.copyfile(os.path.join(source,file), os.path.join(new_path,file))
                    # delete the file after copy
                    # os.remove(os.path.join(source,file))
        break

def find_all_ebook_paths(source):
    ebooks_paths = []
    ebook_names = []
    lookup_pdf_in_root_dir(source)
    for root, dirs, files in os.walk(source):
        # lookup for ebooks in subdirectories
        for directory in dirs:
            if EBOOK_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                ebooks_paths.append(path)
                # strip path name and get the ebook path name
                ebook_names.append(get_ebook_name(path))

        break

    return ebooks_paths, ebook_names


def copy_and_overwrite(src_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    shutil.copytree(src_path, dest_path)


def get_pdf_pages_and_meta(pdf_path):
    reader = PdfReader(pdf_path)
    pdf_page_count = len(reader.pages)
    meta = reader.metadata
    return meta,pdf_page_count

def make_comperhensive_json_metadata_file(pdf_path, pdf_dirs):
    data = {
        "EbookNames": pdf_dirs,
        "numberOfEbooks": len(pdf_dirs)
    }
    print(pdf_path)
    with open(pdf_path, "w") as f:
        json.dump(data, f)


def make_json_metadata_file_for_ebook(ebook_name, ebook_dir):

    meta ,pdf_pages = get_pdf_pages_and_meta(os.path.join(ebook_dir,f"{ebook_name}.pdf",))
    data = {
        "Title":meta.title,
        "Author": meta.author,
        "Pages": pdf_pages,
        "Creator": meta.creator,
        "Subject": meta.subject,
        "KeyWords":meta.get('/Keywords',None),
    }

    with open(os.path.join(ebook_dir,f'{ebook_name}.json'), "w") as f:
        json.dump(data, f)


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    ebook_paths, ebook_new_dirs = find_all_ebook_paths(source_path)
    create_dir(target_path)
    for src, dest in zip(ebook_paths, ebook_new_dirs):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        make_json_metadata_file_for_ebook(ebook_name=dest,ebook_dir=dest_path)

    json_path = os.path.join(target_path, "metadata.json")
    make_comperhensive_json_metadata_file(json_path, ebook_new_dirs)



if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("Please pass source and target directories")

    source, target = args[1:]
    main(source, target)

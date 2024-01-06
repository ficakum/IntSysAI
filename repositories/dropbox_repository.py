import pathlib
import pandas as pd
import dropbox


def dropbox_list_files(dbx, path):
    try:
        files = dbx.files_list_folder(path).entries
        files_list = []
        for file in files:
            if isinstance(file, dropbox.files.FileMetadata):
                metadata = {
                    'name': file.name,
                    'path_display': file.path_display,
                    'client_modified': file.client_modified,
                    'server_modified': file.server_modified
                }
                files_list.append(metadata)

        df = pd.DataFrame.from_records(files_list)

        return df.sort_values(by='server_modified', ascending=False)

    except Exception as e:
        print('Error getting list of files from Dropbox: ' + str(e))



def dropbox_download_file(dbx, dropbox_file_path, local_file_path):
    try:
        with open(local_file_path, 'wb') as f:
            metadata, result = dbx.files_download(path=dropbox_file_path)
            f.write(result.content)

    except Exception as e:
        print('Error downloading file from Dropbox: ' + str(e))


def dropbox_upload_file(dbx, file_name, local_file_path, dropbox_folder_path):
    """
    Example:
        dropbox_upload_file('.', 'test.csv', '/stuff/test.csv')
    """

    try:
        local_file_path = pathlib.Path(local_file_path)
        dropbox_file_path = dropbox_folder_path + file_name + "/" + file_name + ".mp3"

        with local_file_path.open("rb") as f:
            meta = dbx.files_upload(f.read(), dropbox_file_path, mode=dropbox.files.WriteMode("overwrite"))

            return meta, dropbox_file_path
        
    except Exception as e:
        print('Error uploading file to Dropbox: ' + str(e))


def dropbox_get_link(dbx, dropbox_file_path):
    try:
        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(dropbox_file_path)
        shared_link = shared_link_metadata.url

        return shared_link.replace('?dl=0', '?dl=1')
    
    except dropbox.exceptions.ApiError as exception:
        if exception.error.is_shared_link_already_exists():            
            shared_link_metadata = dbx.sharing_list_shared_links(dropbox_file_path, direct_only=True)
            shared_link = shared_link_metadata.links[0].url

            return shared_link.replace('?dl=0', '?dl=1')
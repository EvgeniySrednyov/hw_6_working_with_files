import os
import shutil
import pytest
from zipfile import ZipFile


current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
tmp_dir = os.path.join(project_dir, 'tmp')
archive_dir = os.path.join(project_dir, 'resources')
archive = os.path.join(archive_dir, 'archive.zip')


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(archive_dir):
        os.mkdir(archive_dir)

    with ZipFile(archive, 'w') as zf:
        for file in os.listdir(tmp_dir):
            add_files = os.path.join(tmp_dir, file)
            zf.write(add_files, os.path.basename(add_files))

    yield

    shutil.rmtree(archive_dir)

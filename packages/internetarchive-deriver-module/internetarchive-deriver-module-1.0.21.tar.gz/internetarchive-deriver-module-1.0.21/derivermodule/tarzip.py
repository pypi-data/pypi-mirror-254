import tarfile
import zipfile

import io
import os.path
import time

class TarZipReader(object):
    """
    Interface for reading zip and tar files, currently supports getting a
    listing of files (excludes directories) and opening files within the archive
    through buffered readers.
    """

    def __init__(self, path):
        """
        Open a tar or zip file.

        Args:

        * path (str): Path to the zip file
        """
        self.is_zip = False
        self.is_tar = False
        self.archive = None

        try:
            self.archive = zipfile.ZipFile(path)
            self.is_zip = True
        except zipfile.BadZipFile:
            try:
                self.archive = tarfile.open(path)
                self.is_tar = True
            except tarfile.ReadError:
                raise

    def get_archive_file(self, filepath):
        """
        Get a file object to a file within the archive for reading purposes

        Args:

        * filepath (str): Path to the file within the archive

        Raise KeyError if the file does not exist

        Returns: file-like object
        """
        if self.is_zip:
            return self.archive.open(filepath)
        if self.is_tar:
            return self.archive.extractfile(filepath)

        raise NotImplementedError('')

    def get_file_list(self):
        """
        Returns an iterator that returns the paths of each file in the archive,
        ignores directories.
        """
        if self.is_zip:
            return self._get_file_list_zip()
        if self.is_tar:
            return self._get_file_list_tar()

        raise NotImplementedError('')

    def _get_file_list_zip(self):
        for fi in self.archive.namelist():
            info = self.archive.getinfo(fi)
            if info.is_dir():
                continue

            yield fi

    def _get_file_list_tar(self):
        for fi in self.archive:
            if not fi.isfile():
                continue

            yield fi.name

    def close(self):
        if self.archive:
            self.archive.close()
            self.archive = None

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def __del__(self):
        self.close()


class TarZipWriter(object):
    """
    Unified unterface for writing zip or tar archives, purposefully intended to
    provide an oversimplified interface. Does not currently work with existing
    archives.
    """
    def __init__(self, path):
        self.is_zip = path.endswith('zip')
        self.is_tar = path.endswith('tar')
        self.archive = None

        if os.path.exists(path):
            raise ValueError('Destination path seems to exist already, this simplified class cannot deal with existing archives')

        if not self.is_zip and not self.is_tar:
            raise ValueError('Unknown file extension')

        if self.is_zip:
            self.archive = zipfile.ZipFile(path, 'w', allowZip64=True)
        else:
            self.archive = tarfile.open(path, 'a:', format=tarfile.GNU_FORMAT)

        self._tar_dir_cache = {}

    def _tarfile_ensure_dir(self, arc_name):
        dn = os.path.dirname(arc_name)
        if dn != '':
            dn_components = dn.split(os.path.sep)
            for idx, _ in enumerate(dn_components):
                cons_dn = os.path.join(*dn_components[:idx+1])

                if cons_dn not in self._tar_dir_cache:
                    dir_path = cons_dn
                    dir_tarinfo = tarfile.TarInfo()
                    dir_tarinfo.name = dir_path
                    dir_tarinfo.type = tarfile.DIRTYPE
                    dir_tarinfo.mode = 0o755
                    dir_tarinfo.mtime = time.time()
                    self.archive.addfile(dir_tarinfo)

                    self._tar_dir_cache[cons_dn] = True

    def add_bytes(self, arc_name, data, binary_data_len=None):
        """
        Add data (bytes or file-like object) to archive.
        If data is a file-like object that is *NOT* seekable, pass
        the binary data length to the function in binary_data_len
        """
        if self.is_zip:
            if isinstance(data, bytes):
                self.archive.writestr(arc_name, data)
            elif isinstance(data, io.IOBase):
                self.archive.writestr(arc_name, data.read())
            else:
                raise ValueError('Unsupported data type:', type(data))
        else:
            self._tarfile_ensure_dir(arc_name)

            arc_tarinfo = tarfile.TarInfo()
            arc_tarinfo.name = arc_name
            arc_tarinfo.type = tarfile.REGTYPE
            arc_tarinfo.mode = 0o644
            arc_tarinfo.mtime = time.time()

            if isinstance(data, bytes):
                arc_tarinfo.size = len(data)
                with io.BytesIO() as bio:
                    bio.write(data)
                    bio.seek(0)
                    self.archive.addfile(arc_tarinfo, bio)
            elif isinstance(data, io.IOBase):
                if binary_data_len is not None:
                    arc_tarinfo.size = binary_data_len
                else:
                    data.seek(0, 2)
                    arc_tarinfo.size = data.tell()
                    data.seek(0, 0)
                self.archive.addfile(arc_tarinfo, data)
            else:
                raise ValueError('Unsupported data type:', type(data))


    def add_file(self, arc_name, src_file):
        if self.is_zip:
            self.archive.write(src_file, arc_name)
        else:
            self._tarfile_ensure_dir(arc_name)
            self.archive.add(src_file, arcname=arc_name)

    def close(self):
        if self.archive:
            self.archive.close()
            self.archive = None

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def __del__(self):
        self.close()


if __name__ == '__main__':
    import sys
    with TarZipReader(sys.argv[1]) as tzr:
        print(list(tzr.get_file_list()))

    tzr = TarZipReader(sys.argv[1])
    print(list(tzr.get_file_list()))
    tzr.close()

    #with tarzip.TarZipReader(sys.argv[1]) as tzr:
    #    with tarzip.TarZipWriter(sys.argv[2]) as tzw:
    #        for file in sorted(tzr.get_file_list()):
    #            with tzr.get_archive_file(file) as fp:
    #                tzw.add_bytes(file, fp)

#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import ftplib
import traceback
from io import BytesIO
from pathlib import Path
from typing import Any


class FTP:
    def __init__(self, host: str, user: str, password: str, **kwargs: Any):
        self.ftp = None
        self.host = host
        self.user = user
        self.password = password
        self.port = kwargs.get("port", 21)
        self.timeout = kwargs.get("timeout", 5)
        self.silent = kwargs.get("silent", False)
        self.verbose = kwargs.get("verbose", False)

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass

    def __getattr__(self, name: str) -> Any:
        """
        Delegate all unknown attributes to the ftp object.
        """
        return getattr(self.ftp, name)

    @classmethod
    def get_remote_path(cls, path: str) -> str:
        return f"/{path}".replace("//", "/")

    def connect(self, **kwargs: Any) -> Any:
        ftp = ftplib.FTP()
        host = kwargs.get("host", self.host)
        user = kwargs.get("user", self.user)
        port = kwargs.get("port", self.port)
        password = kwargs.get("password", self.password)
        timeout = kwargs.get("timeout", self.timeout)
        try:
            ftp.connect(host, port, timeout)
            ftp.login(user, password)
            self.ftp = ftp
            return ftp
        except Exception:
            if kwargs.get("silent", self.silent):
                traceback.print_exc()
            else:
                raise

    def close(self) -> None:
        if self.ftp:
            self.ftp.close()

    def run(self, method: str, cmd: str, *args: Any, **kwargs: Any) -> tuple:
        silent = kwargs.pop("silent", self.silent)
        verbose = kwargs.pop("verbose", self.verbose)
        try:
            ftp = self.ftp
            if not ftp:
                ftp = self.connect(silent=silent)

            if ftp:
                return True, getattr(self.ftp, method)(cmd, *args, **kwargs)

        except Exception:
            if silent:
                if verbose:
                    traceback.print_exc()

            else:
                raise

        return False, None

    def upload(self, local: Any, remote: str, **kwargs: Any) -> bool:
        is_ok = False
        fp = Path(local)
        blocksize = kwargs.get("blocksize", 8192)
        remote_path = self.get_remote_path(f"{remote}/{fp.name}")
        if fp.exists():
            with open(str(local), "rb") as fo:
                is_ok, _ = self.run("storbinary", f"STOR {remote_path}", fo, blocksize, **kwargs)

        return is_ok

    def upload_from_string(self, text: Any, remote: str, **kwargs: Any) -> bool:
        bio = BytesIO(bytes(str(text), encoding="utf-8"))
        remote = self.get_remote_path(remote)
        is_ok, _ = self.run("storbinary", f"STOR {remote}", bio, *kwargs)
        return is_ok

    def download(self, remote: str, local: Any, blocksize: int = 8192) -> None:
        remote_path = self.get_remote_path(remote)
        with open(local, "wb") as fo:
            self.run("retrbinary", f"RETR {remote_path}", fo.write, blocksize)

    def download_to_list(self, remote: str, blocksize: int = 8192) -> list:
        lines = []
        remote_path = self.get_remote_path(remote)
        self.run("retrbinary", f"RETR {remote_path}", lines.append, blocksize)
        rows = [line.decode("utf-8") for line in lines]
        return rows

    def listdir(self, remote: str) -> tuple:
        files = []
        folders = []
        for path in self.ftp.nlst(self.get_remote_path(remote)):
            if self.get_size(path) == -1:
                folders.append(path)
            else:
                files.append(path)

        return files, folders

    def delete(self, remote: str) -> None:
        self.run("delete", self.get_remote_path(remote))

    def get_size(self, remote: str) -> int:
        try:
            return self.ftp.size(self.get_remote_path(remote))
        except Exception:
            return -1

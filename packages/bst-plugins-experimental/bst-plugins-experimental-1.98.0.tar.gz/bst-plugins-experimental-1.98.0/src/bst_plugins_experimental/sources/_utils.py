import hashlib
import os
import contextlib
import stat
import tarfile
import zipfile

import requests
from buildstream import SourceFetcher, SourceError


class HTTPFetcher(SourceFetcher):
    def __init__(
        self, source, mirror_directory, url, suffix=None, sha256sum=None
    ):
        super().__init__()
        self.source = source
        self.mirror_directory = mirror_directory
        self.url = url
        self.suffix = suffix
        self.sha256sum = sha256sum
        self.mark_download_url(url)

    @property
    def mirror_file(self):
        assert self.sha256sum is not None, "sha256sum not known yet"
        return os.path.join(self.mirror_directory, self.sha256sum)

    def is_cached(self):
        return os.path.isfile(self.mirror_file)

    def is_resolved(self):
        return self.sha256sum is not None

    def fetch(self, alias_override=None):
        base_url = self.source.translate_url(
            self.url, alias_override=alias_override
        )

        url = base_url + self.suffix

        with contextlib.ExitStack() as stack:
            stack.enter_context(
                self.source.timed_activity("Fetching from {}".format(url))
            )
            try:
                tempdir = stack.enter_context(self.source.tempdir())

                headers = {"Accept": "*/*", "User-Agent": "BuildStream/2"}
                resp = requests.get(
                    url, headers=headers, stream=True, timeout=60
                )

                if not resp.ok:
                    raise SourceError(
                        f"Error mirroring {url}: HTTP Error {resp.status_code}: {resp.reason}"
                    )

                local_file = os.path.join(tempdir, os.path.basename(url))

                h = hashlib.sha256()
                with open(local_file, "wb") as dest:
                    for chunk in resp.iter_content(None):
                        dest.write(chunk)
                        h.update(chunk)

                computed = h.hexdigest()
                if self.sha256sum is None:
                    self.sha256sum = computed
                elif self.sha256sum != computed:
                    raise SourceError(
                        f"{url} expected hash {self.sha256sum}, got {computed}"
                    )

                os.makedirs(self.mirror_directory, exist_ok=True)
                os.rename(local_file, self.mirror_file)

            except requests.ConnectionError as e:
                raise SourceError(
                    f"Error mirroring {url}: {e}", temporary=True
                ) from e
            except OSError as e:
                raise SourceError(
                    f"Error mirroring {url}: {e}", temporary=True
                ) from e

            return self.sha256sum


def _strip_top_dir(members, attr):
    for member in members:
        path = getattr(member, attr)
        trail_slash = path.endswith("/")
        path = path.rstrip("/")
        splitted = getattr(member, attr).split("/", 1)
        if len(splitted) == 2:
            new_path = splitted[1]
            if trail_slash:
                new_path += "/"
            setattr(member, attr, new_path)
            yield member


class TarStager:
    def __init__(self, mirror_file):
        self.mirror_file = mirror_file

    def stage(self, directory):
        with tarfile.open(self.mirror_file, "r:gz") as tar:
            tar.extractall(
                path=directory,
                members=_strip_top_dir(tar.getmembers(), "path"),
            )


class ZipStager:
    def __init__(self, mirror_file):
        self.mirror_file = mirror_file

    def stage(self, directory):
        exec_rights = (stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO) & ~(
            stat.S_IWGRP | stat.S_IWOTH
        )
        noexec_rights = exec_rights & ~(
            stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
        )

        with zipfile.ZipFile(self.mirror_file, mode="r") as zipf:
            # Taken from zip plugin. It is needed to ensure reproducibility of permissions
            for member in _strip_top_dir(zipf.infolist(), "filename"):
                written = zipf.extract(member, path=directory)
                rel = os.path.relpath(written, start=directory)
                assert not os.path.isabs(rel)
                rel = os.path.dirname(rel)
                while rel:
                    os.chmod(os.path.join(directory, rel), exec_rights)
                    rel = os.path.dirname(rel)

                if os.path.islink(written):
                    pass
                elif os.path.isdir(written):
                    os.chmod(written, exec_rights)
                else:
                    os.chmod(written, noexec_rights)

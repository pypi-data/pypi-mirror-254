from urllib.parse import urlparse
from dektools.url import get_auth_url
from dektools.download import download_tree_from_http
from .base import ArtifactBase


class StaticfilesArtifact(ArtifactBase):
    typed = 'staticfiles'

    @classmethod
    def url_to_docker_tag(cls, url):
        tag = urlparse(url).path[1:].replace('/', '-')
        return cls.normalize_docker_tag(url, tag)

    def login(self, registry='', username='', password=''):
        self.login_auth(registry, username=username, password=password)

    def pull(self, url):
        auth = self.get_auth(urlparse(url).netloc)
        if auth:
            url = get_auth_url(url, auth['username'], auth['password'])
        return download_tree_from_http(self.path_objects, [url])[url]

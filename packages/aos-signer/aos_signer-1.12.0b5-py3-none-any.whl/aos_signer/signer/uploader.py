#
#  Copyright (c) 2018-2024 Renesas Inc.
#  Copyright (c) 2018-2024 EPAM Systems Inc.
#
# pylint: disable=R1732,W1514
import json
from pathlib import Path

import requests
from aos_keys.crypto_container import AosCryptoContainer
from aos_signer.service_config.service_configuration import ServiceConfiguration
from aos_signer.signer.common import REQUEST_TIMEOUT, ca_certificate, print_message
from aos_signer.signer.errors import SignerError
from aos_signer.signer.user_credentials import UserCredentials
from requests.exceptions import SSLError


def run_upload(config: ServiceConfiguration, config_path: Path):
    uc = UserCredentials(config, config_path)
    uc.find_upload_key_and_cert()

    upload_data = {'service': config.publish.service_uid, 'package_version': 2}
    version = config.publish.version
    upload_data['version'] = version

    file_to_upload = (config_path.parent.parent / 'service.tar.gz').resolve()
    print_message('Uploading...                   ', end='')

    with ca_certificate() as server_certificate_path:
        publish_url = config.publish.url
        try:
            if uc.pkcs_credentials is None:
                resp = requests.post(
                    f'https://{publish_url}:10000/api/v1/services/versions/',
                    files={'file': open(file_to_upload, 'rb')},  # noqa: WPS515
                    data=upload_data,
                    cert=(uc.upload_cert_path, uc.upload_key_path),
                    verify=server_certificate_path,
                    timeout=REQUEST_TIMEOUT,
                )
            else:
                with AosCryptoContainer(uc.upload_p12_path).create_requests_session() as session:
                    resp = session.post(  # noqa: S113, S106
                        f'https://{publish_url}:10000/api/v1/services/versions/',
                        files={'file': open(file_to_upload, 'rb')},  # noqa: WPS515
                        data=upload_data,
                        verify=server_certificate_path,
                    )
        except SSLError:
            print_message('[yellow]TLS verification against Aos Root CA failed.')
            print_message('[yellow]Try to POST using TLS verification against system CAs.')
            if uc.pkcs_credentials is None:
                resp = requests.post(
                    f'https://{publish_url}:10000/api/v1/services/versions/',
                    files={'file': open(file_to_upload, 'rb')},  # noqa: WPS515
                    data=upload_data,
                    cert=(uc.upload_cert_path, uc.upload_key_path),
                    timeout=REQUEST_TIMEOUT,
                )
            else:
                with AosCryptoContainer(uc.upload_p12_path).create_requests_session() as session:
                    resp = session.post(  # noqa: S113, S106
                        f'https://{publish_url}:10000/api/v1/services/versions/',
                        files={'file': open(file_to_upload, 'rb')},  # noqa: WPS515
                        data=upload_data,
                    )

        if resp.status_code != 201:  # noqa: WPS432
            print_message('[red]ERROR')
            print_message('[red]Server returned error while uploading:')
            try:
                errors = json.loads(resp.text)
                message = ''
                for key, error_value in errors.items():
                    message += f'   {key}: {error_value}'
                    raise SignerError(message)
            except json.JSONDecodeError as exc:
                raise SignerError(resp.text) from exc

    print_message('[green]DONE')
    print_message('[green]Service successfully uploaded!')

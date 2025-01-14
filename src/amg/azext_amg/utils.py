# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import re
import json
import requests
from knack.log import get_logger

logger = get_logger(__name__)


def log_response(resp):
    status_code = resp.status_code
    logger.debug("[DEBUG] resp status: %s", status_code)
    try:
        logger.debug("[DEBUG] resp body: %s", resp.json())
    except ValueError:
        logger.debug("[DEBUG] resp body: %s", resp.text)
    return resp


def search_dashboard(page, limit, grafana_url, http_get_headers):
    url = f'{grafana_url}/api/search/?type=dash-db&limit={limit}&page={page}'
    logger.info("search dashboard in grafana: %s", url)
    return send_grafana_get(url, http_get_headers)


def get_dashboard(board_uri, grafana_url, http_get_headers):
    url = f'{grafana_url}/api/dashboards/{board_uri}'
    logger.info("query dashboard uri: %s", url)
    (status_code, content) = send_grafana_get(url, http_get_headers)
    return (status_code, content)


def search_annotations(grafana_url, ts_from, ts_to, http_get_headers):
    # there is two types of annotations
    # annotation: are user created, custom ones and can be managed via the api
    # alert: are created by Grafana itself, can NOT be managed by the api
    url = f'{grafana_url}/api/annotations?type=annotation&limit=5000&from={ts_from}&to={ts_to}'
    (status_code, content) = send_grafana_get(url, http_get_headers)
    return (status_code, content)


def search_datasource(grafana_url, http_get_headers):
    logger.info("search datasources in grafana:")
    return send_grafana_get(f'{grafana_url}/api/datasources', http_get_headers)


def search_snapshot(grafana_url, http_get_headers):
    logger.info("search snapshots in grafana:")
    return send_grafana_get(f'{grafana_url}/api/dashboard/snapshots', http_get_headers)


def get_snapshot(key, grafana_url, http_get_headers):
    url = f'{grafana_url}/api/snapshots/{key}'
    (status_code, content) = send_grafana_get(url, http_get_headers)
    return (status_code, content)


def search_folders(grafana_url, http_get_headers):
    logger.info("search folder in grafana:")
    return send_grafana_get(f'{grafana_url}/api/search/?type=dash-folder', http_get_headers)


def get_folder(uid, grafana_url, http_get_headers):
    (status_code, content) = send_grafana_get(f'{grafana_url}/api/folders/{uid}', http_get_headers)
    logger.info("query folder:%s, status:%s", uid, status_code)
    return (status_code, content)


def get_folder_permissions(uid, grafana_url, http_get_headers):
    (status_code, content) = send_grafana_get(f'{grafana_url}/api/folders/{uid}/permissions',
                                              http_get_headers)
    logger.info("query folder permissions:%s, status:%s", uid, status_code)
    return (status_code, content)


def get_folder_id(dashboard, grafana_url, http_post_headers):
    folder_uid = ""
    try:
        folder_uid = dashboard['meta']['folderUid']
    except KeyError:
        matches = re.search('dashboards/f/(.*)/.*', dashboard['meta']['folderUrl'])
        if matches is not None:
            folder_uid = matches.group(1)
        else:
            folder_uid = '0'

    if folder_uid != "":
        logger.debug("debug: quering with uid %s", folder_uid)
        response = get_folder(folder_uid, grafana_url, http_post_headers)
        if isinstance(response[1], dict):
            folder_data = response[1]
        else:
            folder_data = json.loads(response[1])

        try:
            return folder_data['id']
        except KeyError:
            return 0
    else:
        return 0


def send_grafana_get(url, http_get_headers):

    r = requests.get(url, headers=http_get_headers)
    log_response(r)
    return (r.status_code, r.json())


def send_grafana_post(url, json_payload, http_post_headers):
    r = requests.post(url, headers=http_post_headers, data=json_payload)
    log_response(r)
    try:
        return (r.status_code, r.json())
    except ValueError:
        return (r.status_code, r.text)


def send_grafana_put(url, json_payload, http_post_headers):
    r = requests.put(url, headers=http_post_headers, data=json_payload)
    log_response(r)
    return (r.status_code, r.json())

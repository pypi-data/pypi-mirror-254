import mimetypes

from eloclient import Client
from eloclient.api.ix_service_port_if import ix_service_port_if_create_doc, ix_service_port_if_checkin_doc_end
from eloclient.models import BRequestIXServicePortIFCreateDoc, Sord, BRequestIXServicePortIFCheckinDocEnd, SordZ, LockZ, \
    LockC, Document, FileData, BStreamReference, DocVersion
from eloservice import eloconstants as elo_const
from eloservice.error_handler import _check_response
from eloservice.login_util import EloConnection


def _read_file(file_path):
    # read file as binary and return it together with the file name
    with open(file_path, "rb") as file:
        file_content = file.read()
        file_name = file.name[file.name.rfind("/") + 1:]
        return file_content, file_name


class FileUtil:
    elo_connection: EloConnection
    elo_client: Client

    def __init__(self, elo_client: Client, elo_connection: EloConnection):
        self.elo_connection = elo_connection
        self.elo_client = elo_client

    def upload_file(self, file_path: str, parent_id: str, filemask_id="0") -> str:
        """
        This function uploads a file to ELO
        :param filemask_id:  The maskID of the filemask in ELO, default is "0" (--> mask "Freie Eingabe" = STD mask)
        :param file_path: The path of the file which should be uploaded
        :param parent_id: The sordID of the parent folder in ELO
        :return: The sordID of the uploaded file
        """
        file_content, file_name = _read_file(file_path)
        return self._checkin_document(self.elo_connection, parent_id, file_name, file_content, filemask_id)

    def _checkin_document(self, elo_connection, parent_id, filename, filecontent, filemask_id="0"):
        document_sord = self._create_doc(elo_connection, filemask_id, parent_id)
        document_sord.name = filename
        mimetype = mimetypes.guess_type(filename)[0]

        # upload File and get the reference link
        streamID = self._upload_file(filecontent)
        docs = DocVersion(
            version="1.0",
            comment="",
            content_type=mimetype,
            file_data=FileData(
                stream=BStreamReference(
                    stream_id=streamID
                )
            )
        )
        document = Document(
            docs=[
                DocVersion(
                    version="1.0",
                    comment="",
                    content_type=mimetype,
                    file_data=FileData(
                        stream=BStreamReference(
                            stream_id=streamID
                        )
                    )
                )],
            atts=[]

        )

        body = BRequestIXServicePortIFCheckinDocEnd(
            ci=elo_connection.ci,
            sord=document_sord,
            sord_z=SordZ(bset=elo_const.ElobitsetEditz.MB_ALL.value),
            unlock_z=LockZ(LockC().bset_yes),
            document=document
        )

        res = ix_service_port_if_checkin_doc_end.sync_detailed(client=self.elo_client, json_body=body)
        _check_response(res)
        return res.parsed.result.obj_id

    def _upload_file(self, filecontent) -> str:
        """
        This function uploads a file to ELO. Which according to their documentation "is kept there for a few minutes."
        :param filecontent: the bytestream of the file
        :return: the streamID of the uploaded file, which can be used to reference the file in checkinDocEnd
        """
        # OPENAPI Spec provided by elo does not match with the real API, therefore we have to use the httpx client
        # directly
        erg = self.elo_client.get_httpx_client().request("POST", "/BUtility/upload", data=filecontent)
        # expected b'{"result":{"streamId":"8066662033750693538"}}'
        return erg.json()["result"]["streamId"]

    def _create_doc(self, elo_connection, filemask_id, parent_id) -> Sord:
        body = BRequestIXServicePortIFCreateDoc(
            ci=elo_connection.ci,
            parent_id=parent_id,
            mask_id=filemask_id,
            edit_info_z=elo_const.EDIT_INFO_Z_MB_ALL
        )
        res = ix_service_port_if_create_doc.sync_detailed(client=self.elo_client, json_body=body)
        _check_response(res)
        document_sord = res.parsed.result.sord
        return document_sord

# async function onInsertDocument() {
#
#   // Files to be uploaded.
# var versionFile = document.getElementById('versionFile').files[0];
# var attachmentFile = document.getElementById('attachmentFile').files[0];
# var files = [versionFile, attachmentFile];
# if (!versionFile || !attachmentFile) {
#     alert('Select files to upload');
# return;
# }
#
# // Read constant values.
#                  // This object should be read only once since it does not change and contains a large number of items.
# const CONST = await \
# xhr.restcall('IXServicePortIF/getConstants');
#
# // Login
# var loginResult = await \
# xhr.restcall('IXServicePortIF/login', {
#     userName : loginUser,
#     userPwd : loginPwd,
#     clientComputer : 'REST Client',
#     runAs : ''
# });
#
# // Initialize Sord with given parent ID and default document mask.
# var parentId = document.getElementById('parentId').value;
# var editInfo = await
# xhr.restcall('IXServicePortIF/createDoc', {
# parentId : parentId,
# maskId : CONST.DOC_MASK.GUID_DOCUMENT,
# editInfoZ : CONST.EDIT_INFO.mbSord
# });
#
# // Assign Sord properties.
# var sord = editInfo.sord;
# sord.name = document.getElementById('name').value;
#
# // Provide DocVersion objects with stream reference
# var version = {
# version : '1.0',
# comment : 'Version uploaded via REST call.',
# contentType : versionFile.type,
# fileData : {
#     stream : { streamId : 'files[0]' }
# }
# };
# var attachment = {
# version : '1.0',
# comment : 'Attachment uploaded via REST call.',
# contentType : attachmentFile.type,
# fileData : {
#     stream : { streamId : 'files[1]' }
# }
# };
#
# // Checkin document.
# var doc = await \
# xhr.restcallWithStreams('IXServicePortIF/checkinDocEnd', {
#     sord : sord,
#     sordZ : CONST.SORD.mbAll,
#     document : {
#         docs : [ version ],
#         atts : [ attachment ]
#     },
#     unlockZ : CONST.LOCK.NO
# }, files); 					// pass files here
# }

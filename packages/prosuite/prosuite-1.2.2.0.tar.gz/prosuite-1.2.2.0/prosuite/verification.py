import os
from typing import Union
from prosuite.data_model import TransformedDataset
import prosuite.generated.quality_verification_service_pb2 as service_util
import prosuite.generated.quality_verification_service_pb2_grpc as qa_service
import prosuite.generated.shared_qa_pb2 as shared_qa
import prosuite.generated.shared_types_pb2 as shared_types
import grpc
import logging

from prosuite.quality import Parameter, Specification, XmlSpecification

class EnvelopePerimeter:
    """
    A spatial envelope defined by the bounding coordinates. The spatial reference must match the 
    spatial reference of the datasets.
    """
    def __init__(self, x_min: float, y_min: float, x_max: float,  y_max: float):
        if x_min is None or x_max is None or y_min is None or y_max is None:
            raise Exception('Not all parameters are defined. Please define all envelope parameters')
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max


class EsriShapePerimeter:
    """
    A polygon in the Esri shape buffer format.
    """
    def __init__(self, esri_shape: bytes):
        self.esri_shape = esri_shape


class WkbPerimeter:
    """
    A polygon in the OGC well-known-binary format. For example, in ArcPy the geometry's WKB 
    property could be used to acquire this format.
    """
    def __init__(self, wkb: bytes):
        self.wkb = wkb

class VerificationParameters():
    """
    Contains all parameters that can be passed to a verification. 

    :param tile_size: size (in meter) for testing quality conditions
    :type tile_size: int
    :param username: the executing user
    :type username: str
    """

    def __init__(self, tile_size: int = 5000, user_name: str = None) -> None:
        #:
        self.tile_size: int = tile_size
        #:
        self.user_name: str = user_name

class InvolvedTable:
    """
    Represents a table involved in a verification issue.

    :param table_name: The name of the table.
    :type table_name: str
    :param object_ids: A list of object IDs from the table that are involved in the issue.
    :type object_ids: list
    """
    def __init__(self, table_name: str, object_ids: list):
        #:
        self.table_name = table_name
        #:
        self.object_ids = list(object_ids)

class Issue:
    """
    Represents an issue found during the verification.

    To initialize an Issue object, pass the issue message to it.
    :param issue_msg: The issue message.
    :type issue_msg: shared_qa.IssueMsg

    The Issue object extracts some properties from the issue message and makes them available as attributes:
    :ivar description: The description of the issue.
    :ivar involved_objects: A list of InvolvedTable objects that are involved in the issue.
    :ivar geometry: The geometry involved of the issue.
    :ivar issue_code: The issue code ID.
    :ivar allowable: If the issue is allowable.
    :ivar stop_condition: If the issue is a stop condition.
    """
    
    def __init__(self, issue_msg: shared_qa.IssueMsg):
        #:
        self.description = issue_msg.description
        #:
        self.involved_objects = list()
        #:
        self.geometry = issue_msg.issue_geometry
        #:
        self.issue_code = issue_msg.issue_code_id # TODO: test
        #:
        self.allowable = issue_msg.allowable # TODO: test
        #:
        self.stop_condition = issue_msg.stop_condition # TODO: test


        for involved_table_msg in issue_msg.involved_tables:
            involvedTable = InvolvedTable(involved_table_msg.table_name, involved_table_msg.object_ids)
            self.involved_objects.append(involvedTable)


        
class VerificationResponse:
    """
    This class represents a VerificationResponse Message.

    :param message: the actual message
    :param message_level: message level -> see class MessageLevel
    :param service_call_status: service status -> see class ServiceStatus

    The str() method is overridden to return all properties from the VerificationResponse when 
    a VerificationResponse object is printed using pythons print() method. 

    """

    def __init__(self, service_call_status: str, message: str, message_level: str, issue_msgs: list):
        #:
        self.message: str = message
        #:
        self.service_call_status = ServiceStatus.status_0
        #:
        self.message_level = MessageLevel.level_40000
        #:
        self._set_service_call_status(service_call_status)
        #:
        self._set_message_level(message_level)
        #:
        self.issues = list()

        for issue_msg in issue_msgs:
            self.issues.append(Issue(issue_msg))

    def __str__(self):
        return f'service_call_status: {self.service_call_status}\t message_level: {self.message_level} \t ' \
               f'message: {self.message}'

    def _set_service_call_status(self, service_call_status: str):
        if service_call_status == 0:
            self.service_call_status = ServiceStatus.status_0
        if service_call_status == 1:
            self.service_call_status = ServiceStatus.status_1
        if service_call_status == 2:
            self.service_call_status = ServiceStatus.status_2
        if service_call_status == 3:
            self.service_call_status = ServiceStatus.status_3
        if service_call_status == 4:
            self.service_call_status = ServiceStatus.status_4

    def _set_message_level(self, message_level: str):
        if message_level == 110000:
            self.message_level = MessageLevel.level_110000
        if message_level == 70000:
            self.message_level = MessageLevel.level_70000
        if message_level == 60000:
            self.message_level = MessageLevel.level_60000
        if message_level == 40000:
            self.message_level = MessageLevel.level_40000
        if message_level == 30000:
            self.message_level = MessageLevel.level_30000
        if message_level == 10000:
            self.message_level = MessageLevel.level_10000

# TODO: Make _AdvancedParameters 'private'? It should not appear anywhere
class AdvancedParameters():
    def __init__(self, specification, output_dir, perimeter, verification_params: VerificationParameters = None) -> None:

        self.specification:  Union[Specification,
                                   XmlSpecification] = specification
        self.perimeter: Union[EnvelopePerimeter,
                              EsriShapePerimeter, WkbPerimeter] = perimeter
        self.output_dir: str = output_dir
        self.tile_size: int = 5000
        self.user_name: str = None
        if (verification_params):
            self.tile_size = verification_params.tile_size
            self.user_name = verification_params.user_name


MAX_MESSAGE_LENGTH_MB = 1024

class Service:
    from prosuite.quality import Condition
    from typing import Iterable

    """
    The service class communicates on the http/2 channel with the server and initiates the 
    quality verifications.

    :param host_name: The name or IP address of the host running the quality verification service.
    :type host_name: str
    :param port_nr: The port used by the quality verification service.
    :type port_nr: int
    :param channel_credentials: The channel credentials to be used for TLS/SSL server 
        authentication, if required by the server (Default: None -> No TLS/SSL).

        Use :py:meth:`prosuite.utils.get_ssl_channel_credentials` to create the basic https 
        credentials if the appropria root certificates are in the windows certificate store.
        For advanced scenarios or credentials on a non-windows platform, see the gRPC Python docs
        (https://grpc.github.io/grpc/python/grpc.html).
    :type channel_credentials: grpc.ChannelCredentials  
    """

    ISSUE_GDB = "Issues.gdb"
    """The name of the issue File Geodatabase. 
        It will be written to the output_dir specified in the :py:meth:`prosuite.service.Service.verify` 
        method. This File Geodatabase contains the issues found during the verification and could 
        be used as the source for the Issue Worklist in the ProSuite QA Add-In for ArcGIS Pro.
    """

    XML_REPORT = "verification.xml"
    """The name of the xml verification report.
        It will be written to the output_dir specified in the :py:meth:`prosuite.service.Service.verify` 
        method.
    """

    HTML_REPORT = "verification.html"
    """The name of the html verification report.
        It will be written to the output_dir specified in the :py:meth:`prosuite.service.Service.verify` 
        method.
    """

    def __init__(self, host_name: str, port_nr: int, channel_credentials: grpc.ssl_channel_credentials = None):
        #:
        self.host_name = host_name
        """The host name.

        :meta private:
        """
        #:
        self.port_nr = port_nr
        """The port.

        :meta private:
        """
        #:
        self.ssl_channel_credentials: grpc.ssl_channel_credentials = channel_credentials
        """The TLS/SSL credentials.

        :meta private:
        """

    def verify(self, 
               specification: Union[Specification, XmlSpecification],
               perimeter: Union[EnvelopePerimeter, EsriShapePerimeter, WkbPerimeter] = None, 
               output_dir: str = None, 
               parameters: VerificationParameters = None) -> Iterable[VerificationResponse]:
        """
        Executes a quality verification by running all the quality conditions defined in the 
        provided quality specification.
        Returns a collection of VerificationResponse objects, containing the verification
        messages.

        Please refer to the :ref:`samples <samples-link>` for more details.

        :param specification: The quality specification containing the conditions to be verified.
            It can be either a :py:class:`prosuite.quality.Specification` directly defined in 
            python code or a :py:class:`prosuite.quality.XmlSpecification` from an XML 
            file, for example created by the XML export in the ProSuite Data Dictionary Editor.
        :param perimeter: The perimeter that defines the polygon or extent of the verification.
            Default: None -> Full extent of the verified datasets.
        :param output_dir: The output directory (must be writable / creatable by the service process).
            Default: No output is written by the server process.
        :param parameters: Additional optional verification parameters.
        :return: Iterator for looping over VerificationResponse objects. The verification response
            contains progress information, found issues and, in the final message, the verification results.
        :rtype: Iterator[VerificationResponse]
        """

        advanced_parameters = AdvancedParameters(
            specification, output_dir, perimeter, parameters)

        self._validate_params(advanced_parameters)

        channel = self._create_channel()

        client = qa_service.QualityVerificationGrpcStub(channel)

        request = self._compile_request(advanced_parameters)

        for response_msg in client.VerifyQuality(request):
            yield VerificationResponse(
                message=response_msg.progress.message,
                message_level=response_msg.progress.message_level,
                service_call_status=response_msg.service_call_status,
                issue_msgs=response_msg.issues
            )

    def _create_channel(self):
        message_length = MAX_MESSAGE_LENGTH_MB * 1024 * 1024
        options=[('grpc.max_send_message_length', message_length),
                 ('grpc.max_receive_message_length', message_length)]
        
        if self.ssl_channel_credentials:
            channel = self._create_secure_channel(options)
        else:
            channel = grpc.insecure_channel(f'{self.host_name}:{self.port_nr}', options)
        return channel

    def _validate_params(self, params: AdvancedParameters):
        if params.output_dir is None:
            params.output_dir = ""            
            logging.warn("No output dir is defined")
        if params.specification is None:
            raise Exception(
                "No specification is defined. Please assign verification.specification.")

    def _compile_request(self, parameters: AdvancedParameters):
        req = service_util.VerificationRequest()

        self._configure_verification_parameter_msg(req.parameters, parameters)
        self._configure_specification_msg(req.specification, parameters.specification)
        
        return req
    
    def _create_secure_channel(self, options) -> grpc.Channel:
        channel = grpc.secure_channel(
            f'{self.host_name}:{self.port_nr}', self.ssl_channel_credentials, options)
        try:
            grpc.channel_ready_future(channel).result(timeout=5)
            logging.info(
                f'Successfully established secure channel to {self.host_name}')
        except:
            logging.exception(
                f'Timeout. Failed to establish secure channel to {self.host_name}')
        return channel
    
    def _configure_specification_msg(self, 
                                     quality_spec_msg: shared_qa.QualitySpecificationMsg, 
                                     specification: Union[Specification, XmlSpecification]):
        if isinstance(specification, XmlSpecification):
            self._configure_xml_quality_specification_msg(quality_spec_msg.xml_specification, specification)
        else:
            self._configure_condition_list_specification_msg(quality_spec_msg.condition_list_specification, specification)
        
    def _configure_xml_quality_specification_msg(self, 
                                                 xml_specification_msg: shared_qa.XmlQualitySpecificationMsg, 
                                                 specification: XmlSpecification):
        xml_specification_msg.xml = specification.xml_string
        xml_specification_msg.selected_specification_name = specification.specification_name
        if specification.data_source_replacements:
            xml_specification_msg.data_source_replacements.extend(
                specification.data_source_replacements)
        return xml_specification_msg

    def _configure_condition_list_specification_msg(self,
                                                    cond_list_spec_msg: shared_qa.ConditionListSpecificationMsg, specification: Specification):
        cond_list_spec_msg.name = specification.name
        cond_list_spec_msg.description = specification.description
        for condition in specification.get_conditions():
            cond_list_spec_msg.elements.append(
                self._to_xml_quality_specification_element_msg(condition))

        data_sources = self._get_data_sources(specification)

        for key, value in data_sources.items():
            data_source_msg = shared_qa.DataSourceMsg()
            data_source_msg.id = key
            data_source_msg.model_name = key
            data_source_msg.catalog_path = value
            cond_list_spec_msg.data_sources.append(data_source_msg)

        return cond_list_spec_msg

    def _configure_shape_msg(self, 
                             shape_msg: shared_types.ShapeMsg, 
                             perimeter: Union[EnvelopePerimeter, WkbPerimeter, EsriShapePerimeter]):
        if isinstance(perimeter, EnvelopePerimeter):
            perimeter: EnvelopePerimeter
            shape_msg.envelope.x_min = perimeter.x_min
            shape_msg.envelope.x_max = perimeter.x_max
            shape_msg.envelope.y_min = perimeter.y_min
            shape_msg.envelope.y_max = perimeter.y_max
        if isinstance(perimeter, EsriShapePerimeter):
            perimeter: EsriShapePerimeter
            shape_msg.esri_shape = perimeter.esri_shape
        if isinstance(perimeter, WkbPerimeter):
            perimeter: WkbPerimeter
            shape_msg.wkb = bytes(perimeter.wkb)

    def _to_xml_quality_specification_element_msg(self, condition: Condition):
        spec_element = shared_qa.QualitySpecificationElementMsg()
        self._configure_quality_condition_msg(
            condition, spec_element.condition)
        spec_element.allow_errors = condition.allow_errors
        spec_element.category_name = condition.category
        # other props
        return spec_element

    def _configure_verification_parameter_msg(self, 
                                              params_msg: shared_qa.VerificationParametersMsg, 
                                              parameters: AdvancedParameters):
        
        params_msg.tile_size = parameters.tile_size

        if parameters.output_dir != '':
            params_msg.issue_file_gdb_path = os.path.join(
                parameters.output_dir, Service.ISSUE_GDB)
            params_msg.html_report_path = os.path.join(
                parameters.output_dir, Service.HTML_REPORT)
            params_msg.verification_report_path = os.path.join(
                parameters.output_dir, Service.XML_REPORT)
            
        if parameters.perimeter:
            self._configure_shape_msg(
                params_msg.perimeter, parameters.perimeter)


    def _configure_quality_condition_msg(self, 
                                         condition: Condition, 
                                         condition_msg: shared_qa.QualityConditionMsg):
        condition_msg.name = condition.name
        condition_msg.test_descriptor_name = condition.test_descriptor
        condition_msg.description = condition.description
        condition_msg.url = condition.url
        for param in condition.parameters:
            if param.contains_list_of_datasets:
                self._handle_dataset_list(condition_msg, param)
            else:
                condition_msg.parameters.append(self._to_parameter_mgs(param))

    def _handle_dataset_list(self, 
                             condition_msg: shared_qa.QualityConditionMsg, 
                             param: Parameter):
        """
        a Parameter value can be of type Dataset. Or it can be of type list[Dataset].
        if it is a Dataset list, each Dataset in the list should be treated as single Parameter
        """
        if param.contains_list_of_datasets:
            # in this case, param.dataset is actually a list of datasets. we need to unpack the list and create
            # single params for each dataset in the list
            if Parameter.value_is_list_of_datasets(param.dataset):
                for parameter in param.dataset:
                    ds_param = Parameter(param.name, parameter)
                    condition_msg.parameters.append(
                        self._to_parameter_mgs(ds_param))

    @staticmethod
    def _to_parameter_mgs(param: Parameter):
        param_msg = shared_qa.ParameterMsg()
        param_msg.name = param.name

        if isinstance(param.value, TransformedDataset):
            # handle transformed dataset here
            param_msg.where_clause = Service._none_to_emtpy_str(
                param.get_where_clause())
        else:
            param_msg.value = Service._none_to_emtpy_str(
                param.get_string_value())
            param_msg.where_clause = Service._none_to_emtpy_str(
                param.get_where_clause())
            param_msg.workspace_id = param.get_workspace_id()
            param_msg.used_as_reference_data = False

        return param_msg

    @staticmethod
    def _none_to_emtpy_str(value) -> str:
        if value is None:
            return ""
        return value

    def _get_data_sources(self, specification: Specification) -> dict:
        result = {}
        for condition in specification.get_conditions():
            for parameter in condition.parameters:
                if parameter.is_dataset_parameter():
                    if parameter.contains_list_of_datasets:
                        for dataset in parameter.dataset:
                            model = dataset.model
                            result[model.name] = model.catalog_path
                        pass
                    else:
                        model = parameter.dataset.model
                        result[model.name] = model.catalog_path
        return result


class ServiceStatus:
    status_0 = 'Undefined'
    status_1 = 'Running'
    status_2 = 'Cancelled'
    status_3 = 'Finished'
    status_4 = 'Failed'


class MessageLevel:
    level_110000 = 'Fatal'
    level_70000 = 'Error'
    level_60000 = 'Warn'
    level_40000 = "Info"
    level_30000 = 'Debug'
    level_10000 = 'Verbose'
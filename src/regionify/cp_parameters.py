class AwsParameters:
    def __init__(self, app_name, ami_id, instance_type, region_name, logo_path):
        self._instance_type = instance_type
        self._ami_id = ami_id
        self._region_name = region_name
        self._app_name = app_name
        self._logo_path = logo_path

    @property
    def app_name(self):
        return self._app_name

    @property
    def instance_type(self):
        return self._instance_type

    @property
    def ami_id(self):
        return self._ami_id

    @property
    def region_name(self):
        return self._region_name

    @property
    def logo_path(self):
        return self._logo_path


class AzureParameters:
    def __init__(self, app_name, region_name, image_publisher, image_offer, image_sku, extension_script_file=None,
                 image_version='latest', vm_size='basic_A0', logo_path=''):
        self._region_name = region_name
        self._image_publisher = image_publisher
        self._image_offer = image_offer
        self._image_sku = image_sku
        self._image_version = image_version
        self._vm_size = vm_size
        self._app_name = app_name
        self._extension_script_file = extension_script_file
        self._logo_path = logo_path

    @property
    def extension_script_file(self):
        return self._extension_script_file

    @property
    def app_name(self):
        return self._app_name

    @property
    def vm_size(self):
        return self._vm_size

    @property
    def region_name(self):
        return self._region_name

    @property
    def image_publisher(self):
        return self._image_publisher

    @property
    def image_offer(self):
        return self._image_offer

    @property
    def image_sku(self):
        return self._image_sku

    @property
    def image_version(self):
        return self._image_version

    @property
    def logo_path(self):
        return self._logo_path

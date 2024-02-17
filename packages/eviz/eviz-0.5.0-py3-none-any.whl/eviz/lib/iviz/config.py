import yaml
import os


class configIviz:
    """
    The ConfigIviz class contains information needed to configure iviz for yaml based
    inputs to the tool. If kwargs are empty, set to defaults.  

    """

    def __init__(self, specs_path=None, **kwargs):
        self.file_dict = kwargs.get('file_dict', None)
        self.file_list = kwargs.get('file_list', None)
        self.inputs = kwargs.get('inputs', None)
        self.outputs = kwargs.get('outputs', None)
        self.app_data = kwargs.get('app_data', None)
        self.filename = kwargs.get('filename', None)
        self.data_dir = kwargs.get('location', '~')
        self.use_trop_field = kwargs.get('use_trop_field', False)
        self.trop_filename = kwargs.get('trop_filename', None)
        self.trop_field_name = kwargs.get('trop_fieldname', None)
        self.trop_conversion = kwargs.get('trop_conversion', None)
        self.use_sphum_field = kwargs.get('use_sphum_field', False)
        self.sphum_field_name = kwargs.get('sphum_field_name', None)

        if self.trop_filename is None:
            self.get_trop()

        if specs_path is None:
            self.specs_data = kwargs.get('specs_data', None)
        else:
            self.specs_data = self.load(specs_path)

        try:
            self.exp_name = self.file_dict[self.file_list[0]]['exp_name']
        except:
            self.exp_name = kwargs.get('exp_name', None)
        try:
            self.output_dir = self.app_data['outputs']['output_dir']
        except:
            self.output_dir = kwargs.get('output_dir', None)
        self.is_yaml = kwargs.get('is_yaml', False)

    def load(self, specs_path):
        try:
            with open(specs_path) as f:
                specs = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            print(f"Error: {e}")
            specs = None

        return specs

    def get_trop(self):
        if self.app_data is not None:
            if 'for_inputs' in self.app_data:
                if 'trop_height' in self.app_data['for_inputs']:
                    if 'location' in self.app_data['for_inputs']['trop_height'][0]:
                        filename = os.path.join(self.app_data['for_inputs']['trop_height'][0]['location'],
                                                self.app_data['for_inputs']['trop_height'][0]['name'])
                    else:
                        filename = self.app_data['for_inputs']['trop_height'][0]['name']
                    self.trop_filename = filename
                    self.trop_field_name = self.app_data['for_inputs']['trop_height'][0]['trop_field_name']

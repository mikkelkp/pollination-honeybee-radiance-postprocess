from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class PointInTimeResults(Function):
    """Calculate annual daylight metrics for annual daylight simulation."""

    folder = Inputs.folder(
        description='This folder is an output folder of annual daylight recipe. Folder '
        'should include grids_info.json and sun-up-hours.txt. The command uses the list '
        'in grids_info.json to find the result files for each sensor grid.',
        path='raw_results'
    )

    spectral_samples = Inputs.int(
        description='The number of spectral samples.', default=20,
        spec={'type': 'integer', 'minimum': 3, 'maximum': 24}
    )

    wavelength_minimum = Inputs.int(
        description='The minimum wavelength of the spectrum.', default=380
    )

    wavelength_maximum = Inputs.int(
        description='The maximum wavelength of the spectrum.', default=780
    )

    metric = Inputs.str(
        description='Text for the type of metric to be output from the calculation. '
        'Choose from: illuminance, irradiance, luminance, radiance.',
        default='illuminance',
        spec={'type': 'string',
              'enum': ['illuminance', 'irradiance', 'luminance', 'radiance']},
    )

    @command
    def pit_results(self):
        return 'honeybee-radiance-postprocess spectral pit-results ' \
            'raw_results --spectral-samples {{self.spectral_samples}} ' \
            '--spectral-range {{self.wavelength_minimum}} {{self.wavelength_maximum}} ' \
            '--metric {{self.metric}} --sub-folder metrics'

    # outputs
    metrics = Outputs.folder(
        description='Annual metrics folder. This folder includes all the other '
        'sub-folders which are also exposed as separate outputs.', path='metrics'
    )

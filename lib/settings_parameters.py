from collections import namedtuple

SettingsParameters = namedtuple('SettingsParameters',
                                ['gain', 'distortion', 'cutoff_hz',
                                 'resonance', 'drive', 'delay_seconds', 'size',
                                 'wet_level', 'dry_level', 'width',
                                 'rate_hz_phaser', 'depth_phaser', 'semitones',
                                 'chorus', ])

# Copyright 2022 Q-CTRL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
===========
qctrlpyquil
===========
"""

__version__ = "0.1.0"

from .program import convert_dds_to_pyquil_program

__all__ = ["convert_dds_to_pyquil_program"]

raise Warning(
    "⚠️ (DEPRECATED) This package has been deprecated ⚠️\n"
    "Visit https://docs.q-ctrl.com for updated information about"
    " how to integrate Q-CTRL software with PyQuil."
)

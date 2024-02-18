#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2023-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------
import pytest

from ibm_watsonx_ai.foundation_models.prompts import PromptTemplateManager
from ibm_watsonx_ai.tests.utils import get_wml_credentials


@pytest.fixture(scope="class")
def set_up_prompt_template_manager():
    wml_credentials = get_wml_credentials()
    project_id = wml_credentials.get('project_id')
    prompt_mgr = PromptTemplateManager(wml_credentials, project_id=project_id)
    return prompt_mgr
